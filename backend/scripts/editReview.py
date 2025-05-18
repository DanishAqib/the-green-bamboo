# Port: 5022
# Routes: /voteReview (POST), /updateReview/<id> (PUT), /voteProducerReview (POST), /updateProducerReview/<id> (PUT)
# -----------------------------------------------------------------------------------------

import os
import s3Images
from flask import Blueprint, g, request, jsonify
from bson.objectid import ObjectId
from datetime import datetime, timedelta
import json
from scripts import badge_helpers

from scripts.adminFunctions import hash_password
from scripts.createReview import create_username

file_name = os.path.basename(__file__)
blueprint = Blueprint(file_name[:-3], __name__)

def is_empty_photo(value):
    return value in (None, '', [])

def is_non_empty_photo(value):
    return not is_empty_photo(value)

# -----------------------------------------------------------------------------------------
# [POST] Vote review
# - Update review with new votes
# - Possible return codes: 201 (Updated), 500 (Error during update)
@blueprint.route('/voteReview', methods=['POST'])
def voteReview():
    conn = g.db
    data = request.get_json()

    review_id = data['reviewID']
    user_id = data['userID']
    action = data['action']
    # current_time = data.get('voteDate', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    # Parse the date string from frontend (ISO format) to the expected format
    if 'voteDate' in data:
        try:
            # Convert ISO format to datetime object
            vote_datetime = datetime.fromisoformat(data['voteDate'].replace('Z', '+00:00'))
            print("code is h")
            # Format to the expected string format
            current_time = vote_datetime.strftime("%Y-%m-%d %H:%M:%S")
        except ValueError:
            print("code is her")
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    else:
        print("code is here")
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with conn.cursor() as cur:
        try:
            cur.execute("SELECT id, upvotes, downvotes FROM \"reviewsUserVotes\" WHERE \"reviewId\" = %s", (review_id,))
            result = cur.fetchone()

            upvotes = result['upvotes'] if result else []
            downvotes = result['downvotes'] if result else []

            # Convert JSONB to Python lists
            upvotes = json.loads(upvotes) if isinstance(upvotes, str) else upvotes
            downvotes = json.loads(downvotes) if isinstance(downvotes, str) else downvotes

            # Track if this is a new upvote
            is_new_upvote = False
            
            if action == "upvote":
                # Check if user has already upvoted
                already_upvoted = any(vote['userId'] == user_id for vote in upvotes)
                if not already_upvoted:
                    upvotes.append({"userId": user_id, "date": current_time})
                    is_new_upvote = True
                
                # Remove downvote if exists
                downvotes = [vote for vote in downvotes if vote['userId'] != user_id]

            elif action == "downvote":
                # Check if user has already downvoted
                already_downvoted = any(vote['userId'] == user_id for vote in downvotes)
                if not already_downvoted:
                    downvotes.append({"userId": user_id, "date": current_time})
                
                # Remove upvote if exists and track that we're removing an upvote
                had_upvote = any(vote['userId'] == user_id for vote in upvotes)
                upvotes = [vote for vote in upvotes if vote['userId'] != user_id]

            elif action == "unupvote":
                upvotes = [vote for vote in upvotes if vote['userId'] != user_id]

            elif action == "undownvote":
                downvotes = [vote for vote in downvotes if vote['userId'] != user_id]

            if result:
                cur.execute("""
                    UPDATE "reviewsUserVotes"
                    SET upvotes = %s, downvotes = %s
                    WHERE id = %s;
                """, (json.dumps(upvotes), json.dumps(downvotes), result['id']))
            else:
                cur.execute("""
                    INSERT INTO "reviewsUserVotes" ("reviewId", upvotes, downvotes)
                    VALUES (%s, %s, %s);
                """, (review_id, json.dumps(upvotes), json.dumps(downvotes)))

            # # Process badge for upvote if this is a new upvote
            # badge_updates = []
            # if is_new_upvote:
            #     badge_updates = badge_helpers.process_badges_for_vote(conn, user_id, review_id, current_time)
            
            # conn.commit()
            
            # # Format badge updates for response
            # badge_details = []
            # if badge_updates:
            #     for badge_id, old_level, new_level in badge_updates:
            #         cur.execute("""
            #             SELECT "badgeName", "badgePhoto", "badgeDesc", "badgeType", "relatedEntity" 
            #             FROM "badges" 
            #             WHERE id = %s
            #         """, (badge_id,))
            #         badge = cur.fetchone()
            #         if badge:
            #             badge_details.append({
            #                 "badgeName": badge['badgeName'],
            #                 "badgeType": badge['badgeType'],
            #                 "relatedEntity": badge['relatedEntity'],
            #                 "oldLevel": old_level,
            #                 "newLevel": new_level
            #             })
            cur.execute(
                'SELECT "userID", "createdDate" FROM "reviews" WHERE id = %s',
                (review_id,)
            )
            review_row = cur.fetchone()
            if review_row:
                review_owner_id = review_row["userID"]          # the badge recipient
                review_created  = review_row["createdDate"]     # datetime from DB
            else:
                review_owner_id = None
                review_created  = None                          # should not happen

            # Convert the supplied vote time into a datetime object
            upvote_dt = datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S")

            # Award badge only if the up-vote is ≤ 7 days after the review date
            within_one_week = (
                review_created is not None
                and (upvote_dt - review_created) <= timedelta(weeks=1)
            )
            # Work out whether we just *added* or *removed* an up-vote
            is_removed_upvote = (
                action == "unupvote" or
                (action == "downvote" and 'had_upvote' in locals() and had_upvote)
            )

            if (is_new_upvote and within_one_week) or is_removed_upvote:
                # 1️⃣  Get DrinkGPT badge id
                cur.execute(
                    'SELECT id FROM "badges" WHERE "relatedEntity" = %s ORDER BY id LIMIT 1',
                    ('Upvote',)
                )
                row = cur.fetchone()
                if row:
                    upvote_badge_id = row['id']

                    # 2️⃣  Existing badge row?
                    cur.execute(
                        'SELECT id, "currentLevel", "currentProgress" '
                        'FROM "userBadges" '
                        'WHERE "userId" = %s AND "badgeId" = %s',
                        (review_owner_id, upvote_badge_id)
                    )
                    ub = cur.fetchone()

                    # 3️⃣  Pull rules once
                    cur.execute(
                        'SELECT "levelStart","levelEnd","actionsRequired" '
                        'FROM "badgeRules" '
                        'WHERE "actionType" = %s ORDER BY "levelStart"',
                        ('Upvote',)
                    )
                    rules = cur.fetchall()

                    def needed_for(lvl: int) -> int:
                        for r in rules:
                            if r["levelStart"] <= lvl <= r["levelEnd"]:
                                return r["actionsRequired"]
                        return rules[-1]["actionsRequired"]

                    old_level = ub["currentLevel"] if ub else 0
                    new_level = old_level

                    # 4️⃣  Apply +1 or -1 change
                    if is_new_upvote:
                        if ub is None:
                            level, progress = 1, 1           # first ever +1
                            # create row straight away; we’ll update after levelling
                            cur.execute(
                                '''INSERT INTO "userBadges"
                                ("userId","badgeId","currentLevel","currentProgress",
                                    "dateEarned","lastUpdated")
                                VALUES (%s,%s,%s,%s,NOW(),NOW())''',
                                (review_owner_id, upvote_badge_id, level, progress)
                            )
                        else:
                            level    = ub["currentLevel"]
                            progress = ub["currentProgress"] + 1
                    else:   # an up-vote was removed
                        if ub is None:
                            # User had no badge – nothing to roll back
                            level = progress = 0
                        else:
                            level    = ub["currentLevel"]
                            progress = ub["currentProgress"] - 1

                    # 5️⃣  Level-up / Level-down math
                    if ub is not None or is_new_upvote:
                        # promote while enough progress
                        while progress >= needed_for(level) and level < 100:
                            progress -= needed_for(level)
                            level    += 1
                        # demote while progress went negative
                        while progress < 0 and level > 1:
                            level   -= 1
                            progress += needed_for(level)

                        # 6️⃣  Delete badge if back to level-1 & no progress
                        if level == 1 and progress <= 0:
                            cur.execute(
                                'DELETE FROM "userBadges" WHERE "userId" = %s AND "badgeId" = %s',
                                (review_owner_id, upvote_badge_id)
                            )
                            new_level = 0
                        else:
                            new_level = level
                            cur.execute(
                                '''UPDATE "userBadges"
                                SET "currentLevel"   = %s,
                                    "currentProgress" = %s,
                                    "lastUpdated"    = NOW()
                                WHERE "userId" = %s AND "badgeId" = %s''',
                                (level, progress, review_owner_id, upvote_badge_id)
                            )

                    # 7️⃣  Capture change for response
                    if old_level != new_level:
                        if "badge_updates" not in locals():
                            badge_updates = []
                        badge_updates.append((upvote_badge_id, old_level, new_level))

                conn.commit()

            return jsonify({
                "code": 201,
                "data": {
                    "upvotes": upvotes,
                    "downvotes": downvotes
                },
                # "badgeUpdates": badge_details
            }), 201

        except Exception as e:
            print(str(e))
            conn.rollback()
            return jsonify({
                "code": 500,
                "message": "An error occurred updating the votes.",
                "details": str(e)
            }), 500

