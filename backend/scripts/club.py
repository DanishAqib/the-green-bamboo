# Routes: /getClubs (GET), /getClubwSearch (GET), /getSpecificClubInfo (GET),
#         /getClubPosts (GET), /getClubPostDetails (GET), /checkUserMembership (GET),
#         /getUserLikesDislikesPost (GET), /getUserLikesDislikesComments (GET), /getUserClubs (GET),
#         /getClubMembers (GET), /getFirstFewClubMembers (GET), /getAllClubMembers (GET),
#         /getClubRequests (GET), /getUserClubRequests (GET), /getUserInvitedClubs (GET),
#         /getRecentActivity (GET), /canCreate (GET)

#         /createClubs (POST), /addClubMembers (POST), /joinClub (POST), 
#         /addPost (POST), /addComment (POST), /requestToJoinClub (POST),
#         /acceptClubRequest (POST), /acceptClubInvite (POST),

#         /editPost (PUT), /editComment (PUT),
#         /dislikeUndislikePost (PUT), /dislikeUndislikeComment (PUT),
#         /likeUnlikePost (PUT), /likeUnlikeComment (PUT), /makeAdmin (PUT), 
#         /revokeAdmin (PUT), /updateClubInfo (PUT),

#         /removeMembers (DELETE), /removePost (DELETE), /removeComment (DELETE),
#         /leaveClub (DELETE), /deleteClub (DELETE), /rejectClubRequests (DELETE),
#         /declineClubInvites (DELETE)
# -----------------------------------------------------------------------------------------

import os
from flask import Blueprint, g, jsonify, request
from datetime import datetime
from scripts import pointsHelperFunc

# Use to upload image to S3
import s3Images

file_name = os.path.basename(__file__)
blueprint = Blueprint(file_name[:-3], __name__)

# Helper function to retrieve the user's information using the member's id
def getUserInfo(cur, member_id):
    
    # Get the user's id and user type from the clubMembers table
    cur.execute('SELECT "userID", "userType" FROM "clubMembers" WHERE id = %s', (member_id,))
    member_info = cur.fetchone()

    # Check the user type and get the user information
    # For type = user:  "id", "displayName", "photo"
    # For type = producer: "id", "producerName", "photo"
    # For type = venue: "id", "venueName", "photo"

    if member_info['userType'] == 'user':
        cur.execute('SELECT "id", "displayName", "photo" FROM "users" WHERE id = %s', (member_info['userID'],))
        user_info = cur.fetchone()

        # Get the user's proof points from the database
        cur.execute('SELECT "currentPoints" FROM "pointsRecorder" WHERE "userID" = %s AND "userType" = %s', (member_info['userID'], member_info['userType'],))
        current_points = cur.fetchone()

        # Add the proof points into the user_info
        if current_points:
            user_info['currentPoints'] = current_points['currentPoints']
            user_info['rank'] = pointsHelperFunc.get_rank(current_points['currentPoints'])

    elif member_info['userType'] == 'producer':
        cur.execute('SELECT "id", "producerName", "photo" FROM "producers" WHERE id = %s', (member_info['userID'],))
        user_info = cur.fetchone()
    else:
        cur.execute('SELECT "id", "venueName", "photo" FROM "venues" WHERE id = %s', (member_info['userID'],))
        user_info = cur.fetchone()

    # Check if the user exist
    if not user_info:
        return None

    # Add the user type into the user_info
    user_info['userType'] = member_info['userType']

    return user_info


# Helper function to retrieve user's information using the user's id and user type
def getUserInfoByID(cur, user_id, user_type):
    
    # Check the user type and get the user information
    # For type = user:  "id", "displayName", "photo"
    # For type = producer: "id", "producerName", "photo"
    # For type = venue: "id", "venueName", "photo"

    if user_type == 'user':
        cur.execute('SELECT "id", "displayName", "photo" FROM "users" WHERE id = %s', (user_id,))
        user_info = cur.fetchone()
    elif user_type == 'producer':
        cur.execute('SELECT "id", "producerName", "photo" FROM "producers" WHERE id = %s', (user_id,))
        user_info = cur.fetchone()
    else:
        cur.execute('SELECT "id", "venueName", "photo" FROM "venues" WHERE id = %s', (user_id,))
        user_info = cur.fetchone()

    # Check if the user exist
    if not user_info:
        return None

    # Add the user type into the user_info
    user_info['userType'] = user_type

    return user_info


