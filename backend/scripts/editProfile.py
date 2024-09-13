# Port: 5100
# Routes: /editDetails (POST), /updateBookmark (POST), /updateFollowLists (POST), /updateModType (POST), /removeModType (POST)
# -----------------------------------------------------------------------------------------

import os
import pytz
import s3Images
from flask import Blueprint, g, request, jsonify
from bson.objectid import ObjectId
from datetime import datetime

file_name = os.path.basename(__file__)
blueprint = Blueprint(file_name[:-3], __name__)

# -----------------------------------------------------------------------------------------
# [POST] Edit user profile
# - Update user profile with new details
# - Possible return codes: 201 (Updated), 500 (Error during update)
@blueprint.route('/editDetails', methods=['POST'])
def editDetails():
    db = g.db
    data = request.get_json()
    print(data)
    userID = data['userID']
    # if data contains image64
    if 'image64' in data:
        existingUser = db.users.find_one({"_id": ObjectId(userID)})
        if existingUser['photo']:
            s3Images.deleteImageFromS3(existingUser['photo'])
        image64 = s3Images.uploadBase64ImageToS3(data['image64'])
        # Upload to S3 by calling function, rmb url

    drinkChoice = data['drinkChoice']

    try: 
        if 'image64' in data:
            updateImage = db.users.update_one({'_id': ObjectId(userID)}, {'$set': {'photo': image64}})
        updateDrinkChoice = db.users.update_one({'_id': ObjectId(userID)}, {'$set': {'choiceDrinks': drinkChoice}})

        return jsonify(
            {   
                "code": 201,
                "data": {
                    "userID": userID,
                    "drinkChoice": drinkChoice
                }
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": {
                    "userID": userID,
                    "drinkChoice": drinkChoice
                },
                "message": "An error occurred updating the image or drink choice."
            }
        ), 500

# -- ========= "users" =========
# CREATE TABLE "users" (
#     "id" SERIAL PRIMARY KEY,
#     "username" VARCHAR(255),
#     "displayName" VARCHAR(255),
#     "choiceDrinks" TEXT[],
#     "modType" TEXT[],
#     "photo" TEXT,
#     "hashedPassword" VARCHAR(255),
#     -- "drinkLists" SERIAL, -- [!] reference "usersDrinkLists" not needed since user followlist ref users
#     "joinDate" TIMESTAMP,
#     -- "followLists" SERIAL, -- [!] reference "usersFollowLists"
#     "firstName" VARCHAR(255),
#     "lastName" VARCHAR(255),
#     "email" VARCHAR(255),
#     "isAdmin" BOOLEAN,
#     "birthday" TIMESTAMP,
#     "pin" VARCHAR(255)
# );

# -- ========= [NEW!] "usersDrinkLists" =========
# CREATE TABLE "usersDrinkLists" (
#     "id" SERIAL PRIMARY KEY,
#     "userId" INTEGER REFERENCES "users"("id") ON DELETE SET NULL,  -- [!] reference "users" FK
#     "listName" TEXT,
#     "drinks" TEXT[],-- Contains "listings"("id")s
#     UNIQUE ("userId", "listName")
# );

    
# -----------------------------------------------------------------------------------------
# [POST] Update user bookmark
# - Update user bookmark with new details
# - Possible return codes: 201 (Updated), 500 (Error during update)
@blueprint.route('/updateBookmark', methods=['POST'])
def updateBookmark():
    conn = g.db
    data = request.get_json()
    print(data)
    userID = data['userID']
    bookmark = data['bookmark']

    try:
        cursor = conn.cursor()
        for listName in bookmark:
            listDesc = bookmark[listName]["listDesc"]
            listItems = bookmark[listName]["listItems"]

            query = """
                INSERT INTO "usersDrinkLists" ("userId", "listName", "drinks")
                VALUES (%s, %s, %s)
                ON CONFLICT ("userId", "listName") DO UPDATE
                SET "drinks" = EXCLUDED."drinks";
            """
            cursor.execute(query, (userID, listName, listItems))
        
        conn.commit()
        cursor.close()

        return jsonify(
            {   
                "code": 201,
                "data": {
                    "userID": userID,
                    "bookmark": bookmark
                }
            }
        ), 201

    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": {
                    "data": {
                        "userID": userID,
                        "bookmark": bookmark
                    }
                },
                "message": "An error occurred updating the drink lists."
            }
        ), 500

# -----------------------------------------------------------------------------------------
# [POST] Update follow lists
# - Update user follow lists with new details
# - Possible return codes: 201 (Updated), 500 (Error during update)
@blueprint.route('/updateFollowLists', methods=['POST'])
def updateFollowList():
    db = g.db
    data = request.get_json()
    print(data)
    userID = data['userID']
    action = data['action']
    target = data['target']
    followerID = data['followerID']

    user_document = db.users.find_one({"_id": ObjectId(userID)})
    followLists = user_document['followLists']

    if action == "unfollow":
        followLists[target] = [user for user in user_document['followLists'][target] if user["followerID"] != ObjectId(followerID)]
    else:
        followLists[target].append({
            "followerID": ObjectId(followerID),
            "date": datetime.now(pytz.timezone('Etc/GMT-8'))
            })

    try: 
        updateFollowLists = db.users.update_one({'_id': ObjectId(userID)}, {'$set': {'followLists': followLists}})


        return jsonify(
            {   
                "code": 201,
                "data": {
                    "userID": userID,
                    "action": action,
                    "target": target,
                    "followerID": followerID
                }
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": {
                    "data": {
                        "userID": userID,
                        "action": action,
                        "target": target,
                        "followerID": followerID
                    }
                },
                "message": "An error occurred follow list."
            }
        ), 500
    
# -----------------------------------------------------------------------------------------
# [POST] Update mod type
# - Update user mod type with new details
# - Possible return codes: 201 (Updated), 500 (Error during update)
@blueprint.route('/updateModType', methods=['POST'])
def updateModType():
    db = g.db
    data = request.get_json()
    print(data)
    userID = data['userID']
    newModType = data['newModType']

    user_document = db.users.find_one({"_id": ObjectId(userID)})
    modType = user_document['modType']

    modType.append(newModType)

    try: 
        updateModType = db.users.update_one({'_id': ObjectId(userID)}, {'$set': {'modType': modType}})


        return jsonify(
            {   
                "code": 201,
                "data": {
                    "userID": userID,
                    "newModType": newModType
                }
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": {
                    "data": {
                        "userID": userID,
                        "newModType": newModType
                    }
                },
                "message": "An error occurred updating mod type."
            }
        ), 500

# -----------------------------------------------------------------------------------------
# [POST] Remove mod type
# - Remove user mod type by specified drink type
# - Possible return codes: 201 (Updated), 500 (Error during update)
@blueprint.route('/removeModType', methods=['POST'])
def removeModType():
    db = g.db
    data = request.get_json()
    print(data)
    userID = data['userID']
    removeModType = data['removeModType']

    user_document = db.users.find_one({"_id": ObjectId(userID)})
    modType = user_document['modType']

    modType.remove(removeModType)

    try: 
        updateModType = db.users.update_one({'_id': ObjectId(userID)}, {'$set': {'modType': modType}})


        return jsonify(
            {   
                "code": 201,
                "data": {
                    "userID": userID,
                    "removeModType": removeModType
                }
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": {
                    "data": {
                        "userID": userID,
                        "removeModType": removeModType
                    }
                },
                "message": "An error occurred updating mod type."
            }
        ), 500
