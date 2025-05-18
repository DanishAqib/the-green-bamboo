# Port: 5300
# Routes: /editDetails (POST), /addUpdates (POST), /sendQuestions (POST), /sendAnswers (POST), /likeUpdates (POST), /unlikeUpdates (POST)
#         /editAddress (POST), /editOpeningHours (POST), /editPublicHolidays (POST), /editReservationDetails (POST), /addListingToMenu (POST)
#         /editSectionName (PUT), /editMenu (POST), /updateVenueStatus (POST), /editUpdate (POST), /deleteUpdate (POST), /editQA (POST)
#         /deleteQA (POST), /addProfileCount (POST), /addNewProfileCount (POST), /deleteMenuItem (DELETE), /updateVenueClaimStatus (POST)
# -----------------------------------------------------------------------------------------

import os
import s3Images
from flask import Blueprint, g, request, jsonify
from datetime import datetime
from scripts import pointsHelperFunc


file_name = os.path.basename(__file__)
blueprint = Blueprint(file_name[:-3], __name__)

# TODO: Create function using BOTO Library to upload images to the S3 bucket
# TODO: Create function using BOTO Library to delete images from the S3 bucket

# -----------------------------------------------------------------------------------------
# [POST] Edit venue profile
# - Update venue profile with new details
# - Possible return codes: 201 (Updated), 500 (Error during update)
@blueprint.route('/editDetails', methods=['POST'])
def editDetails():
    conn = g.db
    cur = conn.cursor()
    data = request.get_json()
    print(data)

    venueID = int(data['venueID'])
    venueName = data['venueName']
    venueDesc = data['venueDesc']
    originLocation = data['originLocation']
    image64 = data.get('image64', '')
    yearOpened = data.get('yearOpened', None)
    openForReservations = data.get('openForReservations')
    website = data.get('website', '')

    try:
        # Find existing venue
        cur.execute('SELECT * FROM venues WHERE id = %s', (venueID,))
        existingVenue = cur.fetchone()

        if existingVenue:
            if existingVenue['photo']:
                s3Images.deleteImageFromS3(existingVenue['photo'])

            if image64:
                image64 = s3Images.uploadBase64ImageToS3(image64)

            # Update the venue details in the database
            cur.execute(
                """
                UPDATE venues 
                SET 
                    "venueName" = %s,
                    "venueDesc" = %s,
                    "originLocation" = %s,
                    "yearOpened" = %s,
                    "openForReservations" = %s,
                    "website" = %s,
                    "photo" = %s
                WHERE id = %s
                """,
                (venueName, venueDesc, originLocation, yearOpened, openForReservations, website, image64, venueID)
            )
            conn.commit()

            return jsonify(
                {
                    "code": 201,
                    "message": "Updated profile successfully!"
                }
            ), 201
        
        else:
            return jsonify(
                {
                    "code": 404,
                    "message": "Venue not found."
                }
            ), 404
        
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred updating profile!"
            }
        ), 500
    
    finally:
        cur.close()

# -----------------------------------------------------------------------------------------
# [POST] Add updates to venue profile
# - Add updates to the venue profile
# - Possible return codes: 201 (Updated), 500 (Error during update)
@blueprint.route('/addUpdates', methods=['POST'])
def addUpdates():
    conn = g.db
    cur = conn.cursor()
    data = request.get_json()
    print(data)
    
    venueID = int(data['venueID'])
    date = datetime.strptime(data['date'], "%Y-%m-%dT%H:%M:%S.%fZ")
    text = data['text']
    image64 = data.get('image64', '')

    try:
        # Find existing venue
        cur.execute('SELECT * FROM venues WHERE id = %s', (venueID,))
        existingVenue = cur.fetchone()

        if existingVenue:
            if image64:
                image64 = s3Images.uploadBase64ImageToS3(image64)

            # Update the venue details in the database
            cur.execute(
                """
                INSERT INTO "venuesUpdates"
                ("venueId", "date", "text", "photo")
                VALUES
                (%s, %s, %s, %s)
                """,
                (venueID, date, text, image64)
            )
            conn.commit()

            return jsonify(
                {
                    "code": 201,
                    "message": "Added update successfully!"
                }
            ), 201
        
        else:
            return jsonify(
                {
                    "code": 404,
                    "message": "Venue not found."
                }
            ), 404
        
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred adding update!"
            }
        ), 500
    
    finally:
        cur.close()