# -----------------------------------------------------------------------------------------
# [GET] getClubs
# Purpose: Get 20 clubs information each time this is called. 
# Used: BrowseClubs.vue [views folder inside Users folder]
# Output: Possible return codes [200 - Retrieval success, 404 - No clubs found in database, 500 - An error occurred retrieving the request]
@blueprint.route('/getClubs/<offset>', methods=['GET']) # id is the starting ID to retrieve from (inclusive)
def getClubs(offset):
    conn = g.db
    cur = conn.cursor()
    return_data = {}

    try:

        # Step 1: Get the 20 clubs
        # ID: Used to define the starting ID to retrieve from
        cur.execute('SELECT * FROM "clubs" ORDER BY "totalMembers" DESC LIMIT 20 OFFSET %s', (offset,))
        clubs_info = cur.fetchall()

        if not clubs_info:
            return jsonify({
                'error': 'No clubs found in database'
            }), 404

        return jsonify({
            'clubs_info': clubs_info
        }), 200

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
# [GET] getClubwSearch
# Purpose: Get 20 clubs information each time this is called. This is used when the user is searching for a specific club using the search bar.
# Used: BrowseClubs.vue [views folder inside Users folder]
# Output: Possible return codes [200 - Retrieval success, 404 - No clubs found in database, 500 - An error occurred retrieving the request]
@blueprint.route('/getClubwSearch/<id>/<search>', methods=['GET']) # id is the starting ID to retrieve from (inclusive)
def getClubwSearch(id, search):
    conn = g.db
    cur = conn.cursor()
    return_data = {}

    try:

        # Step 1: Get the 20 clubs
        # ID: Used to define the starting ID to retrieve from
        cur.execute('''SELECT * FROM "clubs" WHERE "clubName" ILIKE %s AND id >= %s ORDER BY "clubName" ILIKE %s DESC, "id" ASC LIMIT 20''', (f'%{search}%', id, f'%{search}%'))
        clubs_info = cur.fetchall()

        if not clubs_info:
            return jsonify({
                'error': 'No clubs found in database'
            }), 404

        return jsonify({
            'clubs_info': clubs_info
        }), 200

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
# [GET] getSpecificClubInfo
# Purpose: Get the information of a specific club
# Used: ClubView.vue [views folder inside Users folder]
# Output: Possible return codes [200 - Retrieval success, 404 - No such club found in database, 500 - An error occurred retrieving the request]
@blueprint.route('/getSpecificClubInfo/<clubID>', methods=['GET'])
def getSpecificClubInfo(clubID):
    conn = g.db
    cur = conn.cursor()

    try:
        # Step 1: Get the club information
        cur.execute('SELECT * FROM "clubs" WHERE id = %s', (clubID,))
        club_info = cur.fetchone()

        if not club_info:
            return jsonify({
                'error': f'No such club found for club id: {clubID}'
            }), 404

        # Step 3: Get the admin details of the club
        cur.execute('SELECT "userID", "userType" FROM "clubMembers" WHERE "clubID" = %s AND "isAdmin" = TRUE', (clubID,))
        admins = cur.fetchall()

        # Step 4: Get the admin information from the respective table (users, producers or venues)
        admin_data = []
        for admin in admins:

            # Get the user information for each admin
            admin_details = getUserInfoByID(cur, admin['userID'], admin['userType'])
            
            # Add the admin details into admin_data list
            if admin_details:
                admin_data.append(admin_details)

        return jsonify({
            'club_info': club_info,
            'admins': admin_data
        }), 200

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
# [GET] getClubPosts
# Purpose: Get the latest 10 posts in the club. 
# Used: ClubView.vue [views folder inside Users folder]
# Input: 
#   1. Club ID, 
#   2. Last seen ID (i.e., the last post ID that the user has seen)
# Output: Possible return codes [200 - Retrieval success, 404 - No post/club found in database, 500 - An error occurred retrieving the request]
@blueprint.route('/getClubPosts/<clubID>/<last_seen_id>', methods=['GET'])
def getClubPosts(clubID, last_seen_id):
    conn = g.db
    cur = conn.cursor()

    # Dictionary to track if user information has been retrieved (reason being, a single user can post multiple post, this may help to reduce data being sent over to the frontend)
    users_retrieved_list = {}

    # filtered post list to be returned (for event where posterID is null - to exclude posts with no poster)
    filtered_post_list = []

    try:

        # check if club exists
        cur.execute('SELECT * FROM "clubs" WHERE id = %s', (clubID,))
        club = cur.fetchone()

        if not club:
            return jsonify({
                'error': f'No such club exist for club id: {clubID}'
            }), 404
        
        # Set the limit here
        limit = 10

        # Step 1: Get the top 10 latest post in that club
        if last_seen_id == '0':
            cur.execute('SELECT * FROM "clubPosts" WHERE "clubID" = %s ORDER BY "postDate" DESC LIMIT %s', (clubID, limit,))
        elif last_seen_id == '1':
            cur.execute('SELECT * FROM "clubPosts" WHERE "clubID" = %s AND id = 1', (clubID,))
        else:
            cur.execute('SELECT * FROM "clubPosts" WHERE "clubID" = %s AND "id" < %s ORDER BY "postDate" DESC LIMIT %s', (clubID, last_seen_id, limit,))    
        post_info = cur.fetchall() # returns empty list if no result found

        if not post_info:
            return jsonify({
                'error': 'No post yet'
            }), 404
        
        # Step 2: Get the number of likes/dislikes and number of comments for each post and the poster's id, displayName, photo
        for post in post_info:
            posterID = post['posterID'] # This is the club member's ID
            postID = post['id']

            # Check if posterID is null
            if not posterID:
                # Move to the next post if the posterID is null
                continue

            # Get the poster's user ID and user type from the clubMembers table
            if posterID not in users_retrieved_list:
                poster_info = getUserInfo(cur, posterID)

                if not poster_info:
                    # Skip to the next post if the poster info is not found
                    continue

                users_retrieved_list[posterID] = poster_info
                # Add poster info into post
                post['posterInfo'] = poster_info
            else:
                post['posterInfo'] = users_retrieved_list[posterID]

            # Get the total number of likes for each post
            cur.execute('SELECT COUNT(*) AS "totalLikes" FROM "clubPostsLikes" WHERE "postID" = %s', (postID,))
            total_likes = cur.fetchone()

            # Add total likes into post
            post['totalLikes'] = total_likes['totalLikes']

            # Get the total number of dislikes for each post
            cur.execute('SELECT COUNT(*) AS "totalDislikes" FROM "clubPostsDislikes" WHERE "postID" = %s', (postID,))
            total_dislikes = cur.fetchone()

            # Add total dislikes into post
            post['totalDislikes'] = total_dislikes['totalDislikes']

            # Get the total number of comments for each post
            cur.execute('SELECT COUNT(*) AS "totalComments" FROM "clubPostComments" WHERE "postID" = %s', (postID,))
            total_comments = cur.fetchone()

            # Add total comments into post
            post['totalComments'] = total_comments['totalComments']

            # Add post into filtered_post_list
            filtered_post_list.append(post)

        return jsonify({
            'data': filtered_post_list
        }), 200

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
# [GET] getClubPostDetails
# Purpose: Get the latest 20 comments for a specific post
# Used: SpecificClubPost.vue [components folder]
# Output: Possible return codes [200 - Retrieval success (with or without comments), 404 - No such post exist, 500 - An error occurred retrieving the request]
@blueprint.route('/getClubPostDetails/<postID>/<last_seen_id>', methods=['GET']) 
def getClubPostDetails(postID, last_seen_id):
    conn = g.db
    cur = conn.cursor()

    # Dictionary to track if user information has been retrieved (reason being, a single user can post multiple post, this may help to reduce data being sent over to the frontend)
    users_retrieved_list = {}

    # filtered comment list to be returned (for event where commenterID is null - to exclude comments with no commenter)
    filtered_comment_list = []

    try:
        # check if post exist
        cur.execute('SELECT * FROM "clubPosts" WHERE "id" = %s', (postID,))
        post = cur.fetchone()

        if not post:
            return jsonify({
                'error': f"No such post for this post id {postID}"
            }), 404
        
        # Step 1: Get the poster information
        posterID = post['posterID']

        # Check if posterID is null
        if not posterID:
            return jsonify({
                'error': 'No poster ID found for this post'
            }), 404
        
        poster_info = getUserInfo(cur, posterID)

        if not poster_info:
            return jsonify({
                'error': 'No such user for the given poster ID'
            }), 404

        # Step 2: Get a list of members who liked and disliked the post
        cur.execute('SELECT "memberID" FROM "clubPostsLikes" WHERE "postID" = %s', (postID,))
        liked_members = cur.fetchall()

        # Format the liked_members into a list of memberID
        liked_members_list = [member['memberID'] for member in liked_members]
        post['likedMembers'] = liked_members_list

        # Get a list of members who disliked the post
        cur.execute('SELECT "memberID" FROM "clubPostsDislikes" WHERE "postID" = %s', (postID,))
        disliked_members = cur.fetchall()

        # Format the disliked_members into a list of memberID
        disliked_members_list = [member['memberID'] for member in disliked_members]
        post['dislikedMembers'] = disliked_members_list

        # Step 4: Get the latest 20 comments for the specific post
        # Step the limit here 
        limit = 20
        if last_seen_id == '0':
            cur.execute('SELECT * FROM "clubPostComments" WHERE "postID" = %s ORDER BY "commentDate" DESC LIMIT %s', (postID, limit,))
        elif last_seen_id == '1':
            cur.execute('SELECT * FROM "clubPostComments" WHERE "postID" = %s AND id = 1', (postID,))
        else:
            cur.execute('SELECT * FROM "clubPostComments" WHERE "postID" = %s AND "id" < %s ORDER BY "commentDate" DESC LIMIT %s', (postID, last_seen_id, limit,))
        comments_info = cur.fetchall()

        if not comments_info:
            return jsonify({
                'post_info': post,
                'poster_info': poster_info,
                'comments': []
            }), 200
        
        # Step 4: Get the total likes, commenter's id, displayName and photo
        for comment in comments_info:
            commenterID = comment['commenterID']

            # Check if commenterID is null
            if not commenterID:
                # Skip to the next comment if commenterID is null
                continue

            # Get the commenter's user ID and user type from the clubMembers table
            if commenterID not in users_retrieved_list:
                commenter_info = getUserInfo(cur, commenterID)

                if not commenter_info:
                    # Skip to the next comment if the commenter info is not found
                    continue

                users_retrieved_list[commenterID] = commenter_info
                # Add commenter info into comment
                comment['commenterInfo'] = commenter_info
            else:
                comment['commenterInfo'] = users_retrieved_list[commenterID]

            # Get a list of members who liked the comment
            cur.execute('SELECT "memberID" FROM "clubPostCommentsLikes" WHERE "commentID" = %s', (comment['id'],))
            comments_liked_members = cur.fetchall()

            # Format the comments_liked_members into a list of memberID
            comments_liked_members_list = [member['memberID'] for member in comments_liked_members]

            # Add comments_liked_members into comment
            comment['likedMembers'] = comments_liked_members_list

            # Get a list of members who disliked the comment
            cur.execute('SELECT "memberID" FROM "clubPostCommentsDislikes" WHERE "commentID" = %s', (comment['id'],))
            comments_disliked_members = cur.fetchall()

            # Format the comments_disliked_members into a list of memberID
            comments_disliked_members_list = [member['memberID'] for member in comments_disliked_members]

            # Add comments_disliked_members into comment
            comment['dislikedMembers'] = comments_disliked_members_list

            # Add comment into filtered_comment_list
            filtered_comment_list.append(comment)

        return jsonify({
            'post_info': post,
            'poster_info': poster_info,
            'comments': comments_info
        }), 200


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
# [GET] checkUserMembership
# Purpose: Check if a user is a member of a specific club 
#           or if user has been invited to join the club 
#           or if user has requested to join the club
# Used: ClubView.vue [views folder inside Users folder]
# Output: Possible return codes [200 - User has requested to join / User is a member, 404 - User is not a member, 500 - An error occurred retrieving the request]
@blueprint.route('/checkUserMembership/<userID>/<userType>/<clubID>', methods=['GET'])
def checkUserMembership(userID, userType, clubID):
    conn = g.db
    cur = conn.cursor()

    try:
        # Step 1: Check if user has requested to join the club
        cur.execute('SELECT * FROM "clubRequests" WHERE "userID" = %s AND "userType" = %s AND "clubID" = %s', (userID, userType, clubID,))
        request = cur.fetchone()

        if request:
            return jsonify({
                'isRequested': True
            }), 200
        
        # Step 2: Check if the user has been invited to join the club
        cur.execute('SELECT * FROM "clubInvites" WHERE "inviteeID" = %s AND "inviteeUserType" = %s AND "clubID" = %s' , (userID, userType, clubID,))
        invite = cur.fetchone()

        if invite:
            return jsonify({
                'isInvited': True
            }), 200

        # Step 3: Check if the user is already a member of the club
        cur.execute('SELECT * FROM "clubMembers" WHERE "clubID" = %s AND "userID" = %s AND "userType" = %s', (clubID, userID, userType,))
        member = cur.fetchone()

        if not member:
            return jsonify({
                'error': 'User is not a member'
            }), 404
        
        return jsonify({
            'isMember': True,
            'isAdmin': member.get('isAdmin'),
            'memberID': member.get('id')
        }), 200

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
# [GET] getUserLikesDislikesPost
# Purpose: Get the posts that a specific user has liked and disliked in a specific club
# Used: ClubView.vue [views folder inside Users folder]
# Output: Possible return codes [200 - Retrieval success, 404 - No liked posts found, 500 - An error occurred retrieving the request]
@blueprint.route('/getUserLikesDislikesPost/<memberID>/<clubID>', methods=['GET'])
def getUserLikesDislikesPost(memberID, clubID):
    conn = g.db
    cur = conn.cursor()

    try: 
        cur.execute('SELECT "postID" FROM "clubPostsLikes" WHERE "memberID" = %s AND "clubID" = %s' , (memberID, clubID,))
        liked_posts = cur.fetchall()

        cur.execute('SELECT "postID" FROM "clubPostsDislikes" WHERE "memberID" = %s AND "clubID" = %s' , (memberID, clubID,))
        disliked_posts = cur.fetchall()

        
        # Format the liked_posts into a list of postID
        if liked_posts:
            liked_posts = [post['postID'] for post in liked_posts]

        # Format the disliked_posts into a list of postID
        if disliked_posts:
            disliked_posts = [post['postID'] for post in disliked_posts]
    
        return jsonify({
            'liked_posts': liked_posts,
            'disliked_posts': disliked_posts
        }), 200

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
# [GET] getUserLikesDislikesComments
# Purpose: Get the comments that a specific user has liked in a specific post
# Used: SpecificClubPost.vue [components folder]
# Output: Possible return codes [200 - Retrieval success, 404 - No liked comments found, 500 - An error occurred retrieving the request]
@blueprint.route('/getUserLikesDislikesComments/<memberID>/<postID>', methods=['GET'])
def getUserLikesDislikesComments(memberID, postID):
    conn = g.db
    cur = conn.cursor()

    try:
        cur.execute('SELECT "commentID" FROM "clubPostCommentsLikes" WHERE "memberID" = %s AND "postID" = %s', (memberID, postID,))
        liked_comments = cur.fetchall()

        cur.execute('SELECT "commentID" FROM "clubPostCommentsDislikes" WHERE "memberID" = %s AND "postID" = %s', (memberID, postID,))
        disliked_comments = cur.fetchall()
       
        # Format the liked_comments into a list of commentID
        if liked_comments:
            liked_comments_list = [comment['commentID'] for comment in liked_comments]

        # Format the disliked_comments into a list of commentID
        if disliked_comments:
            disliked_comments_list = [comment['commentID'] for comment in disliked_comments]

        return jsonify({
            'liked_comments': liked_comments_list,
            'disliked_comments': disliked_comments_list
        }), 200

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
# [GET] getUserClubs
# Purpose: Get the first 5 clubs that a specific user is a member of / is an admin of (5 clubs each for member and admin)
# Used: BrowseClubs.vue [views folder inside Users folder]
# Output: Possible return codes [200 - Retrieval success, 404 - No clubs found, 500 - An error occurred retrieving the request]
@blueprint.route('/getUserClubs/<userID>/<userType>', methods=['GET'])
def getUserClubs(userID, userType):
    conn = g.db
    cur = conn.cursor()

    try:
        cur.execute('SELECT "clubID", "isAdmin" FROM "clubMembers" WHERE "userID" = %s AND "userType" = %s', (userID, userType,))
        user_clubs = cur.fetchall()

        if not user_clubs:
            return jsonify({
                'error': 'No clubs found'
            }), 404
        
        # Loop through all the user clubs and add them into 3 list (user_clubs_ids, user_club_member, user_club_admin)
        user_clubs_ids = []
        user_club_member = []
        user_club_admin = []

        for club in user_clubs:
            user_clubs_ids.append(club['clubID'])

            # Get the club id, clubName, clubBanner
            cur.execute('SELECT "id", "clubName", "clubBanner" FROM "clubs" WHERE id = %s', (club['clubID'],))
            club_info = cur.fetchone()

            if not club_info:
                # Skip to the next club if the club info is not found
                continue

            # Add club info into club
            club['clubInfo'] = club_info

            if club['isAdmin']:
                user_club_admin.append(club)
            else:
                user_club_member.append(club)

        return jsonify({
            'user_clubs': user_clubs_ids,
            'user_club_member': user_club_member,
            'user_club_admin': user_club_admin
        }), 200

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
# [GET] getClubMembers
# Purpose: Get the members of a specific club (10 members each time this is called)
# Used: ClubSettings.vue [components folder inside frontend folder]
# Output: Possible return codes [200 - Retrieval success, 404 - No members found, 500 - An error occurred retrieving the request]
@blueprint.route('/getClubMembers/<clubID>/<last_seen_id>', methods=['GET'])
def getClubMembers(clubID, last_seen_id):
    conn = g.db
    cur = conn.cursor()

    # Set the limit here 
    limit = 1

    try:
        # Step 1: Get the members of the club
        if last_seen_id == '0':
            cur.execute('SELECT * FROM "clubMembers" WHERE "clubID" = %s ORDER BY "id" DESC LIMIT %s', (clubID, limit,))
        elif last_seen_id == '1':
            cur.execute('SELECT * FROM "clubMembers" WHERE "clubID" = %s LIMIT %s', (clubID, limit,))
        else:
            cur.execute('SELECT * FROM "clubMembers" WHERE "clubID" = %s AND "id" < %s ORDER BY "id" DESC LIMIT %s', (clubID, last_seen_id, limit,))
        members = cur.fetchall()

        if not members:
            return jsonify({
                'error': 'No members found'
            }), 404
        
        # Step 2: Get the user information for each member
        for member in members:
            member_id = member['id']
            member_info = getUserInfo(cur, member_id)

            if not member_info:
                # Skip to the next member if the member info is not found
                continue

            member_info['isAdmin'] = member['isAdmin']
            member_info['memberID'] = member_id
            member_info['joinDate'] = member['joinDate']

            # Add member info into members
            member.update(member_info)

            # Remove the id from the member
            member.pop('clubID')

        return jsonify({
            'members': members
        }), 200

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
# [GET] getFirstFewClubMembers
# Purpose: Get the first few members of a specific club (4 members to show on ClubView.vue)
# Used: ClubView.vue [views folder inside Users folder]
# Output: Possible return codes [200 - Retrieval success, 404 - No members found, 500 - An error occurred retrieving the request]
@blueprint.route('/getFirstFewClubMembers/<clubID>', methods=['GET'])
def getFirstFewClubMembers(clubID):
    conn = g.db
    cur = conn.cursor()

    try:
        # Step 1: Get the first few members of the club
        cur.execute('SELECT * FROM "clubMembers" WHERE "clubID" = %s ORDER BY "id" ASC LIMIT 4', (clubID,))
        members = cur.fetchall()

        if not members:
            return jsonify({
                'error': 'No members found'
            }), 404
        
        # Step 2: Get the user information for each member
        for member in members:
            member_id = member['id']
            member_info = getUserInfo(cur, member_id)

            if not member_info:
                # Skip to the next member if the member info is not found
                continue

            member_info['isAdmin'] = member['isAdmin']
            member_info['memberID'] = member_id
            member_info['joinDate'] = member['joinDate']

            # Add member info into members
            member.update(member_info)

            # Remove the id from the member
            member.pop('clubID')

        return jsonify({
            'members': members
        }), 200

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
# [GET] getAllClubMembers
# Purpose: Get all the members of a specific club (show all members in a modal in ClubView.vue)
# Used: ClubView.vue [views folder inside Users folder]
# Output: Possible return codes [200 - Retrieval success, 404 - No members found, 500 - An error occurred retrieving the request]
@blueprint.route('/getAllClubMembers/<clubID>', methods=['GET'])
def getAllClubMembers(clubID): 
    conn = g.db
    cur = conn.cursor()

    try:
        # Step 1: Get all the members of the club
        cur.execute('SELECT * FROM "clubMembers" WHERE "clubID" = %s', (clubID,))
        members = cur.fetchall()

        if not members:
            return jsonify({
                'error': 'No members found'
            }), 404
        
        # Step 2: Get the user information for each member
        for member in members:
            member_id = member['id']
            member_info = getUserInfo(cur, member_id)

            if not member_info:
                # Skip to the next member if the member info is not found
                continue

            member_info['isAdmin'] = member['isAdmin']
            member_info['memberID'] = member_id
            member_info['joinDate'] = member['joinDate']

            # Add member info into members
            member.update(member_info)

            # Remove the id from the member
            member.pop('clubID')

        return jsonify({
            'members': members
        }), 200

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
# [GET] getClubRequests
# Purpose: Get the requests of users who want to join a specific club
# Used: ClubSettings.vue [components folder inside frontend folder]
# Output: Possible return codes [200 - Retrieval success, 404 - No requests found, 500 - An error occurred retrieving the request]
@blueprint.route('/getClubRequests/<clubID>/<last_seen_id>', methods=['GET'])
def getClubRequests(clubID, last_seen_id):
    conn = g.db
    cur = conn.cursor()

    # Set the limit here
    limit = 1

    try:
        # Step 1: Get the requests of the club
        if last_seen_id == '0':
            cur.execute('SELECT * FROM "clubRequests" WHERE "clubID" = %s ORDER BY "id" DESC LIMIT %s', (clubID, limit,))
        elif last_seen_id == '1':
            cur.execute('SELECT * FROM "clubRequests" WHERE "clubID" = %s LIMIT %s', (clubID, limit,))
        else:
            cur.execute('SELECT * FROM "clubRequests" WHERE "clubID" = %s AND "id" < %s ORDER BY "id" DESC LIMIT %s', (clubID, last_seen_id, limit,))
        requests = cur.fetchall()

        if not requests:
            return jsonify({
                'error': 'No requests found'
            }), 404
        
        # Step 2: Get the user information for each request
        for request in requests:

            # Get the user information for each request
            user_id = request['userID']
            user_type = request['userType']

            if not user_id:
                # Skip to the next request if the user id is null
                continue

            user_info = getUserInfoByID(cur, user_id, user_type)

            # Remove the user id from user_info as the user id is already in the request
            user_info.pop('id')

            # Add user info into requests
            request.update(user_info)

            # Remove the club id from the request
            request.pop('clubID')

            # Rename the id to requestID
            request['requestID'] = request.pop('id')

        # Get the total number of requests in the club
        cur.execute('SELECT COUNT(*) AS "totalRequests" FROM "clubRequests" WHERE "clubID" = %s', (clubID,))
        total_requests = cur.fetchone()

        total_requests = total_requests['totalRequests']

        return jsonify({
            'requests': requests,
            'totalRequests': total_requests
        }), 200

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
# [GET] getUserClubRequests
# Purpose: Get a list of clubs that a specific user has requested to join
# Used: BrowseClubs.vue [views folder inside Users folder]
# Output: Possible return codes [200 - Retrieval success, 404 - No requests found, 500 - An error occurred retrieving the request]
@blueprint.route('/getUserClubRequests/<userID>/<userType>', methods=['GET'])
def getUserClubRequests(userID, userType):
    conn = g.db
    cur = conn.cursor()

    try:
        # Check if user has any requests
        cur.execute('SELECT * FROM "clubRequests" WHERE "userID" = %s AND "userType" = %s', (userID, userType,))
        requests = cur.fetchall()

        if not requests:
            return jsonify({
                'error': 'No requests found'
            }), 404

        club_request_list = []
        # Convert the requests into a list of clubID
        for request in requests:
            club_request_list.append(request['clubID'])

        return jsonify({
            'club_request_list': club_request_list
        }), 200

    except Exception as e:
        print(str(e))
        # Rollback the transaction if an error occurred
        conn.rollback()
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred creating the club."
            }
        ), 500


