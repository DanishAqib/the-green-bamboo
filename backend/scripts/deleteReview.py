# Port: 5023
# Routes: /deleteReview/<id> (DELETE), /deleteProducerReview/<id> (DELETE) , /deleteVenueReview/<id> (DELETE)
# -----------------------------------------------------------------------------------------

# [OLD] TO BE DELETED FOR POSTGRES:
# ------------------------------------------------------


# ======================================================

# [NEW] TO BE ADDED FOR POSTGRES:
# ------------------------------------------------------


# ======================================================
import os
import s3Images
import json
from flask import Blueprint, g, request, jsonify
# [OLD] TO BE DELETED FOR POSTGRES:
# ------------------------------------------------------
from bson import json_util
from bson.objectid import ObjectId
from scripts import badge_helpers
# ======================================================

# [NEW] TO BE ADDED FOR POSTGRES:
# ------------------------------------------------------
# import psycopg2
# from psycopg2.extras import RealDictCursor
# ======================================================


file_name = os.path.basename(__file__)
blueprint = Blueprint(file_name[:-3], __name__)


# [OLD] TO BE DELETED FOR POSTGRES:
# ------------------------------------------------------
def parse_json(data):
    return json.loads(json_util.dumps(data))
# ======================================================

# -----------------------------------------------------------------------------------------
# [DELETE] Deletes a review
# - Delete entry with specified id from the "reviews" collection.
# - Possible return codes: 201 (Deleted), 400 (Review doesn't exist), 500 (Error during deletion)


@blueprint.route("/deleteReview/<id>", methods=['DELETE'])
def deleteReview(id):
    """
    Delete a review and update associated badges and points
    
    This function:
    1. Finds and validates the review
    2. Calculates points to deduct
    3. Processes badge updates for all relevant badge types
    4. Deletes the review and associated data
    5. Returns the results with badge updates
    """
    conn = g.db
    cur = conn.cursor()

    # Step 1: Find and validate the review
    cur.execute("SELECT * FROM reviews WHERE id = %s", (id,))
    existingReview = cur.fetchone()

    if existingReview is None:
        return jsonify({   
            "code": 400,
            "data": {"id": id},
            "message": "Review doesn't exist."
        }), 400
    
    # Step 2: Calculate points to deduct based on review content
    rule_points_id = []

    # Basic review text
    if existingReview.get('reviewDesc'):
        rule_points_id.append(2)

    # Extended review details
    has_extended_details = any([
        existingReview.get('finish'), 
        existingReview.get('colour'),
        existingReview.get('aroma'), 
        existingReview.get('taste')
    ])
    if has_extended_details:
        rule_points_id.append(3)

    # Photo attached
    if existingReview.get('photo'):
        rule_points_id.append(4)

    # Location tagged
    if existingReview.get('location'):
        rule_points_id.append(5)

    # Friends tagged
    if existingReview.get('taggedUsers'):
        rule_points_id.append(6)

    # Get total points to deduct
    total_points = 0
    if rule_points_id:
        # Fix: Handle the case where rule_points_id has only one element
        if len(rule_points_id) == 1:
            cur.execute('SELECT "proofPoints" FROM "pointSystemRules" WHERE id = %s', 
                       (rule_points_id[0],))
            result = cur.fetchone()
            total_points = result['proofPoints'] if result else 0
        else:
            cur.execute('SELECT SUM("proofPoints") FROM "pointSystemRules" WHERE id IN %s', 
                       (tuple(rule_points_id),))
            result = cur.fetchone()
            # Fix: Handle the case where sum returns NULL
            total_points = result['sum'] if result and result['sum'] is not None else 0

    try:
        # Step 3: Get drink information for badge processing
        cur.execute("""
            SELECT "drinkType", "typeCategory", "originCountry"
            FROM "listings"
            WHERE "id" = %s
        """, (existingReview['reviewTarget'],))
        
        drink = cur.fetchone()
        if not drink:
            # Handle case where drink no longer exists
            drink = {'drinkType': None, 'typeCategory': None, 'originCountry': None}
        
        # Step 4: Process all badge updates
        badge_updates = []
        
        # Country badge
        if drink['originCountry']:
            country_updates = badge_helpers.remove_badge_action(
                conn, 
                existingReview['userID'],  # user ID
                'Review',                 # action type  
                drink['originCountry'],    # related entity (country name)
                id,                        # entity ID (review ID)
                'review'                   # entity type
            )
            badge_updates.extend(country_updates)
        
        # Drink Type badge
        if drink['drinkType']:
            type_updates = badge_helpers.remove_badge_action(
                conn, 
                existingReview['userID'], 
                'Review', 
                drink['drinkType'], 
                id, 
                'review'
            )
            badge_updates.extend(type_updates)
        
        # Category badge
        if drink['typeCategory']:
            category_updates = badge_helpers.remove_badge_action(
                conn, 
                existingReview['userID'], 
                'Review', 
                drink['typeCategory'], 
                id, 
                'review'
            )
            badge_updates.extend(category_updates)
        
        # General Review badge
        review_updates = badge_helpers.remove_badge_action(
            conn, 
            existingReview['userID'], 
            'Review', 
            None, 
            id, 
            'review'
        )
        badge_updates.extend(review_updates)
        
        # Extensive Review badge
        if has_extended_details:
            extensive_updates = badge_helpers.remove_badge_action(
                conn, 
                existingReview['userID'], 
                'ExtensiveReview', 
                None, 
                id, 
                'review'
            )
            badge_updates.extend(extensive_updates)
        
        # Photo badge
        if existingReview.get('photo'):
            # Delete the image from S3
            if existingReview['photo']:
                s3Images.deleteImageFromS3(existingReview['photo'])
                
            photo_updates = badge_helpers.remove_badge_action(
                conn, 
                existingReview['userID'], 
                'PhotoAttached', 
                None, 
                id, 
                'review'
            )
            badge_updates.extend(photo_updates)
        
        # Location badge
        if existingReview.get('location'):
            location_updates = badge_helpers.remove_badge_action(
                conn, 
                existingReview['userID'], 
                'LocationTagged', 
                None, 
                id, 
                'review'
            )
            badge_updates.extend(location_updates)
        
        # Friend tagged badge
        if existingReview.get('taggedUsers'):
            friend_updates = badge_helpers.remove_badge_action(
                conn, 
                existingReview['userID'], 
                'FriendTagged', 
                None, 
                id, 
                'review'
            )
            badge_updates.extend(friend_updates)
        
        # Step 5: Delete the review and associated data
        # Delete associated votes
        cur.execute('DELETE FROM "reviewsUserVotes" WHERE "reviewId" = %s', (id,))
        
        # Delete the review itself
        cur.execute('DELETE FROM reviews WHERE id = %s', (id,))
        
        # Step 6: Format badge updates for the response
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
        
        # Step 7: Update user points
        if total_points > 0:
            cur.execute("""
                UPDATE "pointsRecorder" 
                SET "currentPoints" = "currentPoints" - %s 
                WHERE id = %s AND "userType" = %s
            """, (total_points, existingReview['userID'], 'user'))
            
        # Commit all changes
        conn.commit()
        
        # Return success response with details
        return jsonify({   
            "code": 200,
            "data": id,
            "deductedPoints": total_points,
            "badgeUpdates": badge_details
        }), 200

    except Exception as e:
        # Roll back any changes if an error occurs
        conn.rollback()
        print(str(e))
        import traceback
        traceback.print_exc()
        
        return jsonify({
            "code": 500,
            "data": {"id": id},
            "message": "An error occurred deleting the review.",
            "error": str(e)
        }), 500
    