# -----------------------------------------------------------------------------------------
# [POST] Send questions to venue profile
# - Send questions to the venue profile
# - Possible return codes: 201 (Updated), 500 (Error during update)
@blueprint.route('/sendQuestions', methods=['POST'])
def sendQuestions():
    conn = g.db
    cur = conn.cursor()
    data = request.get_json()
    print(data)

    venueID = int(data['venueID'])
    question = data['question']
    answer = data['answer']
    date = datetime.strptime(data['date'], "%Y-%m-%dT%H:%M:%S.%fZ")
    userID = int(data['userID'])

    try:
        cur.execute(
            '''
            INSERT INTO "venuesQuestionAnswers" ("question", "answer", "date", "userId", "venueId")
            VALUES (%s, %s, %s, %s, %s)
            ''',
            (question, answer, date, userID, venueID)
        )
        conn.commit()

        # Award points to user for asking a question
        if pointsHelperFunc.check_max_proof_points(userID):
            return jsonify(
                {
                    "code": 201,
                    "message": "Question sent successfully!",
                }
            ), 201
        
        # get points for asking a question
        cur.execute('SELECT "proofPoints", "ruleName" FROM "pointSystemRules" WHERE id = %s', (15,))
        points = cur.fetchone()

        # Update user's points
        cur.execute('UPDATE "pointsRecorder" SET "currentPoints" = "currentPoints" + %s WHERE "userID" = %s', (points['proofPoints'], userID))
        conn.commit()

        print("Points awarded to user: ", points['proofPoints'])
        cur.execute(
            'SELECT id FROM "badges" '
            'WHERE "relatedEntity" = %s ORDER BY id LIMIT 1',
            ('Question',)
        )
        row = cur.fetchone()
        if not row:                              # no badge configured
            conn.commit()
            return

        question_badge_id = row['id']

        # 2️⃣  Do we already track this badge for the user?
        cur.execute(
            'SELECT id, "currentLevel", "currentProgress" '
            'FROM "userBadges" '
            'WHERE "userId" = %s AND "badgeId" = %s',
            (userID, question_badge_id)
        )
        ub = cur.fetchone()

        if ub is None:
            # First question → badge row with level-1 completed
            cur.execute(
                '''INSERT INTO "userBadges"
                ("userId","badgeId","currentLevel","currentProgress",
                    "dateEarned","lastUpdated")
                VALUES (%s,%s,1,0,NOW(),NOW())''',
                (userID, question_badge_id)
            )
            conn.commit()
            return

        # 3️⃣  Increment progress (every action == level-up)
        level    = ub["currentLevel"]
        progress = ub["currentProgress"] + 1      # will be 1

        if progress >= 1 and level < 100:
            level   += 1
            progress = 0                          # reset because 1 action spent

        # 4️⃣  Persist
        cur.execute(
            '''UPDATE "userBadges"
            SET "currentLevel"   = %s,
                "currentProgress" = %s,
                "lastUpdated"    = NOW()
            WHERE id = %s''',
            (level, progress, ub["id"])
        )
        conn.commit()

        return jsonify(
            {
                "code": 201,
                "message": "Question sent successfully!",
                "pointsEarned": points['proofPoints'],
                "rule": points['ruleName']
            }
        ), 201
    
    except Exception as e:
        conn.rollback()
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred sending the question!"
            }
        ), 500
    
    finally:
        cur.close()