# -----------------------------------------------------------------------------------------
# [GET] getUserInvitedClubs
# Purpose: Get a list of clubs that a specific user has been invited to join
# Used: BrowseClubs.vue [views folder inside Users folder]
# Output: Possible return codes [200 - Retrieval success, 404 - No invites found, 500 - An error occurred retrieving the request]
@blueprint.route('/getUserInvitedClubs/<userID>/<userType>', methods=['GET'])
def getUserInvitedClubs(userID, userType):
    conn = g.db
    cur = conn.cursor()

    try:
        # Check if user has any invites
        cur.execute('SELECT * FROM "clubInvites" WHERE "inviteeID" = %s AND "inviteeUserType" = %s', (userID, userType,))
        invites = cur.fetchall()

        if not invites:
            return jsonify({
                'error': 'No invites found'
            }), 404
        
        # Get the club name for each invite
        for invite in invites:
            clubID = invite['clubID']
            cur.execute('SELECT "clubName" FROM "clubs" WHERE "id" = %s', (clubID,))
            club_name = cur.fetchone()

            # Get the user information for each invite
            user_info = getUserInfoByID(cur, invite['inviterID'], invite['inviterUserType'])

            # Add club name into invite
            invite['clubName'] = club_name['clubName']

            # Add user info into invite
            invite['inviterInfo'] = user_info

        return jsonify({
            'club_invite_list': invites
        }), 200

    except Exception as e:
        print(str(e))
        # Rollback the transaction if an error occurred
        conn.rollback()
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred creating the club."
            }
        ), 500


# -----------------------------------------------------------------------------------------
# [GET] getRecentActivity
# Purpose: Get the 5 most recent activities in any club that a user is a member of
# Used: BrowseClubs.vue [views folder inside Users folder]
# Output: Possible return codes [200 - Retrieval success, 404 - No recent activities found, 500 - An error occurred retrieving the request]
@blueprint.route('/getRecentActivity/<userID>/<userType>', methods=['GET'])
def getRecentActivity(userID, userType):
    conn = g.db
    cur = conn.cursor()

    try:
        # Step 1: Get all the clubs that the user is a member of
        cur.execute('SELECT "clubID", id FROM "clubMembers" WHERE "userID" = %s AND "userType" = %s', (userID, userType,))
        user_clubs = cur.fetchall()

        if not user_clubs:
            return jsonify({
                'error': 'No clubs found'
            }), 404
        
        # Convert the user_clubs into a tuple
        user_clubs_tuple = tuple([club['clubID'] for club in user_clubs])
        
        # Step 2: Get the 5 most recent activities in any club that the user is a member of
        cur.execute('SELECT * FROM "clubPosts" WHERE "clubID" IN %s ORDER BY "postDate" DESC LIMIT 5', (user_clubs_tuple,))
        recent_activities = cur.fetchall()

        if not recent_activities:
            return jsonify({
                'error': 'No recent activities found'
            }), 404

        
        # Step 3: Get the poster information for each activity and club name
        for activity in recent_activities:
            poster_id = activity['posterID']

            # Get the user information for each poster
            poster_info = getUserInfo(cur, poster_id)

            # Add poster info into activity
            activity['posterInfo'] = poster_info

            # Get the club name for each activity
            clubID = activity['clubID']
            cur.execute('SELECT "clubName", "clubBanner" FROM "clubs" WHERE "id" = %s', (clubID,))
            club_name = cur.fetchone()

            # Get the user's memberID in the club from user_clubs
            memberID = None
            for club in user_clubs:
                if club['clubID'] == clubID:
                    memberID = club['id']
                    break

            # Add club name, member ID and club banner into activity
            activity['clubName'] = club_name['clubName']
            activity['memberID'] = memberID
            activity['clubBanner'] = club_name['clubBanner']

        return jsonify({
            'recent_activities': recent_activities
        }), 200

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
# [GET] canCreate
# Purpose: Check if a user can create a club 
# Used: 
# Output: Possible return codes [200 - User can create a club, 400 - User cannot create a club, 500 - An error occurred retrieving the request]
@blueprint.route('/canCreate/<userID>/<userType>', methods=['GET'])
def canCreate(userID, userType):
    conn = g.db
    cur = conn.cursor()

    try:
        # Step 1: Check if the user is a valid type user
        if userType not in ['user', 'producer', 'venue']:
            return jsonify({
                'error': 'User type is not valid'
            }), 400
        
        # Check for user type: user 
        if userType == 'user':

            canCreateTuple = pointsHelperFunc.check_user_can_create_club(userID)

            if not canCreateTuple[0]:

                if canCreateTuple[1] == 'insufficient points':
                    return jsonify({
                        'canCreate': False,
                        'reason': 'insufficient points',
                        'message': 'Almost there! Earn a few more points to unlock club creation.',
                        'pointsNeeded': canCreateTuple[2]
                    }), 200
                
                else:
                    return jsonify({
                        'canCreate': False,
                        'reason': 'max clubs created',
                        'message': 'You have reached your club creation limit for the month. This will reset once again next month!',
                        'numClubsCreated': canCreateTuple[2]
                    }), 200
            
            
            # Else, user can create a club
            return jsonify({
                'canCreate': True
            }), 200

        # Check for user type: producer or venue
        max_num_clubs = 2 # Max club for producer and venue is 2

        cur.execute('SELECT * FROM "clubs" WHERE "createdByID" = %s AND "createdByType" = %s', (userID, userType,))
        club = cur.fetchall()

        if club and len(club) == max_num_clubs:
            return jsonify({
                'canCreate': False,
                'message': 'You have reached your club creation limit for the month. This will reset once again next month!',
                'clubID': club['id'], 
                'maxClubs': max_num_clubs
            }), 200
        
        # Else, user can create a club
        return jsonify({
            'canCreate': True
        }), 200

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
# [POST] createClubs
# Purpose: Create a new club
# Used: CreateClub.vue [views folder inside Users folder]
# Input:
#   1. Creator ID (i.e., the user's ID in the 'users', 'producers' or 'venues' table)
#   2. Creator Type (i.e., 'user', 'producer' or 'venue')
#   3. Club Name
#   4. Club Description
#   5. Is Invite Only (boolean: True = Private, False = Public)
#   6. Club Banner (optional)
# Output: Possible return codes [201 - Club created successfully, 400 - Missing required data, 500 - An error occurred creating the club]
@blueprint.route('/createClubs', methods=['POST'])
def createClub():
    conn = g.db
    cur = conn.cursor()

    try:
        data = request.get_json()

        # Get all the required data
        creator_id = data['creatorID']
        creator_type = data['creatorType']
        club_name = data['clubName']
        club_desc = data['clubDesc']
        is_invite_only = data['isInviteOnly']

        # Check if all the required data is provided
        if not creator_id or not creator_type or not club_name or not club_desc or not is_invite_only:
            return jsonify({
                'error': 'Missing required data'
            }), 400
        
        # Step 1: Get today's date
        date_created = datetime.now()

        # Step 2: Check if the banner image is provided
        if 'image64' in data and data['image64']:
            image64 = s3Images.uploadBase64ImageToS3(data['image64'])
        else:
            image64 = None

        # Step 3: Insert the new club into the database
        cur.execute('INSERT INTO "clubs" ("clubName", "clubDesc", "isInviteOnly", "clubLink", "clubBanner", "dateCreated", "totalMembers", "createdByID", "createdByType") VALUES (%s, %s, %s, %s, %s, %s, 1, %s, %s) RETURNING id', 
                    (club_name, club_desc, is_invite_only, '', image64, date_created, creator_id, creator_type,))
        club_id = cur.fetchone()['id']

        # Step 4: Insert the club admin into the clubMembers table
        cur.execute('INSERT INTO "clubMembers" ("clubID", "userID", "userType", "joinDate", "isAdmin") VALUES (%s, %s, %s, %s, TRUE)', 
                    (club_id, creator_id, creator_type, date_created,))
        conn.commit()

        return jsonify({
            'message': 'Club created successfully',
            'clubID': club_id
        }), 201

    except Exception as e:
        print(str(e))
        # Rollback the transaction if an error occurred
        conn.rollback()
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred creating the club."
            }
        ), 500
    
    finally:
        cur.close()