# -----------------------------------------------------------------------------------------
    
# [PUT] Update review
# - Update review with review metrics
# - Possible return codes: 200 (Updated), 400(Review not found), 500 (Error during update)
@blueprint.route('/updateReview/<id>', methods=['PUT'])
def updateReview(id):
    conn = g.db
    cur = conn.cursor()
    data = request.get_json()

    # Parse the date from the request body
    try:
        created_date = datetime.strptime(data.get('createdDate', ''), "%a, %d %b %Y %H:%M:%S %Z")
    except ValueError:
        return jsonify({
            "code": 400,
            "message": "Invalid date format."
        }), 400

    # Check if review exists
    cur.execute("""
        SELECT * FROM "reviews" WHERE "id" = %s
    """, (id,))
    existing_review = cur.fetchone()

    if existing_review is None:
        return jsonify({
            "code": 400,
            "data": {
                "reviewDesc": data.get('reviewDesc', '')
            },
            "message": "Review does not exist."
        }), 400
    
    # Get proof points from pointSystemRules (id 2 to 6)
    cur.execute("""SELECT * FROM "pointSystemRules" WHERE "id" BETWEEN 2 AND 6""")
    point_system_rules = cur.fetchall()

    # Check the difference between the new review and the existing review
    remove_component = []
    added_component = []

    # [1] Check if text review was removed
    if (not data['reviewDesc'] and existing_review['reviewDesc']):
        remove_component.append(2)
    elif (data['reviewDesc'] and not existing_review['reviewDesc']):
        added_component.append(2)

    # [2] Check if extensive review was removed or added
    updated_review_ext_color = bool(data.get('colour'))
    updated_review_ext_aroma = bool(data.get('aroma'))
    updated_review_ext_taste = bool(data.get('taste'))
    updated_review_ext_finish = bool(data.get('finish'))

    current_review_ext_color = bool(existing_review.get('colour'))
    current_review_ext_aroma = bool(existing_review.get('aroma'))
    current_review_ext_taste = bool(existing_review.get('taste'))
    current_review_ext_finish = bool(existing_review.get('finish'))

   # Count how many fields exist in current and updated review
    current_count = sum([
        current_review_ext_color,
        current_review_ext_aroma,
        current_review_ext_taste,
        current_review_ext_finish
    ])

    updated_count = sum([
        updated_review_ext_color,
        updated_review_ext_aroma,
        updated_review_ext_taste,
        updated_review_ext_finish
    ])

    # Check if anything was removed or added
    if updated_count > 0 and current_count == 0:
        added_component.append(3)
    elif updated_count == 0 and current_count > 0:
        remove_component.append(3)
    
    # [3] Check if photo was removed or added
    if is_empty_photo(data['photo']) and is_non_empty_photo(existing_review['photo']):
        remove_component.append(4)
    # Check if photo was added
    elif is_non_empty_photo(data['photo']) and is_empty_photo(existing_review['photo']):
        added_component.append(4)

    # [4] Check if location was removed or added
    if (not data.get('location') and existing_review.get('location')):
        remove_component.append(5)
    elif (data.get('location') and not existing_review.get('location')):
        added_component.append(5)

    # [5] Check if tagged users were removed or added
    if (not data.get('taggedUsers') and existing_review.get('taggedUsers')):
        remove_component.append(6)
    elif (data.get('taggedUsers') and not existing_review.get('taggedUsers')):
        added_component.append(6)

    # Insert or find the venue
    venue_id = None
    location_name = data.get('location')
    address = data.get('address')

    if location_name and address:
        cur.execute("""
            SELECT "id" FROM "venues" WHERE "venueName" = %s AND "address" = %s
        """, (location_name, address))
        venue_row = cur.fetchone()
        venue_id = venue_row['id'] if venue_row else None

        if not venue_id:
            username = create_username(location_name)  # Assuming this is an existing function
            insert_venue_sql = """INSERT INTO venues ("venueName", "address", "venueType", "originLocation", "venueDesc",
                                  "hashedPassword", "claimStatus", photo, "reservationDetails", username)
                                  VALUES (%s, %s, '', '', '', %s, FALSE, '', '', %s) RETURNING id"""
            hashed_password = 'hashed_password'  # Replace with actual password hashing logic
            cur.execute(insert_venue_sql, (location_name, address, hashed_password, username))
            venue_row = cur.fetchone()
            venue_id = venue_row['id'] if venue_row else None
            print("Venue ID: ", venue_id)
            conn.commit()

    # Update review photo
    if existing_review['photo'] and data.get('photo') != existing_review['photo']:
        s3Images.deleteImageFromS3(existing_review['photo'])
    if data.get('photo') and data.get('photo') != existing_review['photo']:
        data['photo'] = s3Images.uploadBase64ImageToS3(data['photo'])

    tagged_users = data.get('taggedUsers', [])
    flavour_tags = data.get('flavourTag', [])
    observation_tags = data.get('observationTag', [])

    update_review_sql = """
        UPDATE "reviews"
        SET "userID" = %s, "reviewTarget" = %s, "rating" = %s, "reviewDesc" = %s, "reviewType" = %s, "createdDate" = %s,
            "language" = %s, "finish" = %s, "willRecommend" = %s, "wouldBuyAgain" = %s, "taggedUsers" = %s, "flavourTag" = %s,
            "photo" = %s, "colour" = %s, "aroma" = %s, "taste" = %s, "observationTag" = %s, "location" = %s, "address" = %s
        WHERE "id" = %s
    """

    review_values = (
        data.get('userID'), data.get('reviewTarget'), float(data.get('rating', 0.0)), data.get('reviewDesc'),
        data.get('reviewType'), created_date,
        data.get('language'), data.get('finish'), data.get('willRecommend', False), data.get('wouldBuyAgain', False),
        tagged_users, flavour_tags, data.get('photo'), data.get('colour'), data.get('aroma'), data.get('taste'),
        observation_tags, venue_id, address, id
    )

    try:
        # Update the review in the database
        cur.execute(update_review_sql, review_values)
        
        # Process badge changes for the edited review
        badge_updates = badge_helpers.process_badges_for_review_edit(
            conn, data.get('userID'), existing_review, data, id
        )
        
        # Update user points 
        modify_point = 0
        if remove_component or added_component:
            for rule in point_system_rules:
                if rule['id'] in remove_component:
                    modify_point -= rule['proofPoints']
                elif rule['id'] in added_component:
                    modify_point += rule['proofPoints']

            if modify_point != 0:
                cur.execute("""
                    UPDATE "pointsRecorder"
                    SET "currentPoints" = "currentPoints" + %s
                    WHERE "id" = %s
                """, (modify_point, data.get('userID')))
                
            print("Additional points: ", modify_point)
        
        conn.commit()
        
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
            "code": 200,
            "data": data.get('reviewDesc', ''),
            "pointsChange": modify_point,
            "badgeUpdates": badge_details
        }), 200

    except Exception as e:
        print(str(e))
        conn.rollback()
        return jsonify({
            "code": 500,
            "data": {
                "reviewDesc": data.get('reviewDesc', '')
            },
            "message": "An error occurred updating the review.",
            "error": str(e)
        }), 500
    