# -----------------------------------------------------------------------------------------
# [POST] Send answers to venue profile
# - Send answers to the venue profile
# - Possible return codes: 201 (Updated), 500 (Error during update)
@blueprint.route('/sendAnswers', methods=['POST'])
def sendAnswers():
    conn = g.db
    cur = conn.cursor()
    data = request.get_json()
    print(data)

    venueID = int(data['venueID'])
    questionsAnswersID = int(data['questionsAnswersID'])
    answer = data['answer']

    try:
        cur.execute(
            '''
            UPDATE "venuesQuestionAnswers"
            SET "answer" = %s
            WHERE "venueId" = %s AND "id" = %s
            ''',
            (answer, venueID, questionsAnswersID)
        )
        conn.commit()

        return jsonify(
            {
                "code": 201,
                "message": "Answer sent successfully!"
            }
        ), 201
    
    except Exception as e:
        conn.rollback()
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred sending the answer!"
            }
        ), 500
    
    finally:
        cur.close()

# -----------------------------------------------------------------------------------------
# [POST] Like updates
# - Like updates
# - Possible return codes: 201 (Updated), 500 (Error during update)
@blueprint.route('/likeUpdates', methods=['POST'])
def likeUpdates():
    conn = g.db
    cur = conn.cursor()
    data = request.get_json()
    print(data)

    venueID = int(data['venueID'])
    updateID = int(data['updateID'])
    userID = int(data['userID'])
    userType = data['userType']

    try:
        # Verify that the update exists and belongs to the venue
        cur.execute('SELECT "venueId" FROM "venuesUpdates" WHERE "id" = %s', (updateID,))
        existingUpdate = cur.fetchone()

        if not existingUpdate or existingUpdate['venueId'] != venueID:
            return jsonify(
                {
                    "code": 404,
                    "message": "Update not found."
                }
            ), 404
        
        # Insert into the likes table
        cur.execute("""
            INSERT INTO "venueUpdateLikes" ("updateId", "userId", "userType")
            VALUES (%s, %s, %s)
        """, (updateID, userID, userType))
        conn.commit()

        return jsonify(
            {
                "code": 201,
                "message": "Update liked successfully!"
            }
        ), 201
    
    except Exception as e:
        conn.rollback()
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred liking the update!"
            }
        ), 500
    
    finally:
        cur.close()

# -----------------------------------------------------------------------------------------
# [POST] Unlike updates
# - Unlike updates
# - Possible return codes: 201 (Updated), 500 (Error during update)
@blueprint.route('/unlikeUpdates', methods=['POST'])
def unlikeUpdates():
    conn = g.db
    cur = conn.cursor()
    data = request.get_json()
    print(data)

    venueID = int(data['venueID'])
    updateID = int(data['updateID'])
    userID = int(data['userID'])
    userType = data['userType']

    try:
        # Verify that the update exists and belongs to the venue
        cur.execute('SELECT "venueId" FROM "venuesUpdates" WHERE "id" = %s', (updateID,))
        existingUpdate = cur.fetchone()

        if not existingUpdate or existingUpdate['venueId'] != venueID:
            return jsonify(
                {
                    "code": 404,
                    "message": "Update not found."
                }
            ), 404
        
        # Remove from the likes table
        cur.execute("""
            DELETE FROM "venueUpdateLikes"
            WHERE "updateId" = %s AND "userId" = %s AND "userType" = %s
        """, (updateID, userID, userType))
        conn.commit()

        return jsonify(
            {
                "code": 201,
                "message": "Update unliked successfully!"
            }
        ), 201
    
    except Exception as e:
        conn.rollback()
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred unliking the update!"
            }
        ), 500
    
    finally:
        cur.close()

# -----------------------------------------------------------------------------------------
# [POST] Edit address
# - Edit address
# - Possible return codes: 201 (Updated), 500 (Error during update)
@blueprint.route('/editAddress', methods=['POST'])
def editAddress():
    conn = g.db
    cur = conn.cursor()
    data = request.get_json()
    print(data)

    venueID = int(data['venueID'])
    updatedAddress = data['updatedAddress']

    try:
        cur.execute("""
            UPDATE venues
            SET "address" = %s
            WHERE "id" = %s
        """, (updatedAddress, venueID))
        conn.commit()

        return jsonify(
            {
                "code": 201,
                "message": "Updated address successfully!"
            }
        ), 201
    
    except Exception as e:
        conn.rollback()
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred updating address!"
            }
        ), 500
    
    finally:
        cur.close()