# -----------------------------------------------------------------------------------------
# [POST] addClubMembers
# Purpose: Add new members to the club [users will have to accept the invite to join the club - added by another user regardless if the club is public or private]
# Used: 
# Input: 
#   1. A list of new member objects containing the user's ID, user type and isAdmin status (e.g., [{'userID': 1, 'userType': 'user', 'isAdmin': true}, {'userID': 2, 'userType': 'producer', isAdmin: false}])
#   2. Club ID
# Output: Possible return codes [201 - New member added successfully, 400 - Missing required data, 404 - No such club exist, 500 - An error occurred adding the new member]
@blueprint.route('/addClubMembers', methods=['POST'])
def addClubMembers():
    conn = g.db
    cur = conn.cursor()

    try:
        data = request.get_json()

        # Get all the required data
        club_id = data['clubID']

        if not club_id:
            return jsonify({
                'error': 'Missing required data'
            }), 400
        
        inviter_id = data['inviterID']
        inviter_user_type = data['inviterUserType']

        # List of members to be added to the club
        new_members_list = data['new_members']

        if len(new_members_list) == 0:
            return jsonify({
                'error': 'No new members to be added'
            }), 400

        join_date = datetime.now()

        # Step 1: Check if the club exist
        cur.execute('SELECT * FROM "clubs" WHERE id = %s', (club_id,))
        club = cur.fetchone()

        if not club:
            return jsonify({
                'error': 'No such club exist'
            }), 404

        # Step 2: Insert the new member into the clubMembers table
        for user in new_members_list:
            user_id = user['userID']
            user_type = user['userType']

            # Skip to the next member if the user id is null
            if not user_id:
                continue

            user = getUserInfoByID(cur, user_id, user_type)
            
            # Skip to the next member if the user does not exist
            if not user:
                continue

            cur.execute('INSERT INTO "clubInvites" ("clubID", "inviteeID", "inviteeUserType", "inviterID", "invtiterUserType", "inviteDate") VALUES (%s, %s, %s, %s, %s, %s)', (club_id, user_id, user_type, inviter_id, inviter_user_type, join_date,))
            conn.commit()

        return jsonify({
            'message': 'New member added to the club'
        }), 201

    except Exception as e:
        print(str(e))
        # Rollback the transaction if an error occurred
        conn.rollback()
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred adding the new member."
            }
        ), 500
    
    finally:
        cur.close()


# -----------------------------------------------------------------------------------------
# [POST] joinClub
# Purpose: Join a club (not through invite and only for public clubs)
# Used: 
#   1. ClubView.vue [views folder inside Users folder]
#   2. BrowseClubs.vue [views folder inside Users folder]
# Input:
#   1. Club ID
#   2. User ID (i.e., the user's ID in the 'users', 'producers' or 'venues' table)
#   3. User Type
# Output: Possible return codes [201 - User joined the club successfully, 400 - Missing required data, 404 - No such club exist, 409 - User is already a member, 500 - An error occurred joining the club]
@blueprint.route('/joinClub', methods=['POST'])
def joinClub():
    conn = g.db
    cur = conn.cursor()

    try:
        data = request.get_json()

        # Get all the required data
        club_id = data['clubID']
        user_id = data['userID']
        user_type = data['userType']

        # Check if all the required data is provided
        if not club_id or not user_id or not user_type:
            return jsonify({
                'error': 'Missing required data'
            }), 400

        # Step 1: Check if the club exist
        cur.execute('SELECT * FROM "clubs" WHERE id = %s', (club_id,))
        club = cur.fetchone()

        if not club:
            return jsonify({
                'error': 'No such club exist'
            }), 404
        
        # Step 2: Check if the user is already a member of the club
        cur.execute('SELECT * FROM "clubMembers" WHERE "clubID" = %s AND "userID" = %s AND "userType" = %s', (club_id, user_id, user_type,))
        member = cur.fetchone()

        if member:
            return jsonify({
                'error': 'User is already a member of the club'
            }), 409

        # Step 3: Insert the user into the clubMembers table
        join_date = datetime.now()
        cur.execute('INSERT INTO "clubMembers" ("clubID", "userID", "userType", "joinDate", "isAdmin") VALUES (%s, %s, %s, %s, FALSE)', (club_id, user_id, user_type, join_date,))
        conn.commit()

        # Step 4: Append 1 to the totalMembers in the clubs table
        cur.execute('UPDATE "clubs" SET "totalMembers" = "totalMembers" + 1 WHERE id = %s', (club_id,))
        conn.commit()

        # Get the member's ID in the clubMembers table
        cur.execute('SELECT id FROM "clubMembers" WHERE "clubID" = %s AND "userID" = %s AND "userType" = %s', (club_id, user_id, user_type,))
        return jsonify({
            'message': 'User joined the club successfully',
            'memberID': cur.fetchone()['id']
        }), 201

    except Exception as e:
        print(str(e))
        # Rollback the transaction if an error occurred
        conn.rollback()
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred joining the club."
            }
        ), 500
    
    finally:
        cur.close()


# -----------------------------------------------------------------------------------------
# [POST] addPost
# Purpose: Add a new post to the club
# Used: ClubView.vue [views folder inside Users folder]
# Input:
#   1. Poster ID (i.e., the member's ID in the clubMembers table)
#   2. Club ID
#   3. Post Content
#   4. Post Photo (optional)
# Output: Possible return codes [201 - Post added successfully, 400 - Missing required data, 500 - An error occurred adding the post]
@blueprint.route('/addPost', methods=['POST'])
def addPost():
    conn = g.db
    cur = conn.cursor()

    try:
        data = request.get_json()

        # Get all the required data
        poster_id = data['posterID'] # The member's ID in the clubMembers table
        club_id = data['clubID']
        post_content = data['postContent']

        # Check if all the required data is provided
        if not poster_id or not club_id or not post_content:
            return jsonify({
                'error': 'Missing required data'
            }), 400

        # Step 1: Get today's date
        post_date = datetime.now()

        # List to store the image urls
        image_urls = []

        # Step 2: Check if the post has images
        if 'images' in data:

            # Loop through the images and upload them to S3
            for image in data['images']:
                if not image:
                    continue
                image64 = s3Images.uploadBase64ImageToS3(image)
                image_urls.append(image64)

            # Make the postPhotos as a text string starting with { and ending with }
            post_photos = '{' + ','.join(f'"{url}"' for url in image_urls) + '}'
        else:
            post_photos = '{}'

        # Step 3: Insert the new post into the database
        cur.execute('INSERT INTO "clubPosts" ("clubID", "postDate", "postContent", "postPhotos", "posterID") VALUES (%s, %s, %s, %s, %s) RETURNING id', 
                    (club_id, post_date, post_content, post_photos, poster_id,))
        post_id = cur.fetchone()['id']
        conn.commit()

        # Step 4: Add proofPoints to the user for adding a post
    
        # get the user id and user type from the poster id
        cur.execute('SELECT "userID", "userType" FROM "clubMembers" WHERE id = %s', (poster_id,))
        user = cur.fetchone()

        if (user['userType'] == 'user'):

            if pointsHelperFunc.check_max_proof_points(user['userID']):
                return jsonify({
                    'message': 'Post added successfully',
                    'postID': post_id
                }), 201

            # Get the current points for posting
            cur.execute('SELECT "proofPoints", "ruleName" FROM "pointSystemRules" WHERE id = %s', (7,))
            points = cur.fetchone()

            cur.execute('UPDATE "pointsRecorder" SET "currentPoints" = "currentPoints" + %s WHERE "userID" = %s AND "userType" = %s', (points['proofPoints'], user['userID'], 'user',))
            conn.commit()

            print(f"Added {points['proofPoints']} points to user {user['userID']} for adding a post")
                # 1️⃣  Get the badge that tracks club posts
            cur.execute(
                'SELECT id FROM "badges" '
                'WHERE "relatedEntity" = %s '
                'ORDER BY id LIMIT 1',
                ('ClubPost',)
            )
            badge_row = cur.fetchone()
            if not badge_row:           # nothing to do if no badge defined
                conn.commit()
                return

            club_badge_id = badge_row['id']

            # 2️⃣  Does this user already have the badge?
            cur.execute(
                'SELECT id, "currentLevel", "currentProgress" '
                'FROM "userBadges" '
                'WHERE "userId" = %s AND "badgeId" = %s',
                (user['userID'], club_badge_id)
            )
            user_badge = cur.fetchone()

            if user_badge is None:
                # No row yet → give them level-1 badge with 1 action completed
                cur.execute(
                    '''INSERT INTO "userBadges"
                    ("userId","badgeId","currentLevel","currentProgress",
                        "dateEarned","lastUpdated")
                    VALUES (%s,%s,%s,%s,NOW(),NOW())''',
                    (user['userID'], club_badge_id, 1, 1)
                )
                conn.commit()
                return jsonify({
            'message': 'Post added successfully',
            'postID': post_id,
            'pointsEarned': points['proofPoints']
        }), 201
            # 3️⃣  Increment progress
            progress   = user_badge["currentProgress"] + 1
            level      = user_badge["currentLevel"]

            # Pull the ClubPost rules once
            cur.execute(
                'SELECT "levelStart","levelEnd","actionsRequired" '
                'FROM "badgeRules" '
                'WHERE "actionType" = %s '
                'ORDER BY "levelStart"',
                ('ClubPost',)
            )
            rules = cur.fetchall()

            # Helper → actions needed for a specific level
            def needed_for(lvl: int) -> int:
                for r in rules:
                    if r["levelStart"] <= lvl <= r["levelEnd"]:
                        return r["actionsRequired"]
                return rules[-1]["actionsRequired"]   # fallback (shouldn’t hit)

            # 4️⃣  Apply level-ups while we have enough actions
            while progress >= needed_for(level) and level < 100:
                progress -= needed_for(level)
                level    += 1

            # 5️⃣  Persist the new state
            cur.execute(
                '''UPDATE "userBadges"
                SET "currentLevel" = %s,
                    "currentProgress" = %s,
                    "lastUpdated" = NOW()
                WHERE id = %s''',
                (level, progress, user_badge["id"])
            )
            conn.commit()

        return jsonify({
            'message': 'Post added successfully',
            'postID': post_id,
            'pointsEarned': points['proofPoints']
        }), 201

    except Exception as e:
        print(str(e))
        # Rollback the transaction if an error occurred
        conn.rollback()
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred adding the post."
            }
        ), 500
    
    finally:
        cur.close()


# -----------------------------------------------------------------------------------------
# [POST] addComment
# Purpose: Add a new comment to the post
# Used: SpecificClubPost.vue [components folder]
# Input:
#   1. Commenter ID (i.e., the member's ID in the clubMembers table)
#   2. Post ID
#   3. Comment Content
# Output: Possible return codes [201 - Comment added successfully, 400 - Missing required data, 404 - No such post exist, 500 - An error occurred adding the comment]
@blueprint.route('/addComment', methods=['POST'])
def addComment():
    conn = g.db
    cur = conn.cursor()

    try:
        data = request.get_json()

        # Get all the required data
        commenter_id = data['commenterID']
        post_id = data['postID']
        comment_content = data['commentContent']

        # Check if all the required data is provided
        if not commenter_id or not post_id or not comment_content:
            return jsonify({
                'error': 'Missing required data'
            }), 400

        # Step 1: Get today's date
        comment_date = datetime.now()

        # Step 2: Check if the post exist
        cur.execute('SELECT * FROM "clubPosts" WHERE id = %s', (post_id,))
        post = cur.fetchone()

        if not post:
            return jsonify({
                'error': 'No such post exist'
            }), 404

        # Step 3: Insert the new comment into the database
        cur.execute('INSERT INTO "clubPostComments" ("postID", "commentDate", "commentContent", "commenterID") VALUES (%s, %s, %s, %s) RETURNING id', 
                    (post_id, comment_date, comment_content, commenter_id,))
        comment_id = cur.fetchone()['id']
        conn.commit()

        # Step 4: Get the commenter's information
        commenter_info = getUserInfo(cur, commenter_id)

        # Step 5: Award points to the user for adding a comment
        # get the user id and user type from the commenter id
        cur.execute('SELECT "userID", "userType" FROM "clubMembers" WHERE id = %s', (commenter_id,))
        user = cur.fetchone()

        if (user['userType'] == 'user'):
            
            if pointsHelperFunc.check_max_proof_points(user['userID']):
                return jsonify({
                    'message': 'Comment added successfully',
                    'comment_obj': {
                        "commentContent": comment_content,
                        "commentDate": comment_date,
                        "commenterID": commenter_id,
                        "commenterInfo": commenter_info,
                        "id": comment_id,
                        "likedMembers": [],
                        "postID": post_id
                    }
                }), 201

            # Get the current points for commenting
            cur.execute('SELECT "proofPoints", "ruleName" FROM "pointSystemRules" WHERE id = %s', (10,))
            points = cur.fetchone()

            cur.execute('UPDATE "pointsRecorder" SET "currentPoints" = "currentPoints" + %s WHERE "userID" = %s AND "userType" = %s', (points['proofPoints'], user['userID'], 'user',))
            conn.commit()

            print(f"Added {points['proofPoints']} points to user {user['userID']} for adding a comment")

        return jsonify({
            'message': 'Comment added successfully',
            'comment_obj': {
                "commentContent": comment_content,
                "commentDate": comment_date,
                "commenterID": commenter_id,
                "commenterInfo": commenter_info,
                "id": comment_id,
                "likedMembers": [],
                "postID": post_id
            }
        }), 201

    except Exception as e:
        print(str(e))
        # Rollback the transaction if an error occurred
        conn.rollback()
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred adding the comment."
            }
        ), 500
    
    finally:
        cur.close()


