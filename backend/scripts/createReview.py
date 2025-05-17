# Port: 5021
# Routes: /createReview (POST), /createProducerReview (POST), /createVenueReview (POST)
# Dataclass: reviews, producerReviews, venueReviews
# -----------------------------------------------------------------------------------------

import os
import s3Images
from flask import Blueprint, g, request, jsonify
from datetime import datetime
from scripts import pointsHelperFunc, badge_helpers

file_name = os.path.basename(__file__)
blueprint = Blueprint(file_name[:-3], __name__)


# Helper function to create a unique username for the venue
def create_username(location_name):
    conn = g.db
    cur = conn.cursor()

    location_name = location_name.replace(" ", "").lower()

    cur.execute("""
        SELECT id FROM "venues" WHERE "username" LIKE %s
    """, (f"{location_name}%",))

    existing_usernames = cur.fetchall()

    if not existing_usernames:
        return location_name
    else:
        max_suffix = max([int(name[0].split('_')[-1]) for name in existing_usernames if '_' in name[0]], default=0)
        return f"{location_name}_{max_suffix + 1}"
# ======================================================



# -----------------------------------------------------------------------------------------
# [POST] Creates a review
# - Insert entry into the "reviews" collection. Follows reviews dataclass requirements.
# - Duplicate review check: If a review with the same userID and reviewTarget exists, reject the request
# - Possible return codes: 201 (Created), 400 (Duplicate Detected), 500 (Error during creation)
@blueprint.route("/createReview", methods=['POST'])
def createReviews():
    raw_review = request.get_json()
    conn = g.db
    cur = conn.cursor()

    review_target = int(raw_review['reviewTarget'])
    user_id = int(raw_review['userID'])
    created_date = datetime.strptime(raw_review['createdDate'], "%Y-%m-%dT%H:%M:%S.%fZ")

    # Checking for duplicate review
    cur.execute("""
        SELECT * FROM "reviews" WHERE "reviewTarget" = %s AND "userID" = %s
    """, (review_target, user_id))

    if cur.fetchone() is not None:
        return jsonify({
            "code": 400,
            "data": {
                "listingName": raw_review['reviewDesc']
            },
            "message": "Review already exists."
        }), 400

    tagged_users = raw_review.get('taggedUsers', [])
    flavour_tags = raw_review.get('flavourTag', [])
    observation_tags = raw_review.get('observationTag', [])

    will_recommend = raw_review.get('willRecommend')
    would_buy_again = raw_review.get('wouldBuyAgain')

    if will_recommend is None:
        will_recommend = None
    else:
        will_recommend = bool(will_recommend == 'true')

    if would_buy_again is None:
        would_buy_again = None
    else:
        would_buy_again = bool(would_buy_again == 'true')

    # Insert new venue if necessary
    venue_id = None
    if raw_review.get('location') and raw_review.get('address'):
        location_name = raw_review['location']
        address = raw_review['address']
        cur.execute("""SELECT id FROM venues WHERE "venueName" = %s AND "address" = %s""", (location_name, address))
        venue_row = cur.fetchone()
        venue_id = venue_row['id'] if venue_row else None
        if not venue_id:
            username = create_username(location_name)  # Assuming this is an existing function
            insert_venue_sql = """INSERT INTO venues ("venueName", "address", "venueType", "originLocation", "venueDesc",
                                  "hashedPassword", "claimStatus", photo, "reservationDetails", username)
                                  VALUES (%s, %s, '', '', '', %s, FALSE, '', '', %s) RETURNING id"""
            hashed_password = 'hashed_password'
            cur.execute(insert_venue_sql, (location_name, address, hashed_password, username))
            venue_row = cur.fetchone()
            venue_id = venue_row['id'] if venue_row else None
            print(venue_id)
            conn.commit()

    # Upload image into S3
    if raw_review.get('photo'):
        raw_review['photo'] = s3Images.uploadBase64ImageToS3(raw_review['photo'])

    # Prepare the insert SQL for reviews
    insert_review_sql = """INSERT INTO reviews ("userID", "reviewTarget", "rating", "reviewDesc", "reviewType", "createdDate", 
                          language, finish, "willRecommend", "wouldBuyAgain", "taggedUsers", "flavourTag", photo, colour, 
                          aroma, taste, "observationTag", location, address)
                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"""
    review_values = (user_id, review_target, float(raw_review['rating']), raw_review['reviewDesc'], raw_review.get('reviewType', 'regular'),
                     created_date, raw_review.get('language', ''), raw_review.get('finish', ''), will_recommend,
                     would_buy_again, tagged_users, flavour_tags, raw_review.get('photo', ''),
                     raw_review.get('colour', ''), raw_review.get('aroma', ''), raw_review.get('taste', ''),
                     observation_tags, venue_id, raw_review.get('address', ''))

    try:
        cur.execute(insert_review_sql, review_values)
        review_id = cur.fetchone()['id']
        
        # Process badges for this review
        badge_updates = badge_helpers.process_badges_for_review(conn, user_id, raw_review, review_id)
        
        # Create a votes record for this review
        cur.execute("""
            INSERT INTO "reviewsUserVotes" ("reviewId", upvotes, downvotes)
            VALUES (%s, '[]', '[]')
        """, (review_id,))
        
        conn.commit()

        if pointsHelperFunc.check_max_proof_points(user_id):
            return jsonify({
                "code": 201,
                "data": raw_review['reviewDesc'],
                "message": "Review created successfully, but points limit reached."
            }), 201

        # Calculate proof points earned 
        rule_fulfiled_id = []

        # Basic review: Simple text 
        if raw_review.get('reviewDesc'):
            rule_fulfiled_id.append(2)
        
        # Extended review: color, aroma, taste, finish
        if (raw_review.get('finish') or raw_review.get('colour') or 
            raw_review.get('aroma') or raw_review.get('taste')):
            rule_fulfiled_id.append(3)

        # Attach image
        if raw_review.get('photo'):
            rule_fulfiled_id.append(4)

        # Tag location
        if venue_id:
            rule_fulfiled_id.append(5)

        # Tag friends
        if tagged_users:
            rule_fulfiled_id.append(6)

        # Get total proof points earned 
        if rule_fulfiled_id:
            cur.execute('SELECT SUM("proofPoints") FROM "pointSystemRules" WHERE id IN %s', (tuple(rule_fulfiled_id),))
            result = cur.fetchone()
            total_points = result['sum'] if result else 0
        else:
            total_points = 0

        # Update user points
        if total_points:
            cur.execute('UPDATE "pointsRecorder" SET "currentPoints" = "currentPoints" + %s WHERE id = %s AND "userType" = %s', 
                       (total_points, user_id, 'user',))
            conn.commit()
            print(f"Awarded points: {total_points}")

        # Format badge updates for response
        badge_details = []
        if badge_updates:
            for badge_id, old_level, new_level in badge_updates:
                cur.execute("""
                    SELECT "badgeName", "badgePhoto", "badgeDesc", "badgeType", "relatedEntity" 
                    FROM "badges" 
                    WHERE id = %s
                """, (badge_id,))
                badge = cur.fetchone()
                if badge:
                    badge_details.append({
                        "badgeName": badge['badgeName'],
                        "badgeType": badge['badgeType'],
                        "relatedEntity": badge['relatedEntity'],
                        "oldLevel": old_level,
                        "newLevel": new_level
                    })

        return jsonify({
            "code": 201,
            "data": raw_review['reviewDesc'],
            "proofPointsEarned": total_points,
            "badgeUpdates": badge_details
        }), 201
    except Exception as e:
        print(str(e))
        conn.rollback()
        return jsonify({
            "code": 500,
            "data": {
                "listingName": raw_review['reviewDesc']
            },
            "message": "An error occurred creating the review.",
            "error": str(e)
        }), 500