# -----------------------------------------------------------------------------------------
# [POST] Edit opening hours
# - Edit opening hours
# - Possible return codes: 201 (Updated), 500 (Error during update)
@blueprint.route('/editOpeningHours', methods=['POST'])
def editOpeningHours():
    conn = g.db
    cur = conn.cursor()
    data = request.get_json()
    print(data)

    venueID = int(data['venueID'])
    updatedOpeningHours = data['updatedOpeningHours']

    # Prepare the updated opening hours for insertion
    opening_hours = (
        updatedOpeningHours.get('Monday', []),
        updatedOpeningHours.get('Tuesday', []),
        updatedOpeningHours.get('Wednesday', []),
        updatedOpeningHours.get('Thursday', []),
        updatedOpeningHours.get('Friday', []),
        updatedOpeningHours.get('Saturday', []),
        updatedOpeningHours.get('Sunday', [])
    )

    try:
        # Check if opening hours entry already exists
        cur.execute('SELECT id FROM "venuesOpeningHours" WHERE "venueId" = %s', (venueID,))
        existing_entry = cur.fetchone()

        if existing_entry:
            cur.execute("""
                UPDATE "venuesOpeningHours" 
                SET "Monday" = %s, "Tuesday" = %s, "Wednesday" = %s, 
                    "Thursday" = %s, "Friday" = %s, "Saturday" = %s, 
                    "Sunday" = %s 
                WHERE "venueId" = %s
            """, (*opening_hours, venueID))

        else:
            cur.execute(
                """
                    INSERT INTO "venuesOpeningHours" ("Monday", "Tuesday", "Wednesday", 
                    "Thursday", "Friday", "Saturday", "Sunday", "venueId") 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (*opening_hours, venueID)
            )
        conn.commit()

        return jsonify(
            {
                "code": 201,
                "message": "Updated opening hours successfully!"
            }
        ), 201
    
    except Exception as e:
        conn.rollback()
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred updating opening hours!"
            }
        ), 500
    
    finally:
        cur.close()

# -----------------------------------------------------------------------------------------
# [POST] Edit public holidays
# - Edit public holidays
# - Possible return codes: 201 (Updated), 500 (Error during update)
@blueprint.route('/editPublicHolidays', methods=['POST'])
def editPublicHolidays():
    conn = g.db
    cur = conn.cursor()
    data = request.get_json()
    print(data)

    venueID = int(data['venueID'])
    publicHolidays = data['updatedPublicHolidays']

    try:
        cur.execute("""
            UPDATE venues
            SET "publicHolidays" = %s
            WHERE "id" = %s
        """, (publicHolidays, venueID))
        conn.commit()

        return jsonify(
            {
                "code": 201,
                "message": "Updated public holidays successfully!"
            }
        ), 201
    
    except Exception as e:
        conn.rollback()
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred updating public holidays!"
            }
        ), 500
    
    finally:
        cur.close()

# -----------------------------------------------------------------------------------------
# [POST] Edit reservation details
# - Edit reservation details
# - Possible return codes: 201 (Updated), 500 (Error during update)
@blueprint.route('/editReservationDetails', methods=['POST'])
def editReservationDetails():
    conn = g.db
    cur = conn.cursor()
    data = request.get_json()
    print(data)

    venueID = int(data['venueID'])
    reservationDetails = data['updatedReservationDetails']

    try:
        cur.execute("""
            UPDATE venues
            SET "reservationDetails" = %s
            WHERE "id" = %s
        """, (reservationDetails, venueID))
        conn.commit()

        return jsonify(
            {
                "code": 201,
                "message": "Updated reservation details successfully!"
            }
        ), 201
    
    except Exception as e:
        conn.rollback()
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred updating reservation details!"
            }
        ), 500
    
    finally:
        cur.close()

# -----------------------------------------------------------------------------------------
# [POST] Add listing to menu
# - Add listing to menu
# - Possible return codes: 201 (Updated), 500 (Error during update)
@blueprint.route('/addListingToMenu', methods=['POST'])
def addListingToMenu():
    conn = g.db
    cur = conn.cursor()
    data = request.get_json()
    print(data)

    venueID = int(data['venueID'])
    menuOrder = int(data['menuOrder'])
    listingID = int(data['listingID'])
    itemPrice = data['itemPrice']
    servingType = int(data['servingType'])
    sectionName = data['sectionName']

    try:
        # Get sectionId based on the sectionName
        cur.execute(
            'SELECT id FROM "venuesMenu" WHERE "sectionName" = %s AND "venueId" = %s',
            (sectionName, venueID)
        )
        section = cur.fetchone()

        if section is None:
            return jsonify(
                {
                    "code": 404,
                    "message": "Menu section not found."
                }
            ), 404
        
        sectionId = section['id']

        cur.execute(
            """
                INSERT INTO "menuItems" ("itemOrder", "itemPrice", "itemAvailability", "itemID", "itemServingType", "sectionId")
                VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (menuOrder, itemPrice, True, listingID, servingType, sectionId)
        )
        conn.commit()

        return jsonify(
            {
                "code": 201,
                "message": "Listing added to menu successfully!"
            }
        ), 201
    
    except Exception as e:
        conn.rollback()
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred adding the listing to menu!"
            }
        ), 500
    
    finally:
        cur.close()
