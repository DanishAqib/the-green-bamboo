# Port: 5052
# Routes: /updateObservationTag (PUT)
# -----------------------------------------------------------------------------------------

import bson
import json
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from werkzeug.utils import secure_filename

from bson.objectid import ObjectId

from gridfs import GridFS
import os
from datetime import datetime

import csv
import io
import codecs
import data

from urllib.request import urlopen
import base64

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config["MONGO_URI"] = "mongodb+srv://jwleong2020:uOfXCrxLPCjgyA92@greenbamboo.wbiambw.mongodb.net/GreenBamboo?retryWrites=true&w=majority"
db = PyMongo(app).db

mongo = PyMongo(app)
fs = GridFS(mongo.db)

# -----------------------------------------------------------------------------------------
# [POST] Creates an observation tag
# - Insert entry into the "observationTags" collection. Follows observationTag dataclass requirements.
# - Duplicate review check: If an observationTag with the same observationTag, reject the request
# - Possible return codes: 201 (Created), 400 (Duplicate Detected), 500 (Error during creation)
@app.route("/createObservationTag", methods= ['POST'])
def createObservationTag():
    rawTag = request.get_json()
    print(rawTag)
    rawObservation= rawTag['observationTag']
    # Duplicate listing check: Reject if review with the same observation exists in the database
    existingAccount = db.observationTags.find_one({"observationTag": rawObservation})
    if(existingAccount!= None):
        return jsonify(
            {   
                "code": 400,
                "data": {
                    "ObservationTag": rawObservation
                },
                "message": "Observation tag already exists."
            }
        ), 400
    
    
    # Insert new review into database
    newAccount = data.observationTags(**rawTag)
    try:
        insertResult = db.observationTags.insert_one(data.asdict(newAccount))

        return jsonify( 
            {   
                "code": 201,
                "data": rawObservation
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": {
                    "ObservationTag": rawObservation
                },
                "message": "An error occurred creating the observation tag."
            }
        ), 500

# -----------------------------------------------------------------------------------------
    
# [PUT] Update review
# - Update review with review metrics
# - Possible return codes: 201 (Updated), 400(Observation tag not found), 500 (Error during update)
@app.route('/updateObservationTag', methods=['PUT'])
def updateObservationTag():
    data = request.get_json()
    # for loop for each observation tag and update
    updates = []
    for elem in data:

        existingObservationTag = db.observationTags.find_one({'_id': ObjectId(elem["_id"]["$oid"])})

        if(existingObservationTag == None):
            return jsonify(
                {   
                    "code": 400,
                    "data": {
                        "observationTag": elem['observationTag']
                    },
                    "message": "Observation Tag does not exist."
                }
            ), 400

        tag_key, tag_value = list(elem.items())[1]
        tag_dict = {"$set":{tag_key: tag_value}}
        updates.append({"filter": {"_id": ObjectId(elem["_id"]["$oid"])}, "update": tag_dict})


    try: 
        for update in updates:
            filter_criteria = update["filter"]
            update_data = update["update"]
            db.observationTags.update_many(filter_criteria, update_data)
        return jsonify(
            {   
                "code": 201,
                "data": elem['observationTag']
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": {
                    "data": elem['observationTag']
                },
                "message": "An error occurred updating the observation tags."
            }
        ), 500
    
# -----------------------------------------------------------------------------------------
# [DELETE] Deletes a observationTag
# - Delete entry with specified id from the "observationTag" collection.
# - Possible return codes: 201 (Deleted), 400 (Review doesn't exist), 500 (Error during deletion)
@app.route("/deleteObservationTag/<id>", methods= ['DELETE'])
def deleteObservationTag(id):

    # Find the review entry with the specified id
    existingObservation = db.observationTags.find_one({"_id": ObjectId(id)})
    if(existingObservation == None):
        return jsonify(
            {   
                "code": 400,
                "data": {
                    "id": id
                },
                "message": "Observation tag doesn't exist."
            }
        ), 400
    

    # Delete the review entry with the specified id
    try:
        deleteObservation = db.observationTags.delete_one({"_id": ObjectId(id)})

        return jsonify( 
            {   
                "code": 200,
                "data": id
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": {
                    "id": id
                },
                "message": "An error occurred deleting the observation."
            }
        ), 500
    
