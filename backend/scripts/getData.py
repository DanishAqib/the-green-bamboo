# Port: 5000
# Routes: /getAccountRequests (GET), /getCountries (GET), /getListings (GET), /getListing/<id> (GET), /getProducers (GET), /getProducer/<id> (GET),
#           /getReviews (GET), /getReviewByTarget/<id> (GET), /getReviewsByUserIds (GET), /getUsers (GET), /getUser/<id> (GET), /getUserByUsername/<username> (GET), /getVenues (GET), 
#           /getVenue/<id> (GET), /getVenuesAPI (GET), /getDrinkTypes (GET), /getRequestListings (GET), /getRequestListing/<id> (GET), /getRequestEdits (GET), 
#           /getRequestEdit/<id> (GET), /getModRequests (GET), /getFlavourTags (GET), /getSubTags (GET), /getObservationTags (GET), /getColours (GET), 
#           /getSpecialColours (GET), /getLanguages (GET), /getServingTypes (GET), /getProducersProfileViews (GET), /getVenuesProfileViewsByVenue/<id> (GET), /getRequestInaccuracyByVenue/<id> (GET)
# -----------------------------------------------------------------------------------------

# pip install python-bsonjs
# pip install Flask
# pip install Flask Flask-PyMongo
# pip install pymongo
# pip install flask-cors

import os
import json
from bson import json_util, ObjectId
from flask import Blueprint, g, jsonify, request
from bson.objectid import ObjectId

file_name = os.path.basename(__file__)
blueprint = Blueprint(file_name[:-3], __name__)

# converts BSON to JSON
def parse_json(data):
    return json.loads(json_util.dumps(data))

# Helper function to fetch user data from the database
def fetch_user_data(cursor, user_id):
    cursor.execute('SELECT * FROM "users" WHERE "id" = %s', (user_id,))
    return cursor.fetchone()

# Helper function to fetch drink lists for a user
def fetch_drink_lists(cursor, user_id):

    cursor.execute("""
        SELECT "listName", "drinks"
        FROM "usersDrinkLists"
        WHERE "userId" = %s
    """, (user_id,))
    drink_lists_data = cursor.fetchall()
    result = {}
    for row in drink_lists_data:
            list_name = row["listName"]
            drinks = row["drinks"]
            result[list_name] = {
                "listDesc": "",  # You can customize or fetch descriptions for each list if needed
                "listItems": drinks if drinks else []
            }
    return result

# Helper function to fetch follow lists for a user
def fetch_follow_lists(cursor, user_id):
    cursor.execute("""
        SELECT "users", "producers", "venues"
        FROM "usersFollowLists"
        WHERE "userId" = %s
    """, (user_id,))
    follow_lists_data = cursor.fetchone()
    
    return {
        "users": follow_lists_data["users"] if follow_lists_data and follow_lists_data["users"] else [],
        "producers": follow_lists_data["producers"] if follow_lists_data and follow_lists_data["producers"] else [],
        "venues": follow_lists_data["venues"] if follow_lists_data and follow_lists_data["venues"] else []
    }

# def modifyPhotos():
#     data = db.producers.find({})
#     dataEncode = parse_json(data)
#     for doc in dataEncode:
#         try:
#             if(doc['photo']):
#                 photo = s3Images.uploadBase64ImageToS3(doc['photo'])
#                 updateImage = db.producers.update_one({'_id': ObjectId(doc['_id']['$oid'])}, {'$set': {'photo': photo, 'updates': []}})
#         except Exception as e:
#             print(e)
#         print(doc['_id'])

# modifyPhotos()

# -----------------------------------------------------------------------------------------
# [GET] accountRequests
@blueprint.route('/getAccountRequests', methods=['GET'])
def getAccountRequests():
    conn = g.db
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM "accountRequests"')
        allAccountRequests = cursor.fetchall()

    if not allAccountRequests:
        return jsonify([])

    return jsonify(allAccountRequests)

# -----------------------------------------------------------------------------------------
# [GET] Countries
@blueprint.route('/getCountries', methods=['GET'])
def getCountries():
    conn = g.db
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM countries")
        allCountries = cursor.fetchall()

    if not allCountries:
        return jsonify([])
    
    return jsonify(allCountries)

# -----------------------------------------------------------------------------------------
# [GET] Listings
@blueprint.route("/getListings")
def getListings():
    conn = g.db

    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM "listings"')
        listings_data = cursor.fetchall()
    
    if not listings_data:
        return jsonify([])

    return jsonify(listings_data)

# [GET] Get Listings from db where id> last item in list
@blueprint.route("/getNext30/<id>")
def getNext30(id):
    conn = g.db
    id = int(id)
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM "listings" where "id" > %s LIMIT 30', (id,))
        listings_data = cursor.fetchall()
    
    if not listings_data:
        return jsonify([])

    return jsonify(listings_data)

# [GET] Listings
@blueprint.route("/getFiltered30/<id>")
def getFiltered30(id):
    conn = g.db
    id = int(id)
    drinkType= request.args.get('drinkType')  # e.g. ?age=30
    drinkCategory = request.args.get('drinkCategory')
    # if drinkType:
    #     condition1 = 'AND "drinkType" = %s', drinkType
    # else:
    #     condition1 = ''
    # if drinkCategory:
    #     condition2 = 'AND "drinkCategory" = %s', drinkCategory
    # else:
    #     condition2 = ''
    # print(condition1)
    # print(condition2)
    with conn.cursor() as cursor:
        if(drinkType and drinkCategory):
            cursor.execute('SELECT * FROM "listings" where "id" > %s AND "drinkType" = %s AND "typeCategory" = %s LIMIT 30', (id,drinkType,drinkCategory,))
        elif(drinkType):
            cursor.execute('SELECT * FROM "listings" where "id" > %s AND "drinkType" = %s LIMIT 30', (id,drinkType,))      
        else:
            cursor.execute('SELECT * FROM "listings" where "id" > %s LIMIT 30', (id,))
        listings_data = cursor.fetchall()
    
    if not listings_data:
        return jsonify([])

    return jsonify(listings_data)

# [GET] Specific Listing
@blueprint.route("/getListing/<id>")
def getListing(id):
    conn = g.db

    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM "listings" WHERE "id" = %s', (id,))
        listing_data = cursor.fetchone()

    if listing_data is None:
        return jsonify([])
    
    return jsonify(listing_data)

# [GET] Specific Listings By Producer
@blueprint.route("/getListingsByProducer/<id>")
def getListingsByProducer(id):
    conn = g.db

    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM "listings" WHERE "producerID" = %s', (id,))
        listings_data = cursor.fetchall()

    if not listings_data:
        return jsonify([])

    return jsonify(listings_data)

# -----------------------------------------------------------------------------------------

# ================== POSTGRESQL FORMAT ==================

