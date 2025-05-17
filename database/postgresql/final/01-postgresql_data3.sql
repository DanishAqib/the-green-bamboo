-- DROP TABLES IF EXISTS -- 
DROP TABLE IF EXISTS "eventAttendees" CASCADE;
DROP TABLE IF EXISTS "events" CASCADE;
DROP TABLE IF EXISTs "clubPostCommentsLikes" CASCADE;
DROP TABLE IF EXISTS "clubPostCommentsDislikes" CASCADE;
DROP TABLE IF EXISTS "clubPostComments" CASCADE;
DROP TABLE IF EXISTS "clubPostsLikes" CASCADE;
DROP TABLE IF EXISTS "clubPostsDislikes" CASCADE;
DROP TABLE IF EXISTS "clubPosts" CASCADE;
DROP TABLE IF EXISTS "clubRequests" CASCADE;
DROP TABLE IF EXISTS "clubInvites" CASCADE;
DROP TABLE IF EXISTS "clubMembers" CASCADE;
DROP TABLE IF EXISTS "clubs" CASCADE;
DROP TABLE IF EXISTS "accountRequests" CASCADE;
DROP TABLE IF EXISTS "badges" CASCADE;
DROP TABLE IF EXISTS "badgeActions" CASCADE;
DROP TABLE IF EXISTS "badgeRules" CASCADE;
DROP TABLE IF EXISTS "userBadges" CASCADE;
DROP TABLE IF EXISTS "colours" CASCADE;
DROP TABLE IF EXISTS "countries" CASCADE;
DROP TABLE IF EXISTS "drinkTypes" CASCADE;
DROP TABLE IF EXISTS "flavourTags" CASCADE;
DROP TABLE IF EXISTS "languages" CASCADE;
DROP TABLE IF EXISTS "listings" CASCADE;
DROP TABLE IF EXISTS "menuItems" CASCADE;
DROP TABLE IF EXISTS "modRequests" CASCADE;
DROP TABLE IF EXISTS "observationTags" CASCADE;
DROP TABLE IF EXISTS "producerUpdateLikes" CASCADE;
DROP TABLE IF EXISTS "producers" CASCADE;
DROP TABLE IF EXISTS "producersProfileViews" CASCADE;
DROP TABLE IF EXISTS "producersOpeningHours" CASCADE;
DROP TABLE IF EXISTS "producersProfileViewsViews" CASCADE;
DROP TABLE IF EXISTS "producersQuestionAnswers" CASCADE;
DROP TABLE IF EXISTS "producersUpdates" CASCADE;
DROP TABLE IF EXISTS "requestEdits" CASCADE;
DROP TABLE IF EXISTS "requestInaccuracy" CASCADE;
DROP TABLE IF EXISTS "requestListings" CASCADE;
DROP TABLE IF EXISTS "reviews" CASCADE;
DROP TABLE IF EXISTS "reviewsUserVotes" CASCADE;
DROP TABLE IF EXISTS "producerReviews" CASCADE;
DROP TABLE IF EXISTS "producerReviewsUserVotes" CASCADE;
DROP TABLE IF EXISTS "servingTypes" CASCADE;
DROP TABLE IF EXISTS "specialColours" CASCADE;
DROP TABLE IF EXISTS "subTags" CASCADE;
DROP TABLE IF EXISTS "tokens" CASCADE;
DROP TABLE IF EXISTS "users" CASCADE;
DROP TABLE IF EXISTS "usersDrinkLists" CASCADE;
DROP TABLE IF EXISTS "usersDrinkListItems" CASCADE;
DROP TABLE IF EXISTS "usersFollowLists" CASCADE;
DROP TABLE IF EXISTS "venueUpdateLikes" CASCADE;
DROP TABLE IF EXISTS "venues" CASCADE;
DROP TABLE IF EXISTS "venuesMenu" CASCADE;
DROP TABLE IF EXISTS "venuesOpeningHours" CASCADE;
DROP TABLE IF EXISTS "venuesProfileViews" CASCADE;
DROP TABLE IF EXISTS "venuesProfileViewsViews" CASCADE;
DROP TABLE IF EXISTS "venuesQuestionAnswers" CASCADE;
DROP TABLE IF EXISTS "venuesUpdates" CASCADE;
DROP TABLE IF EXISTS "typeCategories" CASCADE;
DROP TABLE IF EXISTS "associations" CASCADE; -- ADDED BY SMU GROUP 3
DROP TABLE IF EXISTS "pointsRecorder" CASCADE; -- ADDED BY SMU GROUP 3
DROP TABLE IF EXISTS "pointSystemRules" CASCADE; -- ADDED BY SMU GROUP 3
DROP TABLE IF EXISTS "venueReviews" CASCADE;
DROP TABLE IF EXISTS "venueReviewsUserVotes" CASCADE;