# -----------------------------------------------------------------------------------------
# [POST] requestToJoinClub
# Purpose: Request to join a club (for private clubs) [user can only request to join a club if the club is invite only and has not been invited to join the club yet]
# Used: 
#   1. BrowseClubs.vue [views folder inside Users folder]
#   2. ClubView.vue [views folder inside Users folder]
# Input:
#   1. Club ID
#   2. User ID
#   3. User Type
# Output: Possible return codes [201 - Request to join the club sent successfully, 400 - Missing required data, 404 - No such club exist, 500 - An error occurred sending the request]
@blueprint.route('/requestToJoinClub', methods=['POST'])
def requestToJoinClub():
    conn = g.db
    cur = conn.cursor()

    try:
        data = request.get_json()

        # Get all the required data
        club_id = data['clubID']
        user_id = data['userID']
        user_type = data['userType']

        # Check if all the required data is provided
        if not club_id or not user_id or not user_type:
            return jsonify({
                'error': 'Missing required data'
            }), 400

        # Step 1: Check if the club exist
        cur.execute('SELECT * FROM "clubs" WHERE id = %s', (club_id,))
        club = cur.fetchone()

        if not club:
            return jsonify({
                'error': 'No such club exist'
            }), 404
        
        # Step 2: Check if user exist 
        user = getUserInfoByID(cur, user_id, user_type)

        if not user:
            return jsonify({
                'error': 'No such user exist'
            }), 404
        

        # Step 3: Insert the user into the clubRequests table
        request_date = datetime.now()
        cur.execute('INSERT INTO "clubRequests" ("clubID", "userID", "userType", "requestDate") VALUES (%s, %s, %s, %s)', (club_id, user_id, user_type, request_date,))
        conn.commit()

        return jsonify({
            'message': 'Request to join the club sent successfully'
        }), 201

    except Exception as e:
        print(str(e))
        # Rollback the transaction if an error occurred
        conn.rollback()
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred sending the request."
            }
        ), 500
    
    finally:
        cur.close()


# -----------------------------------------------------------------------------------------
# [POST] acceptClubRequest
# Purpose: Accept a user's request to join the club (remove the request from the clubRequests table and add the user to the clubMembers table)
# Used: ClubSettings.vue [components folder inside frontend folder]
# Input:
#   1. Club ID
#   2. Requester ID (i.e., the user who requested to join the club)
#   3. User Type (i.e., the user type of the requester)
#   4. Admin ID (i.e., the member id who is accepting the request)
# Output: Possible return codes [200 - User accepted successfully, 400 - Missing required data, 403 - No permission to accept the request, 404 - No such club/requester, 500 - An error occurred accepting the request]
@blueprint.route('/acceptClubRequest', methods=['POST'])
def acceptClubRequest():
    conn = g.db
    cur = conn.cursor()

    try:
        data = request.get_json()

        # Get all the required data
        club_id = data['clubID']
        requester_id = data['requesterID']
        user_type = data['userType']
        admin_id = data['adminID']

        # Check if all the required data is provided
        if not club_id or not requester_id or not user_type or not admin_id:
            return jsonify({
                'error': 'Missing required data'
            }), 400

        # Step 1: Check if the club exist
        cur.execute('SELECT * FROM "clubs" WHERE id = %s', (club_id,))
        club = cur.fetchone()

        if not club:
            return jsonify({
                'error': 'No such club exist'
            }), 404

        # Step 2: Check if the user who is accepting the request is an admin of the club
        cur.execute('SELECT * FROM "clubMembers" WHERE "clubID" = %s AND "id" = %s AND "isAdmin" = TRUE', (club_id, admin_id,))
        isAdmin = cur.fetchone()

        if not isAdmin:
            return jsonify({
                'error': 'You do not have the permission to accept the request'
            }), 403

        # Step 3: Check if the user who requested to join the club exist and has a valid request
        cur.execute('SELECT * FROM "clubRequests" WHERE "clubID" = %s AND "userID" = %s AND "userType" = %s', (club_id, requester_id, user_type,))
        user_request = cur.fetchone()

        if not user_request:
            return jsonify({
                'error': 'No such requester'
            }), 404

        # Step 4: Remove the request from the clubRequests table
        cur.execute('DELETE FROM "clubRequests" WHERE "clubID" = %s AND "userID" = %s AND "userType" = %s', (club_id, requester_id, user_type,))

        # Step 5: Insert the user into the clubMembers table
        join_date = datetime.now()
        cur.execute('INSERT INTO "clubMembers" ("clubID", "userID", "userType", "joinDate", "isAdmin") VALUES (%s, %s, %s, %s, FALSE)', (club_id, requester_id, user_type, join_date,))
        conn.commit()

        # Step 6: Append 1 to the totalMembers in the clubs table
        cur.execute('UPDATE "clubs" SET "totalMembers" = "totalMembers" + 1 WHERE id = %s', (club_id,))
        conn.commit()

        return jsonify({
            'message': 'User accepted successfully'
        }), 200

    except Exception as e:
        print(str(e))
        # Rollback the transaction if an error occurred
        conn.rollback()
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred accepting the request."
            }
        ), 500


# -----------------------------------------------------------------------------------------
# [POST] acceptClubInvite
# Purpose: Join a club after accepting friend's invite to the club 
# Used: 
#   1. ClubView.vue [views folder inside Users folder]
# Input: 
#   1. User ID
#   2. UserType
#   2. Club ID
# Output: Possible return codes [201 - User joined the club successfully, 400 - Missing required data, 404 - No such club/user exist or user not yet invited to the club, 500 - An error occurred joining the club]
@blueprint.route('/acceptClubInvite', methods=['POST'])
def acceptClubInvite():
    conn = g.db
    cur = conn.cursor()

    try:
        data = request.get_json()

        # Get all the required data
        user_id = data['userID']
        user_type = data['userType']
        club_id = data['clubID']


        # Check if all the required data is provided
        if not user_id or not user_type or not club_id:
            return jsonify({
                'error': 'Missing required data'
            }), 400

        # Step 1: Check if the club exist
        cur.execute('SELECT * FROM "clubs" WHERE id = %s', (club_id,))
        club = cur.fetchone()

        if not club:
            return jsonify({
                'error': 'No such club exist'
            }), 404

        # Step 2: Check if the user exist 
        user = getUserInfoByID(cur, user_id, user_type)

        if not user:
            return jsonify({
                'error': 'No such user exist'
            }), 404
        
        # Step 3: Check if the user has been invited to the club
        cur.execute('SELECT * FROM "clubInvites" WHERE "clubID" = %s AND "inviteeID" = %s AND "inviteeUserType" = %s', (club_id, user_id, user_type,))
        member = cur.fetchone()

        if not member:
            return jsonify({
                'error': 'User has not been invited to the club'
            }), 404
        
        # Get today's date
        join_date = datetime.now()

        # Step 4: Remove club invite from the clubInvites table
        cur.execute('DELETE FROM "clubInvites" WHERE "clubID" = %s AND "inviteeID" = %s AND "inviteeUserType" = %s', (club_id, user_id, user_type,))
        conn.commit()

        # Step 5: Insert the user into the clubMembers table
        cur.execute('INSERT INTO "clubMembers" ("clubID", "userID", "userType", "joinDate", "isAdmin") VALUES (%s, %s, %s, %s, FALSE)', (club_id, user_id, user_type, join_date,))
        conn.commit()

        # Step 6: Append 1 to the totalMembers in the clubs table
        cur.execute('UPDATE "clubs" SET "totalMembers" = "totalMembers" + 1 WHERE id = %s', (club_id,))
        conn.commit()

        return jsonify({
            'message': 'User joined the club successfully'
        }), 201

    except Exception as e:
        print(str(e))
        # Rollback the transaction if an error occurred
        conn.rollback()
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred joining the club."
            }
        ), 500
    
    finally:
        cur.close()


#   -----------------------------------------------------------------------------------------
# [PUT] editPost
# Purpose: Edit a post 
# Used: ClubView.vue [views folder inside Users folder]
# Input:
#   1. Post ID
#   2. Post Content
#   3. Editor ID (i.e., the member ID who edited the post)
#   4. Post Photos (optional)
# Output: Possible return codes [200 - Post edited successfully, 400 - Missing required data, 403 - No permission to edit post, 404 - No such post exist, 500 - An error occurred editing the post]
@blueprint.route('/editPost', methods=['PUT'])
def editPost():
    conn = g.db
    cur = conn.cursor()

    try:
        data = request.get_json()

        # Get all the required data
        post_id = data['postID']
        post_content = data['postContent']
        editor_id = data['editorID'] 

        # Check if all the required data is provided
        if not post_id or not post_content or not editor_id:
            return jsonify({
                'error': 'Missing required data'
            }), 400

        # List to store the image urls
        image_urls = []

        # Step 1: Check if the editor is the creator of the post
        cur.execute('SELECT * FROM "clubPosts" WHERE id = %s AND "posterID" = %s', (post_id, editor_id,))
        isCreator = cur.fetchone()

        if not isCreator:
            # Step 2: Check if the editor is an admin of the club
            cur.execute('SELECT * FROM "clubMembers" WHERE "clubID" = (SELECT "clubID" FROM "clubPosts" WHERE id = %s) AND id = %s AND "isAdmin" = TRUE', (post_id, editor_id,))
            isAdmin = cur.fetchone()

            if not isAdmin:
                return jsonify({
                    'error': 'You do not have the permission to edit this post'
                }), 403

        # Step 3: Check if the post exist
        cur.execute('SELECT * FROM "clubPosts" WHERE id = %s', (post_id,))
        post = cur.fetchone()

        if not post:
            return jsonify({
                'error': 'No such post exist'
            }), 404
        
        # Step 4: Check if the post photo is provided
        if len(data['images']) > 0:

            # Loop through the images and upload them to S3
            for image in data['images']:
                if not image:
                    continue

                # Check if the image is already in S3
                if 's3' in image:
                    image_urls.append(image)
                    continue
                else:
                    image64 = s3Images.uploadBase64ImageToS3(image)
                    image_urls.append(image64)

            # Make the postPhotos as a text string starting with { and ending with }
            post_photos = '{' + ','.join(f'"{url}"' for url in image_urls) + '}'
        else:
            post_photos = '{}'
            
        # Step 5: Update the post content and post photos
        cur.execute('UPDATE "clubPosts" SET "postContent" = %s, "postPhotos" = %s WHERE id = %s', (post_content, post_photos, post_id,))
        conn.commit()

        return jsonify({
            'message': 'Post edited successfully'
        }), 200
    
    except Exception as e:
        print(str(e))
        # Rollback the transaction if an error occurred
        conn.rollback()
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred editing the post."
            }
        ), 500
    
    finally:
        cur.close()


# -----------------------------------------------------------------------------------------
# [PUT] editComment
# Purpose: Edit a comment
# Used: 
# Input:
#   1. Comment ID
#   2. Comment Content
#   3. Editor ID (i.e., the user who edited the comment)
# Output: Possible return codes [200 - Comment edited successfully, 400 - Missing required data, 403 - No permission to edit comment, 404 - No such comment exist, 500 - An error occurred editing the comment]
@blueprint.route('/editComment', methods=['PUT'])
def editComment():
    conn = g.db
    cur = conn.cursor()

    try:
        data = request.get_json()

        # Get all the required data
        comment_id = data['commentID']
        comment_content = data['commentContent']
        editor_id = data['editorID'] # The user who edited the comment

        # Check if all the required data is provided
        if not comment_id or not comment_content or not editor_id:
            return jsonify({
                'error': 'Missing required data'
            }), 400

        # Step 1: Check if the editor is the creator of the comment
        cur.execute('SELECT * FROM "clubPostComments" WHERE id = %s AND "commenterID" = %s', (comment_id, editor_id,))
        isCreator = cur.fetchone()

        if not isCreator:
            # Step 2: Check if the editor is an admin of the club
            cur.execute('SELECT * FROM "clubMembers" WHERE "clubID" = (SELECT "clubID" FROM "clubPostComments" WHERE id = %s) AND "id" = %s AND "isAdmin" = TRUE', (comment_id, editor_id,))
            isAdmin = cur.fetchone()

            if not isAdmin:
                return jsonify({
                    'error': 'You do not have the permission to edit this comment'
                }), 403

        # Step 3: Check if the comment exist
        cur.execute('SELECT * FROM "clubPostComments" WHERE id = %s', (comment_id,))
        comment = cur.fetchone()

        if not comment:
            return jsonify({
                'error': 'No such comment exist'
            }), 404
        
        # Step 4: Update the comment content
        cur.execute('UPDATE "clubPostComments" SET "commentContent" = %s WHERE id = %s', (comment_content, comment_id,))
        conn.commit()

        return jsonify({
            'message': 'Comment edited successfully'
        }), 200
    
    except Exception as e:
        print(str(e))
        # Rollback the transaction if an error occurred
        conn.rollback()
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred editing the comment."
            }
        ), 500
    
    finally:
        cur.close()