# ----------------------
# [OLD] TO BE DELETED:
# ----------------------

# [GET] Producers
@blueprint.route("/getProducers")
def getProducers():
    conn = g.db
    cur = conn.cursor()

    try:
        # Query to get producers and related data
        query = """
            SELECT 
                p.id, p."producerName", p."producerDesc", p."originCountry", p."mainDrinks", p.photo, 
                p."hashedPassword", p."claimStatus", p."statusOB", p.username, p."producerLink", 
                p."stripeCustomerId", p."claimStatusCheckDate",
                COALESCE((
                    SELECT json_agg(json_build_object(
                        'id', qa.id,
                        'question', qa.question,
                        'answer', qa.answer,
                        'date', qa.date,
                        'userId', qa."userId",
                        'producerId', qa."producerId"
                    ))
                    FROM "producersQuestionAnswers" qa
                    WHERE qa."producerId" = p.id
                ), '[]') AS "questionsAnswers",
                COALESCE((
                    SELECT json_agg(json_build_object(
                        'id', u.id,
                        'date', u.date,
                        'text', u.text,
                        'photo', u.photo,
                        'producerId', u."producerId",
                        'likes', COALESCE((
                            SELECT json_agg(json_build_object('userId', l."userId", 'userType', l."userType"))
                            FROM "producerUpdateLikes" l
                            WHERE l."updateId" = u.id
                        ), '[]')
                    ) ORDER BY u.id)
                    FROM "producersUpdates" u
                    WHERE u."producerId" = p.id
                ), '[]') AS updates
            FROM producers p
            ORDER BY p.id
        """

        cur.execute(query)
        producers_data = cur.fetchall()

        if not producers_data:
            return jsonify([])

        producers_list = []
        for row in producers_data:
            producer = dict(row)
            producer['questionsAnswers'] = producer['questionsAnswers'] if producer['questionsAnswers'] else []
            producer['updates'] = producer['updates'] if producer['updates'] else []
            producers_list.append(producer)

        return jsonify(producers_list), 200

    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred retrieving producers."
            }
        ), 500

    finally:
        cur.close()

# [GET] Specific Producer
@blueprint.route("/getProducer/<int:id>")
def getProducer(id):
    conn = g.db
    cur = conn.cursor()

    try:
        # Query to get a specific producer and related data
        query = """
            SELECT 
                p.id, p."producerName", p."producerDesc", p."originCountry", p."mainDrinks", p.photo, 
                p."hashedPassword", p."claimStatus", p."statusOB", p.username, p."producerLink", 
                p."stripeCustomerId", p."claimStatusCheckDate",
                COALESCE((
                    SELECT json_agg(json_build_object(
                        'id', qa.id,
                        'question', qa.question,
                        'answer', qa.answer,
                        'date', qa.date,
                        'userId', qa."userId",
                        'producerId', qa."producerId"
                    ))
                    FROM "producersQuestionAnswers" qa
                    WHERE qa."producerId" = p.id
                ), '[]') AS "questionsAnswers",
                COALESCE((
                    SELECT json_agg(json_build_object(
                        'id', u.id,
                        'date', u.date,
                        'text', u.text,
                        'photo', u.photo,
                        'producerId', u."producerId",
                        'likes', COALESCE((
                            SELECT json_agg(json_build_object('userId', l."userId", 'userType', l."userType"))
                            FROM "producerUpdateLikes" l
                            WHERE l."updateId" = u.id
                        ), '[]')
                    ))
                    FROM "producersUpdates" u
                    WHERE u."producerId" = p.id
                ), '[]') AS updates
            FROM producers p
            WHERE p.id = %s
        """

        cur.execute(query, (id,))
        producer_data = cur.fetchone()

        if producer_data is None:
            return jsonify({"message": "Producer not found"}), 404

        producer = dict(producer_data)
        producer['questionsAnswers'] = producer['questionsAnswers'] if producer['questionsAnswers'] else []
        producer['updates'] = producer['updates'] if producer['updates'] else []

        return jsonify(producer), 200

    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred retrieving the producer."
            }
        ), 500

    finally:
        cur.close()

# [GET] Specific Producer
@blueprint.route("/getProducerByRequestId/<id>")
def getProducerByRequestId(id):
    conn = g.db
    cur = conn.cursor()

    try:
        query = """
            SELECT 
                p.id, p."producerName", p."producerDesc", p."originCountry", p."mainDrinks", p.photo, 
                p."hashedPassword", p."claimStatus", p."statusOB", p.username, p."producerLink", 
                p."stripeCustomerId", p."claimStatusCheckDate",
                COALESCE((
                    SELECT json_agg(json_build_object(
                        'id', qa.id,
                        'question', qa.question,
                        'answer', qa.answer,
                        'date', qa.date,
                        'userId', qa."userId",
                        'producerId', qa."producerId"
                    ))
                    FROM "producersQuestionAnswers" qa
                    WHERE qa."producerId" = p.id
                ), '[]') AS "questionsAnswers",
                COALESCE((
                    SELECT json_agg(json_build_object(
                        'id', u.id,
                        'date', u.date,
                        'text', u.text,
                        'photo', u.photo,
                        'producerId', u."producerId",
                        'likes', COALESCE((
                            SELECT json_agg(json_build_object('userId', l."userId", 'userType', l."userType"))
                            FROM "producerUpdateLikes" l
                            WHERE l."updateId" = u.id
                        ), '[]')
                    ))
                    FROM "producersUpdates" u
                    WHERE u."producerId" = p.id
                ), '[]') AS updates
            FROM "producers" p
            WHERE p.id = %s
        """

        cur.execute(query, (id,))
        producer_data = cur.fetchone()

        if producer_data is None:
            return jsonify({"message": "Producer not found"}), 404

        producer = dict(producer_data)
        producer['questionsAnswers'] = producer['questionsAnswers'] if producer['questionsAnswers'] else []
        producer['updates'] = producer['updates'] if producer['updates'] else []

        return jsonify(producer), 200
    
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred retrieving the producer."
            }
        ), 500
    
    finally:
        cur.close()

# ----------------------
# [NEW] TO BE ADDED:
# ----------------------

# # [GET] Producers
# @blueprint.route("/getProducers")
# def getProducers():
#     db = g.db
#     # Fetch all producers
#     producers_data = db.producers.find({})
#     allProducers = []
#     for producer in producers_data:
#         # Fetch the related question answers based on the id stored in producer's questionAnswers
#         question_answers_data = db.producersQuestionAnswers.find({
#             "id": {"$in": producer['questionAnswers']}
#         })
#         producer['questionsAnswers'] = list(question_answers_data)
#         # Fetch the related updates based on the id stored in producer's updates
#         updates_data = db.producersUpdates.find({
#             "id": {"$in": producer['updates']}
#         })
#         producer['updates'] = list(updates_data)
#         allProducers.append(producer)
#     return parse_json(allProducers)

