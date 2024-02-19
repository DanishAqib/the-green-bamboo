# Port: 5005
# Routes: /createReview (POST)
# -----------------------------------------------------------------------------------------

import bson
import json
from bson import json_util
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from werkzeug.local import LocalProxy

from pymongo.errors import DuplicateKeyError, OperationFailure
from bson.objectid import ObjectId
from bson.errors import InvalidId

import data

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config["MONGO_URI"] = "mongodb+srv://jwleong2020:uOfXCrxLPCjgyA92@greenbamboo.wbiambw.mongodb.net/GreenBamboo?retryWrites=true&w=majority"
db = PyMongo(app).db

def parse_json(data):
    return json.loads(json_util.dumps(data))

# -----------------------------------------------------------------------------------------
# [POST] Creates a review
# - Insert entry into the "reviews" collection. Follows reviews dataclass requirements.
# - Duplicate review check: If a review with the same userID and reviewTarget exists, reject the request
# - Possible return codes: 201 (Created), 400 (Duplicate Detected), 500 (Error during creation)
@app.route("/createReview", methods= ['POST'])
def createReviews():
    rawReview = request.get_json()
    rawReview['reviewTarget'] = ObjectId(rawReview['reviewTarget'])  # Convert reviewTarget to ObjectId
    rawReview['userID'] = ObjectId(rawReview['userID'])  # Convert userID to ObjectId

    # Duplicate listing check: Reject if review with the same userID and reviewTarget exists in the database
    rawReviewBottle = rawReview["reviewTarget"]
    rawReviewUserID = rawReview["userID"]
    existingReview = db.reviews.find_one({"reviewTarget": rawReviewBottle, "userID": rawReviewUserID})
    if(existingReview != None):
        return jsonify(
            {   
                "code": 400,
                "data": {
                    "listingName": rawReview['reviewDesc']
                },
                "message": "Review already exists."
            }
        ), 400
    
    
    # Insert new review into database
    newReview = data.reviews(**rawReview)
    try:
        insertResult = db.reviews.insert_one(data.asdict(newReview))

        return jsonify( 
            {   
                "code": 201,
                "data": rawReview['reviewDesc']
            }
        ), 201
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "data": {
                    "listingName": rawReview['reviewDesc']
                },
                "message": "An error occurred creating the listing."
            }
        ), 500

# -----------------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True, port = 5005)