# -----------------------------------------------------------------------------------------
# [POST] Creates a flavour family tag
# - Insert entry into the "familyTags" collection. Follows flavourTag dataclass requirements.
# - Duplicate review check: If a flavourTag with the same flavourTag, reject the request
# - Possible return codes: 201 (Created), 400 (Duplicate Detected), 500 (Error during creation)
@app.route("/createFamilyTag", methods= ['POST'])
def createFamilyTag():
    rawTag = request.get_json()
    print(rawTag)
    rawFamily= rawTag['familyTag']
    # Duplicate listing check: Reject if review with the same observation exists in the database
    existingTag = db.flavourTags.find_one({"familyTag": rawFamily})
    if(existingTag!= None):
        return jsonify(
            {   
                "code": 400,
                "data": {
                    "familyTag": rawFamily
                },
                "message": "Family tag already exists."
            }
        ), 400
    
    
    # Insert new review into database
    newFamily = data.flavourTags(**rawTag)
    try:
        insertResult = db.flavourTags.insert_one(data.asdict(newFamily))

        return jsonify( 
            {   
                "code": 201,
                "data": rawFamily
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": {
                    "familyTag": rawFamily
                },
                "message": "An error occurred creating the family tag."
            }
        ), 500
# -----------------------------------------------------------------------------------------
# [POST] Creates a flavour sub tag
# - Insert entry into the "subTags" collection. Follows subTag dataclass requirements.
# - Duplicate review check: If a subTag with the same subTag, reject the request
# - Possible return codes: 201 (Created), 400 (Duplicate Detected), 500 (Error during creation)
@app.route("/createSubTag", methods= ['POST'])
def createSubTag():
    rawTag = request.get_json()
    print(rawTag)
    rawSub= rawTag['subTag']
    # Duplicate listing check: Reject if review with the same observation exists in the database
    existingTag = db.subTags.find_one({"subTag": rawSub})
    if(existingTag!= None):
        return jsonify(
            {   
                "code": 400,
                "data": {
                    "subTag": rawSub
                },
                "message": "Sub tag already exists."
            }
        ), 400
    
    
    # Insert new review into database
    rawTag['familyTagId']= ObjectId(rawTag['familyTagId'])
    newSub = data.subTags(**rawTag)
    try:
        insertResult = db.subTags.insert_one(data.asdict(newSub))

        return jsonify( 
            {   
                "code": 201,
                "data": rawSub
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": {
                    "subTag": rawSub
                },
                "message": "An error occurred creating the sub tag."
            }
        ), 500
# -----------------------------------------------------------------------------------------
    
# To convert image URL to base64    
def image_url_to_base64(url):
    try:
        # Fetch the image from the URL
        with urlopen(url) as response:
            # Read the image data
            image_data = response.read()
            # Convert the image data to base64
            base64_str = base64.b64encode(image_data).decode('utf-8')
            return base64_str
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
# -----------------------------------------------------------------------------------------

# To hash the password
def hash_password(id, password):
    combinedString = str(id) + password
    hash = 0

    for i in range(len(combinedString)):
        char = ord(combinedString[i])
        hash = (hash << 5) - hash + char
        hash &= 0xFFFFFFFF  # Convert to 32-bit integer

    if hash & (1 << 31):  # If the highest bit is set
        hash -= 1 << 32  # Convert to a signed integer

    return hash

# -----------------------------------------------------------------------------------------