# -----------------------------------------------------------------------------------------

# [POST] Vote producer review
# - Update producer review with new votes
# - Possible return codes: 201 (Updated), 500 (Error during update)
@blueprint.route('/voteProducerReview', methods=['POST'])
def voteProducerReview():
    conn = g.db
    data = request.get_json()

    review_id = data['reviewID']
    user_votes = data['userVotes']
    action = data['action']

    with conn.cursor() as cur:
        try:
            cur.execute("SELECT id, upvotes, downvotes FROM \"producerReviewsUserVotes\" WHERE \"reviewId\" = %s", (review_id,))
            result = cur.fetchone()
            print("Result: ", result)

            if result:
                cur.execute("""
                    UPDATE "producerReviewsUserVotes"
                    SET upvotes = %s, downvotes = %s
                    WHERE id = %s;
                """, (user_votes['upvotes'], user_votes['downvotes'], result['id']))

            else:
                cur.execute("""
                    INSERT INTO "producerReviewsUserVotes" ("reviewId", upvotes, downvotes)
                    VALUES (%s, %s, %s);
                """, (review_id, user_votes['upvotes'], user_votes['downvotes']))

            conn.commit()

            return jsonify({
                "code": 201,
                "data": {
                    "upvotes": current_upvotes if 'current_upvotes' in locals() else user_votes['upvotes'],
                    "downvotes": current_downvotes if 'current_downvotes' in locals() else user_votes['downvotes']
                }
            }), 201
        
        except Exception as e:
            print(str(e))
            conn.rollback()
            return jsonify({
                "code": 500,
                "message": "An error occurred updating the votes.",
                "details": str(e)
            }), 500
        
