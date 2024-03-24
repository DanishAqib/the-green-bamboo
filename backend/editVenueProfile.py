# Port: 5300
# Routes: /editDetails (POST), /addUpdates (POST), /sendQuestions (POST), /sendAnswers (POST), /likeUpdates (POST), /unlikeUpdates (POST)
#         /editOpeningHours (POST), /editPublicHolidays (POST), /editReservationDetails (POST), /editMenu (POST)
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

from gridfs import GridFS
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config["MONGO_URI"] = "mongodb+srv://jwleong2020:uOfXCrxLPCjgyA92@greenbamboo.wbiambw.mongodb.net/GreenBamboo?retryWrites=true&w=majority"
db = PyMongo(app).db

mongo = PyMongo(app)
fs = GridFS(mongo.db)

# -----------------------------------------------------------------------------------------
# [POST] Edit venue profile
# - Update venue profile with new details
# - Possible return codes: 201 (Updated), 500 (Error during update)
@app.route('/editDetails', methods=['POST'])
def editDetails():

    # fetch sent data
    data = request.get_json()
    print(data)

    # extract components of the data
    venueID = data['venueID']
    venueName = data['venueName']
    venueDesc = data['venueDesc']
    originLocation = data['originLocation']
    image64 = data['image64']

    try: 
        update = db.venues.update_one({'_id': ObjectId(venueID)}, 
                                        {'$set': {
                                                    'photo': image64,
                                                    'venueName': venueName,
                                                    'venueDesc': venueDesc,
                                                    'originLocation': originLocation
                                                    }
                                            })
        return jsonify(
            {   
                "code": 201,
                "message": "Updated profile successfully!"
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": data,
                "message": "An error occurred updating profile!"
            }
        ), 500

# -----------------------------------------------------------------------------------------
# [POST] Add updates to venue profile
# - Add updates to the venue profile
# - Possible return codes: 201 (Updated), 500 (Error during update)
@app.route('/addUpdates', methods=['POST'])
def addUpdates():

    # fetch sent data
    data = request.get_json()
    print(data)

    # extract components of the data
    venueID = data['venueID']
    date = datetime.strptime(data['date'], "%Y-%m-%dT%H:%M:%S.%fZ")
    text = data['text']
    image64 = data['image64']

    try:
        submitReq = db.venues.update_one(
            {'_id': ObjectId(venueID)},
            {'$push': {'updates': 
                        {
                            "_id": ObjectId(),
                            'date': date,
                            'text': text,
                            'photo': image64,
                            'likes': []
                        }
                    }
            }
        )

        return jsonify( 
            {   
                "code": 201,
                "message": "Update added successfully!"
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": data,
                "message": "An error occurred creating the update!"
            }
        ), 500

# -----------------------------------------------------------------------------------------
# [POST] Send questions to venue profile
# - Send questions to the venue profile
# - Possible return codes: 201 (Updated), 500 (Error during update)
@app.route('/sendQuestions', methods=['POST'])
def sendQuestions():

    # fetch sent data
    data = request.get_json()
    print(data)

    # extract components of the data
    venueID = data['venueID']
    question = data['question']
    answer = data['answer']

    try:
        submitReq = db.venues.update_one(
            {'_id': ObjectId(venueID)},
            {'$push': {'questionsAnswers': 
                        {
                            '_id': ObjectId(),
                            'question': question,
                            'answer': answer
                        }
                    }
            }
        )

        return jsonify( 
            {   
                "code": 201,
                "message": "Question sent successfully!"
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": data,
                "message": "An error occurred sending the question!"
            }
        ), 500

# -----------------------------------------------------------------------------------------
# [POST] Send answers to venue profile
# - Send answers to the venue profile
# - Possible return codes: 201 (Updated), 500 (Error during update)
@app.route('/sendAnswers', methods=['POST'])
def sendAnswers():

    # fetch sent data
    data = request.get_json()
    print(data)

    # extract components of the data
    venueID = data['venueID']
    questionsAnswersID = data['questionsAnswersID']
    answer = data['answer']

    try:
        submitReq = db.venues.update_one(
            {'_id': ObjectId(venueID), 'questionsAnswers._id': ObjectId(questionsAnswersID)},
            {'$set': {'questionsAnswers.$.answer': answer}}
        )
        return jsonify( 
            {   
                "code": 201,
                "message": "Answer sent successfully!"
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": data,
                "message": "An error occurred sending the answer!"
            }
        ), 500