# # [GET] Specific Producer by ID
# @blueprint.route("/getProducer/<id>")
# def getProducer(id):
#     db = g.db
#     # Fetch the specific producer
#     producer = db.producers.find_one({"_id": ObjectId(id)})
#     if producer is None:
#         return []
#     # Fetch related question answers based on the id(s) in producer's questionAnswers
#     question_answers_data = db.producersQuestionAnswers.find({
#         "id": {"$in": producer['questionAnswers']}
#     })
#     producer['questionsAnswers'] = list(question_answers_data)
#     # Fetch related updates based on the id(s) in producer's updates
#     updates_data = db.producersUpdates.find({
#         "id": {"$in": producer['updates']}
#     })
#     producer['updates'] = list(updates_data)
#     return parse_json(producer)

# # [GET] Specific Producer by Request ID
# @blueprint.route("/getProducerByRequestId/<id>")
# def getProducerByRequestId(id):
#     db = g.db
#     # Fetch the specific producer by requestId
#     producer = db.producers.find_one({"requestId": ObjectId(id)})
#     if producer is None:
#         return []
#     # Fetch related question answers based on the id(s) in producer's questionAnswers
#     question_answers_data = db.producersQuestionAnswers.find({
#         "id": {"$in": producer['questionAnswers']}
#     })
#     producer['questionsAnswers'] = list(question_answers_data)
#     # Fetch related updates based on the id(s) in producer's updates
#     updates_data = db.producersUpdates.find({
#         "id": {"$in": producer['updates']}
#     })
#     producer['updates'] = list(updates_data)
#     return parse_json(producer)

# =======================================================

# -----------------------------------------------------------------------------------------

# ================== POSTGRESQL FORMAT ==================

# ----------------------
# [OLD] TO BE DELETED:
# ----------------------

# -- ========= [NEW!] "reviewsUserVotes" =========
# CREATE TABLE "reviewsUserVotes" (
#     "id" SERIAL PRIMARY KEY,
#     "upvotes" TEXT[], -- Contain "users"("id")s
#     "downvotes" TEXT[], -- Contain "users"("id")s
#     "reviewId" INTEGER REFERENCES "reviews"("id") on DELETE SET NULL -- [!] reference "reviews" FK
# );

# [GET] Reviews
@blueprint.route("/getReviews")
def getReviews():
    conn = g.db
    
    with conn.cursor() as cursor:
        cursor.execute("""
            SELECT "reviews".*, "reviewsUserVotes"."upvotes", "reviewsUserVotes"."downvotes"
            FROM "reviews"
            LEFT JOIN "reviewsUserVotes" ON "reviews"."id" = "reviewsUserVotes"."reviewId"
        """)

        reviews_data = cursor.fetchall()
    
    if not reviews_data:
        return jsonify([])

    for review in reviews_data:
        review["userVotes"] = {
            "upvotes": review["upvotes"] if review["upvotes"] else [],
            "downvotes": review["downvotes"] if review["downvotes"] else []
        }
        del review["upvotes"]
        del review["downvotes"]

    return jsonify(reviews_data)

# [GET] Specific Reviews by reviewTarget
@blueprint.route("/getReviewByTarget/<id>")
def getReviewByTarget(id):
    conn = g.db
    
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM "reviews" WHERE "reviewTarget" = %s', (id,))
        reviews_data = cursor.fetchall()
    
    if not reviews_data:
        return jsonify([])

    return jsonify(reviews_data)


# [GET] Latest 10 Specific Reviews by usr(s) - using one or more user IDs (retrieve latest reviews for the specified user(s) as well as the review target(s) data)
@blueprint.route("/getReviewsByUserIds")
def getReviewsByUserIds():

    user_ids_str = request.args.get('user_ids')
    user_ids = user_ids_str.split(',')
    conn = g.db
    
    with conn.cursor() as cursor:
        # Fetch latest reviews for the specified user(s)
        cursor.execute('''
            WITH latest_reviews AS (
                SELECT "reviewDesc", "rating", "reviewTarget", "createdDate", "userID"
                FROM "reviews"
                WHERE "userID" IN %s
                ORDER BY "createdDate" DESC
                LIMIT 10
            )
            SELECT "reviewDesc", "rating", "reviewTarget", "createdDate", "userID"
            FROM latest_reviews
            ORDER BY "createdDate" DESC;
        ''', (tuple(user_ids),))
        latest_reviews = cursor.fetchall()

        # Retrieve the display name(s) for each user
        cursor.execute('SELECT "id", "displayName", "photo" FROM "users" WHERE "id" IN %s', (tuple(user_ids),))
        user_display_names = cursor.fetchall()

        # Convert the user display names to dictionary format where the key is the user ID
        user_display_names = {user['id']: user for user in user_display_names}

        # Retrieve the review target(s) for each review
        review_target_list = []
        for review in latest_reviews:
            review = dict(review)
            if (review['reviewTarget'] not in review_target_list):
                review_target_list.append(review['reviewTarget'])
        
        # Fetch the review target(s) data
        cursor.execute('SELECT "id", "listingName", "photo" FROM "listings" WHERE "id" IN %s', (tuple(review_target_list),))
        review_targets_data = cursor.fetchall()

        # Map the review target data to the reviews
        for review in latest_reviews:
            review['userInfo'] = user_display_names[review['userID']]
            review['reviewTarget'] = next((item for item in review_targets_data if item["id"] == review['reviewTarget']), None)
        
        # Convert the reviews to JSON format
        latest_reviews = parse_json(latest_reviews)
    
    if not latest_reviews:
        return jsonify({
            'code': 404,
            'message': 'No reviews found for the specified user(s).'
        })

    return jsonify({
        'code': 200,
        'message': 'Latest reviews fetched successfully.',
        'data': latest_reviews
    })

# ----------------------
# [NEW] TO BE ADDED:
# ----------------------

# # [GET] Reviews
# @blueprint.route("/getReviews")
# def getReviews():
#     db = g.db
#     reviews_data = db.reviews.find({})
#     allReviews = []
#     for review in reviews_data:
#         # Fetch related user votes based on the id(s) in review's userVotes
#         user_votes_data = db.reviewsUserVotes.find({
#             "_id": {"$in": review['userVotes']}
#         })
#         review['userVotes'] = list(user_votes_data)
#         allReviews.append(review)
#     return parse_json(allReviews)

# # [GET] Specific Reviews by reviewTarget
# @blueprint.route("/getReviewByTarget/<id>")
# def getReviewByTarget(id):
#     db = g.db
#     reviews_data = db.reviews.find({"reviewTarget": ObjectId(id)})
#     if reviews_data is None:
#         return []
#     allReviews = []
#     for review in reviews_data:
#         # Fetch related user votes based on the id(s) in review's userVotes
#         user_votes_data = db.reviewsUserVotes.find({
#             "_id": {"$in": review['userVotes']}
#         })
#         review['userVotes'] = list(user_votes_data)
#         allReviews.append(review)
#     return parse_json(allReviews)

