<!-- HTML -->
<template>
    <NavBar />

    <!-- Display when data is still loading -->
    <div class="text-info-emphasis fst-italic fw-bold fs-5 pt-5" v-if="dataLoaded == false">
        <span>Loading dashboard, please wait...</span>
        <br><br>
        <div class="spinner-border" role="status">
            <span class="visually-hidden">Loading...</span>
        </div>
    </div>

    <!-- Display when data fails to load -->
    <div class="text-danger fst-italic fw-bold fs-3 pt-5" v-if="dataLoaded == null"> 
        <span>An error occurred while loading this page, please try again!</span>
        <br>
        <button class="btn primary-btn btn-sm" @click="this.$router.go(-1)">
            <span class="fs-5 fst-italic"> Return to previous page </span>
        </button>
        <router-link :to="'/'" class="mx-1">
            <button class="btn primary-btn btn-sm">
                <span class="fs-5 fst-italic"> Go to Home page </span>
            </button>
        </router-link>
    </div>

    <!-- main content -->

    <div v-if="user && dataLoaded" class="userprofile mt-5 mobile-mt-3">

        <div class="container text-start">

            <div class="row">

            <!-- left pane -->
            <div class="col-lg-4 col-md-12 col-sm-12">
                <div class="container">
                    <!-- row 1: producer info -->
                    <div class="row">
                        <!-- producer profile photo -->
                        <div class="col-4 text-start pe-0">
                            <!-- <img :src="selectedImage || 'data:image/jpeg;base64,' + (user['photo'] || defaultProfilePhoto)" 
                                alt="" style="width: 100px; height: auto; z-index: 1;" class="rounded-circle-no-bg border border-dark profile-img"> -->
                            <img :src="selectedImage || (user['photo'] || defaultProfilePhoto)" 
                                alt="" style="width: 100px; height: auto; z-index: 1;" class="rounded-circle-no-bg border border-dark profile-img">
                        </div>
                        <!-- producer name -->
                        <div class="col-8 text-start">
                            <h3 class="mb-1"> {{ user.displayName }} </h3>
                            <!--<b>@{{ user.username }}</b>-->
                            {{ drinkCount }} Drinks Tasted 
                            <br>
                            {{ followerCount }} Followers
                            <br>
                            {{ totalBadges }} Badges Unlocked
                        </div>
                    </div>

                    <!-- row 2: return to profile -->
                    <div class="row pt-3 mobile-view-hide">
                        <button type="button" class="btn primary-btn-outline-thick rounded-0 default-clickable-text" v-on:click="goBack()"> 
                            Return to profile 
                        </button>
                    </div>
                    
                    <!-- badges -->
                    <div class="mt-3">
                        <h3 class="mobile-view-hide">Badges Unlocked</h3>
                        <p class="mobile-view-show"><strong>Badges Unlocked</strong></p>
                        <!--<hr>-->

                        <div v-if="topCategoriesReviewed.length == 0 && otherBadges.length == 0">
                            You have no badges yet.
                        </div>

                        <div v-else class="container text-center mb-3">
                            <!-- badges for different drink types -->
                            <div class="row">
                                <div class="mobile-col-3 col-12 col-sm-4 col-md-6 col-xl-4 p-2 mobile-pt-0 mobile-pb-0 mobile-pe-2 mobile-mb-2 " v-for="drinkTypeDetails in matchedDrinkTypes" :key="drinkTypeDetails._id">
                                    <!-- image of actual badge  style="width: 100px; height: 100px;"  -->
                                    <!-- <img :src="'data:image/png;base64,'+ (drinkTypeDetails.badgePhoto || defaultProfilePhoto)" 
                                        alt="" class="rounded-circle-white-bg border border-dark badge-img"> -->
                                    <img :src="(drinkTypeDetails.badgePhoto || defaultProfilePhoto)" 
                                        alt="" class="rounded-circle-white-bg border border-dark badge-img">
                                    <!-- badge description -->
                                    <div class="pt-1" style="line-height: 1;"> 
                                        <small> 
                                            <b> {{ drinkTypeDetails.drinkType }} {{ categoryBadges[drinkTypeDetails.drinkType] }} </b>
                                        </small>
                                        <br>
                                        <small class="xs-text" v-for="(subcategory, category) of topSubcategoriesReviewed" :key="category">
                                            <span v-if="category === drinkTypeDetails.drinkType">
                                                <i>
                                                    (Power: <span v-for="item in subcategory" :key="item">
                                                        {{ item }}<span v-if="subcategory.indexOf(item) !== subcategory.length - 1">, </span>
                                                    </span>)
                                                </i>
                                            </span>
                                        </small>
                                    </div>
                                </div>
                            </div>
                            <!-- badges based on other user activities -->
                            <div class="row">
                                <div class="mobile-col-3 col-12 col-sm-4 col-md-6 col-xl-4 p-2 mobile-pt-0 mobile-pb-0 mobile-pe-2 mobile-mb-2" v-for="badge in otherBadges" :key="badge">
                                    <!-- image of actual badge style="width: 100px; height: 100px;" -->
                                    <!-- <img :src="'data:image/png;base64,'+ (getBadgeInfo(badge).badgePhoto)" 
                                        alt="" class="rounded-circle-white-bg border border-dark badge-img"> -->
                                    <img :src="(getBadgeInfo(badge).badgePhoto)" 
                                        alt="" class="rounded-circle-white-bg border border-dark badge-img">
                                    <!-- badge description -->
                                    <p class="pt-1" style="line-height: 1;"> 
                                        <small> 
                                            <b> {{ getBadgeInfo(badge).badgeDesc }} </b>
                                        </small> 
                                    </p>
                                </div>
                            </div>
                        </div>
                        
                        <div>
                            <a href="#" style="color: black">Learn more about badges.</a>
                        </div>

                    </div>

                    <!-- row 3: recent activity from followers mobile -->
                    <div class="row mobile-view-show ps-2 pe-2 mt-3">
                        <button v-if="showFollowerActivity"
                        type="button" 
                        class="active-toggle-producer-QnA tertiary-text pt-2 pb-2 border" 
                        data-bs-toggle="collapse" 
                        data-bs-target="#collapseFollowerActivity" 
                        aria-expanded="false" 
                        aria-controls="collapseFollowerActivity" 
                        style="font-weight:bold;"
                        @click="checkToShowFollowerActivity()">Follower Activity ↑</button>
                        <button v-else
                        type="button" 
                        class="primary-btn-less-round-green tertiary-text pt-2 pb-2 border" 
                        data-bs-toggle="collapse" 
                        data-bs-target="#collapseFollowerActivity" 
                        aria-expanded="false" 
                        aria-controls="collapseFollowerActivity" 
                        style="font-weight:bold;"
                        @click="checkToShowFollowerActivity()">Follower Activity ↓</button>
                        <div class="collapse pt-3 pe-0 ps-0" id="collapseFollowerActivity">
                            <div class="square primary-square rounded p-3 mb-3 text-start">
                            <!-- header text -->
                            <div class="square-inline pb-2">
                                <h4 class="square-inline text-start mr-auto"> Recent Activity from Your Followers </h4>
                            </div>
                            <!-- body -->
                            <div style="height: 85%;">
                                <div class="overflow-auto" style="max-height: 100%;">
                                    <!-- v-for loop here-->
                                    <div v-for="activity in recentFollowerActivity" v-bind:key="activity._id" class="py-2">
                                        <div v-if="activity.type === 'tag'">
                                            <i> 
                                                <router-link :to="{ path: '/profile/user/' + activity.userID }" class="reverse-clickable-text">
                                                    @<b> {{ getUserFromID(activity.userID).username }} </b>
                                                </router-link> 
                                                tagged you in a review on 
                                                <router-link :to="{ path: '/listing/view/' + activity.listingID }" class="reverse-clickable-text">
                                                    <u> {{ getListingFromID(activity.listingID).listingName }} </u>
                                                </router-link>
                                                {{ getTimeDifference(activity.date) }}
                                            </i>
                                        </div>
                                        <div v-else-if="activity.type === 'follow'">
                                            <i> 
                                                <router-link :to="{ path: '/profile/user/' + activity.userID }" class="reverse-clickable-text">
                                                    @<b> {{ activity.username }} </b>
                                                </router-link> 
                                                started following you
                                                {{ getTimeDifference(activity.date) }}
                                            </i>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            </div>
                        </div>    
                    </div>
                    <!-- row 3: recent activity from followers desktop -->
                    <div class="row pt-3 mobile-view-hide">
                        <div class="square primary-square-green rounded p-3 mb-3 text-start">
                            <!-- header text -->
                            <div class="square-inline pb-2">
                                <h4 class="square-inline text-start mr-auto"> Recent Activity from Your Followers </h4>
                            </div>
                            <!-- body -->
                            <div style="height: 85%;">
                                <div class="overflow-auto" style="max-height: 100%;">
                                    <!-- v-for loop here-->
                                    <div v-for="activity in recentFollowerActivity" v-bind:key="activity._id" class="py-2">
                                        <div v-if="activity.type === 'tag'">
                                            <i> 
                                                <router-link :to="{ path: '/profile/user/' + activity.userID }" class="reverse-clickable-text">
                                                    @<b> {{ getUserFromID(activity.userID).username }} </b>
                                                </router-link> 
                                                tagged you in a review on 
                                                <router-link :to="{ path: '/listing/view/' + activity.listingID }" class="reverse-clickable-text">
                                                    <u> {{ getListingFromID(activity.listingID).listingName }} </u>
                                                </router-link>
                                                {{ getTimeDifference(activity.date) }}
                                            </i>
                                        </div>
                                        <div v-else-if="activity.type === 'follow'">
                                            <i> 
                                                <router-link :to="{ path: '/profile/user/' + activity.userID }" class="reverse-clickable-text">
                                                    @<b> {{ activity.username }} </b>
                                                </router-link> 
                                                started following you
                                                {{ getTimeDifference(activity.date) }}
                                            </i>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- row 4: recent activity on reviews mobile -->
                    <div class="row pt-3 mobile-view-show ps-2 pe-2">
                        <button v-if="showReviewActivity"
                        type="button" 
                        class="active-toggle-producer-QnA tertiary-text pt-2 pb-2 border" 
                        data-bs-toggle="collapse" 
                        data-bs-target="#collapseReviewActivity" 
                        aria-expanded="false" 
                        aria-controls="collapseReviewActivity" 
                        style="font-weight:bold;"
                        @click="checkToShowReviewActivity()">Activity On Your Reviews ↑</button>
                        <button v-else
                        type="button" 
                        class="primary-btn-less-round-green tertiary-text pt-2 pb-2 border" 
                        data-bs-toggle="collapse" 
                        data-bs-target="#collapseReviewActivity" 
                        aria-expanded="false" 
                        aria-controls="collapseReviewActivity" 
                        style="font-weight:bold;"
                        @click="checkToShowReviewActivity()">Activity On Your Reviews ↓</button>
                        
                        <div class="mt-3 collapse square primary-square rounded p-3 mb-3 text-start" style="height: 325px;" id="collapseReviewActivity">
                            <div class="square-inline pb-2">
                                <h4 class="square-inline text-start mr-auto"> Recent Activity on Your Reviews </h4>
                            </div>
                            <!-- body -->
                            <div style="height: 85%;">
                                <div class="overflow-auto" style="max-height: 100%;">
                                    <!-- v-for loop here-->
                                    <div v-for="activity in recentReviewActivity" v-bind:key="activity._id" class="py-2">
                                        <div v-if="activity.type === 'upvote' || activity.type === 'downvote'">
                                            <svg v-if="activity.type == 'upvote'" fill="#ffffff" height="16" viewBox="0 0 24 24" width="16" xmlns="http://www.w3.org/2000/svg"><path d="m4 14h2 2v3 4c0 .553.447 1 1 1h6c.553 0 1-.447 1-1v-5-2h1 3c.385 0 .734-.221.901-.566.166-.347.12-.758-.12-1.059l-8-10c-.381-.475-1.181-.475-1.562 0l-8 10c-.24.301-.286.712-.12 1.059.167.345.516.566.901.566z"/></svg>
                                            <svg v-if="activity.type == 'downvote'" fill="#ffffff" height="16" viewBox="0 0 24 24" width="16" xmlns="http://www.w3.org/2000/svg"><path d="m20.901 10.566c-.167-.345-.516-.566-.901-.566h-2-2v-3-4c0-.553-.447-1-1-1h-6c-.553 0-1 .447-1 1v5 2h-1-3c-.385 0-.734.221-.901.566-.166.347-.12.758.12 1.059l8 10c.19.237.477.375.781.375s.591-.138.781-.375l8-10c.24-.301.286-.712.12-1.059z"/></svg>
                                            <i> 
                                                Someone <span :style="{ color: activity.type === 'upvote' ? '#90ee90' : '#ff7f7f' }">{{ activity.type }}d</span> your review on 
                                                <router-link :to="{ path: '/listing/view/' + activity.reviewTarget }" class="reverse-clickable-text">
                                                    <u> {{ getListingFromID(activity.reviewTarget).listingName }} </u>
                                                </router-link>
                                                {{ getTimeDifference(activity.date) }}
                                            </i>
                                        </div>
                                        <div v-else-if="activity.type === 'follow'">
                                            <i> 
                                                <router-link :to="{ path: '/profile/user/' + activity.userID }" class="reverse-clickable-text">
                                                    @<b> {{ activity.username }} </b>
                                                </router-link> 
                                                started following you
                                                {{ getTimeDifference(activity.date) }}
                                            </i>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- row 4: recent activity on reviews desktop -->
                    <div class="row pt-3 mobile-view-hide">
                        <div class="square primary-square-green rounded p-3 mb-3 text-start">
                            <!-- header text -->
                            <div class="square-inline pb-2">
                                <h4 class="square-inline text-start mr-auto"> Recent Activity on Your Reviews </h4>
                            </div>
                            <!-- body -->
                            <div style="height: 85%;">
                                <div class="overflow-auto" style="max-height: 100%;">
                                    <!-- v-for loop here-->
                                    <div v-for="activity in recentReviewActivity" v-bind:key="activity._id" class="py-2">
                                        <div v-if="activity.type === 'upvote' || activity.type === 'downvote'">
                                            <svg v-if="activity.type == 'upvote'" fill="#ffffff" height="16" viewBox="0 0 24 24" width="16" xmlns="http://www.w3.org/2000/svg"><path d="m4 14h2 2v3 4c0 .553.447 1 1 1h6c.553 0 1-.447 1-1v-5-2h1 3c.385 0 .734-.221.901-.566.166-.347.12-.758-.12-1.059l-8-10c-.381-.475-1.181-.475-1.562 0l-8 10c-.24.301-.286.712-.12 1.059.167.345.516.566.901.566z"/></svg>
                                            <svg v-if="activity.type == 'downvote'" fill="#ffffff" height="16" viewBox="0 0 24 24" width="16" xmlns="http://www.w3.org/2000/svg"><path d="m20.901 10.566c-.167-.345-.516-.566-.901-.566h-2-2v-3-4c0-.553-.447-1-1-1h-6c-.553 0-1 .447-1 1v5 2h-1-3c-.385 0-.734.221-.901.566-.166.347-.12.758.12 1.059l8 10c.19.237.477.375.781.375s.591-.138.781-.375l8-10c.24-.301.286-.712.12-1.059z"/></svg>
                                            <i> 
                                                Someone <span :style="{ color: activity.type === 'upvote' ? '#90ee90' : '#ff7f7f' }">{{ activity.type }}d</span> your review on 
                                                <router-link :to="{ path: '/listing/view/' + activity.reviewTarget }" class="reverse-clickable-text">
                                                    <u> {{ getListingFromID(activity.reviewTarget).listingName }} </u>
                                                </router-link>
                                                {{ getTimeDifference(activity.date) }}
                                            </i>
                                        </div>
                                        <div v-else-if="activity.type === 'follow'">
                                            <i> 
                                                <router-link :to="{ path: '/profile/user/' + activity.userID }" class="reverse-clickable-text">
                                                    @<b> {{ activity.username }} </b>
                                                </router-link> 
                                                started following you
                                                {{ getTimeDifference(activity.date) }}
                                            </i>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- right pane -->
            <div class="col-lg-8 col-md-12 col-sm-12 ps-lg-5">
                <!--mobile toggle buttons for graph tzh -->
                <ul class="nav nav-pills mobile-view-show pt-2"  role="tablist" >
                <hr>  
                    <li class="nav-item pe-2 pt-2 " role="presentation">
                        <button class="nav-link active"  data-bs-toggle="pill" data-bs-target="#countofreviews" type="button" role="tab" aria-controls="countofreviews" aria-selected="true">Count of Reviews</button>
                    </li>
                    <li class="nav-item pe-2 pt-2 " role="presentation">
                        <button class="nav-link "  data-bs-toggle="pill" data-bs-target="#spreadofratings" type="button" role="tab" aria-controls="spreadofratings" aria-selected="false">Spread of Ratings</button>
                    </li>
                </ul>

                    <!-- row 1: review of your expressions & profile visits -->
                    <div class="row mobile-view-show tab-content" >
                    
                        <!-- col 1: review of your expressions -->
                        <div id="countofreviews" class="tab-pane fade show active col-lg-5 col-md-12 col-sm-12 text-start pt-5 mobile-pt-3 mx-lg-3 ps-lg-0 pe-lg-0">
                            <Line :data="reviewsData" :options="chartOptions"></Line>
                        </div>

                        <!-- col 2: profile visits -->
                        <div id="spreadofratings" class="tab-pane fade col-lg-5 col-md-12 col-sm-12 text-start pt-5 mobile-pt-3 mx-lg-3 ps-lg-0 pe-lg-0">
                            
                            <Bar :data="ratingsData" :options="chartOptions" />
                        </div>
                        
                    </div>

                <ul class="nav nav-pills mobile-view-show pt-2"  role="tablist" >
                    <hr>
                <li class="nav-item pe-2 pt-2 " role="presentation">
                    <button class="nav-link active"  data-bs-toggle="pill" data-bs-target="#BestRatedExpressions" type="button" role="tab" aria-controls="BestRatedExpressions" aria-selected="true">Best Rated Drinks</button>
                </li>
                <li class="nav-item pe-2 pt-2 " role="presentation">
                    <button class="nav-link "  data-bs-toggle="pill" data-bs-target="#BestRatedCategories" type="button" role="tab" aria-controls="BestRatedCategories" aria-selected="false">Best Rated Categories</button>
                </li>
                </ul>    
                    <div style="min-height:450px;" class="row mobile-view-show tab-content">
                        <!-- col 1: your best rated drinks -->
                        <div id="BestRatedExpressions" class="tab-pane fade show active col-lg-5 col-md-12 col-sm-12 text-start pt-5 mx-3 ps-lg-0 pe-lg-0 mobile-mx-0">
                            <div class="text-start pb-2" v-for="listing in bestRatedListings" v-bind:key="listing._id">
                                <router-link :to="{ path: '/listing/view/' + listing.id }" class="reverse-clickable-text">
                                    <div class="d-flex align-items-center">
                                        <!-- <img :src="'data:image/png;base64,'+ (listing.photo || defaultProfilePhoto)" style="width: 70px; height: 70px;"> -->
                                        <img :src="(listing.photo || defaultProfilePhoto)" style="width: 70px; height: 70px;">
                                        <p class="ms-3 default-clickable-text"> 
                                            <b> {{ listing.listingName }} </b> 
                                            <br>
                                            {{ listing.rating || "-" }} 
                                            <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" fill="currentColor" class="bi bi-star-fill ms-1" viewBox="0 0 16 16">
                                                <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
                                            </svg>
                                        </p>
                                    </div>
                                </router-link>
                            </div>
                        </div>

                        <!-- col 2: your best rated categories -->
                        <div id="BestRatedCategories" class="tab-pane fade  col-lg-5 col-md-12 col-sm-12 text-start pt-5 mx-3 ps-lg-0 pe-lg-0 mobile-mx-0"> <!-- padding classes added by tzh-->
                        
                            <div class="text-start pb-2" v-for="(category, index) in bestRatedCategories" v-bind:key="category">
                                <div class="row ms-0 default-clickable-text "> 
                                    <div class="col-2 d-flex align-items-center justify-content-center rounded-circle me-3">
                                        <h5 class="my-auto"> {{ index + 1 }} </h5>
                                    </div>
                                    <div class="col-10 shrink-width-on-dashboard" > <!-- style added by tzh-->
                                        <b> {{ category.category }} </b> 
                                        <br>
                                        {{ category.averageRating.toFixed(2) || "-" }} 
                                        <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" fill="currentColor" class="bi bi-star-fill ms-1" viewBox="0 0 16 16">
                                            <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
                                        </svg>
                                    </div>
                                </div>
                            </div>
                        </div>

                    </div>

                <!-- row 1: review count and spread of ratings -->
                <div class="row mobile-view-hide">

                    <!-- col 1: review count -->
                    <div class="col-lg-5 col-md-12 col-sm-12 text-start mx-3 ps-lg-0 pe-lg-0">
                        <h3> Review Count </h3>
                        <Line :data="reviewsData" :options="chartOptions"></Line>
                    </div>

                    <!-- col 2: spread of ratings -->
                    <div class="col-lg-5 col-md-12 col-sm-12 text-start mx-3 mx-3 ps-lg-0 pe-lg-0">
                        <h3> Spread of Ratings </h3>
                        <Bar :data="ratingsData" :options="chartOptions" />
                    </div>

                </div>

                <!-- row 2: your best rated drinks & your best rated categories -->
                <div class="row mobile-view-hide">

                    <!-- col 1: your best rated drinks -->
                    <div class="col-lg-5 col-md-12 col-sm-12 text-start pt-5  mx-3 ps-lg-0 pe-lg-0">
                        <h3> Your Best Rated Drinks </h3>
                        <div class="text-start pb-2" v-for="listing in bestRatedListings" v-bind:key="listing._id">
                            <router-link :to="{ path: '/listing/view/' + listing.id }" class="reverse-clickable-text">
                                <div class="d-flex align-items-center">
                                    <!-- <img :src="'data:image/png;base64,'+ (listing.photo || defaultProfilePhoto)" style="width: 70px; height: 70px;"> -->
                                    <img :src="(listing.photo || defaultProfilePhoto)" style="width: 70px; height: 70px;">
                                    <p class="ms-3 default-clickable-text"> 
                                        <b> {{ listing.listingName }} </b> 
                                        <br>
                                        {{ listing.rating || "-" }} 
                                        <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" fill="currentColor" class="bi bi-star-fill ms-1" viewBox="0 0 16 16">
                                            <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
                                        </svg>
                                    </p>
                                </div>
                            </router-link>
                        </div>
                    </div>

                    <!-- col 2: your best rated categories -->
                    <div class="col-lg-5 col-md-12 col-sm-12 text-start pt-5 mx-3 ps-lg-0 pe-lg-0"> <!-- padding classes added by tzh-->
                        <h3> Your Best Rated Categories </h3>
                        <div class="text-start pb-2" v-for="(category, index) in bestRatedCategories" v-bind:key="category">
                            <div class="row ms-0 default-clickable-text "> 
                                <div class="col-2 d-flex align-items-center justify-content-center rounded-circle me-3">
                                    <h5 class="my-auto"> {{ index + 1 }} </h5>
                                </div>
                                <div class="col-10 shrink-width-on-dashboard" > <!-- style added by tzh-->
                                    <b> {{ category.category }} </b> 
                                    <br>
                                    {{ category.averageRating.toFixed(2) || "-" }} 
                                    <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" fill="currentColor" class="bi bi-star-fill ms-1" viewBox="0 0 16 16">
                                        <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
                                    </svg>
                                </div>
                            </div>
                        </div>
                    </div>

                </div> <!-- end of row 2-->

            </div>


            </div> <!-- end of row -->
        </div>
        
    </div> <!-- end of main content -->