# [POST] Import listings
# - Bulk import listings
# - Possible return codes: 201 (Updated), 400(Observation tag not found), 500 (Error during update)
@app.route('/importListings', methods=['POST'])
def importListings():

    
    file = request.files['file']

    # Specify data types for each column
    column_data_types = [str, str, str, str, str, str, str, str, str, str, str, str]

    #Read the CSV file
    csv_data = csv.reader(io.TextIOWrapper(file, 'utf-8'))

    # Skip to the data import rows
    next(csv_data)
    next(csv_data)
    next(csv_data)
    next(csv_data)

    # Create a list to store all the documents to be inserted
    documents = []

    # Create a dict to store all the id and name of producer in producer collection 
    producer_name_id_dict={}
    for doc in db.producers.find({}):
        producer_name_id_dict[doc["producerName"]]=doc["_id"]
    
    # print(producer_name_id_dict)

    for row in csv_data:
            
        # Convert each value to the specified data type
        converted_row = [data_type(value) for data_type, value in zip(column_data_types, row)]
        
        # Lookup producer ID based on producer name

        producer_name = converted_row[1]  # Assuming producerName is at index 1
        producer_id=producer_name_id_dict.get(producer_name)

        if producer_id == None:
            producer_to_insert =   {
                "producerName": producer_name,
                "producerDesc": "",
                "originCountry": "",
                "statusOB": "",
                "mainDrinks": [],
                "photo": "",
                "hashedPassword": hash_password(producer_name, "admin1234"),
                "questionsAnswers": [],
                "updates": [],
                "producerLink": "",
                "claimStatus": False,
            }
            new_producer_result = db.producers.insert_one(producer_to_insert)
            producer_id = new_producer_result.inserted_id
        
            # Cache the new producer ID to avoid future database queries for this producer
            producer_name_id_dict[producer_name] = producer_id


        # Convert the image URL to base64
        base64_str = image_url_to_base64(converted_row[11])
            
        # Create a dictionary representing the row
        row_dict = {
            'listingName': converted_row[0],
            'producerID': producer_id,
            'bottler': converted_row[2],
            'originCountry': converted_row[3],
            'drinkType': converted_row[4],
            'typeCategory': converted_row[5],
            'age': converted_row[6],
            'abv': converted_row[7],
            'reviewLink': converted_row[8],
            'officialDesc': converted_row[9],
            'sourceLink': converted_row[10],
            'photo': base64_str,
            'allowMod':True,
            'addedDate': datetime.now()
        }
        
        # Insert the row into MongoDB
        documents.append(row_dict)

    try:
        db.listings.insert_many(documents)


    # If error occurs, return 500 error
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "Bulk Import Listings Failed. An error occurred."
            }
        ), 500

    # If successful, return 201
    return jsonify(
        {
            "code": 201,
            "message": "Bulk Import Listings Successful"
        }), 201




    # for loop for each observation tag and update
    updates = []
    for elem in data:

        existingObservationTag = db.observationTags.find_one({'_id': ObjectId(elem["_id"]["$oid"])})

        if(existingObservationTag == None):
            return jsonify(
                {   
                    "code": 400,
                    "data": {
                        "observationTag": elem['observationTag']
                    },
                    "message": "Observation Tag does not exist."
                }
            ), 400

        tag_key, tag_value = list(elem.items())[1]
        tag_dict = {"$set":{tag_key: tag_value}}
        updates.append({"filter": {"_id": ObjectId(elem["_id"]["$oid"])}, "update": tag_dict})


    try: 
        for update in updates:
            filter_criteria = update["filter"]
            update_data = update["update"]
            db.observationTags.update_many(filter_criteria, update_data)
        return jsonify(
            {   
                "code": 201,
                "data": elem['observationTag']
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": {
                    "data": elem['observationTag']
                },
                "message": "An error occurred updating the observation tags."
            }
        ), 500

# -----------------------------------------------------------------------------------------
@app.route('/readCSV', methods=['GET'])
def readCSV():
    with codecs.open('Dataset/listingsFormat.csv', 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return jsonify(
        {
            "code": 201,
            "data": data
        }), 201

# -----------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True, port=5052)