# =======================================================

# -----------------------------------------------------------------------------------------

# ================== POSTGRESQL FORMAT ==================

# ----------------------
# [OLD] TO BE DELETED:
# ----------------------

# [GET] Users
@blueprint.route("/getUsers")
def getUsers():
    conn = g.db
    
    try:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM "users"')
            users_data = cursor.fetchall()

            for user_data in users_data:
                user_id = user_data['id']
                
                user_data["drinkLists"] = fetch_drink_lists(cursor, user_id)
                user_data["followLists"] = fetch_follow_lists(cursor, user_id)

        return jsonify(users_data), 200

    except Exception as e:
        print(str(e))
        return jsonify({"code": 500, "message": "An error occurred while fetching users."}), 500

# [GET] Specific User by ID
@blueprint.route("/getUser/<id>")
def getUser(id):
    print("Getting user with id: ", id)
    conn = g.db
    
    try:
        with conn.cursor() as cursor:
            user_data = fetch_user_data(cursor, id)
            if not user_data:
                return jsonify({}), 404

            user_data["drinkLists"] = fetch_drink_lists(cursor, id)
            user_data["followLists"] = fetch_follow_lists(cursor, id)

        return jsonify(user_data), 200

    except Exception as e:
        print(str(e))
        return jsonify({"code": 500, "message": "An error occurred while fetching the user."}), 500

# [GET] Specific User by Username
@blueprint.route("/getUserByUsername/<username>")
def getUserByUsername(username):
    conn = g.db
    
    try:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM "users" WHERE "username" = %s', (username,))
            user_data = cursor.fetchone()
        
            if not user_data:
                return jsonify([]), 404

            user_id = user_data['id']

            user_data["drinkLists"] = fetch_drink_lists(cursor, user_id)
            user_data["followLists"] = fetch_follow_lists(cursor, user_id)

        return jsonify(user_data), 200

    except Exception as e:
        print(str(e))
        return jsonify({"code": 500, "message": "An error occurred while fetching the user."}), 500

# ----------------------
# [NEW] TO BE ADDED:
# ----------------------

# # [GET] Users
# @blueprint.route("/getUsers")
# def getUsers():
#     db = g.db
#     users_data = db.users.find({})
#     allUsers = []
#     for user in users_data:
#         # Fetch related drink lists based on the id(s) in user's drinkLists
#         drink_lists_data = db.usersDrinkLists.find({
#             "_id": {"$in": user['drinkLists']}
#         })
#         user['drinkLists'] = list(drink_lists_data)
#         # Fetch related follow lists based on the id(s) in user's followLists
#         follow_lists_data = db.usersFollowLists.find({
#             "_id": {"$in": user['followLists']}
#         })
#         user['followLists'] = list(follow_lists_data)
#         allUsers.append(user)
#     return parse_json(allUsers)

# # [GET] Specific User by ID
# @blueprint.route("/getUser/<id>")
# def getUser(id):
#     db = g.db
#     user = db.users.find_one({"_id": ObjectId(id)})
#     if user is None:
#         return []
#     # Fetch related drink lists based on the id(s) in user's drinkLists
#     drink_lists_data = db.usersDrinkLists.find({
#         "_id": {"$in": user['drinkLists']}
#     })
#     user['drinkLists'] = list(drink_lists_data)
#     # Fetch related follow lists based on the id(s) in user's followLists
#     follow_lists_data = db.usersFollowLists.find({
#         "_id": {"$in": user['followLists']}
#     })
#     user['followLists'] = list(follow_lists_data)
#     return parse_json(user)

# # [GET] Specific User by Username
# @blueprint.route("/getUserByUsername/<username>")
# def getUserByUsername(username):
#     db = g.db
#     user = db.users.find_one({"username": username})
#     if user is None:
#         return []
#     # Fetch related drink lists based on the id(s) in user's drinkLists
#     drink_lists_data = db.usersDrinkLists.find({
#         "_id": {"$in": user['drinkLists']}
#     })
#     user['drinkLists'] = list(drink_lists_data)
#     # Fetch related follow lists based on the id(s) in user's followLists
#     follow_lists_data = db.usersFollowLists.find({
#         "_id": {"$in": user['followLists']}
#     })
#     user['followLists'] = list(follow_lists_data)
#     return parse_json(user)

# =======================================================

# -----------------------------------------------------------------------------------------

# ================== POSTGRESQL FORMAT ==================

# ----------------------
# [OLD] TO BE DELETED:
# ----------------------

# [GET] Venues
@blueprint.route("/getVenues")
def getVenues():
    conn = g.db
    cur = conn.cursor()

    try:
        # Query to get venues and related data
        query = """
            SELECT 
                v.id, v.address, v."claimStatus", v."hashedPassword", v."venueName", v."venueDesc", 
                v."originLocation", v.photo, v."publicHolidays", v."reservationDetails", v."claimStatusCheckDate",
                v.username, v."venueType", v."stripeCustomerId", v.pin,
                -- Build the menu JSON
                COALESCE((
                    SELECT json_agg(json_build_object(
                        'sectionOrder',vm."sectionOrder",
                        'sectionName', vm."sectionName",
                        'sectionId', vm.id,
                        'sectionMenu', COALESCE((
                            SELECT json_agg(json_build_object(
                                'itemOrder', mi."itemOrder",
                                'itemPrice', mi."itemPrice",
                                'itemAvailability', mi."itemAvailability",
                                'itemID', mi."itemID",
                                'itemServingType', mi."itemServingType"
                            ) ORDER BY mi."itemOrder")
                            FROM "menuItems" mi
                            WHERE mi."sectionId" = vm.id
                        ), '[]')
                    ) ORDER BY vm."sectionOrder")
                    FROM "venuesMenu" vm
                    WHERE vm."venueId" = v.id
                ), '[]') AS menu,
                -- Build openingHours JSON
                COALESCE((
                    SELECT row_to_json(oh)
                    FROM "venuesOpeningHours" oh
                    WHERE oh."venueId" = v.id
                ), '{}'::json) AS "openingHours",
                -- Build questionsAnswers JSON
                COALESCE((
                    SELECT json_agg(json_build_object(
                        'id', qa.id,
                        'question', qa.question,
                        'answer', qa.answer,
                        'date', qa.date,
                        'userId', qa."userId"
                    ))
                    FROM "venuesQuestionAnswers" qa
                    WHERE qa."venueId" = v.id
                ), '[]') AS "questionsAnswers",
                -- Build updates JSON
                COALESCE((
                    SELECT json_agg(json_build_object(
                        'id', u.id,
                        'date', u.date,
                        'text', u.text,
                        'photo', u.photo,
                        'venueId', u."venueId",
                        'likes', COALESCE((
                            SELECT json_agg(json_build_object('userId', l."userId", 'userType', l."userType"))
                            FROM "venueUpdateLikes" l
                            WHERE l."updateId" = u.id
                        ), '[]')
                    ) ORDER BY u.date DESC)
                    FROM "venuesUpdates" u
                    WHERE u."venueId" = v.id
                ), '[]') AS updates
            FROM venues v
            ORDER BY v.id
        """

        cur.execute(query)
        venues_data = cur.fetchall()

        if not venues_data:
            return jsonify([])

        venues_list = []
        for row in venues_data:
            venue = dict(row)
            venue['menu'] = venue['menu'] if venue['menu'] else []
            venue['openingHours'] = venue['openingHours'] if venue['openingHours'] else {}
            venue['questionsAnswers'] = venue['questionsAnswers'] if venue['questionsAnswers'] else []
            venue['updates'] = venue['updates'] if venue['updates'] else []
            venues_list.append(venue)

        return jsonify(venues_list), 200

    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred retrieving venues."
            }
        ), 500

    finally:
        cur.close()