# -----------------------------------------------------------------------------------------

# [PUT] Update producer review
# - Update producer review with review metrics
# - Possible return codes: 200 (Updated), 400(Review not found), 500 (Error during update)
@blueprint.route('/updateProducerReview/<id>', methods=['PUT'])
def updateProducerReview(id):
    conn = g.db
    cur = conn.cursor()
    data = request.get_json()

    try:
        created_date = datetime.strptime(data.get('createdDate', ''), "%a, %d %b %Y %H:%M:%S %Z")
    except ValueError:
        return jsonify({"code": 400, "message": "Invalid date format."}), 400

    # Check if review exists
    cur.execute("""SELECT EXISTS(SELECT 1 FROM "producerReviews" WHERE id = %s)""", (id,))

    if not cur.fetchone()['exists']:
        return jsonify({"code": 400, "message": "Review does not exist."}), 400
    
    cur.execute("""SELECT photos FROM "producerReviews" WHERE id = %s""", (id,))
    old_photos = cur.fetchone()['photos'] or []
    
    from threading import Thread
    def async_delete_images(photo_list):
        for photo in photo_list:
            s3Images.deleteImageFromS3(photo)

    Thread(target=async_delete_images, args=(old_photos,)).start()


    new_photos = [s3Images.uploadBase64ImageToS3(photo) for photo in data.get('photos', []) if photo]

    update_review_sql = """
        UPDATE "producerReviews"
        SET "userID" = %s, "producerID" = %s, "rating" = %s, "reviewDesc" = %s, "createdDate" = %s, "photos" = %s
        WHERE "id" = %s
    """
    
    review_values = (
        data.get('userID'), data.get('producerID'), float(data.get('rating', 0.0)), data.get('reviewDesc'),
        created_date, new_photos, id
    )

    # Get the existing review 
    cur.execute("""SELECT * FROM "producerReviews" WHERE id = %s""", (id,))
    existing_review = cur.fetchone()

    # Get proof points from pointSystemRules (id 2 and 4)
    cur.execute("""SELECT * FROM "pointSystemRules" WHERE "id" IN (2, 4)""")
    point_system_rules = cur.fetchall()

    # Check the difference between the new review and the existing review
    remove_component = []
    added_component = []

    print("New data: ", data)
    print("Old Data: ", existing_review)

    # ===== Need to edit this part =====
    # [1] Check if photo was removed or added  
    if data['photos'] == [] and existing_review['photos'] != []:
        remove_component.append(4)
    elif data.get('photos') and existing_review['photos'] == []:
        added_component.append(4)

    # =========================================

    try:
        cur.execute(update_review_sql, review_values)
        conn.commit()

        # Update user points
        modify_point = 0
        if remove_component or added_component:
            for rule in point_system_rules:
                if rule['id'] in remove_component:
                    modify_point -= rule['proofPoints']
                elif rule['id'] in added_component:
                    modify_point += rule['proofPoints']

            cur.execute("""
                UPDATE "pointsRecorder"
                SET "currentPoints" = "currentPoints" + %s
                WHERE "id" = %s
            """, (modify_point, data.get('userID')))
            conn.commit()

            print("Additional points: ", modify_point)

        return jsonify({"code": 200, "data": data.get('reviewDesc', '')}), 200

    except Exception as e:
        print(str(e))
        return jsonify({"code": 500, "message": "An error occurred updating the review."}), 500
    