# -----------------------------------------------------------------------------------------
# [POST] Like updates
# - Like updates
# - Possible return codes: 201 (Updated), 500 (Error during update)
@app.route('/likeUpdates', methods=['POST'])
def likeUpdates():
    data = request.get_json()
    print(data)
    venueID = data['venueID']
    updateID = data['updateID']
    userID = data['userID']

    try: 
        likeUpdate = db.venues.update_one(
            {'_id': ObjectId(venueID), 'updates._id': ObjectId(updateID)},
            {'$push': {'updates.$.likes': ObjectId(userID)}}
        )
        return jsonify(
            {   
                "code": 201,
                "message": "Update liked successfully!"
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": data,
                "message": "An error occurred liking the update!"
            }
        ), 500

# -----------------------------------------------------------------------------------------
# [POST] Unlike updates
# - Unlike updates
# - Possible return codes: 201 (Updated), 500 (Error during update)
@app.route('/unlikeUpdates', methods=['POST'])
def unlikeUpdates():
    data = request.get_json()
    print(data)
    venueID = data['venueID']
    updateID = data['updateID']
    userID = data['userID']

    try: 
        unlikeUpdate = db.venues.update_one(
            {'_id': ObjectId(venueID), 'updates._id': ObjectId(updateID)},
            {'$pull': {'updates.$.likes': ObjectId(userID)}}
        )
        return jsonify(
            {   
                "code": 201,
                "message": "Update unliked successfully!"
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": data,
                "message": "An error occurred unliking the update!"
            }
        ), 500

# -----------------------------------------------------------------------------------------
# [POST] Edit address
# - Edit address
# - Possible return codes: 201 (Updated), 500 (Error during update)
@app.route('/editAddress', methods=['POST'])
def editAddress():
    data = request.get_json()
    print(data)
    venueID = data['venueID']
    updatedAddress = data['updatedAddress']

    try: 
        editAddress = db.venues.update_one(
            {'_id': ObjectId(venueID)},
            {'$set': {'address': updatedAddress}}
        )
        return jsonify(
            {   
                "code": 201,
                "message": "Address edited successfully!"
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": data,
                "message": "An error occurred editing the address!"
            }
        ), 500

# -----------------------------------------------------------------------------------------
# [POST] Edit opening hours
# - Edit opening hours
# - Possible return codes: 201 (Updated), 500 (Error during update)
@app.route('/editOpeningHours', methods=['POST'])
def editOpeningHours():
    data = request.get_json()
    print(data)
    venueID = data['venueID']
    updatedOpeningHours = data['updatedOpeningHours']

    try: 
        editOpeningHours = db.venues.update_one(
            {'_id': ObjectId(venueID)},
            {'$set': {'openingHours': updatedOpeningHours}}
        )
        return jsonify(
            {   
                "code": 201,
                "message": "Opening hours edited successfully!"
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": data,
                "message": "An error occurred editing the opening hours!"
            }
        ), 500

# -----------------------------------------------------------------------------------------
# [POST] Edit public holidays
# - Edit public holidays
# - Possible return codes: 201 (Updated), 500 (Error during update)
@app.route('/editPublicHolidays', methods=['POST'])
def editPublicHolidays():
    data = request.get_json()
    print(data)
    venueID = data['venueID']
    updatedPublicHolidays = data['updatedPublicHolidays']

    try: 
        editOpeningHours = db.venues.update_one(
            {'_id': ObjectId(venueID)},
            {'$set': {'publicHolidays': updatedPublicHolidays}}
        )
        return jsonify(
            {   
                "code": 201,
                "message": "Public holidays details edited successfully!"
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": data,
                "message": "An error occurred editing the public holidays!"
            }
        ), 500