# [GET] Specific Venue
@blueprint.route("/getVenue/<id>")
def getVenue(id):
    conn = g.db
    cur = conn.cursor()

    try:
        # Query to get a specific venue and related data
        query = """
            SELECT 
                v.id, v.address, v."claimStatus", v."hashedPassword", v."venueName", v."venueDesc", 
                v."originLocation", v.photo, v."publicHolidays", v."reservationDetails", v."claimStatusCheckDate",
                v.username, v."venueType", v."stripeCustomerId", v.pin,
                -- Build the menu JSON
                COALESCE((
                    SELECT json_agg(json_build_object(
                        'sectionOrder', vm."sectionOrder",
                        'sectionName', vm."sectionName",
                        'sectionId', vm.id,
                        'sectionMenu', COALESCE((
                            SELECT json_agg(json_build_object(
                                'itemOrder', mi."itemOrder",
                                'itemPrice', mi."itemPrice",
                                'itemAvailability', mi."itemAvailability",
                                'itemID', mi."itemID",
                                'itemServingType', mi."itemServingType"
                            ) ORDER BY mi."itemOrder")
                            FROM "menuItems" mi
                            WHERE mi."sectionId" = vm.id
                        ), '[]')
                    ) ORDER BY vm."sectionOrder")
                    FROM "venuesMenu" vm
                    WHERE vm."venueId" = v.id
                ), '[]') AS menu,
                -- Build openingHours JSON
                COALESCE((
                    SELECT row_to_json(oh)
                    FROM "venuesOpeningHours" oh
                    WHERE oh."venueId" = v.id
                ), '{}'::json) AS "openingHours",
                -- Build questionsAnswers JSON
                COALESCE((
                    SELECT json_agg(json_build_object(
                        'id', qa.id,
                        'question', qa.question,
                        'answer', qa.answer,
                        'date', qa.date,
                        'userId', qa."userId"
                    ))
                    FROM "venuesQuestionAnswers" qa
                    WHERE qa."venueId" = v.id
                ), '[]') AS "questionsAnswers",
                -- Build updates JSON
                COALESCE((
                    SELECT json_agg(json_build_object(
                        'id', u.id,
                        'date', u.date,
                        'text', u.text,
                        'photo', u.photo,
                        'venueId', u."venueId",
                        'likes', COALESCE((
                            SELECT json_agg(json_build_object('userId', l."userId", 'userType', l."userType"))
                            FROM "venueUpdateLikes" l
                            WHERE l."updateId" = u.id
                        ), '[]')
                    ) ORDER BY u.date DESC)
                    FROM "venuesUpdates" u
                    WHERE u."venueId" = v.id
                ), '[]') AS updates
            FROM venues v
            WHERE v.id = %s
            GROUP BY v.id
        """

        cur.execute(query, (id,))
        venue_data = cur.fetchone()

        if venue_data is None:
            return jsonify({"message": "Venue not found"}), 404

        venue = dict(venue_data)
        venue['menu'] = venue['menu'] if venue['menu'] else []
        venue['openingHours'] = venue['openingHours'] if venue['openingHours'] else {}
        venue['questionsAnswers'] = venue['questionsAnswers'] if venue['questionsAnswers'] else []
        venue['updates'] = venue['updates'] if venue['updates'] else []

        return jsonify(venue), 200

    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred retrieving the venue."
            }
        ), 500

    finally:
        cur.close()

# [GET] Specific Producer
@blueprint.route("/getVenueByRequestId/<id>")
def getVenueByRequestId(id):
    conn = g.db
    cur = conn.cursor()

    try:
        # Query to get a specific venue by requestId and related data
        query = """
            SELECT 
                v.id, v.address, v."claimStatus", v."hashedPassword", v."venueName", v."venueDesc", 
                v."originLocation", v.photo, v."publicHolidays", v."reservationDetails", v."claimStatusCheckDate",
                v.username, v."venueType", v."stripeCustomerId", v.pin,
                -- Build the menu JSON
                COALESCE((
                    SELECT json_agg(json_build_object(
                        'sectionOrder', vm."sectionOrder",
                        'sectionName', vm."sectionName",
                        'sectionId', vm.id,
                        'sectionMenu', COALESCE((
                            SELECT json_agg(json_build_object(
                                'itemOrder', mi."itemOrder",
                                'itemPrice', mi."itemPrice",
                                'itemAvailability', mi."itemAvailability",
                                'itemID', mi."itemID",
                                'itemServingType', mi."itemServingType"
                            ) ORDER BY mi."itemOrder")
                            FROM "menuItems" mi
                            WHERE mi."sectionId" = vm.id
                        ), '[]')
                    ) ORDER BY vm."sectionOrder")
                    FROM "venuesMenu" vm
                    WHERE vm."venueId" = v.id
                ), '[]') AS menu,
                -- Build openingHours JSON
                COALESCE((
                    SELECT row_to_json(oh)
                    FROM "venuesOpeningHours" oh
                    WHERE oh."venueId" = v.id
                ), '{}'::json) AS "openingHours",
                -- Build questionsAnswers JSON
                COALESCE((
                    SELECT json_agg(json_build_object(
                        'id', qa.id,
                        'question', qa.question,
                        'answer', qa.answer,
                        'date', qa.date,
                        'userId', qa."userId"
                    ))
                    FROM "venuesQuestionAnswers" qa
                    WHERE qa."venueId" = v.id
                ), '[]') AS "questionsAnswers",
                -- Build updates JSON
                COALESCE((
                    SELECT json_agg(json_build_object(
                        'id', u.id,
                        'date', u.date,
                        'text', u.text,
                        'photo', u.photo,
                        'venueId', u."venueId",
                        'likes', COALESCE((
                            SELECT json_agg(json_build_object('userId', l."userId", 'userType', l."userType"))
                            FROM "venueUpdateLikes" l
                            WHERE l."updateId" = u.id
                        ), '[]')
                    ) ORDER BY u.date DESC)
                    FROM "venuesUpdates" u
                    WHERE u."venueId" = v.id
                ), '[]') AS updates
            FROM venues v
            WHERE v.id = %s
            GROUP BY v.id
        """

        cur.execute(query, (id,))
        venue_data = cur.fetchone()

        if venue_data is None:
            return jsonify({"message": "Venue not found"}), 404

        venue = dict(venue_data)
        venue['menu'] = venue['menu'] if venue['menu'] else []
        venue['openingHours'] = venue['openingHours'] if venue['openingHours'] else {}
        venue['questionsAnswers'] = venue['questionsAnswers'] if venue['questionsAnswers'] else []
        venue['updates'] = venue['updates'] if venue['updates'] else []

        return jsonify(venue), 200
    
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred retrieving the venue."
            }
        ), 500
    
    finally:
        cur.close()