# -----------------------------------------------------------------------------------------
# [PUT] dislikeUndislikePost
# Purpose: Dislike a post or un-dislike a post
# Used:
#   1. ClubView.vue [views folder inside Users folder]
# Input:
#   1. Member ID
#   2. Post ID
#   3. Club ID
# Output: Possible return codes [200 - Post disliked/un-disliked successfully, 400 - Missing required data, 404 - No such user/post exist, 500 - An error occurred disliking the post]
@blueprint.route('/dislikeUndislikePost', methods=['PUT'])
def dislikeUndislikePost():
    conn = g.db
    cur = conn.cursor()

    try:
        data = request.get_json()

        # Get all the required data
        member_id = data['memberID']
        post_id = data['postID']
        club_id = data['clubID']

        # Check if all the required data is provided
        if not member_id or not post_id or not club_id:
            return jsonify({
                'error': 'Missing required data'
            }), 400

        # Step 1: Check if the member exist
        cur.execute('SELECT * FROM "clubMembers" WHERE id = %s', (member_id,))
        member = cur.fetchone()

        if not member:
            return jsonify({
                'error': 'No such member exist'
            }), 404

        # Step 2: Check if the post exist
        cur.execute('SELECT * FROM "clubPosts" WHERE id = %s', (post_id,))
        post = cur.fetchone()

        if not post:
            return jsonify({
                'error': 'No such post exist'
            }), 404
        
        # Step 3: Check if the member has already disliked the post
        cur.execute('SELECT * FROM "clubPostsDislikes" WHERE "clubID" = %s AND "memberID" = %s AND "postID" = %s', (club_id, member_id, post_id,))
        disliked = cur.fetchone()

        if disliked:
            # Un-dislike the post
            cur.execute('DELETE FROM "clubPostsDislikes" WHERE "clubID" = %s AND "memberID" = %s AND "postID" = %s', (club_id, member_id, post_id,))
            conn.commit()

            return jsonify({
                'message': 'Post un-disliked successfully',
                "disliked": False
            }), 200
        
        # Step 4: Insert the dislike into the clubPostsDislikes table
        cur.execute('INSERT INTO "clubPostsDislikes" ("clubID", "memberID", "postID") VALUES (%s, %s, %s)', (club_id, member_id, post_id,))
        conn.commit()
    
        return jsonify({
            'message': 'Post disliked successfully',
            "disliked": True
        }), 200
    
    except Exception as e:
        print(str(e))
        # Rollback the transaction if an error occurred
        conn.rollback()
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred disliking the post."
            }
        ), 500
    
    finally:
        cur.close()


# -----------------------------------------------------------------------------------------
# [PUT] dislikeUndislikeComment
# Purpose: Dislike a comment or un-dislike a comment
# Used:
# Input:
#   1. Post ID
#   2. Comment ID
#   3. Member ID
# Output: Possible return codes [200 - Comment disliked/un-disliked successfully, 400 - Missing required data, 404 - No such user/comment exist, 500 - An error occurred disliking the comment]
@blueprint.route('/dislikeUndislikeComment', methods=['PUT'])
def dislikeUndislikeComment():
    conn = g.db
    cur = conn.cursor()

    try:
        # Get all the required data
        data = request.get_json()
        post_id = data['postID']
        comment_id = data['commentID']
        member_id = data['memberID']

        # Check if all the required data is provided
        if not post_id or not comment_id or not member_id:
            return jsonify({
                'error': 'Missing required data'
            }), 400

        # Step 1: Check if the member exist
        cur.execute('SELECT * FROM "clubMembers" WHERE id = %s', (member_id,))
        member = cur.fetchone()

        if not member:
            return jsonify({
                'error': 'No such member exist'
            }), 404

        # Step 2: Check if the comment exist
        cur.execute('SELECT * FROM "clubPostComments" WHERE id = %s', (comment_id,))
        comment = cur.fetchone()

        if not comment:
            return jsonify({
                'error': 'No such comment exist'
            }), 404
        
        # Step 3: Check if the member has already disliked the comment
        cur.execute('SELECT * FROM "clubPostCommentsDislikes" WHERE "postID" = %s AND "memberID" = %s AND "commentID" = %s', (post_id, member_id, comment_id,))
        disliked = cur.fetchone()

        if disliked:
            # Un-dislike the comment
            cur.execute('DELETE FROM "clubPostCommentsDislikes" WHERE "postID" = %s AND "memberID" = %s AND "commentID" = %s', (post_id, member_id, comment_id,))
            conn.commit()

            return jsonify({
                'message': 'Comment un-disliked successfully',
                'disliked': False
            }), 200

        # Step 4: Insert the dislike into the clubPostCommentsDislikes table
        cur.execute('INSERT INTO "clubPostCommentsDislikes" ("postID", "memberID", "commentID") VALUES (%s, %s, %s)', (post_id, member_id, comment_id,))
        conn.commit()

        return jsonify({
            'message': 'Comment disliked successfully',
            'disliked': True
        }), 200
    
    except Exception as e:
        print(str(e))
        # Rollback the transaction if an error occurred
        conn.rollback()
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred disliking the comment."
            }
        ), 500
    
    finally:
        cur.close()


# -----------------------------------------------------------------------------------------
# [PUT] likeUnlikePost
# Purpose: Like or Unlike a post
# Used: 
#   1. ClubView.vue [views folder inside Users folder]
# Input:
#   1. Member ID
#   2. Post ID
#   3. Club ID
# Output: Possible return codes [200 - Post liked/unliked successfully, 400 - Missing required data, 404 - No such user/post exist, 500 - An error occurred liking the post]
@blueprint.route('/likeUnlikePost', methods=['PUT'])
def likePost():
    conn = g.db
    cur = conn.cursor()

    try:
        data = request.get_json()

        # Get all the required data
        member_id = data['memberID']
        post_id = data['postID']
        club_id = data['clubID']

        # Check if all the required data is provided
        if not member_id or not post_id or not club_id:
            return jsonify({
                'error': 'Missing required data'
            }), 400

        # Step 1: Check if the member exist
        cur.execute('SELECT * FROM "clubMembers" WHERE id = %s', (member_id,))
        member = cur.fetchone()

        if not member:
            return jsonify({
                'error': 'No such member exist'
            }), 404

        # Step 2: Check if the post exist
        cur.execute('SELECT * FROM "clubPosts" WHERE id = %s', (post_id,))
        post = cur.fetchone()

        if not post:
            return jsonify({
                'error': 'No such post exist'
            }), 404
        
        # Step 3: Check if the member has already liked the post
        cur.execute('SELECT * FROM "clubPostsLikes" WHERE "clubID" = %s AND "memberID" = %s AND "postID" = %s', (club_id, member_id, post_id,))
        liked = cur.fetchone()

        if liked:
            # Unlike the post
            cur.execute('DELETE FROM "clubPostsLikes" WHERE "clubID" = %s AND "memberID" = %s AND "postID" = %s', (club_id, member_id, post_id,))
            conn.commit()

            return jsonify({
                'message': 'Post unliked successfully',
                "liked": False
            }), 200

        # Step 4: Insert the like into the clubPostsLikes table
        cur.execute('INSERT INTO "clubPostsLikes" ("clubID", "memberID", "postID") VALUES (%s, %s, %s)', (club_id, member_id, post_id,))
        conn.commit()

        return jsonify({
            'message': 'Post liked successfully',
            "liked": True
        }), 200
    
    except Exception as e:
        print(str(e))
        # Rollback the transaction if an error occurred
        conn.rollback()
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred liking the post."
            }
        ), 500
    
    finally:
        cur.close()


# -----------------------------------------------------------------------------------------
# [PUT] likeUnlikeComment
# Purpose: Like or Unlike a comment
# Used: 
# Input:
#   1. Post ID
#   2. Comment ID
#   3. Member ID
# Output: Possible return codes [200 - Comment liked/unliked successfully, 400 - Missing required data, 404 - No such user/comment exist, 500 - An error occurred liking the comment]
@blueprint.route('/likeUnlikeComment', methods=['PUT'])
def likeUnlikeComment():
    conn = g.db
    cur = conn.cursor()

    try:
        # Get all the required data
        data = request.get_json()
        post_id = data['postID']
        comment_id = data['commentID']
        member_id = data['memberID']

        # Check if all the required data is provided
        if not post_id or not comment_id or not member_id:
            return jsonify({
                'error': 'Missing required data'
            }), 400

        # Step 1: Check if the member exist
        cur.execute('SELECT * FROM "clubMembers" WHERE id = %s', (member_id,))
        member = cur.fetchone()

        if not member:
            return jsonify({
                'error': 'No such member exist'
            }), 404

        # Step 2: Check if the comment exist
        cur.execute('SELECT * FROM "clubPostComments" WHERE id = %s', (comment_id,))
        comment = cur.fetchone()

        if not comment:
            return jsonify({
                'error': 'No such comment exist'
            }), 404
        
        # Step 3: Check if the member has already liked the comment
        cur.execute('SELECT * FROM "clubPostCommentsLikes" WHERE "postID" = %s AND "memberID" = %s AND "commentID" = %s', (post_id, member_id, comment_id,))
        liked = cur.fetchone()

        if liked:
            # Unlike the comment
            cur.execute('DELETE FROM "clubPostCommentsLikes" WHERE "postID" = %s AND "memberID" = %s AND "commentID" = %s', (post_id, member_id, comment_id,))
            conn.commit()

            return jsonify({
                'message': 'Comment unliked successfully',
                'liked': False
            }), 200

        # Step 4: Insert the like into the clubPostCommentsLikes table
        cur.execute('INSERT INTO "clubPostCommentsLikes" ("postID", "memberID", "commentID") VALUES (%s, %s, %s)', (post_id, member_id, comment_id,))
        conn.commit()

        return jsonify({
            'message': 'Comment liked successfully',
            'liked': True
        }), 200

    except Exception as e:
        print(str(e))
        # Rollback the transaction if an error occurred
        conn.rollback()
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred liking the comment."
            }
        ), 500
    
    finally:
        cur.close()


# -----------------------------------------------------------------------------------------
# [PUT] makeAdmin
# Purpose: Make a member an admin of the club
# Used:
# Input:
#   1. Member ID (i.e., the member ID who is being made an admin)
#   2. Club ID
#   3. Admin ID (i.e., the member ID who is making the member an admin)
# Output: Possible return codes [200 - Member is now an admin, 400 - Missing required data, 403 - No permission to make member an admin, 404 - No such club/member exist or user is not a member of the club yet, 500 - An error occurred making the member an admin]
@blueprint.route('/makeAdmin', methods=['PUT'])
def makeAdmin():
    conn = g.db
    cur = conn.cursor()

    try:
        data = request.get_json()

        # Get all the required data
        member_id = data['memberID']
        club_id = data['clubID']
        admin_id = data['adminID']

        # Check if all the required data is provided
        if not member_id or not club_id or not admin_id:
            return jsonify({
                'error': 'Missing required data'
            }), 400

        # Step 1: Check if the club exist
        cur.execute('SELECT * FROM "clubs" WHERE id = %s', (club_id,))
        club = cur.fetchone()

        if not club:
            return jsonify({
                'error': 'No such club exist'
            }), 404

        # Step 2: Check if the user who is making someone an admin is an admin of the club
        cur.execute('SELECT * FROM "clubMembers" WHERE "clubID" = %s AND "id" = %s AND "isAdmin" = TRUE', (club_id, admin_id,))
        isAdmin = cur.fetchone()

        if not isAdmin:
            return jsonify({
                'error': 'You do not have the permission to make a member an admin of this club'
            }), 403

        # Step 3: Check if the member exist and is a member of the club
        cur.execute('SELECT * FROM "clubMembers" WHERE "clubID" = %s AND id = %s', (club_id, member_id,))
        member = cur.fetchone()

        if not member:
            return jsonify({
                'error': 'No such member exist or user is not a member of the club yet'
            }), 404

        # Step 4: Make the member an admin
        cur.execute('UPDATE "clubMembers" SET "isAdmin" = TRUE WHERE "clubID" = %s AND id = %s', (club_id, member_id,))
        conn.commit()

        return jsonify({
            'message': 'Member is now an admin'
        }), 200

    except Exception as e:
        print(str(e))
        # Rollback the transaction if an error occurred
        conn.rollback()
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred making the member an admin."
            }
        ), 500
    
    finally:
        cur.close()