-- CREATE TABLES -- 
-- ========= "accountRequests" =========
CREATE TABLE "accountRequests" (
    "id" SERIAL PRIMARY KEY,
    "businessId" INTEGER,
    "businessName" VARCHAR(255),
    "businessType" VARCHAR(255),
    "isIndependentBottler" BOOLEAN DEFAULT FALSE,
    "businessDesc" TEXT,
    "country" VARCHAR(255),
    "pricing" VARCHAR(255),
    "businessLink" VARCHAR(255),
    "firstName" VARCHAR(255),
    "lastName" VARCHAR(255),
    "relationship" VARCHAR(255),
    "email" VARCHAR(255),
    "contact" VARCHAR(255),
    "referenceDocument" TEXT,  -- Changed to TEXT
    "photo" TEXT,
    "joinDate" TIMESTAMP,
    "isPending" BOOLEAN,
    "isApproved" BOOLEAN,
    "isNew" BOOLEAN
);

-- ========= "servingTypes" =========
CREATE TABLE "servingTypes" (
    "id" SERIAL PRIMARY KEY,
    "servingType" VARCHAR(255)
);

-- ========= "specialColours" =========
CREATE TABLE "specialColours" (
    "id" SERIAL PRIMARY KEY,
    "hexList" TEXT[],
    "colour" VARCHAR(255)
);

-- ========= "flavourTags" =========
CREATE TABLE "flavourTags" (
    "id" SERIAL PRIMARY KEY,
    "hexcode" VARCHAR(7),
    "familyTag" VARCHAR(255)
);

-- ========= "subTags" =========
CREATE TABLE "subTags" (
    "id" SERIAL PRIMARY KEY,
    "familyTagId" INTEGER REFERENCES "flavourTags"("id") ON DELETE SET NULL, -- [!] reference "flavourTags" as FK
    "subTag" VARCHAR(255) UNIQUE
);

-- ========= "badges" =========
CREATE TABLE "badges" (
    "id" SERIAL PRIMARY KEY,
    "badgeName" VARCHAR(255),
    "badgePhoto" TEXT,
    "badgeDesc" TEXT,
    "badgeType" VARCHAR(50), -- 'Country', 'Category', 'Action'
    "relatedEntity" VARCHAR(255) NULL, -- Stores country name, drink category, or action type
    "badgeLevel" INTEGER DEFAULT 1
);

-- ========= "userBadges" =========
CREATE TABLE "userBadges" (
    "id" SERIAL PRIMARY KEY,
    "userId" INTEGER REFERENCES "users"("id") ON DELETE CASCADE,
    "badgeId" INTEGER REFERENCES "badges"("id") ON DELETE CASCADE,
    "currentLevel" INTEGER DEFAULT 1,
    "currentProgress" INTEGER DEFAULT 0, -- Progress toward next level
    "dateEarned" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    "lastUpdated" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE("userId", "badgeId")
);

-- ========= "badgeRules" =========
CREATE TABLE "badgeRules" (
    "id" SERIAL PRIMARY KEY,
    "actionType" VARCHAR(50) NOT NULL, -- 'Country', 'Category', 'Action'
    "levelStart" INTEGER NOT NULL,
    "levelEnd" INTEGER NOT NULL,
    "actionsRequired" INTEGER NOT NULL -- Number of actions needed for levels in this range
);