# ----------------------
# [NEW] TO BE ADDED:
# ----------------------

# # [GET] Venues
# @blueprint.route("/getVenues")
# def getVenues():
#     db = g.db
#     venues_data = db.venues.find({})
#     allVenues = []
#     for venue in venues_data:
#         # Fetch related menu based on the id(s) in venue's menu
#         menu_data = db.venuesMenu.find({
#             "_id": {"$in": venue['menu']}
#         })
#         venue['menu'] = list(menu_data)
#         # Fetch related opening hours based on the id(s) in venue's openingHours
#         opening_hours_data = db.venuesOpeningHours.find({
#             "_id": {"$in": venue['openingHours']}
#         })
#         venue['openingHours'] = list(opening_hours_data)
#         # Fetch related question answers based on the id(s) in venue's questionAnswers
#         question_answers_data = db.venuesQuestionAnswers.find({
#             "_id": {"$in": venue['questionAnswers']}
#         })
#         venue['questionAnswers'] = list(question_answers_data)
#         # Fetch related updates based on the id(s) in venue's updates
#         updates_data = db.venuesUpdates.find({
#             "_id": {"$in": venue['updates']}
#         })
#         venue['updates'] = list(updates_data)
#         allVenues.append(venue)
#     return parse_json(allVenues)

# # [GET] Specific Venue by ID
# @blueprint.route("/getVenue/<id>")
# def getVenue(id):
#     db = g.db
#     venue = db.venues.find_one({"_id": ObjectId(id)})
#     if venue is None:
#         return []
#     # Fetch related menu based on the id(s) in venue's menu
#     menu_data = db.venuesMenu.find({
#         "_id": {"$in": venue['menu']}
#     })
#     venue['menu'] = list(menu_data)
#     # Fetch related opening hours based on the id(s) in venue's openingHours
#     opening_hours_data = db.venuesOpeningHours.find({
#         "_id": {"$in": venue['openingHours']}
#     })
#     venue['openingHours'] = list(opening_hours_data)
#     # Fetch related question answers based on the id(s) in venue's questionAnswers
#     question_answers_data = db.venuesQuestionAnswers.find({
#         "_id": {"$in": venue['questionAnswers']}
#     })
#     venue['questionAnswers'] = list(question_answers_data)
#     # Fetch related updates based on the id(s) in venue's updates
#     updates_data = db.venuesUpdates.find({
#         "_id": {"$in": venue['updates']}
#     })
#     venue['updates'] = list(updates_data)
#     return parse_json(venue)

# # [GET] Specific Venue by Request ID
# @blueprint.route("/getVenueByRequestId/<id>")
# def getVenueByRequestId(id):
#     db = g.db
#     venue = db.venues.find_one({"requestId": ObjectId(id)})
#     if venue is None:
#         return []
#     # Fetch related menu based on the id(s) in venue's menu
#     menu_data = db.venuesMenu.find({
#         "_id": {"$in": venue['menu']}
#     })
#     venue['menu'] = list(menu_data)
#     # Fetch related opening hours based on the id(s) in venue's openingHours
#     opening_hours_data = db.venuesOpeningHours.find({
#         "_id": {"$in": venue['openingHours']}
#     })
#     venue['openingHours'] = list(opening_hours_data)
#     # Fetch related question answers based on the id(s) in venue's questionAnswers
#     question_answers_data = db.venuesQuestionAnswers.find({
#         "_id": {"$in": venue['questionAnswers']}
#     })
#     venue['questionAnswers'] = list(question_answers_data)
#     # Fetch related updates based on the id(s) in venue's updates
#     updates_data = db.venuesUpdates.find({
#         "_id": {"$in": venue['updates']}
#     })
#     venue['updates'] = list(updates_data)
#     return parse_json(venue)

# =======================================================

# -----------------------------------------------------------------------------------------
# [GET] VenuesAPI
# @blueprint.route("/getVenuesAPI")
# def getVenuesAPI():
#     db = g.db
#     data = db.venuesAPI.find({})
#     print(len(list(data.clone())))
#     allVenuesAPI = []
#     dataEncode = parse_json(data)
#     for doc in dataEncode:
#         allVenuesAPI.append(doc)
#     return allVenuesAPI

# -----------------------------------------------------------------------------------------
# [GET] DrinkTypes
@blueprint.route("/getDrinkTypes")
def getDrinkTypes():
    conn = g.db
    
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM "drinkTypes"')
        drink_types_data = cursor.fetchall()
    
    if not drink_types_data:
        return jsonify([])

    return jsonify(drink_types_data)

# -----------------------------------------------------------------------------------------
# [GET] RequestListings
@blueprint.route("/getRequestListings")
def getRequestListings():
    conn = g.db
    
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM "requestListings"')
        request_listings_data = cursor.fetchall()
    
    if not request_listings_data:
        return jsonify([])

    return jsonify(request_listings_data)

# [GET] Specific Request Listing
@blueprint.route("/getRequestListing/<id>")
def getRequestListing(id):
    conn = g.db
    
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM "requestListings" WHERE "id" = %s', (id,))
        request_listing_data = cursor.fetchone()
    
    if request_listing_data is None:
        return jsonify([])

    return jsonify(request_listing_data)

# -----------------------------------------------------------------------------------------
# [GET] RequestEdits
@blueprint.route("/getRequestEdits")
def getRequestEdits():
    conn = g.db
    
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM "requestEdits"')
        request_edits_data = cursor.fetchall()
    
    if not request_edits_data:
        return jsonify([])

    return jsonify(request_edits_data)

# [GET] Specific Request Edit
@blueprint.route("/getRequestEdit/<id>")
def getRequestEdit(id):
    conn = g.db
    
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM "requestEdits" WHERE "id" = %s', (id,))
        request_edit_data = cursor.fetchone()
    
    if request_edit_data is None:
        return jsonify([])

    return jsonify(request_edit_data)