# -----------------------------------------------------------------------------------------


#  -----------------------------------------------------------------------------------------
# [POST] Change Section Name 
# - Change Section Name
# - Possible return codes: 201 (Updated), 500 (Error during update)
@blueprint.route('/editSectionName', methods=['PUT'])
def editSectionName():
    conn = g.db
    cur = conn.cursor()
    data = request.get_json()
    print(data)

    venueID = int(data['venueID'])
    sectionOrder = int(data['order'])
    sectionName = data['sectionName']

    try:
        cur.execute(
            '''
            UPDATE "venuesMenu"
            SET "sectionName" = %s
            WHERE "venueId" = %s AND "sectionOrder" = %s
            ''',
            (sectionName, venueID, sectionOrder)
        )
        conn.commit()

        return jsonify(
            {
                "code": 201,
                "message": "Section name changed successfully!"
            }
        ), 201
    
    except Exception as e:
        conn.rollback()
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred changing the section name!"
            }
        ), 500
    
    finally:
        cur.close()
# -----------------------------------------------------------------------------------------
    
# -----------------------------------------------------------------------------------------
# [POST] Edit menu
# - Edit menu
# - Possible return codes: 201 (Updated), 500 (Error during update)
@blueprint.route('/editMenu', methods=['POST'])
def editMenu():
    conn = g.db
    cur = conn.cursor()
    data = request.get_json()
    print(data)

    venueID = int(data['venueID'])
    updatedMenu = data['updatedMenu']

    try:
        # Clear existing menu
        cur.execute('DELETE FROM "menuItems" WHERE "sectionId" IN (SELECT "id" FROM "venuesMenu" WHERE "venueId" = %s)', (venueID,))
        cur.execute('DELETE FROM "venuesMenu" WHERE "venueId" = %s', (venueID,))

        # Insert updated menu sections
        for section in updatedMenu:
            cur.execute(
                '''
                INSERT INTO "venuesMenu" ("sectionName", "sectionOrder", "venueId")
                VALUES (%s, %s, %s)
                RETURNING id
                ''',
                (section['sectionName'], section['sectionOrder'], venueID)
            )
            sectionId = cur.fetchone()['id']

            # Insert items for each section
            for item in section.get('sectionMenu', []):
                cur.execute(
                    '''
                    INSERT INTO "menuItems" ("itemOrder", "itemPrice", "itemAvailability", "itemID", "itemServingType", "sectionId")
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ''',
                    (item.get('itemOrder'), item.get('itemPrice'), item.get('itemAvailability'), item.get('itemID'), item.get('itemServingType'), sectionId)
                )

        conn.commit()
        return jsonify(
            {
                "code": 201,
                "message": "Menu edited successfully!"
            }
        ), 201
    
    except Exception as e:
        conn.rollback()
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred editing the menu!"
            }
        ), 500
    
    finally:
        cur.close()

    
