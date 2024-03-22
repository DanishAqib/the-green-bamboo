# Port: 5100
# Routes: /editDetails (POST), /updateBookmark (POST), /submitModRequest (POST)
# -----------------------------------------------------------------------------------------

import bson
import json
from bson import json_util
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from werkzeug.utils import secure_filename

from pymongo.errors import DuplicateKeyError, OperationFailure
from bson.objectid import ObjectId
from bson.errors import InvalidId

from datetime import datetime
import pytz

from gridfs import GridFS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config["MONGO_URI"] = "mongodb+srv://jwleong2020:uOfXCrxLPCjgyA92@greenbamboo.wbiambw.mongodb.net/GreenBamboo?retryWrites=true&w=majority"
db = PyMongo(app).db

mongo = PyMongo(app)
fs = GridFS(mongo.db)

# -----------------------------------------------------------------------------------------
# [POST] Edit user profile
# - Update user profile with new details
# - Possible return codes: 201 (Updated), 500 (Error during update)
@app.route('/editDetails', methods=['POST'])
def editDetails():
    data = request.get_json()
    print(data)
    userID = data['userID']
    # if data contains image64
    if 'image64' in data:
        image64 = data['image64']
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
                    "image": image64[:8],
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
                    "image": image64[:8],
                    "drinkChoice": drinkChoice
                },
                "message": "An error occurred updating the image or drink choice."
            }
        ), 500
    
# -----------------------------------------------------------------------------------------
# [POST] Update user bookmark
# - Update user bookmark with new details
# - Possible return codes: 201 (Updated), 500 (Error during update)
@app.route('/updateBookmark', methods=['POST'])
def updateBookmark():
    data = request.get_json()
    print(data)
    userID = data['userID']
    bookmark = data['bookmark']

    # convert date (str) to datetime object
    for listName in bookmark:
        listItems = bookmark[listName]["listItems"]
        for item in listItems:
            if isinstance(item[0], str):
                item[0] = datetime.strptime(item[0], "%Y-%m-%dT%H:%M:%S.%fZ")

    try: 
        updateBookmark = db.users.update_one({'_id': ObjectId(userID)}, {'$set': {'drinkLists': bookmark}})

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
@app.route('/updateFollowLists', methods=['POST'])
def updateFollowList():
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
@app.route('/updateModType', methods=['POST'])
def updateModType():
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
@app.route('/removeModType', methods=['POST'])
def removeModType():
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

# -----------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True, port=5100)