# -----------------------------------------------------------------------------------------
# [GET] modRequests
@blueprint.route("/getModRequests")
def getModRequests():
    conn = g.db

    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM "modRequests"')
        mod_requests_data = cursor.fetchall()

    if not mod_requests_data:
        return jsonify([])

    return jsonify(mod_requests_data)

# -----------------------------------------------------------------------------------------
# [GET] flavourTags
@blueprint.route("/getFlavourTags")
def getFlavourTags():
    conn = g.db

    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM "flavourTags"')
        flavour_tags_data = cursor.fetchall()

    if not flavour_tags_data:
        return jsonify([])

    return jsonify(flavour_tags_data)
# -----------------------------------------------------------------------------------------
# [GET] subTags
@blueprint.route("/getSubTags")
def getSubTags():
    conn = g.db

    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM "subTags"')
        allSubTags = cursor.fetchall()

    if not allSubTags:
        return jsonify([])

    return jsonify(allSubTags)

# -----------------------------------------------------------------------------------------
# [GET] observationTags
@blueprint.route("/getObservationTags")
def getObservationTags():
    conn = g.db

    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM "observationTags"')
        observation_tags_data = cursor.fetchall()

    if not observation_tags_data:
        return jsonify([])

    return jsonify(observation_tags_data)

# -----------------------------------------------------------------------------------------
# [GET] colours
@blueprint.route("/getColours")
def getColours():
    conn = g.db

    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM "colours"')
        colours_data = cursor.fetchall()

    if not colours_data:
        return jsonify([])

    return jsonify(colours_data)

# -----------------------------------------------------------------------------------------
# [GET] specialColours
@blueprint.route("/getSpecialColours")
def getSpecialColours():
    conn = g.db

    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM "specialColours"')
        allSpecialColours = cursor.fetchall()

    if not allSpecialColours:
        return jsonify([])

    return jsonify(allSpecialColours)

# -----------------------------------------------------------------------------------------
# [GET] languages
@blueprint.route("/getLanguages")
def getLanguages():
    conn = g.db

    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM "languages"')
        languages = cursor.fetchall()

    if not languages:
        return jsonify([])

    return jsonify(languages)

# -----------------------------------------------------------------------------------------
# [GET] servingTypes
@blueprint.route("/getServingTypes")
def getServingTypes():
    conn = g.db

    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM "servingTypes"')
        serving_types_data = cursor.fetchall()

    if not serving_types_data:
        return jsonify([])
    
    return jsonify(serving_types_data), 200

# -----------------------------------------------------------------------------------------

# ================== POSTGRESQL FORMAT ==================

# ----------------------
# [OLD] TO BE DELETED:
# ----------------------

# [GET] producersProfileViews
@blueprint.route("/getProducersProfileViews")
def getProducersProfileViews():
    conn = g.db
    cur = conn.cursor()

    try:
        cur.execute('SELECT * FROM "producersProfileViews"')
        producers_profile_views_data = cur.fetchall()

        if not producers_profile_views_data:
            return jsonify([])

        return jsonify(producers_profile_views_data), 200
    
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred retrieving the profile views."
            }
        ), 500
    
    finally:
        cur.close()

# [GET] producersProfileViews by producerID
@blueprint.route("/getProducersProfileViewsByProducer/<id>")
def getProducersProfileViewsByProducer():
    conn = g.db
    cur = conn.cursor()

    try:
        cur.execute('SELECT * FROM "producersProfileViews" WHERE "producerID" = %s', (id,))
        producers_profile_views_data = cur.fetchall()

        if not producers_profile_views_data:
            return jsonify([]), 404

        return jsonify(producers_profile_views_data), 200
    
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred retrieving the profile views."
            }
        ), 500
    
    finally:
        cur.close()

# ----------------------
# [NEW] TO BE ADDED:
# ----------------------

# # [GET] producersProfileViews
# @blueprint.route("/getProducersProfileViews")
# def getProducersProfileViews():
#     db = g.db
#     profile_views_data = db.producersProfileViews.find({})
#     allProfileViews = []
#     for profile_view in profile_views_data:
#         # Fetch related views data based on the id(s) in profile_view's views
#         views_data = db.producersProfileViewsViews.find({
#             "_id": {"$in": profile_view['views']}
#         })
#         profile_view['views'] = list(views_data)
#         allProfileViews.append(profile_view)
#     return parse_json(allProfileViews)

# # [GET] producersProfileViews by producerID
# @blueprint.route("/getProducersProfileViewsByProducer/<id>")
# def getProducersProfileViewsByProducer(id):
#     db = g.db
#     profile_views_data = db.producersProfileViews.find({"producerID": ObjectId(id)})
#     allProfileViews = []
#     for profile_view in profile_views_data:
#         # Fetch related views data based on the id(s) in profile_view's views
#         views_data = db.producersProfileViewsViews.find({
#             "_id": {"$in": profile_view['views']}
#         })
#         profile_view['views'] = list(views_data)
#         allProfileViews.append(profile_view)
    # return parse_json(allProfileViews)

# =======================================================

# -----------------------------------------------------------------------------------------

# ================== POSTGRESQL FORMAT ==================

# ----------------------
# [OLD] TO BE DELETED:
# ----------------------

# [GET] venuesProfileViews
@blueprint.route("/getVenuesProfileViews")
def getVenuesProfileViews():
    conn = g.db
    cur = conn.cursor()

    try:
        cur.execute('SELECT * FROM "venuesProfileViews"')
        profile_views_data = cur.fetchall()

        if not profile_views_data:
            return jsonify([])

        return jsonify(profile_views_data), 200
    
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred retrieving the profile views."
            }
        ), 500
    
    finally:
        cur.close()

# [GET] venuesProfileViews by venueID
@blueprint.route("/getVenuesProfileViewsByVenue/<id>")
def getVenuesProfileViewsByVenue(id):
    conn = g.db
    cur = conn.cursor()

    try:
        cur.execute('SELECT * FROM "venuesProfileViews" WHERE "venueId" = %s', (id,))
        profile_views_data = cur.fetchall()

        if not profile_views_data:
            return jsonify([])

        return jsonify(profile_views_data), 200
    
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred retrieving the profile views."
            }
        ), 500
    
    finally:
        cur.close()

# ----------------------
# [NEW] TO BE ADDED:
# ----------------------

# # [GET] venuesProfileViews
# @blueprint.route("/getVenuesProfileViews")
# def getVenuesProfileViews():
#     db = g.db
#     profile_views_data = db.venuesProfileViews.find({})
#     allProfileViews = []
#     for profile_view in profile_views_data:
#         # Fetch related views data based on the id(s) in profile_view's views
#         views_data = db.venuesProfileViewsViews.find({
#             "_id": {"$in": profile_view['views']}
#         })
#         profile_view['views'] = list(views_data)
#         allProfileViews.append(profile_view)
#     return parse_json(allProfileViews)