# -----------------------------------------------------------------------------------------
# [POST] Edit venue profile
# - Update producer profile with new details
# - Possible return codes: 201 (Updated), 500 (Error during update)
@blueprint.route('/updateVenueStatus', methods=['POST'])
def updateVenueStatus():
    conn = g.db
    cur = conn.cursor()
    data = request.get_json()
    print(data)

    venueID = int(data['businessID'])
    venueName = data['newBusinessData']["businessName"]
    venueDesc = data['newBusinessData']["businessDesc"]
    originLocation = data['newBusinessData']["country"]
    hashedPassword = data['newBusinessData']["hashedPassword"]
    claimStatus = data['newBusinessData']["claimStatus"]
    requestId = int(data['newBusinessData']["requestId"])

    try:
        cur.execute('UPDATE venues SET "venueName" = %s, "venueDesc" = %s, "originLocation" = %s, "hashedPassword" = %s, "claimStatus" = %s, "requestId" = %s WHERE "id" = %s', (venueName, venueDesc, originLocation, hashedPassword, claimStatus, requestId, venueID))
        conn.commit()

        return jsonify(
            {
                "code": 201,
                "message": "Updated claim status successfully!"
            }
        ), 201
    
    except Exception as e:
        conn.rollback()
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred updating claim status!"
            }
        ), 500
    
    finally:
        cur.close()

# -----------------------------------------------------------------------------------------

# [POST] Edit venue update
# - Update a venue update with new details
# - Possible return codes: 201 (Updated), 500 (Error during update)
@blueprint.route('/editUpdate', methods=['POST'])
def editUpdate():
    conn = g.db
    cur = conn.cursor()
    data = request.get_json()
    print(data)

    venueID = int(data['venueID'])
    updateID = int(data['updateID'])
    update = data['update']
    image64 = data.get('image64', '')

    try:
        # Find existing venue
        cur.execute('SELECT * FROM "venuesUpdates" WHERE "venueId" = %s AND "id" = %s', (venueID, updateID))
        existingUpdate = cur.fetchone()

        if existingUpdate:
            # Delete old photo from S3 if it exists
            if existingUpdate['photo']:
                s3Images.deleteImageFromS3(existingUpdate['photo'])

            if image64:
                image64 = s3Images.uploadBase64ImageToS3(image64)

            # Update the venue details in the database
            cur.execute(
                """
                UPDATE "venuesUpdates"
                SET 
                    "text" = %s,
                    "photo" = %s
                WHERE "venueId" = %s AND "id" = %s
                """,
                (update, image64, venueID, updateID)
            )
            conn.commit()

            return jsonify(
                {
                    "code": 201,
                    "message": "Updated update successfully!"
                }
            ), 201
        
        else:
            return jsonify(
                {
                    "code": 404,
                    "message": "Update not found."
                }
            ), 404
        
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred updating update!"
            }
        ), 500
    
    finally:
        cur.close()

# -----------------------------------------------------------------------------------------