# -----------------------------------------------------------------------------------------
# [POST] Vote venue review
# - Update venue review with new votes
# - Possible return codes: 201 (Updated), 500 (Error during update)
@blueprint.route('/voteVenueReview', methods=['POST'])
def voteVenueReview():
    conn = g.db
    data = request.get_json()

    review_id = data['reviewID']
    user_votes = data['userVotes']
    action = data['action']

    with conn.cursor() as cur:
        try:
            cur.execute(
                "SELECT id, upvotes, downvotes FROM \"venueReviewsUserVotes\" WHERE \"reviewId\" = %s",
                (review_id,)
            )
            result = cur.fetchone()
            print("Result: ", result)

            if result:
                cur.execute("""
                    UPDATE "venueReviewsUserVotes"
                    SET upvotes = %s, downvotes = %s
                    WHERE id = %s;
                """, (user_votes['upvotes'], user_votes['downvotes'], result['id']))
            else:
                cur.execute("""
                    INSERT INTO "venueReviewsUserVotes" ("reviewId", upvotes, downvotes)
                    VALUES (%s, %s, %s);
                """, (review_id, user_votes['upvotes'], user_votes['downvotes']))

            conn.commit()

            return jsonify({
                "code": 201,
                "data": {
                    "upvotes": user_votes['upvotes'],
                    "downvotes": user_votes['downvotes']
                }
            }), 201

        except Exception as e:
            print(str(e))
            conn.rollback()
            return jsonify({
                "code": 500,
                "message": "An error occurred updating the votes.",
                "details": str(e)
            }), 500