# # [GET] venuesProfileViews by venueID
# @blueprint.route("/getVenuesProfileViewsByVenue/<id>")
# def getVenuesProfileViewsByVenue(id):
#     db = g.db
#     profile_views_data = db.venuesProfileViews.find({"venueID": ObjectId(id)})
#     allProfileViews = []
#     for profile_view in profile_views_data:
#         # Fetch related views data based on the id(s) in profile_view's views
#         views_data = db.venuesProfileViewsViews.find({
#             "_id": {"$in": profile_view['views']}
#         })
#         profile_view['views'] = list(views_data)
#         allProfileViews.append(profile_view)
#     return parse_json(allProfileViews)

# =======================================================

# -----------------------------------------------------------------------------------------
# [GET] requestInaccuracy by venueID
@blueprint.route("/getRequestInaccuracyByVenue/<id>")
def getRequestInaccuracyByVenue(id):
    # only get requestInaccuracy that has reviewStatus = False
    conn = g.db
    cur = conn.cursor()

    try:
        cur.execute('SELECT * FROM "requestInaccuracy" WHERE "venueId" = %s AND "reviewStatus" = FALSE', (id,))
        request_inaccuracy_data = cur.fetchall()

        if not request_inaccuracy_data:
            return jsonify([])

        return jsonify(request_inaccuracy_data), 200
    
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred retrieving the request inaccuracy."
            }
        ), 500
    
    finally:
        cur.close()

# -----------------------------------------------------------------------------------------
# [GET] Badges
@blueprint.route("/getBadges")
def getBadges():
    conn = g.db
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM "badges"')
        badges_data = cursor.fetchall()

    if not badges_data:
        return jsonify([])

    return jsonify(badges_data)

# -----------------------------------------------------------------------------------------
# [GET] Specific Token
@blueprint.route("/getToken/<token>")
def getToken(token):
    conn = g.db
    cur = conn.cursor()

    try:
        cur.execute("""
            SELECT * FROM "tokens" WHERE "token" = %s
        """, (token,))

        token_data = cur.fetchone()

        if token_data is None:
            return jsonify({
                "code": 404,
                "message": "Token not found."
            }), 404
        
        if token_data['userId'] is not None:
            user_id = token_data['userId']
        elif token_data['producerId'] is not None:
            user_id = token_data['producerId']
        elif token_data['venueId'] is not None:
            user_id = token_data['venueId']
        else:
            return jsonify({
                "code": 500,
                "message": "Token does not have a valid associated user."
            }), 500
        
        response_data = {
            "id": token_data['id'],
            "token": token_data['token'],
            "requestId": token_data['requestId'],
            "expiry": token_data['expiry'],
            "userId": user_id
        }

        
        return jsonify({
            "code": 200,
            "data": response_data
        }), 200
    
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred retrieving the token."
            }
        ), 500
    
    finally:
        cur.close()

@blueprint.route("/getTokenByRequestId/<requestId>")
def getTokenByRequestId(requestId):
    conn = g.db
    cur = conn.cursor()

    try:
        cur.execute("""
            SELECT * FROM "tokens" WHERE "requestId" = %s
        """, (requestId,))
        token_data = cur.fetchone()

        if token_data is None:
            return jsonify({
                "code": 404,
                "message": "Token not found."
            }), 404
        
        if token_data['userId'] is not None:
            user_id = token_data['userId']
        elif token_data['producerId'] is not None:
            user_id = token_data['producerId']
        elif token_data['venueId'] is not None:
            user_id = token_data['venueId']
        else:
            return jsonify({
                "code": 500,
                "message": "Token does not have a valid associated user."
            }), 500
        
        response_data = {
            "id": token_data['id'],
            "token": token_data['token'],
            "requestId": token_data['requestId'],
            "expiry": token_data['expiry'],
            "userId": user_id
        }

        return jsonify({
            "code": 200,
            "data": response_data
        }), 200
    
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred retrieving the token."
            }
        ), 500
    
    finally:
        cur.close()

# -----------------------------------------------------------------------------------------
# [GET] Specific Request
@blueprint.route("/getAccountRequest/<id>")
def getAccountRequest(id):
    conn = g.db
    cur = conn.cursor()

    try:
        cur.execute("""
            SELECT * FROM "accountRequests" WHERE "id" = %s
        """, (id,))

        request_data = cur.fetchone()

        if request_data is None:
            return jsonify([]), 404
        
        return jsonify(request_data), 200
    
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred retrieving the request."
            }
        ), 500
    
    finally:
        cur.close()

# -----------------------------------------------------------------------------------------
# [GET] Producers
@blueprint.route("/getUsernames")
def getUsernames():
    conn = g.db
    cur = conn.cursor()

    try:
        cur.execute('SELECT "username" FROM "producers"')
        producer_usernames = cur.fetchall()

        cur.execute('SELECT "username" FROM "venues"')
        venue_usernames = cur.fetchall()

        # Combine and filter usernames
        usernames = (
            [username['username'] for username in producer_usernames] +
            [username['username'] for username in venue_usernames]
        )
        usernames = [username for username in usernames if username]  # Filter out any None values

        return jsonify(usernames), 200
    
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred retrieving usernames."
            }
        ), 500
    
    finally:
        cur.close()


# -----------------------------------------------------------------------------------------
# [GET] Any User Regardless of Type by Email
@blueprint.route("/getUserByEmail/<email>")
def getUserByEmail(email):
    conn = g.db
    cur = conn.cursor()

    # Define return data
    return_data = None

    try:
        # Check if user is a user and retrieve the id 
        cur.execute('SELECT * FROM "users" WHERE "email" = %s', (email,))
        user_data = cur.fetchone()

        if user_data is not None:
            return_data = {'id': user_data['id'], 'type': 'user', 'username': user_data['username']}
            
            return jsonify(return_data), 200
        
        # Check if user is a producer and retrieve the id
        cur.execute('SELECT * FROM "producers" WHERE "email" = %s', (email,))
        producer_data = cur.fetchone()

        if producer_data is not None:
            return_data = {'id': producer_data['id'], 'type': 'producer', 'username': producer_data['username']}
            
            return jsonify(return_data), 200
        
        # Check if user is a venue and retrieve the id
        cur.execute('SELECT * FROM "venues" WHERE "email" = %s', (email,))
        venue_data = cur.fetchone()

        if venue_data is not None:
            return_data = {'id': venue_data['id'], 'type': 'venue', 'username': venue_data['username']}
            
            return jsonify(return_data), 200
        
        return jsonify(
            {
                "code": 404,
                "message": "Email not found."
            }
        ), 404
    
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": str(e)
            }
        ), 500
    
    finally:
        cur.close()