# [POST] Delete venue update
# - Delete a venue update with new details
# - Possible return codes: 201 (Updated), 500 (Error during update)
@blueprint.route('/deleteUpdate', methods=['POST'])
def deleteUpdate():
    conn = g.db
    cur = conn.cursor()
    data = request.get_json()
    print(data)

    venueID = int(data['venueID'])
    updateID = int(data['updateID'])

    try:
        # Find existing venue and see if photo exists, if it does delete it from S3 bucket
        cur.execute('SELECT * FROM "venuesUpdates" WHERE "venueId" = %s AND "id" = %s', (venueID, updateID))
        existingUpdate = cur.fetchone()

        if existingUpdate:
            if existingUpdate['photo']:
                s3Images.deleteImageFromS3(existingUpdate['photo'])

            # Delete the venue update from the database
            cur.execute('DELETE FROM "venuesUpdates" WHERE "venueId" = %s AND "id" = %s', (venueID, updateID))
            conn.commit()

            return jsonify(
                {
                    "code": 201,
                    "message": "Update deleted successfully!"
                }
            ), 201
        
        else:
            return jsonify(
                {
                    "code": 404,
                    "message": "Update not found."
                }
            ), 404
        
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred deleting update!"
            }
        ), 500
    
    finally:
        cur.close()


# -----------------------------------------------------------------------------------------

# [POST] Edit Q&A
# - Update a venue Q&A with new details
# - Possible return codes: 201 (Updated), 500 (Error during update)
@blueprint.route('/editQA', methods=['POST'])
def editQA():
    conn = g.db
    cur = conn.cursor()
    data = request.get_json()
    print(data)

    venueID = int(data['venueID'])
    questionsAnswersID = int(data['questionsAnswersID'])
    answer = data['answer']

    try:
        # Update the answer
        cur.execute('UPDATE "venuesQuestionAnswers" SET "answer" = %s WHERE "venueId" = %s AND "id" = %s', (answer, venueID, questionsAnswersID))
        conn.commit()

        return jsonify(
            {
                "code": 201,
                "message": "Updated venue's Q&A!"
            }
        ), 201
    
    except Exception as e:
        conn.rollback()
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred updating venue's Q&A!"
            }
        ), 500
    
    finally:
        cur.close()

# -----------------------------------------------------------------------------------------

# [POST] Delete venue Q&A
# - Delete a venue Q&A with new details
# - Possible return codes: 201 (Updated), 500 (Error during update)
@blueprint.route('/deleteQA', methods=['POST'])
def deleteQA():
    conn = g.db
    cur = conn.cursor()
    data = request.get_json()
    print(data)

    venueID = int(data['venueID'])
    questionsAnswersID = int(data['questionsAnswersID'])

    try:
        # get the user id of the user who asked the question
        cur.execute('SELECT "userId" FROM "venuesQuestionAnswers" WHERE "venueId" = %s AND "id" = %s', (venueID, questionsAnswersID))
        userId = cur.fetchone()['userId'] 

        cur.execute('DELETE FROM "venuesQuestionAnswers" WHERE "venueId" = %s AND "id" = %s', (venueID, questionsAnswersID))
        conn.commit()

        # Deduct points from user for deleting a question
 
        # get points for deleting a question
        cur.execute('SELECT "proofPoints", "ruleName" FROM "pointSystemRules" WHERE id = %s', (15,))
        points = cur.fetchone()

        # Update user's points
        cur.execute('UPDATE "pointsRecorder" SET "currentPoints" = "currentPoints" - %s WHERE "userID" = %s', (points['proofPoints'], userId,))
        conn.commit()

        print("Points deducted from user: ", points['proofPoints'])
        
        return jsonify(
            {
                "code": 201,
                "message": "Deleted venue's Q&A!",
                "pointsDeducted": points['proofPoints'],
                "rule": points['rule']
            }
        ), 201
    
    except Exception as e:
        conn.rollback()
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred deleting venue's Q&A!"
            }
        ), 500
    
    finally:
        cur.close()

# -----------------------------------------------------------------------------------------