# -----------------------------------------------------------------------------------------
# [DELETE] Deletes a producer review
# - Delete entry with specified id from the "producerReviews" collection.
# - Possible return codes: 201 (Deleted), 400 (Review doesn't exist), 500 (Error during deletion)
@blueprint.route("/deleteProducerReview/<id>", methods=['DELETE'])
def deleteProducerReview(id):
    conn = g.db
    cur = conn.cursor()

    cur.execute("""SELECT EXISTS(SELECT 1 FROM "producerReviews" WHERE id = %s)""", (id,))
    exists = cur.fetchone()['exists']

    if not exists:
        return jsonify(
            {   
                "code": 400,
                "data": {"id": id},
                "message": "Review doesn't exist."
            }
        ), 400

    try:
        # Fetch the points for simple review
        cur.execute('SELECT "proofPoints" FROM "pointSystemRules" WHERE id = 2')
        points = cur.fetchone()['proofPoints']

        # Fetch only the photos instead of the entire review
        cur.execute("""SELECT "userID", photos FROM "producerReviews" WHERE id = %s""", (id,))
        results = cur.fetchone()
        photos = results['photos']
        userID = results['userID']

        if photos:

            # Get points for image upload
            cur.execute('SELECT "proofPoints" FROM "pointSystemRules" WHERE id = 4')
            points += cur.fetchone()['proofPoints']

            from threading import Thread
            def async_delete_images(photo_list):
                for photo in photo_list:
                    s3Images.deleteImageFromS3(photo)

            Thread(target=async_delete_images, args=(photos,)).start()

        cur.execute("DELETE FROM \"producerReviewsUserVotes\" WHERE \"reviewId\" = %s", (id,))
        cur.execute("DELETE FROM \"producerReviews\" WHERE id = %s RETURNING id", (id,))
        
        conn.commit()

        # Update user points
        cur.execute('UPDATE "pointsRecorder" SET "currentPoints" = "currentPoints" - %s WHERE id = %s AND "userType" = %s', (points, userID, 'user',))
        conn.commit()

        print(f"Deducted {points} points from user {userID} for deleting review {id}.")

        return jsonify({"code": 200, "data": id}), 200

    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": {"id": id},
                "message": "An error occurred deleting the listing."
            }
        ), 500
    
# -----------------------------------------------------------------------------------------
# [DELETE] Deletes a venue review
# - Delete entry with specified id from the "venueReviews" collection.
# - Possible return codes: 200 (Deleted), 400 (Review doesn't exist), 500 (Error during deletion)
@blueprint.route("/deleteVenueReview/<id>", methods=['DELETE'])
def deleteVenueReview(id):
    conn = g.db
    cur = conn.cursor()

    cur.execute("""SELECT EXISTS(SELECT 1 FROM "venueReviews" WHERE id = %s)""", (id,))
    exists = cur.fetchone()['exists']

    if not exists:
        return jsonify(
            {
                "code": 400,
                "data": {"id": id},
                "message": "Review doesn't exist."
            }
        ), 400

    try:
        # Fetch only the photos instead of the entire review
        cur.execute("""SELECT photos FROM "venueReviews" WHERE id = %s""", (id,))
        photos = cur.fetchone()['photos']

        if photos:
            from threading import Thread
            def async_delete_images(photo_list):
                for photo in photo_list:
                    s3Images.deleteImageFromS3(photo)
            Thread(target=async_delete_images, args=(photos,)).start()

        cur.execute("DELETE FROM \"venueReviewsUserVotes\" WHERE \"reviewId\" = %s", (id,))
        cur.execute("DELETE FROM \"venueReviews\" WHERE id = %s RETURNING id", (id,))

        conn.commit()

        return jsonify({"code": 200, "data": id}), 200

    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": {"id": id},
                "message": "An error occurred deleting the review."
            }
        ), 500