# -----------------------------------------------------------------------------------------
# [PUT] Update venue review
# - Update venue review with review metrics
# - Possible return codes: 200 (Updated), 400 (Review not found), 500 (Error during update)
@blueprint.route('/updateVenueReview/<id>', methods=['PUT'])
def updateVenueReview(id):
    conn = g.db
    cur = conn.cursor()
    data = request.get_json()

    try:
        created_date = datetime.strptime(data.get('createdDate', ''), "%a, %d %b %Y %H:%M:%S %Z")
    except ValueError:
        return jsonify({"code": 400, "message": "Invalid date format."}), 400

    # Check if review exists
    cur.execute("""SELECT EXISTS(SELECT 1 FROM "venueReviews" WHERE id = %s)""", (id,))
    if not cur.fetchone()['exists']:
        return jsonify({"code": 400, "message": "Review does not exist."}), 400

    cur.execute("""SELECT photos FROM "venueReviews" WHERE id = %s""", (id,))
    old_photos = cur.fetchone()['photos'] or []

    from threading import Thread
    def async_delete_images(photo_list):
        for photo in photo_list:
            s3Images.deleteImageFromS3(photo)

    Thread(target=async_delete_images, args=(old_photos,)).start()

    new_photos = [s3Images.uploadBase64ImageToS3(photo) for photo in data.get('photos', []) if photo]

    update_review_sql = """
        UPDATE "venueReviews"
        SET "userID" = %s, "venueID" = %s, "rating" = %s, "reviewDesc" = %s, "createdDate" = %s, "photos" = %s
        WHERE "id" = %s
    """
    
    review_values = (
        data.get('userID'),
        data.get('venueID'),
        float(data.get('rating', 0.0)),
        data.get('reviewDesc'),
        created_date,
        new_photos,
        id
    )

    try:
        cur.execute(update_review_sql, review_values)
        conn.commit()
        return jsonify({"code": 200, "data": data.get('reviewDesc', '')}), 200

    except Exception as e:
        print(str(e))
        return jsonify({"code": 500, "message": "An error occurred updating the review."}), 500