# -----------------------------------------------------------------------------------------
# [PUT] revokeAdmin
# Purpose: Revoke a member's admin status
# Used: ClubSettings.vue [components folder inside frontend folder]
# Input:
#   1. Member ID (i.e., the member ID who is being revoked of admin status)
#   2. Club ID
#   3. Admin ID (i.e., the member ID who is revoking the member of admin status)
# Output: Possible return codes [200 - Member is no longer an admin, 400 - Missing required data, 403 - No permission to revoke admin status, 404 - No such club/member exist or user is not an admin of the club yet, 500 - An error occurred revoking the member of admin status]
@blueprint.route('/revokeAdmin', methods=['PUT'])
def revokeAdmin():
    conn = g.db
    cur = conn.cursor()

    try:
        data = request.get_json()

        # Get all the required data
        member_id = data['memberID']
        club_id = data['clubID']
        admin_id = data['adminID']

        # Check if all the required data is provided
        if not member_id or not club_id or not admin_id:
            return jsonify({
                'error': 'Missing required data'
            }), 400

        # Step 1: Check if the club exist
        cur.execute('SELECT * FROM "clubs" WHERE id = %s', (club_id,))
        club = cur.fetchone()

        if not club:
            return jsonify({
                'error': 'No such club exist'
            }), 404

        # Step 2: Check if the user who is revoking someone's admin status is an admin of the club
        cur.execute('SELECT * FROM "clubMembers" WHERE "clubID" = %s AND "id" = %s AND "isAdmin" = TRUE', (club_id, admin_id,))
        isAdmin = cur.fetchone()

        if not isAdmin:
            return jsonify({
                'error': 'You do not have the permission to revoke a member of admin status of this club'
            }), 403

        # Step 3: Check if the member exist and is an admin of the club
        cur.execute('SELECT * FROM "clubMembers" WHERE "clubID" = %s AND id = %s AND "isAdmin" = TRUE', (club_id, member_id,))
        member = cur.fetchone()

        if not member:
            return jsonify({
                'error': 'No such member exist or user is not an admin of the club yet'
            }), 404

        # Step 4: Revoke the member's admin status
        cur.execute('UPDATE "clubMembers" SET "isAdmin" = FALSE WHERE "clubID" = %s AND id = %s', (club_id, member_id,))
        conn.commit()

        return jsonify({
            'message': 'Member is no longer an admin'
        }), 200

    except Exception as e:
        print(str(e))
        # Rollback the transaction if an error occurred
        conn.rollback()
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred revoking the member of admin status."
            }
        ), 500
    
    finally:
        cur.close()


# -----------------------------------------------------------------------------------------
# [PUT] updateClubInfo
# Purpose: Update the club information
# Used: ClubSettings.vue [components folder inside frontend folder]
# Input:
#   1. Club ID
#   2. Club Name 
#   3. Club Description
#   4. Is Invite Only (boolean: True = Private, False = Public)
#   5. Club Banner (optional)
#   6. Editor ID (i.e., the user who is updating the club information)
# Output: Possible return codes [200 - Club information updated successfully, 400 - Missing required data, 403 - No permission to edit the club information, 404 - No such club exist, 500 - An error occurred updating the club information]
@blueprint.route('/updateClubInfo', methods=['PUT'])
def updateClubInfo():
    conn = g.db
    cur = conn.cursor()

    try:
        data = request.get_json()

        # Get all the required data
        club_id = data['clubID']
        club_name = data['clubName']
        club_desc = data['clubDesc']
        is_invite_only = data['isInviteOnly']
        editor_id = data['editorID']

        # Check if all the required data is provided
        if not club_id or not club_name or not club_desc or not is_invite_only or not editor_id:
            return jsonify({
                'error': 'Missing required data'
            }), 400

        # Step 1: Check if the club exist
        cur.execute('SELECT * FROM "clubs" WHERE id = %s', (club_id,))
        club = cur.fetchone()

        if not club:
            return jsonify({
                'error': 'No such club exist'
            }), 404

        # Step 2: Check if the user who is updating the club information is an admin of the club
        cur.execute('SELECT * FROM "clubMembers" WHERE "clubID" = %s AND "id" = %s AND "isAdmin" = TRUE', (club_id, editor_id,))
        isAdmin = cur.fetchone()

        if not isAdmin:
            return jsonify({
                'error': 'You do not have the permission to edit the club information'
            }), 403

        # Step 3: Check if the club banner is provided
        if 'image64' in data and data['image64']:
            image64 = s3Images.uploadBase64ImageToS3(data['image64'])

            # Update the club banner
            cur.execute('UPDATE "clubs" SET "clubBanner" = %s WHERE id = %s', (image64, club_id,))
            conn.commit()

        # Step 4: Update the club information
        cur.execute('UPDATE "clubs" SET "clubName" = %s, "clubDesc" = %s, "isInviteOnly" = %s WHERE id = %s', (club_name, club_desc, is_invite_only, club_id,))
        conn.commit()

        return jsonify({
            'message': 'Club information updated successfully'
        }), 200
    
    except Exception as e:
        print(str(e))
        # Rollback the transaction if an error occurred
        conn.rollback()
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred updating the club information."
            }
        ), 500
    
    finally:
        cur.close()


# -----------------------------------------------------------------------------------------
# [DELETE] removeMembers
# Purpose: Remove members from the club
# Used:
# Input:
#   1. A list of member IDs to be removed from the club
#   2. Club ID
#   3, Remover ID (i.e., the user who is removing the members)
# Output: Possible return codes [200 - Members removed successfully, 400 - Missing required data, 403 - No permission to remove members, 404 - No such club exist, 500 - An error occurred removing the members]
@blueprint.route('/removeMembers', methods=['DELETE'])
def removeMembers():
    conn = g.db
    cur = conn.cursor()

    try:
        data = request.get_json()

        # Get all the required data
        club_id = data['clubID']
        members_list = data['members']
        remover_id = data['removerID']

        # Check if all the required data is provided
        if not club_id or len(members_list) == 0 or not remover_id:
            return jsonify({
                'error': 'Missing required data'
            }), 400

        # Step 1: Check if the club exist
        cur.execute('SELECT * FROM "clubs" WHERE id = %s', (club_id,))
        club = cur.fetchone()

        if not club:
            return jsonify({
                'error': 'No such club exist'
            }), 404
        
        # Step 2: Check if the remover is an admin of the club
        cur.execute('SELECT * FROM "clubMembers" WHERE "clubID" = %s AND "id" = %s AND "isAdmin" = TRUE', (club_id, remover_id,))
        isAdmin = cur.fetchone()

        if not isAdmin:
            return jsonify({
                'error': 'You do not have the permission to remove members from this club'
            }), 403
        
        # Counter to track the number of members removed
        count = 0

        # Step 3: Remove the members from the club
        for member_id in members_list:

            # Check if the user is an existing member of the club
            cur.execute('SELECT * FROM "clubMembers" WHERE "clubID" = %s AND id = %s', (club_id, member_id,))
            member = cur.fetchone()

            if not member: # Skip to the next member if the user is not an existing member of the club
                continue

            cur.execute('DELETE FROM "clubMembers" WHERE "clubID" = %s AND id = %s', (club_id, member_id,))
            conn.commit()
            count += 1

        # Step 4: Update the totalMembers in the clubs table
        cur.execute('UPDATE "clubs" SET "totalMembers" = "totalMembers" - %s WHERE id = %s', (count, club_id,))
        conn.commit()

        return jsonify({
            'message': 'Members removed successfully'
        }), 200

    except Exception as e:
        print(str(e))
        # Rollback the transaction if an error occurred
        conn.rollback()
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred removing the members."
            }
        ), 500
    
    finally:
        cur.close()


# -----------------------------------------------------------------------------------------
# [DELETE] removePost
# Purpose: Remove a post
# Used: ClubView.vue [views folder inside Users folder]
# Input:
#   1. Post ID
#   2. Remover ID (i.e., the member ID who is removing the post)
# Output: Possible return codes [200 - Post removed successfully, 400 - Missing required data, 403 - No permission to remove post, 404 - No such post exist, 500 - An error occurred removing the post]
@blueprint.route('/removePost', methods=['DELETE'])
def removePost():
    conn = g.db
    cur = conn.cursor()

    try:
        # Get all the required data
        data = request.get_json()

        post_id = data['postID']
        remover_id = data['removerID']

        # Check if all the required data is provided
        if not post_id or not remover_id:
            return jsonify({
                'error': 'Missing required data'
            }), 400

        # Step 1: Check if the remover is the creator of the post
        cur.execute('SELECT * FROM "clubPosts" WHERE id = %s AND "posterID" = %s', (post_id, remover_id,))
        isCreator = cur.fetchone()

        if not isCreator:
            # Step 2: Check if the remover is an admin of the club
            cur.execute('SELECT * FROM "clubMembers" WHERE "clubID" = (SELECT "clubID" FROM "clubPosts" WHERE id = %s) AND "id" = %s AND "isAdmin" = TRUE', (post_id, remover_id,))
            isAdmin = cur.fetchone()

            if not isAdmin:
                return jsonify({
                    'error': 'You do not have the permission to remove this post'
                }), 403
        
        # Step 3: Check if the post exist
        cur.execute('SELECT * FROM "clubPosts" WHERE id = %s', (post_id,))
        post = cur.fetchone()

        if not post:
            return jsonify({
                'error': 'No such post exist'
            }), 404

        # Step 4: Remove all the likes for the comments in the post
        cur.execute('DELETE FROM "clubPostCommentsLikes" WHERE "postID" = %s', (post_id,))

        # Step 5: Remove all the comments for the post
        cur.execute('DELETE FROM "clubPostComments" WHERE "postID" = %s', (post_id,))

        # Step 6: Remove all the likes for the post
        cur.execute('DELETE FROM "clubPostsLikes" WHERE "postID" = %s', (post_id,))

        # Step 7: Remove all the dislikes for the post
        cur.execute('DELETE FROM "clubPostsDislikes" WHERE "postID" = %s', (post_id,))
        
        # Step 7: Remove the post
        cur.execute('DELETE FROM "clubPosts" WHERE id = %s', (post_id,))
        conn.commit()

        # Step 8: Deduct points for removing the post

        # get user id and user type from the remover id
        cur.execute('SELECT "userID", "userType" FROM "clubMembers" WHERE id = %s', (remover_id,))
        user = cur.fetchone()

        if user['userType'] == 'user':
            # get current points for creating a post
            cur.execute('SELECT "proofPoints", "ruleName" FROM "pointSystemRules" WHERE id = %s', (7,))
            points = cur.fetchone()

            # deduct points from the user
            cur.execute('UPDATE "pointsRecorder" SET "currentPoints" = "currentPoints" - %s WHERE id = %s', (points['proofPoints'], user['userID'],))
            conn.commit()

            print(f"Deducted {points['proofPoints']} points from user {user['userID']} for removing the post.")

            cur.execute(
                'SELECT id FROM "badges" WHERE "relatedEntity" = %s ORDER BY id LIMIT 1',
                ('ClubPost',)
                )
            badge_row = cur.fetchone()
            if not badge_row:        # nothing to adjust if badge doesn’t exist
                conn.commit()
                return
            
            club_badge_id = badge_row['id']
            # poster_id     = user['userID']  
            cur.execute(
                'SELECT id, "currentLevel", "currentProgress" '
                'FROM "userBadges" '
                'WHERE "userId" = %s AND "badgeId" = %s',
                (user['userID'], club_badge_id)
            )
            user_badge = cur.fetchone()
            if user_badge is None:                # user never had the badge
                conn.commit()
                return
            progress = user_badge["currentProgress"] - 1
            level    = user_badge["currentLevel"]
            cur.execute(
                'SELECT "levelStart","levelEnd","actionsRequired" '
                'FROM "badgeRules" '
                'WHERE "actionType" = %s '
                'ORDER BY "levelStart"',
                ('ClubPost',)
            )
            rules = cur.fetchall()

            def needed_for(lvl: int) -> int:
                for r in rules:
                    if r["levelStart"] <= lvl <= r["levelEnd"]:
                        return r["actionsRequired"]
                return rules[-1]["actionsRequired"]
            while progress < 0 and level > 1:
                level -= 1
                progress += needed_for(level)
            if level == 1 and progress <= 0:
                cur.execute('DELETE FROM "userBadges" WHERE id = %s', (user_badge["id"],))
                conn.commit()
                return
            # 6️⃣  Otherwise persist the downgraded state
            cur.execute(
                '''UPDATE "userBadges"
                SET "currentLevel"   = %s,
                    "currentProgress" = %s,
                    "lastUpdated"    = NOW()
                WHERE id = %s''',
                (level, progress, user_badge["id"])
            )
            conn.commit()

        return jsonify({
            'message': 'Post removed successfully',
            'pointsDeducted': points['proofPoints'],
            'rule': points['ruleName']
        }), 200
    
    except Exception as e:
        print(str(e))
        # Rollback the transaction if an error occurred
        conn.rollback()
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred removing the post."
            }
        ), 500
    
    finally:
        cur.close()


