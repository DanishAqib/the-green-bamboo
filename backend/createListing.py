# Port: 5001
# Routes: /createListing (POST)
# Dataclass: listings
# -----------------------------------------------------------------------------------------

import bson
import json
from bson import json_util
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS

from datetime import datetime
import pytz

import data

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config["MONGO_URI"] = "mongodb+srv://jwleong2020:uOfXCrxLPCjgyA92@greenbamboo.wbiambw.mongodb.net/GreenBamboo?retryWrites=true&w=majority"
db = PyMongo(app).db

def parse_json(data):
    return json.loads(json_util.dumps(data))

# -----------------------------------------------------------------------------------------
# [POST] Creates a listing
# - Insert entry into the "listings" collection. Follows listings dataclass requirements.
# - Duplicate listing check: If a listing with the same name exists, reject the request
# - Possible return codes: 201 (Created), 400 (Duplicate Detected), 500 (Error during creation)
@app.route("/createListing", methods= ['POST'])
def createListings():
    rawBottle = request.get_json()
    # Add current datetime to the listing
    rawBottle['addedDate'] = datetime.now(pytz.timezone('Etc/GMT-8'))
    rawBottle["allowMod"] = True

    # Duplicate listing check: Reject if listing with the same bottle name already exists in the database
    rawBottleName = rawBottle["listingName"]
    existingBottle = db.listings.find_one({"listingName": rawBottleName})
    if(existingBottle != None):
        return jsonify(
            {   
                "code": 400,
                "data": {
                    "listingName": rawBottleName
                },
                "message": "Bottle already exists."
            }
        ), 400
    
    
    # Insert new listing into database
    newBottle = data.listings(**rawBottle)
    try:
        insertResult = db.listings.insert_one(data.asdict(newBottle))

        return jsonify( 
            {   
                "code": 201,
                "data": rawBottleName
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": {
                    "listingName": rawBottleName
                },
                "message": "An error occurred creating the listing."
            }
        ), 500

# -----------------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True, port = 5001)