# ======================================================

# [POST] Creates a producer tour review
@blueprint.route("/createProducerReview", methods=['POST'])
def createProducerReviews():
    raw_review = request.get_json()
    conn = g.db
    cur = conn.cursor()

    producer_id = int(raw_review['producerID'])
    user_id = int(raw_review['userID'])
    created_date = datetime.strptime(raw_review['createdDate'], "%Y-%m-%dT%H:%M:%S.%fZ")

    # Check for duplicate review using EXISTS
    cur.execute("""SELECT EXISTS(SELECT 1 FROM "producerReviews" WHERE "producerID" = %s AND "userID" = %s)""",
                (producer_id, user_id))
    if cur.fetchone()['exists']:
        return jsonify({"code": 400, "message": "Review already exists."}), 400

    # Upload images & store their returned URLs
    photos = [s3Images.uploadBase64ImageToS3(photo) for photo in raw_review.get('photos', []) if photo]

    insert_review_sql = """
        INSERT INTO "producerReviews" ("userID", "producerID", "rating", "reviewDesc", "createdDate", "photos") 
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    review_values = (user_id, producer_id, float(raw_review['rating']), raw_review['reviewDesc'], created_date, photos)

    try:
        cur.execute(insert_review_sql, review_values)
        conn.commit()

        total_points = 0

        if pointsHelperFunc.check_max_proof_points(user_id):
            return jsonify({"code": 201, "data": raw_review['reviewDesc']}), 201

        # Get the proof points for simple text review
        if raw_review['reviewDesc']:
            cur.execute("""SELECT "proofPoints" FROM "pointSystemRules" WHERE id = 2""")
            total_points += cur.fetchone()['proofPoints']

        # Check if photo was provided
        if photos:
            cur.execute("""SELECT "proofPoints" FROM "pointSystemRules" WHERE id = 4""")
            total_points += cur.fetchone()['proofPoints']

        # Update user points
        cur.execute('UPDATE "pointsRecorder" SET "currentPoints" = "currentPoints" + %s WHERE id = %s AND "userType" = %s', (total_points, user_id, 'user',))
        conn.commit()

        print(f"Points awarded: {total_points}")

        return jsonify({"code": 201, "data": raw_review['reviewDesc'], "pointsEarned": total_points}), 201

    except Exception as e:
        print(str(e))
        return jsonify({"code": 500, "message": "An error occurred creating the review."}), 500
    
# ======================================================

# [POST] Creates a venue review
@blueprint.route("/createVenueReview", methods=['POST'])
def createVenueReviews():
    raw_review = request.get_json()
    conn = g.db
    cur = conn.cursor()

    venue_id = int(raw_review['venueID'])
    user_id = int(raw_review['userID'])
    created_date = datetime.strptime(raw_review['createdDate'], "%Y-%m-%dT%H:%M:%S.%fZ")

    # Check for duplicate review using EXISTS
    cur.execute(
        """SELECT EXISTS(SELECT 1 FROM "venueReviews" WHERE "venueID" = %s AND "userID" = %s)""",
        (venue_id, user_id)
    )
    if cur.fetchone()['exists']:
        return jsonify({"code": 400, "message": "Review already exists."}), 400

    # Upload images & store their returned URLs
    photos = [s3Images.uploadBase64ImageToS3(photo) for photo in raw_review.get('photos', []) if photo]

    insert_review_sql = """
        INSERT INTO "venueReviews" ("userID", "venueID", "rating", "reviewDesc", "createdDate", "photos") 
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    review_values = (
        user_id,
        venue_id,
        float(raw_review['rating']),
        raw_review['reviewDesc'],
        created_date,
        photos
    )

    try:
        cur.execute(insert_review_sql, review_values)
        conn.commit()

        total_points = 0

        if pointsHelperFunc.check_max_proof_points(user_id):
            return jsonify({"code": 201, "data": raw_review['reviewDesc']}), 201
        
        # Get the proof points for simple text review
        if raw_review['reviewDesc']:
            cur.execute("""SELECT "proofPoints" FROM "pointSystemRules" WHERE id = 2""")
            total_points += cur.fetchone()['proofPoints']

        # Check if photo was provided
        if photos:
            cur.execute("""SELECT "proofPoints" FROM "pointSystemRules" WHERE id = 4""")
            total_points += cur.fetchone()['proofPoints']

        # Update user points
        cur.execute('UPDATE "pointsRecorder" SET "currentPoints" = "currentPoints" + %s WHERE id = %s AND "userType" = %s', (total_points, user_id, 'user',))
        conn.commit()
        
        return jsonify({"code": 201, "data": raw_review['reviewDesc']}), 201

    except Exception as e:
        print(str(e))
        return jsonify({"code": 500, "message": "An error occurred creating the review."}), 500