# -----------------------------------------------------------------------------------------
# [DELETE] removeComment
# Purpose: Remove a comment
# Used: 
# Input:
#   1. Comment ID
#   2. Remover ID (i.e., the member ID who is removing the comment)
# Output: Possible return codes [200 - Comment removed successfully, 400 - Missing required data, 403 - No permission to remove comment, 404 - No such comment exist, 500 - An error occurred removing the comment]
@blueprint.route('/removeComment', methods=['DELETE'])
def removeComment():
    conn = g.db
    cur = conn.cursor()

    try:
        # Get all the required data
        data = request.get_json()

        comment_id = data['commentID']
        remover_id = data['removerID']

        # Check if all the required data is provided
        if not comment_id or not remover_id:
            return jsonify({
                'error': 'Missing required data'
            }), 400

        # Step 1: Check if the remover is the creator of the comment
        cur.execute('SELECT * FROM "clubPostComments" WHERE id = %s AND "commenterID" = %s', (comment_id, remover_id,))
        isCreator = cur.fetchone()

        if not isCreator:
            # Step 2: Check if the remover is an admin of the club
            cur.execute('SELECT * FROM "clubMembers" WHERE "clubID" = (SELECT "clubID" FROM "clubPostComments" WHERE id = %s) AND "id" = %s AND "isAdmin" = TRUE', (comment_id, remover_id,))
            isAdmin = cur.fetchone()

            if not isAdmin:
                return jsonify({
                    'error': 'You do not have the permission to remove this comment'
                }), 403

        # Step 3: Check if the comment exist
        cur.execute('SELECT * FROM "clubPostComments" WHERE id = %s', (comment_id,))
        comment = cur.fetchone()

        if not comment:
            return jsonify({
                'error': 'No such comment exist'
            }), 404
        
        # Step 4: Remove all the likes for the comment
        cur.execute('DELETE FROM "clubPostCommentsLikes" WHERE "commentID" = %s', (comment_id,))

        # Step 5: Remove the comment
        cur.execute('DELETE FROM "clubPostComments" WHERE id = %s', (comment_id,))
        conn.commit()

        # Step 6: Deduct points for removing the comment
        # get user id and user type from the remover id
        cur.execute('SELECT "userID", "userType" FROM "clubMembers" WHERE id = %s', (remover_id,))
        user = cur.fetchone()

        if user['userType'] == 'user':
            # get current points for creating a comment
            cur.execute('SELECT "proofPoints", "ruleName" FROM "pointSystemRules" WHERE id = %s', (10,))
            points = cur.fetchone()

            # deduct points from the user
            cur.execute('UPDATE "pointsRecorder" SET "currentPoints" = "currentPoints" - %s WHERE id = %s', (points['proofPoints'], user['userID'],))
            conn.commit()

            print(f"Deducted {points['proofPoints']} points from user {user['userID']} for removing the comment.")

        return jsonify({
            'message': 'Comment removed successfully',
            'pointsDeducted': points['proofPoints'],
            'rule': points['ruleName']
        }), 200
    
    except Exception as e:
        print(str(e))
        # Rollback the transaction if an error occurred
        conn.rollback()
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred removing the comment."
            }
        ), 500
    
    finally:
        cur.close()


# -----------------------------------------------------------------------------------------
# [DELETE] leaveClub
# Purpose: Leave the club
# Used: ClubView.vue [views folder inside Users folder]
# Input:
#   1. Member ID
#   2. Club ID
# Output: Possible return codes [200 - Member left the club successfully, 400 - Missing required data, 404 - No such club/member exist, 500 - An error occurred leaving the club]
@blueprint.route('/leaveClub', methods=['DELETE'])
def leaveClub():
    conn = g.db
    cur = conn.cursor()

    try:
        data = request.get_json()

        # Get all the required data
        member_id = data['memberID']
        club_id = data['clubID']

        # Check if all the required data is provided
        if not member_id or not club_id:
            return jsonify({
                'error': 'Missing required data'
            }), 400

        # Step 1: Check if the club exist
        cur.execute('SELECT * FROM "clubs" WHERE id = %s', (club_id,))
        club = cur.fetchone()

        if not club:
            return jsonify({
                'error': 'No such club exist'
            }), 404

        # Step 2: Check if the member exist
        cur.execute('SELECT * FROM "clubMembers" WHERE id = %s', (member_id,))
        member = cur.fetchone()

        if not member:
            return jsonify({
                'error': 'No such member exist'
            }), 404
        
        # Step 3: Remove comments, likes and posts of the member
        cur.execute('DELETE FROM "clubPostCommentsLikes" WHERE "memberID" = %s', (member_id,))
        cur.execute('DELETE FROM "clubPostComments" WHERE "commenterID" = %s', (member_id,))
        cur.execute('DELETE FROM "clubPostsLikes" WHERE "memberID" = %s', (member_id,))
        cur.execute('DELETE FROM "clubPosts" WHERE "posterID" = %s', (member_id,))
        
        # Step 4: Leave the club
        cur.execute('DELETE FROM "clubMembers" WHERE "clubID" = %s AND id = %s', (club_id, member_id,))
        conn.commit()

        # Step 5: Update the totalMembers in the clubs table
        cur.execute('UPDATE "clubs" SET "totalMembers" = "totalMembers" - 1 WHERE id = %s', (club_id,))
        conn.commit()

        return jsonify({
            'message': 'Member left the club successfully'
        }), 200

    except Exception as e:
        print(str(e))
        # Rollback the transaction if an error occurred
        conn.rollback()
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred leaving the club."
            }
        ), 500
    
    finally:
        cur.close()


# -----------------------------------------------------------------------------------------
# [DELETE] deleteClub
# Purpose: Delete the club
# Used: ClubSettings.vue [components folder inside frontend folder]
# Input:
#   1. Club ID
#   2. Remover ID (i.e., the user who is deleting the club)
# Output: Possible return codes [200 - Club deleted successfully, 400 - Missing required data, 403 - No permission to delete club, 404 - No such club exist, 500 - An error occurred deleting the club]
@blueprint.route('/deleteClub', methods=['DELETE'])
def deleteClub():
    conn = g.db
    cur = conn.cursor()

    try:
        data = request.get_json()

        # Get all the required data
        club_id = data['clubID']
        remover_id = data['removerID']

        # Check if all the required data is provided
        if not club_id or not remover_id:
            return jsonify({
                'error': 'Missing required data'
            }), 400

        # Step 1: Check if the club exist
        cur.execute('SELECT * FROM "clubs" WHERE id = %s', (club_id,))
        club = cur.fetchone()

        if not club:
            return jsonify({
                'error': 'No such club exist'
            }), 404
        
        # Step 2: Check if the remover is an admin of the club
        cur.execute('SELECT * FROM "clubMembers" WHERE "clubID" = %s AND "id" = %s AND "isAdmin" = TRUE', (club_id, remover_id,))
        isAdmin = cur.fetchone()
        
        if not isAdmin:
            return jsonify({
                'error': 'You do not have the permission to delete this club'
            }), 403
        
        # Step 3: Remove all the club members
        cur.execute('DELETE FROM "clubMembers" WHERE "clubID" = %s', (club_id,))

        # Step 4: Remove all the post in the club
        cur.execute('DELETE FROM "clubPosts" WHERE "clubID" = %s', (club_id,))

        # Step 5: Remove all the likes for the post, comments for deleted posts and likes for the comments where the post ID is null
        cur.execute('DELETE FROM "clubPostsLikes" WHERE "clubID" = %s', (club_id,))
        cur.execute('DELETE FROM "clubPostComments" WHERE "postID" IS NULL')
        cur.execute('DELETE FROM "clubPostCommentsLikes" WHERE "postID" IS NULL')

        # Step 6: Remove the club
        cur.execute('DELETE FROM "clubs" WHERE id = %s', (club_id,))
        conn.commit()

        return jsonify({
            'message': 'Club deleted successfully'
        }), 200

    except Exception as e:
        print(str(e))
        # Rollback the transaction if an error occurred
        conn.rollback()
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred deleting the club."
            }
        ), 500
    
    finally:
        cur.close()


# -----------------------------------------------------------------------------------------
# [DELETE] rejectClubRequests
# Purpose: Reject a club request (will remove the request from the clubRequests table)
# Used: ClubSettings.vue [components folder inside frontend folder]
# Input:
#   1. Club ID
#   2. Requester ID (i.e., the user id who requested to join the club)
#   3. User Type
#   4. Admin ID (i.e., the member id who is rejecting the request)
# Output: Possible return codes [200 - Request rejected successfully, 400 - Missing required data, 403 - No permission to reject request, 404 - No such requester exist, 500 - An error occurred rejecting the request]
@blueprint.route('/rejectClubRequests', methods=['DELETE'])
def rejectClubRequests():
    conn = g.db
    cur = conn.cursor()

    try:
        data = request.get_json()

        # Get all the required data
        club_id = data['clubID']
        requester_id = data['requesterID']
        user_type = data['userType']
        admin_id = data['adminID']

        # Check if all the required data is provided
        if not club_id or not requester_id or not user_type or not admin_id:
            return jsonify({
                'error': 'Missing required data'
            }), 400

        # Step 1: Check if the admin is an admin of the club
        cur.execute('SELECT * FROM "clubMembers" WHERE "clubID" = %s AND "id" = %s AND "isAdmin" = TRUE', (club_id, admin_id,))
        isAdmin = cur.fetchone()

        if not isAdmin:
            return jsonify({
                'error': 'You do not have the permission to reject the request'
            }), 403

        # Step 2: Check if the requester exist
        cur.execute('SELECT * FROM "clubRequests" WHERE "clubID" = %s AND "userID" = %s AND "userType" = %s', (club_id, requester_id, user_type,))
        requester = cur.fetchone()

        if not requester:
            return jsonify({
                'error': 'No such requester exist'
            }), 404

        # Step 3: Remove the request from the clubRequests table
        cur.execute('DELETE FROM "clubRequests" WHERE "clubID" = %s AND "userID" = %s AND "userType" = %s', (club_id, requester_id, user_type,))
        conn.commit()

        return jsonify({
            'message': 'Request rejected successfully'
        }), 200

    except Exception as e:
        print(str(e))
        # Rollback the transaction if an error occurred
        conn.rollback()
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred rejecting the request."
            }
        ), 500


# -----------------------------------------------------------------------------------------
# [DELETE] declineClubInvites
# Purpose: Reject a club invite (will remove the invite from the clubInvites table)
# Used: BrowseClubs.vue [components folder inside frontend folder]
# Input:
#   1. Club ID
#   2. Invitee ID (i.e., the user id who was invited to join the club)
#   3. User Type
# Output: Possible return codes [200 - Invite rejected successfully, 400 - Missing required data, 404 - No such invitee exist, 500 - An error occurred rejecting the invite]
@blueprint.route('/declineClubInvites', methods=['DELETE'])
def declineClubInvites():
    conn = g.db
    cur = conn.cursor()

    try:
        data = request.get_json()

        # Get all the required data
        club_id = data['clubID']
        invitee_id = data['userID']
        user_type = data['userType']

        # Check if all the required data is provided
        if not club_id or not invitee_id or not user_type:
            return jsonify({
                'error': 'Missing required data'
            }), 400

        # Step 1: Check if the invitee exist
        cur.execute('SELECT * FROM "clubInvites" WHERE "clubID" = %s AND "inviteeID" = %s AND "inviteeUserType" = %s', (club_id, invitee_id, user_type,))
        invitee = cur.fetchone()

        if not invitee:
            return jsonify({
                'error': 'No such invitee exist'
            }), 404

        # Step 2: Remove the invite from the clubInvites table
        cur.execute('DELETE FROM "clubInvites" WHERE "clubID" = %s AND "inviteeID" = %s AND "inviteeUserType" = %s', (club_id, invitee_id, user_type,))
        conn.commit()

        return jsonify({
            'message': 'Invite rejected successfully'
        }), 200

    except Exception as e:
        print(str(e))
        # Rollback the transaction if an error occurred
        conn.rollback()
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred rejecting the invite."
            }
        ), 500