# [POST] Add profile view count
# - Add profile view count
# - Possible return codes: 201 (Updated), 500 (Error during update)
@blueprint.route('/addProfileCount', methods=['POST'])
def addProfileCount():
    conn = g.db
    cur = conn.cursor()
    data = request.get_json()
    print(data)

    venueID = int(data['venueID'])
    date = datetime.strptime(data['date'], "%Y-%m-%dT%H:%M:%S.%fZ")

    try:
        # Check if a record already exists for the venue
        cur.execute('SELECT * FROM "venuesProfileViews" WHERE "venueId" = %s', (venueID,))
        existingRecord = cur.fetchone()

        if existingRecord:
            cur.execute(
                """
                UPDATE "venuesProfileViews"
                SET "date" = %s, "count" = "count" + 1
                WHERE "venueId" = %s
                """,
                (date, venueID)
            )
        else:
            cur.execute(
                """
                INSERT INTO "venuesProfileViews" ("date", "count", "venueId")
                VALUES (%s, 1, %s)
                """,
                (date, venueID)
            )

        conn.commit()

        return jsonify(
            {
                "code": 201,
                "message": "Profile view count updated successfully!"
            }
        ), 201
    
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred updating the profile view count."
            }
        ), 500
    
    finally:
        cur.close()

# -----------------------------------------------------------------------------------------

# [POST] Add new profile view count
# - Add new profile view count
# - Possible return codes: 201 (Updated), 500 (Error during update)
@blueprint.route('/addNewProfileCount', methods=['POST'])
def addNewProfileCount():
    conn = g.db
    cur = conn.cursor()
    data = request.get_json()
    print(data)

    venueID = int(data['venueID'])
    date = datetime.strptime(data['date'], "%Y-%m-%dT%H:%M:%S.%fZ")

    try:
        # Check if a record already exists for the venue
        cur.execute('SELECT * FROM "venuesProfileViews" WHERE "venueId" = %s', (venueID,))
        existingRecord = cur.fetchone()

        if existingRecord:
            cur.execute(
                """
                UPDATE "venuesProfileViews"
                SET "date" = %s, "count" = "count" + 1
                WHERE "venueId" = %s
                """,
                (date, venueID)
            )
        else:
            cur.execute(
                """
                INSERT INTO "venuesProfileViews" ("date", "count", "venueId")
                VALUES (%s, 1, %s)
                """,
                (date, venueID)
            )

        conn.commit()

        return jsonify(
            {
                "code": 201,
                "message": "New profile view count updated successfully!"
            }
        ), 201
    
    except Exception as e:
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred updating the new profile view count."
            }
        ), 500
    
    finally:
        cur.close()
    
# -----------------------------------------------------------------------------------------
# [POST] Edit venue profile claim status
# - Update venue profile with new details
# - Possible return codes: 201 (Updated), 500 (Error during update)
@blueprint.route('/updateVenueClaimStatus', methods=['POST'])
def updateVenueClaimStatus():
    conn = g.db
    cur = conn.cursor()
    data = request.get_json()
    print(data)

    venueID = int(data['businessId'])
    claimStatus = data['claimStatus']

    try:
        cur.execute('UPDATE venues SET "claimStatus" = %s WHERE "id" = %s', (claimStatus, venueID))
        conn.commit()

        return jsonify(
            {
                "code": 201,
                "message": "Updated claim status successfully!"
            }
        ), 201
    
    except Exception as e:
        conn.rollback()
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred updating claim status!"
            }
        ), 500
    
    finally:
        cur.close()


# -----------------------------------------------------------------------------------------
# [POST] Edit venue profile last check claim status date
# - Update venue profile with new details
# - Possible return codes: 201 (Updated), 500 (Error during update)
@blueprint.route('/updateVenueClaimStatusCheckDate', methods=['POST'])
def updateVenueClaimStatusCheckDate():
    conn = g.db
    cur = conn.cursor()
    data = request.get_json()
    print(data)

    venueID = int(data['businessId'])
    claimStatusCheckDate = datetime.strptime(data['claimStatusCheckDate'], "%Y-%m-%dT%H:%M:%S.%fZ")

    try:
        cur.execute('UPDATE venues SET "claimStatusCheckDate" = %s WHERE "id" = %s', (claimStatusCheckDate, venueID))
        conn.commit()

        return jsonify(
            {
                "code": 201,
                "message": "Updated claim status check date successfully!"
            }
        ), 201
    
    except Exception as e:
        conn.rollback()
        print(str(e))
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred updating claim status check date!"
            }
        ), 500
    
    finally:
        cur.close()