-- ========= "badgeActions" =========
CREATE TABLE "badgeActions" (
    "id" SERIAL PRIMARY KEY,
    "userId" INTEGER REFERENCES "users"("id") ON DELETE CASCADE,
    "actionType" VARCHAR(100) NOT NULL, -- 'Review', 'ExtensiveReview', 'PhotoAttached', etc.
    "entityId" INTEGER NULL, -- Related entity ID (review ID, post ID, etc.)
    "entityType" VARCHAR(100) NULL, -- Type of entity ('review', 'comment', 'post', etc.)
    "relatedEntity" VARCHAR(255) NULL, -- For country/category badges (country name, category name)
    "createdDate" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ========= "colours" =========
CREATE TABLE "colours" (
    "id" SERIAL PRIMARY KEY,
    "hexcode" VARCHAR(7)
);

-- ========= "countries" =========
CREATE TABLE "countries" (
    "id" SERIAL PRIMARY KEY,
    "originCountry" VARCHAR(255),
    "legalAge" INT
);

-- ========= "drinkTypes" =========
CREATE TABLE "drinkTypes" (
    "id" SERIAL PRIMARY KEY,
    "drinkType" VARCHAR(255),
    "badgePhoto" TEXT,
    "typeCategory" TEXT[]
);

-- ========= "typeCategories" -added by tzh for drinkStyle =========
CREATE TABLE "typeCategories" (
    "id" SERIAL PRIMARY KEY,
    "drinkType_id" INT REFERENCES "drinkTypes"(id) ON DELETE CASCADE,
    "typeCategory" VARCHAR(255) NOT NULL,
    "drinkStyle" TEXT[],
    UNIQUE("drinkType_id", "typeCategory") 
);

-- ========= "languages" =========
CREATE TABLE "languages" (
    "id" SERIAL PRIMARY KEY,
    "language" VARCHAR(255)
);

-- ========= "observationTags" =========
CREATE TABLE "observationTags" (
    "id" SERIAL PRIMARY KEY,
    "observationTag" VARCHAR(255)
);

-- ========= "producers" =========
CREATE TABLE "producers" (
    "id" SERIAL PRIMARY KEY,
    "producerName" VARCHAR(255),
    "producerDesc" TEXT,
    "originCountry" VARCHAR(255),
    "isIndependentBottler" BOOLEAN DEFAULT FALSE,
    "mainDrinks" TEXT[],
    "photo" TEXT,
    "hashedPassword" VARCHAR(255),
    "claimStatus" BOOLEAN,
    "claimStatusCheckDate" TIMESTAMP,
    "statusOB" VARCHAR(255),
    "yearFounded" INTEGER,
    "activeStatus" VARCHAR(10),
    "owner" VARCHAR(255),
    "location" VARCHAR(255),
    "openForTours" BOOLEAN,
    "website" TEXT,
    -- "questionAnswers" INTEGER REFERENCES "producersQuestionAnswers"("id") ON DELETE SET NULL, -- Alternative ON DELETE CASCADE to delete all related child records[!] reference "producersQuestionAnswers" as FK
    -- "updates" INTEGER REFERENCES "producersUpdates"("id") ON DELETE SET NULL, -- Alternative ON DELETE CASCADE to delete all related child records[!] reference "producersUpdates" as FK
    "username" VARCHAR(255),
    "producerLink" TEXT,
    "stripeCustomerId" VARCHAR(255)
);

-- ========= "venues" =========
CREATE TABLE "venues" (
    "id" SERIAL PRIMARY KEY,
    "venueName" VARCHAR(255),
    "address" VARCHAR(255),
    "venueType" VARCHAR(255),
    "originLocation" VARCHAR(255),
    "venueDesc" TEXT,
    -- "menu" SERIAL, -- [!] reference "venuesMenu"
    "hashedPassword" VARCHAR(255),
    "photo" TEXT,
    "claimStatus" BOOLEAN,
    "claimStatusCheckDate" TIMESTAMP,
    "yearOpened" INTEGER,
    "openForReservations" BOOLEAN,
    "website" TEXT,
    -- "openingHours" SERIAL, -- [!] reference "venuesOpeningHours"
    -- "questionAnswers" SERIAL, -- [!] reference "venuesQuestionAnswers"
    -- "updates" SERIAL, -- [!] reference "venuesUpdates"
    "reservationDetails" VARCHAR(255),
    "username" VARCHAR(255),
    "publicHolidays" VARCHAR(255),
    "stripeCustomerId" VARCHAR(255),
    "pin" VARCHAR(255)
);

-- ========= "users" =========
CREATE TABLE "users" (
    "id" SERIAL PRIMARY KEY,
    "username" VARCHAR(255),
    "displayName" VARCHAR(255),
    "choiceDrinks" TEXT[],
    "modType" TEXT[],
    "photo" TEXT,
    "hashedPassword" VARCHAR(255),
    -- "drinkLists" SERIAL, -- [!] reference "usersDrinkLists" not needed since user followlist ref users
    "joinDate" TIMESTAMP,
    -- "followLists" SERIAL, -- [!] reference "usersFollowLists"
    "firstName" VARCHAR(255),
    "lastName" VARCHAR(255),
    "email" VARCHAR(255),
    "isAdmin" BOOLEAN,
    "birthday" TIMESTAMP,
    "pin" VARCHAR(255),
    "choiceFlavours" TEXT[], -- SMU Group 3 added in "choiceFlavours"
    "preferences" TEXT[],-- SMU Group 3 added in "preferences"
    "grails" TEXT[], -- SMU Group 3 added in "grails"
    "upAndComing" TEXT[], -- SMU Group 3 added in "upAndComing"
    "goats" TEXT[] -- SMU Group 3 added in "goats"
);

-- ========= [NEW!] "producersQuestionAnswers" =========
CREATE TABLE "producersQuestionAnswers" (
    "id" SERIAL PRIMARY KEY,
    "question" VARCHAR(255),
    "answer" VARCHAR(255),
    "date" TIMESTAMP,
    "userId" INTEGER REFERENCES "users"("id") ON DELETE SET NULL, -- [!] reference "users"("id")
    "producerId" INTEGER REFERENCES "producers"("id") ON DELETE SET NULL -- [!] reference "producers"("id")
);

-- ========= [NEW!] "producersUpdates" =========
CREATE TABLE "producersUpdates" (
    "id" SERIAL PRIMARY KEY,
    "date" TIMESTAMP,
    "text" VARCHAR(255),
    "photo" TEXT,
    "producerId" INTEGER REFERENCES "producers"("id") ON DELETE SET NULL
    -- need to add likes?
);

-- ========= [NEW!] "producerUpdateLikes" =========
CREATE TABLE "producerUpdateLikes" (
    "id" SERIAL PRIMARY KEY,
    "updateId" INTEGER REFERENCES "producersUpdates"("id") ON DELETE CASCADE,
    "userId" INTEGER,
    "userType" VARCHAR(50)
);

-- ========= "producersProfileViews" =========
CREATE TABLE "producersProfileViews" (
    "id" SERIAL PRIMARY KEY,
    "date" TIMESTAMP, 
    "count" INTEGER, -- do i need this?
    "producerId" INTEGER REFERENCES "producers"("id") ON DELETE SET NULL -- [!] reference "producers" FK
    -- "views" INTEGER REFERENCES "producersProfileViewsViews"("id") ON DELETE SET NULL  -- [!] reference "producersProfileViewsViews" FK
);

-- ========= "producersOpeningHours" =========
CREATE TABLE "producersOpeningHours" (
    "id" SERIAL PRIMARY KEY,
    "Monday" TEXT[],
    "Tuesday" TEXT[],
    "Wednesday" TEXT[],
    "Thursday" TEXT[],
    "Friday" TEXT[],
    "Saturday" TEXT[],
    "Sunday" TEXT[],
    "producerId" INTEGER REFERENCES "producers"("id") ON DELETE SET NULL -- [!] reference "producers" FK
);

-- -- ========= [NEW!] "producersProfileViewsViews" =========
-- CREATE TABLE "producersProfileViewsViews" (
--     "id" SERIAL PRIMARY KEY,
--     "date" TIMESTAMP,
--     "count" INTEGER,
--     "producersProfileViewsId" INTEGER REFERENCES "producersProfileViews"("id"),
--     "producerId" INTEGER REFERENCES "producers"("id") ON DELETE SET NULL, -- [!] reference "producers" FK
-- );

-- ========= "listings" =========
CREATE TABLE "listings" (
    "id" SERIAL PRIMARY KEY,
    "listingName" VARCHAR(500),
    "producerID" INTEGER REFERENCES "producers"("id") ON DELETE SET NULL, -- [!] reference "producers" FK
    "bottler" VARCHAR(255),
    "bottlerID" INTEGER REFERENCES "producers"("id") ON DELETE SET NULL, -- [!] reference "producers" FK
    "originCountry" VARCHAR(255),
    "drinkType" VARCHAR(255),
    "abv" FLOAT,
    "officialDesc" TEXT,
    "allowMod" BOOLEAN,
    "addedDate" TIMESTAMP,
    "typeCategory" VARCHAR(255),
    "age" VARCHAR(500),
    "reviewLink" VARCHAR(255),
    "sourceLink" VARCHAR(255),
    "photo" TEXT,
    "drinkStyle" VARCHAR(255) -- added by tzh 
);

-- ========= "modRequests" =========
CREATE TABLE "modRequests" (
    "id" SERIAL PRIMARY KEY,
    "userID" INTEGER REFERENCES "users"("id") ON DELETE SET NULL,
    "drinkType" VARCHAR(255),
    "modDesc" TEXT,
    "reviewStatus" BOOLEAN
);

-- ========= [NEW!] "usersFollowLists" =========
CREATE TABLE "usersFollowLists" (
    "id" SERIAL PRIMARY KEY, 
    "userId" INTEGER REFERENCES "users"("id") ON DELETE SET NULL, -- [!] reference "users"("id")
    "users" TEXT[], -- Contains "users"("id")s
    "producers" TEXT[], -- Contains "producers"("id")s
    "venues" TEXT[] -- Contains "venues"("id")s
);

-- ========= [NEW!] "usersDrinkLists" =========
CREATE TABLE "usersDrinkLists" (
    "id" SERIAL PRIMARY KEY,
    "userId" INTEGER REFERENCES "users"("id") ON DELETE SET NULL,  -- [!] reference "users" FK
    "listName" TEXT,
    -- "drinks" TEXT[],-- Contains "listings"("id")s
    UNIQUE ("userId", "listName")
);

-- ========= [NEW!] "usersDrinkListItems" =========
CREATE TABLE "usersDrinkListItems" (
    "id" SERIAL PRIMARY KEY,
    "listId" INTEGER REFERENCES "usersDrinkLists"("id") ON DELETE CASCADE, -- [!] reference "usersDrinkLists" FK
    "drinkId" INTEGER REFERENCES "listings"("id") ON DELETE CASCADE,
    "addedDate" TIMESTAMP,
    UNIQUE ("listId", "drinkId")
);

-- ========= "reviews" =========
CREATE TABLE "reviews" (
    "id" SERIAL PRIMARY KEY,
    "userID" INTEGER REFERENCES "users"("id") ON DELETE SET NULL, -- [!] reference "users"("id")
    "reviewTarget" INTEGER REFERENCES "listings"("id") ON DELETE SET NULL, -- [!] reference "listings"("id")
    "rating" DECIMAL(3,1),
    "reviewDesc" TEXT,
    "reviewType" VARCHAR(255),
    "createdDate" TIMESTAMP,
    "language" VARCHAR(255),
    "finish" VARCHAR(255),
    "willRecommend" BOOLEAN NULL,
    "wouldBuyAgain" BOOLEAN NULL,
    -- "userVotes" SERIAL, -- [!] reference "reviewsUserVotes" FK
    "taggedUsers" TEXT[], -- Contains "users"("id")s
    "flavourTag" TEXT[], -- Contains "flavourTags"("id")s
    "photo" TEXT,
    "colour" VARCHAR(7),
    "aroma" VARCHAR(255),
    "location" INTEGER REFERENCES "venues"("id") ON DELETE SET NULL, -- [!] references "venues" FK
    "taste" VARCHAR(255),
    "observationTag" TEXT[], -- Contains "observationTags"("id")s
    "address" VARCHAR(255)
);

-- ========= [NEW!] "reviewsUserVotes" =========
CREATE TABLE "reviewsUserVotes" (
    "id" SERIAL PRIMARY KEY,
    "upvotes" JSONB DEFAULT '[]', -- Contains "users"("id")s and date
    "downvotes" JSONB DEFAULT '[]', -- Contains "users"("id")s and date
    "reviewId" INTEGER REFERENCES "reviews"("id") on DELETE SET NULL -- [!] reference "reviews" FK
);

CREATE TABLE "producerReviews" (
    "id" SERIAL PRIMARY KEY,
    "userID" INTEGER REFERENCES "users"("id") ON DELETE SET NULL, -- Reference to users table
    "producerID" INTEGER REFERENCES "producers"("id") ON DELETE SET NULL, -- Reference to producers table
    "rating" DECIMAL(3,1),
    "reviewDesc" TEXT,
    "createdDate" TIMESTAMP,
    "photos" TEXT[]
    -- "userVotes" SERIAL, -- [!] reference "producerReviewsUserVotes" FK
);

CREATE TABLE "producerReviewsUserVotes" (
    "id" SERIAL PRIMARY KEY,
    "upvotes" TEXT[], -- Contain "users"("id")s
    "downvotes" TEXT[], -- Contain "users"("id")s
    "reviewId" INTEGER REFERENCES "producerReviews"("id") on DELETE SET NULL -- [!] reference "producerReviews" FK
);

-- ==========================================
-- VENUE REVIEWS
-- ==========================================
CREATE TABLE "venueReviews" (
    "id" SERIAL PRIMARY KEY,
    "userID" INTEGER REFERENCES "users"("id") ON DELETE SET NULL,
    "venueID" INTEGER REFERENCES "venues"("id") ON DELETE SET NULL,
    "rating" DECIMAL(3,1),
    "reviewDesc" TEXT,
    "createdDate" TIMESTAMP,
    "photos" TEXT[]
);

-- ==========================================
-- VENUE REVIEWS USER VOTES
-- ==========================================
CREATE TABLE "venueReviewsUserVotes" (
    "id" SERIAL PRIMARY KEY,
    "upvotes" TEXT[], -- Contain "users"("id")s
    "downvotes" TEXT[], -- Contain "users"("id")s
    "reviewId" INTEGER REFERENCES "venueReviews"("id") ON DELETE SET NULL    
);


-- ========= "tokens" =========
CREATE TABLE "tokens" (
    "id" SERIAL PRIMARY KEY,
    "token" VARCHAR(255),
    "userId" INTEGER REFERENCES "users"("id") ON DELETE SET NULL, -- [!] reference "users" FK
    "producerId" INTEGER REFERENCES "producers"("id") ON DELETE SET NULL, -- [!] reference "producers" FK
    "venueId" INTEGER REFERENCES "venues"("id") ON DELETE SET NULL, -- [!] reference "venues" FK
    "requestId" INTEGER REFERENCES "accountRequests"("id") ON DELETE SET NULL, -- [!] reference "accountRequests" FK
    "expiry" TIMESTAMP
);

-- ========= [NEW!] "venuesMenu" =========
CREATE TABLE "venuesMenu" (
    "id" SERIAL PRIMARY KEY,
    "sectionName" VARCHAR(255),
    "sectionOrder" VARCHAR(255),
    -- "sectionMenu" TEXT[], -- [!] Contains listings(id)
    "venueId" INTEGER REFERENCES "venues"("id") ON DELETE SET NULL -- [!] References venues FK
);

-- ========= [NEW] "menuItems" =========
CREATE TABLE "menuItems" (
    "id" SERIAL PRIMARY KEY,
    "itemOrder" INTEGER,
    "itemPrice" DECIMAL(10,2),
    "itemAvailability" BOOLEAN,
    "itemID" INTEGER REFERENCES "listings"("id") ON DELETE SET NULL,
    "itemServingType" INTEGER REFERENCES "servingTypes"("id") ON DELETE SET NULL,
    "sectionId" INTEGER REFERENCES "venuesMenu"("id") ON DELETE CASCADE
);

-- ========= [NEW!] "venuesOpeningHours" =========
CREATE TABLE "venuesOpeningHours" (
    "id" SERIAL PRIMARY KEY,
    "Monday" TEXT[],
    "Tuesday" TEXT[],
    "Wednesday" TEXT[],
    "Thursday" TEXT[],
    "Friday" TEXT[],
    "Saturday" TEXT[],
    "Sunday" TEXT[],
    "venueId" INTEGER REFERENCES "venues"("id") ON DELETE SET NULL -- [!] References venues FK
);

-- ========= [NEW!] "venuesQuestionAnswers" =========
CREATE TABLE "venuesQuestionAnswers" (
    "id" SERIAL PRIMARY KEY,
    "question" VARCHAR(255),
    "answer" VARCHAR(255),
    "date" TIMESTAMP,
    "userId" INTEGER REFERENCES "users"("id") ON DELETE SET NULL,
    "venueId" INTEGER REFERENCES "venues"("id") ON DELETE SET NULL -- [!] References venues FK
);

-- ========= [NEW!] "venuesUpdates" =========
CREATE TABLE "venuesUpdates" (
    "id" SERIAL PRIMARY KEY,
    "date" TIMESTAMP,
    "text" VARCHAR(255),
    "photo" TEXT,
    "venueId" INTEGER REFERENCES "venues"("id") ON DELETE SET NULL -- [!] References venues FK
    -- need add likes?
);

-- ========= [NEW!] "venueUpdateLikes" =========
CREATE TABLE "venueUpdateLikes" (
    "id" SERIAL PRIMARY KEY,
    "updateId" INTEGER REFERENCES "venuesUpdates"("id") ON DELETE CASCADE,
    "userId" INTEGER,
    "userType" VARCHAR(50)
);

-- -- ========= [NEW!] "venuesProfileViewsViews" =========
-- CREATE TABLE "venuesProfileViewsViews" (
--     "id" SERIAL PRIMARY KEY,
--     "date" TIMESTAMP,
--     "count" INT
-- );

-- ========= [NEW!] "venuesProfileViews" =========
CREATE TABLE "venuesProfileViews" (
    "id" SERIAL PRIMARY KEY,
    "date" TIMESTAMP,
    "count" INT,
    "venueId" INTEGER REFERENCES "venues"("id") ON DELETE SET NULL -- [!] References venues FK
);

-- -- ========= "venuesProfileViews" =========
-- CREATE TABLE "venuesProfileViews" (
--     "id" SERIAL PRIMARY KEY,
--     "venueId" INT, -- [!] FK VENUES
--     "views" TEXT[] -- [!] reference venuesProfileViewsViews FK
--     "venueId" INTEGER REFERENCES "venues"("id") ON DELETE SET NULL -- [!] References venues FK
-- );

-- ========= "requestInaccuracy" =========
CREATE TABLE "requestInaccuracy" (
    "id" SERIAL PRIMARY KEY,
    "listingId" INTEGER REFERENCES "listings"("id") ON DELETE SET NULL, -- [!] References listings FK
    "userId" INTEGER REFERENCES "users"("id") ON DELETE SET NULL, -- [!] References users FK
    "venueId" INTEGER REFERENCES "venues"("id") ON DELETE SET NULL, -- [!] References venues FK
    "reportDate" TIMESTAMP,
    "inaccurateReason" TEXT,
    "reviewStatus" BOOLEAN 
);

-- ========= "requestListings" =========
CREATE TABLE "requestListings" (
    "id" SERIAL PRIMARY KEY,
    "listingName" VARCHAR(255),
    "bottler" VARCHAR(255), 
    "drinkType" VARCHAR(255),
    "sourceLink" VARCHAR(255),
    "brandRelation" VARCHAR(255),
    "reviewStatus" BOOLEAN,
    "userID" INTEGER REFERENCES "users"("id") ON DELETE SET NULL, -- [!] References users FK
    "photo" TEXT,
    "originCountry" VARCHAR(255),
    "producerID" INTEGER REFERENCES "producers"("id") ON DELETE SET NULL, -- [!] References producers FK
    "bottlerID" INTEGER REFERENCES "producers"("id") ON DELETE SET NULL, -- [!] References producers FK
    "producerNew" VARCHAR(255),
    "typeCategory" VARCHAR(255),
    "abv" VARCHAR(255),
    "age" VARCHAR(255),
    "reviewLink" VARCHAR(255),
    "drinkStyle" VARCHAR(255) -- added by tzh 
);

-- ========= "requestEdits" =========
CREATE TABLE "requestEdits" (
    "id" SERIAL PRIMARY KEY,
    "editDesc" TEXT,
    "listingID" INTEGER REFERENCES "listings"("id") ON DELETE SET NULL, -- [!] References listings FK
    "userID" INTEGER REFERENCES "users"("id") ON DELETE SET NULL, -- [!] References users FK
    "brandRelation" VARCHAR(255),
    "reviewStatus" BOOLEAN,
    "duplicateLink" VARCHAR(255),
    "sourceLink" VARCHAR(255)
);

-- ========= "clubs" =========
CREATE TABLE "clubs" (
    "id" SERIAL PRIMARY KEY,
    "clubName" VARCHAR(255),
    "clubDesc" TEXT,
    "isInviteOnly" BOOLEAN,
    "clubLink" VARCHAR(255),
    "clubBanner" TEXT,
    "dateCreated" TIMESTAMP,
    "totalMembers" INTEGER,
    "createdByID" INTEGER, -- [!] "producers" or "venues" or "users" id in their respective tables
    "createdByType" VARCHAR(255) -- [!] "producers" or "venues" or "users"
);

-- ========= "clubMembers" =========
CREATE TABLE "clubMembers" (
    "id" SERIAL PRIMARY KEY,
    "clubID" INTEGER REFERENCES "clubs"("id") ON DELETE SET NULL, -- [!] References clubs FK
    "userID" INTEGER,
    "userType" VARCHAR(255),
    "joinDate" TIMESTAMP,
    "isAdmin" BOOLEAN
);

-- ========= "clubInvites" =========
CREATE TABLE "clubInvites" (
    "id" SERIAL PRIMARY KEY,
    "clubID" INTEGER REFERENCES "clubs"("id") ON DELETE SET NULL, -- [!] References clubs FK
    "inviteeID" INTEGER,
    "inviteeUserType" VARCHAR(255),
    "inviterID" INTEGER,
    "inviterUserType" VARCHAR(255),
    "inviteDate" TIMESTAMP
);

-- ========= "clubRequests" =========
CREATE TABLE "clubRequests" (
    "id" SERIAL PRIMARY KEY,
    "clubID" INTEGER REFERENCES "clubs"("id") ON DELETE SET NULL, -- [!] References clubs FK
    "userID" INTEGER,
    "userType" VARCHAR(255),
    "requestDate" TIMESTAMP
);

-- ========= "clubPosts" =========
CREATE TABLE "clubPosts" (
    "id" SERIAL PRIMARY KEY,
    "clubID" INTEGER REFERENCES "clubs"("id") ON DELETE SET NULL, -- [!] References clubs FK
    "postDate" TIMESTAMP,
    "postContent" TEXT,
    "postPhotos" TEXT[],
    "posterID" INTEGER REFERENCES "clubMembers"("id") ON DELETE SET NULL -- [!] References clubMembers FK
);

-- ========= "clubPostsLikes" =========
CREATE TABLE "clubPostsLikes" (
    "id" SERIAL PRIMARY KEY,
    "clubID" INTEGER REFERENCES "clubs"("id") ON DELETE SET NULL, -- [!] References clubs FK
    "postID" INTEGER REFERENCES "clubPosts"("id") ON DELETE SET NULL, -- [!] References clubPOsts FK
    "memberID" INTEGER REFERENCES "clubMembers"("id") ON DELETE SET NULL -- [!] References clubMembers FK
);

-- ========= "clubPostsDislikes" =========
 CREATE TABLE "clubPostsDislikes" (
     "id" SERIAL PRIMARY KEY,
     "clubID" INTEGER REFERENCES "clubs"("id") ON DELETE SET NULL, -- [!] References clubs FK
     "postID" INTEGER REFERENCES "clubPosts"("id") ON DELETE SET NULL, -- [!] References clubPOsts FK
     "memberID" INTEGER REFERENCES "clubMembers"("id") ON DELETE SET NULL -- [!] References clubMembers FK
 );

-- ========= "clubPostComments" =========
CREATE TABLE "clubPostComments" (
    "id" SERIAL PRIMARY KEY,
    "postID" INTEGER REFERENCES "clubPosts"("id") ON DELETE SET NULL, -- [!] References clubPosts FK
    "commentDate" TIMESTAMP,
    "commentContent" TEXT,
    "commenterID" INTEGER REFERENCES "clubMembers"("id") ON DELETE SET NULL -- [!] References clubMembers FK
);

-- ========= "clubPostCommentsLikes" =========
CREATE TABLE "clubPostCommentsLikes" (
    "id" SERIAL PRIMARY KEY,
    "postID" INTEGER REFERENCES "clubPosts"("id") ON DELETE CASCADE, -- Automatically delete when clubPosts record is deleted
    "commentID" INTEGER REFERENCES "clubPostComments"("id") ON DELETE SET NULL, -- Keep as SET NULL if needed
    "memberID" INTEGER REFERENCES "clubMembers"("id") ON DELETE SET NULL -- Keep as SET NULL if needed
);

-- ========= "clubPostCommentsDislikes" =========
CREATE TABLE "clubPostCommentsDislikes" (
    "id" SERIAL PRIMARY KEY,
    "postID" INTEGER REFERENCES "clubPosts"("id") ON DELETE CASCADE, -- Automatically delete when clubPosts record is deleted
    "commentID" INTEGER REFERENCES "clubPostComments"("id") ON DELETE SET NULL, -- Keep as SET NULL if needed
    "memberID" INTEGER REFERENCES "clubMembers"("id") ON DELETE SET NULL -- Keep as SET NULL if needed
);

-- ========= "events" =========
CREATE TABLE "events" (
    "id" SERIAL PRIMARY KEY,
    "eventName" VARCHAR(255),
    "eventDesc" TEXT,
    "eventType" VARCHAR(255),
    "eventStartDate" DATE,
    "eventEndDate" DATE,
    "eventStartTime" TIME,
    "eventEndTime" TIME,
    "eventLimit" INTEGER,
    "eventBanners" TEXT[],
    "ticketed" BOOLEAN,
    "paidEvent" BOOLEAN,
    "eventLocation" TEXT,
    "paymentLink" VARCHAR(255),
    "eventOwnerID" INTEGER, -- [!] "producers" or "venues" or "users" id in their respective tables 
    "eventOwnerType" VARCHAR(255), -- [!] "producers" or "venues" or "users"
    "numAttendees" INTEGER,
    "createdDate" TIMESTAMP
);

-- ========= "eventAttendees" =========
CREATE TABLE "eventAttendees" (
    "id" SERIAL PRIMARY KEY,
    "eventID" INTEGER REFERENCES "events"("id") ON DELETE SET NULL, -- [!] References events FK
    "eventDate" DATE,
    "eventStartTime" TIME,
    "userID" INTEGER,
    "attendeeType" VARCHAR(255),
    "attendeeStatus" BOOLEAN
);

-- ========= [NEW!] "associations" - by SMU GROUP 3 =========
CREATE TABLE "associations" (
    "id" SERIAL PRIMARY KEY,
    "subTag1" VARCHAR(255) REFERENCES "subTags"("subTag") ON DELETE SET NULL, -- [!] References subTags FK
    "subTag2" VARCHAR(255) REFERENCES "subTags"("subTag") ON DELETE SET NULL -- [!] References subTags FK
);

-- ======== [NEW!] "pointsRecorder" - by SMU GROUP 3 =========
CREATE TABLE "pointsRecorder" (
    "id" SERIAL PRIMARY KEY,
    "userID" INTEGER,
    "userType" VARCHAR(255),
    "currentPoints" INTEGER
);

-- ========= [NEW!] "pointSystemRules" - by SMU GROUP 3 =========
CREATE TABLE "pointSystemRules" (
    "id" SERIAL PRIMARY KEY,
    "ruleName" VARCHAR(255),
    "ruleDesc" TEXT,
    "ruleCategory" VARCHAR(255),
    "proofPoints" INTEGER
);