# -----------------------------------------------------------------------------------------
# [POST] Edit reservation details
# - Edit reservation details
# - Possible return codes: 201 (Updated), 500 (Error during update)
@app.route('/editReservationDetails', methods=['POST'])
def editReservationDetails():
    data = request.get_json()
    print(data)
    venueID = data['venueID']
    updatedReservationDetails = data['updatedReservationDetails']

    try: 
        editOpeningHours = db.venues.update_one(
            {'_id': ObjectId(venueID)},
            {'$set': {'reservationDetails': updatedReservationDetails}}
        )
        return jsonify(
            {   
                "code": 201,
                "message": "Reservation details edited successfully!"
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": data,
                "message": "An error occurred editing the reservation details!"
            }
        ), 500

# -----------------------------------------------------------------------------------------
# [POST] Add listing to menu
# - Add listing to menu
# - Possible return codes: 201 (Updated), 500 (Error during update)
@app.route('/addListingToMenu', methods=['POST'])
def addListingToMenu():
    data = request.get_json()
    print(data)
    venueID = data['venueID']
    menuOrder = data['menuOrder']
    listingID = data['listingID']
    itemPrice = data['itemPrice']
    servingType = data['servingType']
    sectionName = data['sectionName']

    try: 
        addListing = db.venues.update_one(
            {'_id': ObjectId(venueID), 'menu.sectionName': sectionName},
            {'$push': {'menu.$.listingsID': 
                        {
                            'itemOrder': menuOrder,
                            'itemID': ObjectId(listingID),
                            'itemPrice': itemPrice,
                            'servingType': ObjectId(servingType),
                            'itemAvailability': True,
                        }
                    }
                }
        )
        return jsonify(
            {   
                "code": 201,
                "message": "Listing added to menu successfully!"
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": data,
                "message": "An error occurred adding the listing to menu!"
            }
        ), 500
# -----------------------------------------------------------------------------------------


#  -----------------------------------------------------------------------------------------
# [POST] Change Section Name 
# - Change Section Name
# - Possible return codes: 201 (Updated), 500 (Error during update)
@app.route('/editSectionName', methods=['PUT'])
def editSectionName():
    data = request.get_json()
    print(data)
    venueID = data['venueID']
    sectionOrder = data['order']
    sectionName = data['sectionName']

    try: 
        addListing = db.venues.update_one(
            {'_id': ObjectId(venueID), 'menu.order': 0},
            {'$set': {'menu.$.sectionName': sectionName}}
        )
        return jsonify(
            {   
                "code": 201,
                "message": "Section Name changed successfully!"
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": data,
                "message": "Section Name was not changed"}
        ), 500
# -----------------------------------------------------------------------------------------
    
# -----------------------------------------------------------------------------------------
# [POST] Edit menu
# - Edit menu
# - Possible return codes: 201 (Updated), 500 (Error during update)
@app.route('/editMenu', methods=['POST'])
def editMenu():
    data = request.get_json()
    print(data)
    venueID = data['venueID']
    updatedMenu = data['updatedMenu']

    try: 
        editMenu = db.venues.update_one(
            {'_id': ObjectId(venueID)},
            {'$set': {'menu': updatedMenu}}
        )
        return jsonify(
            {   
                "code": 201,
                "message": "Menu edited successfully!"
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": data,
                "message": "An error occurred while editing the menu!"
            }
        ), 500
    
# -----------------------------------------------------------------------------------------
# [POST] Edit venue profile
# - Update producer profile with new details
# - Possible return codes: 201 (Updated), 500 (Error during update)
@app.route('/updateVenueStatus', methods=['POST'])
def updateVenueStatus():
    # fetch sent data
    data = request.get_json()
    print(data)

    # extract components of the data
    venueID = data['businessID']
    venueName = data['newBusinessData']["businessName"]
    venueDesc = data['newBusinessData']["businessDesc"]
    originLocation = data['newBusinessData']["country"]
    hashedPassword = data['newBusinessData']["hashedPassword"]
    claimStatus = data['newBusinessData']["claimStatus"]

    try: 
        update = db.venues.update_one({'_id': ObjectId(venueID)}, 
                                         {'$set': {
                                                'venueName': venueName,
                                                'venueDesc': venueDesc,
                                                'originLocation': originLocation,
                                                'hashedPassword': hashedPassword,
                                                'claimStatus': claimStatus
                                            }})
        return jsonify(
            {   
                "code": 201,
                "message": "Updated claim status successfully!"
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": data,
                "message": "An error occurred updating claim status!"
            }
        ), 500
# -----------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True, port=5300)