</template>

<!-- ---------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<!-- JavaScript -->
<script>

    import NavBar from '@/components/NavBar.vue';
    import { Bar } from 'vue-chartjs'
    import { Line } from 'vue-chartjs'
    import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
    import { LineElement, PointElement } from 'chart.js'

    ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)
    ChartJS.register(LineElement, PointElement)

    export default {
        components: {
            NavBar,
            Bar,
            Line
        },
        computed: {
            userReviews() {
                return this.reviews.filter(review => review.userID === parseInt(this.userID) && review.reviewType === 'Listing');
            },
            reviewsData() {
                const dates = [...new Set(this.userReviews.map(review => this.formatDateMonthYear(review.createdDate)))];
                dates.sort((a, b) => {
                    const [monthA, yearA] = a.split('/');
                    const [monthB, yearB] = b.split('/');
                    if (yearA !== yearB) {
                        return yearA - yearB;
                    } else {
                        return monthA - monthB;
                    }
                });
                const counts = dates.map(date => this.userReviews.filter(review => this.formatDateMonthYear(review.createdDate) === date).length);
                return {
                    labels: dates,
                    datasets: [
                        {
                            label: 'Number of Reviews',
                            backgroundColor: '#747D92',
                            data: counts
                        }
                    ]
                }
            }, 
            ratingsData() { 
                const ratings = Array.from({length: 11}, (_, i) => i);
                const counts = ratings.map(value => Object.values(this.userReviews).filter(obj => Math.round(obj.rating) === value).length);
                return {
                    labels: [...new Set([...ratings, ...Array.from({length: 11}, (_, i) => i)])].sort((a, b) => a - b),
                    datasets: [
                        {
                            label: 'Number of Ratings',
                            backgroundColor: '#747D92',
                            data: counts
                        }
                    ]
                }
            },
            bestRatedListings() {
                const top5reviews = [...this.userReviews]
                    .sort((a, b) => b.rating - a.rating)
                    .slice(0, 5)
                const bestRatedListings = top5reviews
                    .map(review => {
                        const listing = this.listings.find(listing => listing.id === review.reviewTarget);
                        return {
                            ...listing,
                            rating: review ? review.rating : '',
                        };
                    });
                return bestRatedListings;
            },
            bestRatedCategories() {
                const reviewsWithCat = this.userReviews.map(review => {
                    const listing = this.listings.find(listing => listing.id === review.reviewTarget);
                    return {
                        ...review,
                        drinkType: listing.drinkType
                    };
                });
                const categories = [...new Set(reviewsWithCat.map(review => review.drinkType))];
                const bestRatedCategories = categories.map(category => {
                    const reviewsInCategory = reviewsWithCat.filter(review => review.drinkType === category);
                    const averageRating = reviewsInCategory.reduce((acc, review) => acc + review.rating, 0) / reviewsInCategory.length;
                    return {
                        category,
                        averageRating
                    };
                });
                bestRatedCategories.sort((a, b) => b.averageRating - a.averageRating);
                bestRatedCategories.splice(5);
                return bestRatedCategories;
            }, 
            recentFollowerActivity() {
                // follows and review tags
                const follows = this.users
                    .map(user => {
                        const followUser = user.followLists.users.find(followUser => followUser.followerI === this.userID);
                        return followUser ? {
                            username: user.username,
                            userID: user._id,
                            date: followUser.date
                        } : null;
                    })
                    .filter(Boolean);
                const tags = this.reviews
                    .filter(review => review.reviewType === 'Listing' && review.taggedUsers)
                    .map(review => {
                        const taggedReviews = review.taggedUsers.find(taggedUser => taggedUser === this.userID);
                        return taggedReviews ? {
                            userID: review.userID,
                            listingID: review.reviewTarget,
                            date: review.createdDate
                        } : null;
                    })
                    .filter(Boolean);

                const activities = [
                    ...tags.map(tag => ({ ...tag, type: 'tag' })),
                    ...follows.map(follow => ({ ...follow, type: 'follow' }))
                ];
                activities.sort((a, b) => new Date(b.date) - new Date(a.date));
                
                return activities;

            },
            recentReviewActivity() {
                // upvotes and downvotes

                const upvotes = this.userReviews
                    .map(review => review.userVotes.upvotes
                        .map(upvote => ({ ...upvote, reviewTarget: review.reviewTarget, date: review.createdDate }))
                    )
                    .filter(upvote => upvote.length > 0)
                    .flat();
                const downvotes = this.userReviews
                    .map(review => review.userVotes.downvotes
                        .map(downvote => ({ ...downvote, reviewTarget: review.reviewTarget, date: review.createdDate }))
                    )
                    .filter(downvote => downvote.length > 0)
                    .flat();

                const activities = [
                    ...upvotes.map(upvote => ({ ...upvote, type: 'upvote' })),
                    ...downvotes.map(downvote => ({ ...downvote, type: 'downvote' })),
                ];
                activities.sort((a, b) => new Date(b.date) - new Date(a.date));
                
                return activities;
            }
        },
        data() {
            return {
                dataLoaded: false,
                // user details
                userID: null,
                userType: null,
                user: null,
                ownProfile: false,


                // user details - tzh try
                loggedIn: false,
                
                
                userBookmarks: {},
                

                // user being viewed - tzh try
                displayUserID: null,
                displayUser: {},
                drinkChoice: "",
                //drinkCount: 0,
                joinDate: "",
                following: false,

                // data from database - tzh try
                listings: [],
                //producers: [],
                //venues: [],
                reviews: [],
                reversedReviews: [],
                users: [],
                drinkCategories: [],
                //drinkTypes: [],
                badges: [],
                drinkType: [],
                subTags: null,
                flavourTags: null,

                filteredDrinkType: [],

                chartOptions: {
                    responsive: true,
                    type: Object,
                    default: () => {},
                    scales: {
                        x: {
                            grid: {
                                display: false
                            }
                        },
                        y: {
                            grid: {
                                display: false
                            },
                            beginAtZero: true,
                            precision: 0,
                            ticks: {
                                stepSize: 1
                            }
                        }
                    }
                },

                producers: [],
                venues: [],

                drinkCount: 0,
                drinkTypes: [],
                
                // defaultProfilePhoto: "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",
                defaultProfilePhoto:"https://drinkximages.s3.amazonaws.com/images/27e129b8-2d6e-44a3-8c14-d78c815b8056.jpg",
                
                // to get follower activity
                showFollowerActivity: false,

                // to get review activity
                showReviewActivity: false,
               

                // display user drink activity
                favouriteListings: {},
                recentActivity: {},
                recentReviews: {},

                // followers
                followerCount: 0,

                // for badges
                allListingsReviewedByUser: [],
                allCategoriesReviewedByUser: {},
                allSubCategoriesReviewedByUser: {},
                matchedDrinkTypes: [],
                topCategoriesReviewed: [],
                topSubcategoriesReviewed: {},
                reviewCountriesTagged: [],
                badgeLevels: { // CHANGE THIS! if there is a change in criterion for minimum # of reviews that a user needs to gain a badge level
                    novice: 3,
                    lover: 10,
                    master: 30,
                },
                categoryBadges: {},
                otherBadgesLimit: { // CHANGE THIS! if there is a change in minimum # that a user needs to gain a badge level
                    reviewDrinkCategory: 10,
                    tagFriend: 3,
                    tagLocation: 5,
                    tagCountry: 3,
                    upvotes: 10
                },
                otherBadges: [],
                totalBadges: 0,

                // for points
                pointSystem: { // CHANGE THIS! if there is a change in the point system (just change this.pointsDefault to a numerical value for the corresponding criteria)
                    // format: { action: [count, points] }
                    logReview: [0, 50], // log a review
                    tagFriend: [0, 50], // tag a friend
                    tagLocation: [0, 50], // tag a location
                    tagCountry: [0, 50], // tag a country
                    askProducer: [0, 50], // ask a producer a question
                    askVenue: [0, 50], // ask a venue a question
                },
                totalPoints: 0,
            };
        },
        async mounted() {
            var userID = localStorage.getItem('88B_accID')
            if (userID != null) {
                this.userID = userID;
            }

            var userType = localStorage.getItem('88B_accType');
            if (userType != null) {
                this.userType = userType;
                if (this.userType != 'user') {
                    this.$router.push('/login');
                }
            }

            // get displayUserID from URL
            try {
                this.displayUserID = this.$route.params.userID;
                if (this.displayUserID === this.userID) {
                    this.$router.push('/profile/user');
                }
                else if (!this.displayUserID) {
                    this.displayUserID = this.userID;
                }
            }
            catch (error) {
                console.error(error);
            }

            await this.loadData();

        },
        methods: {
            async loadData() {
                // listings
                // _id, listingName, producerID, bottler, originCountry, drinkType, typeCategory, age, abv, reviewLink, officialDesc, sourceLink, photo
                try {
                        const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getListings`);
                        this.listings = response.data;
                    } 
                    catch (error) {
                        console.error(error);
                        this.dataLoaded = null;
                    }
                // Producers
                try {
                    const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getProducers`);
                    this.producers = response.data;
                    this.dataLoaded = true;
                } 
                catch (error) {
                    console.error(error);
                    this.dataLoaded = null;
                }
                // Venues
                try {
                    const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getVenues`);
                    this.venues = response.data;
                    this.dataLoaded = true;
                } 
                catch (error) {
                    console.error(error);
                    this.dataLoaded = null;
                }
                // reviews
                // _id, userID, reviewTarget, date, rating, reviewDesc, taggedUsers, reviewTitle, reviewType, flavorTag, photo
                try {
                        const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getReviews`);
                        this.reviews = response.data;
                        this.reversedReviews = this.reviews.reverse();
                        this.recentReviews = this.reversedReviews.filter(review => review.userID === this.displayUserID && review.reviewType === 'Listing');
                    }
                    catch (error) {
                        console.error(error);
                        this.dataLoaded = null;
                    }
                
                // Set data loaded to true
                if (this.dataLoaded != null) {
                    this.dataLoaded = true;
                }
                
                // for Badges
                try {
                    const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getBadges`);
                    this.badges = response.data;
                    this.dataLoaded = true;
                } 
                catch (error) {
                    console.error(error);
                    this.dataLoaded = null;
                }
                // users
                // _id, username, displayName, choiceDrinks, drinkLists, modType, photo
                try {
                        const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getUsers`);
                        this.users = response.data;
                        this.user = this.users.find(user => user.id == this.userID);
                        this.displayUser = this.getUser(this.displayUserID);
                        
                        if (this.userID === this.displayUserID) {
                            this.ownProfile = true;
                        }
                        else {
                            this.ownProfile = false;
                        }
                        
                        //drink count
                        this.drinkCount = this.getDrinkCount();

                        // for followers
                        this.getTotalFollowers();

                        // ==== for badges ====
                        this.getAllListingsReviewed();
                        this.getAllCategoriesReviewed();
                        await this.getAllCountriesTagged();

                        // ==== for points ====
                        this.pointSystem.logReview[0] = this.allListingsReviewedByUser.length;
                        this.getTotalFriendsTagged();
                        this.getTotalLocationsTagged();
                        this.getTotalCountriesTagged();
                        this.getAskedProducerQuestions();
                        this.getAskedVenueQuestions();
                        this.calculateTotalPoints();

                        // ==== for badges (others) ====
                        this.checkEnoughLocationTagged();
                        this.checkEnoughCountriesTagged();
                        this.checkEnoughFriendsTagged();
                        this.getTotalUpvotes();
                        this.checkEnoughUpvotes();

                    } 
                    catch (error) {
                        console.error(error);
                        this.dataLoaded = null;
                    }
                // drinkCategories
                try {
                    const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getDrinkTypes`);
                    this.drinkTypes = response.data;

                    // ==== for badges ====
                    this.getTopCategoriesReviewed();
                    this.getMatchedDrinkType();
                    this.calculateTotalBadges();

                } 
                catch (error) {
                    console.error(error);
                    this.dataLoaded = null;
                }
                
            }, 

            // get user from user ID
            getUser(id) {
                return this.users.find(user => user.id === id);
            },

            // get display user details
            getDrinkCount() {
                if (this.ownProfile) {
                    return this.reviews.filter(review => review.userID === parseInt(this.userID) && review.reviewType === 'Listing').length;
                }
                else {
                    return this.reviews.filter(review => review.userID === parseInt(this.displayUserID) && review.reviewType === 'Listing').length;
                }
            },

            // go back to profile page
            goBack() {
                this.$router.go(-1)
            },

            formatDateMonthYear(dateTimeString) {
                let date = new Date(dateTimeString);
                let month = date.toLocaleString('default', { month: 'short' });
                let year = date.getFullYear();
                let formattedDate = `${month}/${year}`;
                return formattedDate;
            }, 

            getTimeDifference(date) {
                let currentDate = new Date();
                let updateDate = new Date(date);
                let timeDifference = currentDate - updateDate;
                let seconds = Math.floor(timeDifference / 1000);
                let minutes = Math.floor(seconds / 60);
                let hours = Math.floor(minutes / 60);
                let days = Math.floor(hours / 24);
                let months = Math.floor(days / 30);
                let years = Math.floor(months / 12);
                if (years > 0) {
                    return years + (years === 1 ? ' year ago' : ' years ago');
                } else if (months > 0) {
                    return months + (months === 1 ? ' month ago' : ' months ago');
                } else if (days > 0) {
                    return days + (days === 1 ? ' day ago' : ' days ago');
                } else if (hours > 0) {
                    return hours + (hours === 1 ? ' hour ago' : ' hours ago');
                } else if (minutes > 0) {
                    return minutes + (minutes === 1 ? ' minute ago' : ' minutes ago');
                } else {
                    return seconds + (seconds === 1 ? ' second ago' : ' seconds ago');
                }
            }, 

            getListingFromID(listingID) {
                return this.listings.find(listing => listing.id == listingID);
            },

            getUserFromID(userID) {
                return this.users.find(user => user.id == userID);
            },

            // to check if follower activity should be shown
            checkToShowFollowerActivity() {
                if (this.showFollowerActivity == true) {
                    this.showFollowerActivity = false;
                } 
                else {
                    this.showFollowerActivity = true;
                }
            },

            // to check if review activity should be shown
            checkToShowReviewActivity() {
                if (this.showReviewActivity == true) {
                    this.showReviewActivity = false;
                } 
                else {
                    this.showReviewActivity = true;
                }
            },

            // get total followers of user
            getTotalFollowers() {
                let followers = this.users.filter(user => user.followLists.users.some(follower => follower.followerID === this.userID));
                this.followerCount = followers.length;
            },

            // ------------------- Badges -------------------

            // get all listings reviewed by the user
            getAllListingsReviewed() {
                this.allListingsReviewedByUser = this.recentReviews.map(review => this.listings.find(listing => listing.id === review.reviewTarget));
            },

            // get all drinkType and typeCategory reviewed by the user
            getAllCategoriesReviewed() {
                for (let listing of this.allListingsReviewedByUser) {
                    // check if this.allCategoriesReviewedByUser already contains the count for listing.drinkType
                    // [if] no, assign the count as 1
                    // [else] yes, add 1 to the count
                    this.allCategoriesReviewedByUser[listing.drinkType] = (this.allCategoriesReviewedByUser[listing.drinkType] || 0) + 1;
                    // check if this.allSubCategoriesReviewedByUser already contains the count for listing.typeCategory for that listing.drinkType
                    // [if] no, assign the count as 1
                    // [else] yes, add 1 to the count
                    if (!this.allSubCategoriesReviewedByUser[listing.drinkType]) {
                        this.allSubCategoriesReviewedByUser[listing.drinkType] = {};
                    }
                    this.allSubCategoriesReviewedByUser[listing.drinkType][listing.typeCategory] = (this.allSubCategoriesReviewedByUser[listing.drinkType][listing.typeCategory] || 0) + 1;
                }
            },

            // extract out only the drink categories that the user has >= this.badgeLevels.novice (most basic level) reviews for
            // assign this.categoryBadges[category] to user based on # of reviews for that category
            // CHANGE! name of this.categoryBadges[category] if the criterion for minimum # of reviews to get a badge changes
            getTopCategoriesReviewed() {
                this.topCategoriesReviewed = Object.keys(this.allCategoriesReviewedByUser).reduce((acc, category) => {
                    // check if user has reviewed enough subcategories for this category
                    for (let subcategory in this.allSubCategoriesReviewedByUser[category]) {
                        let count = this.allSubCategoriesReviewedByUser[category][subcategory];
                        if (count >= this.otherBadgesLimit.reviewDrinkCategory) {
                            this.topSubcategoriesReviewed[category] = this.topSubcategoriesReviewed[category] || [];
                            this.topSubcategoriesReviewed[category].push(subcategory);
                        }
                    }
                    // --> HIGHEST TIER : MASTER (>= 30 reviews)
                    if (this.allCategoriesReviewedByUser[category] >= this.badgeLevels.master) {
                        acc[category] = this.allCategoriesReviewedByUser[category];
                        this.categoryBadges[category] = "Master"
                    }
                    // --> MIDDLE TIER: LOVER (>= 10 reviews)
                    else if (this.allCategoriesReviewedByUser[category] >= this.badgeLevels.lover) {
                        acc[category] = this.allCategoriesReviewedByUser[category];
                        this.categoryBadges[category] = "Lover"
                    }
                    // --> LOWEST TIER: NOVICE (>= 3 reviews)
                    else if (this.allCategoriesReviewedByUser[category] >= this.badgeLevels.novice) {
                        acc[category] = this.allCategoriesReviewedByUser[category];
                        this.categoryBadges[category] = "Novice"
                    }
                    return acc;
                }, {});
            },

            // match categories to "drinkType" database
            // currently all "drinkTypes" in the reviews are hardcoded, so there is a need to map the objects so that all the badgePhoto can be retrieved
            getMatchedDrinkType() {
                this.matchedDrinkTypes = Object.keys(this.topCategoriesReviewed).map(category => this.drinkTypes.find(drinkType => drinkType.drinkType === category));
            },

            // get all countries user has tagged location in reviews
            async getAllCountriesTagged() {
                const apiKey = process.env.VUE_APP_GOOGLE_MAPS_API_KEY;
                const promises = this.recentReviews.map(async (review) => {
                    const address = encodeURIComponent(review.address);
                    if (address) {
                        const response = await this.$axios.get(`https://maps.googleapis.com/maps/api/geocode/json?address=${address}&key=${apiKey}`);
                        const { results } = response.data;
                        if (results[0]) {
                            const countryComponent = results[0].address_components.find(component => component.types.includes('country'));
                            if (countryComponent) {
                                const country = countryComponent.long_name;
                                if (!this.reviewCountriesTagged.includes(country)) {
                                    this.reviewCountriesTagged.push(country);
                                }
                            }
                        }
                    }
                });

                await Promise.all(promises);
            },

            // check if user has tagged locations in reviews
            checkEnoughLocationTagged() {
                if (this.pointSystem.tagLocation[0] >= this.otherBadgesLimit.tagLocation) {
                    this.otherBadges.push("tagLocation")
                }
            },

            // check if user has tagged locations in reviews
            checkEnoughCountriesTagged() {
                if (this.pointSystem.tagCountry[0] >= this.otherBadgesLimit.tagCountry) {
                    this.otherBadges.push("tagCountry")
                }
            },

            // check if user has tagged friends in reviews
            checkEnoughFriendsTagged() {
                if (this.pointSystem.tagFriend[0] >= this.otherBadgesLimit.tagFriend) {
                    this.otherBadges.push("tagFriend")
                }
            },

            // get total number of upvotes received
            getTotalUpvotes() {
                let totalUpvotes = this.recentReviews.reduce((count, review) => {
                    if (review.userVotes.upvotes.some(vote => vote.userID === this.displayUserID)) {
                        count += 1;
                    }
                    return count;
                }, 0);
                return totalUpvotes;
            },

            // check if user has upvotes from reviews
            checkEnoughUpvotes() {
                if (this.getTotalUpvotes() >= this.otherBadgesLimit.upvotes) {
                    this.otherBadges.push("upvotes")
                }
            },

            getBadgeInfo(badgeName) {
                if (badgeName) {
                    const badge = this.badges.find(badge => badge.badgeName === badgeName);
                    return badge ? badge : null;
                }
            },

            calculateTotalBadges() {
                this.totalBadges = Object.keys(this.categoryBadges).length + this.otherBadges.length;
            },

            // ------------------- Points -------------------

            // get total number of friends tagged
            getTotalFriendsTagged() {
                // loop through all reviews and get the number of friends tagged for each review
                // add up all the friends tagged
                this.pointSystem.tagFriend[0] = this.recentReviews.reduce((sum, review) => sum + review.taggedUsers.length, 0);
            },

            // get total number of locations tagged in reviews
            getTotalLocationsTagged() {
                // loop through all reviews and get the number of locations tagged for each review
                // add up all the locations tagged
                this.pointSystem.tagLocation[0] = this.recentReviews.reduce((sum, review) => sum + (review.location.length !== 0 ? 1 : 0), 0);
            },

            // get total number of countries user tagged in reviews
            getTotalCountriesTagged() {
                // loop through all reviews and get the number of countries tagged
                this.pointSystem.tagCountry[0] = this.reviewCountriesTagged.length;
            },

            // get total number of questions asked by user to producers
            getAskedProducerQuestions() {
                this.pointSystem.askProducer[0] = this.producers.reduce((totalQuestions, producer) => {
                    return totalQuestions + producer.questionsAnswers.filter(qa => qa.userID === this.displayUserID).length;
                }, 0);
            },

            // get total number of questions asked by user to venues
            getAskedVenueQuestions() {
                this.pointSystem.askVenue[0] = this.venues.reduce((totalQuestions, venue) => {
                    return totalQuestions + venue.questionsAnswers.filter(qa => qa.userID === this.displayUserID).length;
                }, 0);
            },

            // calculate total points
            calculateTotalPoints() {
                // in this.pointSystem, the key is the action, and the value is an array of [points, count]
                // to calculate total points, take value[0] = points | value[1] = count, and sum up all points * count
                this.totalPoints = Object.values(this.pointSystem).reduce((sum, value) => sum + (value[0] * value[1]), 0);
            },
        }
    };
</script>