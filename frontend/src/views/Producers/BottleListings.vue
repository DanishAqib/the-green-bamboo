<!-- HTML -->
<template>
    <NavBar />

    <!-- Display when data is still loading -->
    <div class="text-info-emphasis fst-italic fw-bold fs-5 pt-5" v-if="dataLoaded == false">
        <span>Loading listing, please wait...</span>
        <br><br>
        <div class="spinner-border" role="status">
            <span class="visually-hidden">Loading...</span>
        </div>
    </div>

    <!-- Display when data fails to load -->
    <div class="text-danger fst-italic fw-bold fs-3 pt-5" v-if="dataLoaded == null && listingExists == true"> 
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

    <!-- Display when listing does not exist -->
    <div class="text-danger fst-italic fw-bold fs-3 pt-5" v-if="dataLoaded == null && listingExists == false"> 
        <span>This listing does not exist! Please try another listing!</span>
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
    <div class="container pt-5 mobile-pt-4" v-if="dataLoaded">
        <div class="row">
            <!-- producer information -->
            <div class="col-12 col-md-9 no-margin no-right-padding-large-screen">
                
                <!-- header -->
                <div class="row container">
                    <!-- image -->
                    <div class="col-12 col-lg-4 col-xl-3 image-container text-start mobile-col-5">
                        <img :src="( specified_listing['photo'] || defaultPhoto )" class="producer-bottle-listing-page-image" >
                    </div>
                    <!-- details -->
                    <div class="col-12 col-lg-8 col-xl-9 text-start mobile-col-7 mobile-ps-0 mobile-pe-0">
                        <div class="container text-start mobile-ps-0 mobile-pe-0">
                            <!-- drink category -->
                            <div class="row">
                                <div class="col-9 mobile-view-hide">
                                    <h5 class="text-body-secondary fst-italic"> {{ specified_listing["drinkType"] }} </h5>
                                </div>
                                <div v-if="correctProducer" class="col-3">
                                    <div class="text-end mb-3 m-1">
                                        <div class="form-check form-switch form-check-inline">
                                            <input class="form-check-input"  type="checkbox" role="switch" id="lockCheck" name="lockCheck" v-model="specified_listing.allowMod" data-bs-toggle="modal" data-bs-target="#lockModal">
                                            <label class="form-check-label" for="IBCheck" v-if="specified_listing.allowMod">Unlocked</label>
                                            <label class="form-check-label" for="IBCheck" v-if="!specified_listing.allowMod">Locked</label>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- modal for lock listing to moderators -->
                            <div class="modal fade" id="lockModal" tabindex="-1" data-bs-keyboard="false" aria-labelledby="lockModalLabel" aria-hidden="true" data-bs-backdrop="static">
                                <div class="modal-dialog modal-xl">
                                    <div class="modal-content">
                                        <div class="modal-header" style="background-color: #535C72">
                                            <h1 class="modal-title fs-5" id="exampleModalLabel" style="color: white;">Toggle Moderator</h1>
                                            <button type="button" @click="resetToggle" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                        </div>

                                        <div class="modal-body text-center">
                                            <p v-if="specified_listing.allowMod && inToggle" class="text-primary fst-italic fw-bold fs-3">Are you sure you want to allow moderators to edit this listing?</p>
                                            <p v-if="!specified_listing.allowMod && inToggle" class="text-primary fst-italic fw-bold fs-3">Are you sure you want to stop moderators from editing this listing?</p>  

                                            <!-- if toggle is successful -->
                                            <p v-if="specified_listing.allowMod && toggleSuccess" class="text-success fst-italic fw-bold fs-3">Moderators are now allowed to edit this listing!</p>
                                            <p v-if="!specified_listing.allowMod && toggleSuccess" class="text-success fst-italic fw-bold fs-3">Moderators are now not allowed to edit this listing!</p>      
                                            
                                            <!-- if toggle faces error -->
                                            <p v-if="toggleError" class ="text-danger fst-italic fw-bold fs-3">There is an error toggling the permission, please try again later!</p>
                                        </div>

                                        <div class="modal-footer">
                                            <button type="button" @click="resetToggle" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                            <button v-if="inToggle" type="button" @click="updateToggle" class="btn btn-primary">Save Changes</button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- end of modal-->

                            <!-- expression name -->
                            <div class="row">
                                <div class="col-12 col-lg-8">
                                    <div class="row">
                                        <h3 class="text-body-secondary mb-0 mobile-view-hide"> <b> {{ specified_listing["listingName"] }} </b> </h3>
                                        <h4 class="text-body-secondary mb-0 mobile-view-show col-10 pe-1"> <b> {{ specified_listing["listingName"] }} </b> </h4>
                                        <div class="col-2 mobile-view-show px-1">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="29" height="29" data-bs-toggle="modal" data-bs-target="#whereToBuyModal" viewBox="0 0 24 24" fill="none" stroke="#000000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="arcs"><path d="M3.8 3.8l16.4 16.4M20.2 3.8L3.8 20.2M15 3h6v6M9 3H3v6M15 21h6v-6M9 21H3v-6"/></svg>
                                        </div>
                                    </div>
                                    <div class="row pt-1">
                                        <!-- producer -->
                                        <div class="col-12 col-lg-6">
                                            <h6 class="text-body-secondary producer-page">
                                                <router-link :to="{ path: '/profile/producer/' + this.producer_id }" class="default-text-no-background">
                                                    <p class="mobile-mb-0"> {{ getProducerName(specified_listing["producerID"]) }} </p>
                                                </router-link>
                                            </h6>
                                        </div>
                                        <!-- bottler -->
                                        <div class="col-12 col-lg-6">
                                            <h6 v-if="specified_listing['bottler'] != 'OB'" class="text-body-secondary producer-page"> Bottler: <u> {{ specified_listing["bottler"] }} </u>  </h6>
                                                <h6 v-else class="text-body-secondary producer-page"> Bottler:
                                                    <router-link :to="{ path: '/profile/producer/' + this.producer_id }" class="default-text-no-background"> 
                                                        <u style="color:black;"> {{ getProducerName(specified_listing["producerID"]) }} </u>  
                                                    </router-link>
                                                </h6>
                                        </div>
                                    </div>
                                </div>
                                <!-- tzh edited classes suggest edit & report duplicate padding-top-for-suggesteditslink-large-screen-->
                                <div class="col-12 col-md-4 col-lg-4 text-end padding-left-for-suggesteditslink-large-screen padding-right-for-suggesteditslink-large-screen mobile-view-hide" style="position: relative;">
                                    <!-- [if] correct producer-->
                                    <!-- TODO: check if moderator type is for the listing -->
                                    <div v-if="correctProducer || correctModerator" class="edit-listing-report-duplicate-btn" >
                                        <button type="button" class="btn tertiary-btn reverse-clickable-text m-1">
                                            <router-link :to="`/listing/edit/${specified_listing.id}`" class="reverse-clickable-text">
                                                Edit Listing
                                            </router-link>
                                        </button>
                                        <!-- delete listing -->
                                        <button type="button" class="btn btn-danger reverse-clickable-text p-1" data-bs-toggle="modal" data-bs-target="#deleteListingModal">
                                            <!-- v-on:click="deleteListings(specified_listing)" -->
                                            <a class="reverse-clickable-text">
                                                Delete Listing
                                            </a>
                                        </button>
                                    </div>

                                    <!-- [else] not correct producer -->
                                    <div v-else >
                                        <router-link :to="{ path: '/request/modify/edit/' + this.listing_id }">
                                        <p class="text-body-secondary no-margin text-decoration-underline fst-italic text-end"> Suggest Edit </p>
                                        </router-link>
                                        <router-link :to="{ path: '/request/modify/duplicate/' + this.listing_id }">
                                            <p class="text-body-secondary no-margin text-decoration-underline fst-italic text-end"> Report Duplicate </p>
                                        </router-link>
                                    </div>
                                </div>
                            </div>
                            
                            <!-- The Modal xyz-->
                            
                            <div class="modal fade" id="whereToBuyModal" tabindex="-1" aria-labelledby="whereToBuyModalLabel" aria-hidden="true">
                                <div class="modal-dialog modal-lg">
                                    <div class="modal-content">
                                        <div class="modal-header" style="background-color: #535C72">
                                            <h5  class="modal-title" style="color: white;">More Details</h5>
                                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                        </div>    
                                        <div class="modal-body">
                                            <div class="col-sm-12 col-md-9 col-lg-3 ">
                                                <!-- where to buy -->
                                                <div class="row">
                                                    <div class="square primary-square-green rounded p-3 mb-3 text-start" style="height: 250px;"> <!-- TZH added '-green'-->
                                                        <!-- header text -->
                                                        <div class="square-inline text-start">
                                                            <h4 class="mr-auto"> Where to Buy </h4>
                                                        </div>
                                                        <!-- body -->
                                                        <div style="height: 85%;">
                                                            <div class="text-start pt-2 overflow-auto" style="max-height: 100%;">
                                                                <!-- [function] where to buy -->
                                                                <div v-for="producer in producerListings" v-bind:key="producer">
                                                                    <router-link :to="{ path: '/profile/producer/' + producer }" class="reverse-clickable-text">
                                                                        <p> {{ getProducerName(producer) }} </p>
                                                                    </router-link>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>

                                                <!-- not sure what this line supposed to do -->
                                                <!-- {{ drinkList }} -->
                                            
                                                <!-- where to try -->
                                                <div class="row">
                                                    <div class="square primary-square-green rounded p-3 mb-3 text-start" style="height: 250px;">  <!-- TZH added '-green'-->
                                                        <!-- header text -->
                                                        <div class="square-inline text-start">
                                                            <h4 class="mr-auto"> Where to Try </h4>
                                                        </div>
                                                        <!-- body -->
                                                        <div style="height: 85%;">
                                                            <div class="text-start pt-2 overflow-auto" style="max-height: 100%;">
                                                                <!-- [function] where to try -->
                                                                <!-- [if] user does not allow location -->
                                                                <div v-if="nearestBars.length == 0" >
                                                                    <div v-for="venue in venueListings" v-bind:key="venue.id">
                                                                        <router-link :to="{ path: '/profile/venue/' + venue.id }" class="reverse-clickable-text">
                                                                            <p class="mb-1"> {{ venue.venueName }} </p>
                                                                        </router-link>
                                                                    </div>
                                                                </div>
                                                                <!-- [else] user allows location -->
                                                                <div v-else>
                                                                    <div v-for="(distance, venueID) in nearestBars" v-bind:key="venueID">
                                                                        <router-link :to="{ path: '/profile/venue/' + venueID }" class="reverse-clickable-text">
                                                                            <p class="mb-4"> 
                                                                                <u> {{ getVenueNameFromID(venueID) }}  </u>
                                                                                <br>
                                                                                <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" fill="currentColor" class="bi bi-geo-alt-fill" viewBox="0 0 16 16">
                                                                                    <path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10m0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6"/>
                                                                                </svg>
                                                                                Distance: {{ venueDetails[venueID]["distance"] }}
                                                                                <br>
                                                                                <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" fill="currentColor" class="bi bi-clock" viewBox="0 0 16 16">
                                                                                    <path d="M8 3.5a.5.5 0 0 0-1 0V9a.5.5 0 0 0 .252.434l3.5 2a.5.5 0 0 0 .496-.868L8 8.71z"/>
                                                                                    <path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16m7-8A7 7 0 1 1 1 8a7 7 0 0 1 14 0"/>
                                                                                </svg>
                                                                                Duration: {{ venueDetails[venueID]["duration"] }}
                                                                            </p>
                                                                        </router-link>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                                
                                                <!-- 88 bamboo's review -->
                                                <div class="row">
                                                    <div class="square primary-square-green-outline xsecondary-square rounded p-3 mb-3">  <!-- TZH added 'primary-square-green-outline'-->
                                                        <!-- header text -->
                                                        <div class="py-2 text-start">
                                                            <h4> 88 Bamboo's Review </h4>
                                                            <a v-if="isHttpValid(specified_listing['reviewLink'])" :href="specified_listing['reviewLink']" class="text-left default-text-no-background row">
                                                                <div class="row">
                                                                    <div class="col-lg-4 col-md-6 col-sm-12">
                                                                        {{ getOGImage(specified_listing['reviewLink']) }}
                                                                        <!-- [if] there is a cover image for the post-->
                                                                        <img v-if="ogImage != null" :src="ogImage[specified_listing.reviewLink]" alt="OG Image" style="width: 80px; height: 80px;">
                                                                        <!-- [else] there is no cover image for the post (put 88 bamboo's logo) -->                    
                                                                        <img v-else src="https://88bamboo.co/cdn/shop/files/88B_New_Logo_-_white_face_transparent_background_180x.png?v=1655894111" style="width: 80px; height: 80px;">                                   
                                                                    </div>
                                                                    <div class="col-lg-8 col-md-12">
                                                                        {{ deepDiveLinkFormatted }}
                                                                    </div>
                                                                </div>
                                                            </a>
                                                            <div v-else>
                                                                <div class="text-body-secondary">
                                                                    <div class="fst-italic">
                                                                        No reviews available for this listing.
                                                                        For other 88 Bamboo reviews, 
                                                                        <a href="https://88bamboo.co/blogs/news" class="default-text-no-background">click here</a>.
                                                                    </div>
                                                                </div>
                                                            </div>

                                                        </div>
                                                        <div class="py-2"></div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        
                                    </div>
                                </div>
                            </div>


                            <!-- description -->
                            <div class="row scrollable mobile-view-hide">
                                <div class="col-lg-12 padding-right-for-suggesteditslink-large-screen">
                                    <!--<div class="py-2"></div>-->
                                    <!-- below truncated-->
                                    <div v-if="specified_listing.officialDesc?.length > 250">
                                        <p v-if="!showFullDescription" class="mobile-rating-smaller-text-2" style="margin-bottom:0.2rem;"><!-- tzh added truncated description --->
                                            <em>{{ specified_listing["officialDesc"].slice(0, 250) + (specified_listing["officialDesc"].length > 250 ? '...' : '') }}</em>
                                            <a @click="showFullDescription = true" style="font-weight: bold;">(Read More)</a>
                                        </p>
                                        <p v-else style="margin-bottom:0.2rem;" class="mobile-rating-smaller-text-2"> <!-- tzh added full description --->
                                            <em>{{ specified_listing["officialDesc"] }}</em>
                                            <a @click="showFullDescription = false" style="font-weight: bold;">(Read Less)</a>
                                        </p>
                                    </div>
                                    <p v-else style="margin-bottom:0.2rem;" class="mobile-rating-smaller-text-2">
                                        <em>{{ specified_listing["officialDesc"] }}</em>
                                    </p>  
                                    <!-- above truncated-->  
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row scrollable mobile-view-show text-start">
                                <div class="col-lg-12 padding-right-for-suggesteditslink-large-screen">
                                    <!--<div class="py-2"></div>-->
                                    <div v-if="specified_listing.officialDesc?.length > 250">
                                        <p v-if="!showFullDescription" class="mobile-rating-smaller-text-2 " style="margin-bottom:0.2rem; padding-left:0.8rem !important;"><!-- tzh added truncated description --->
                                            <em>{{ specified_listing["officialDesc"].slice(0, 250) + (specified_listing["officialDesc"].length > 250 ? '...' : '') }}</em>
                                            <a @click="showFullDescription = true" style="font-weight: bold;">(Read More)</a>
                                        </p>
                                        <p v-else style="margin-bottom:0.2rem; padding-left:0.8rem !important;" class="mobile-rating-smaller-text-2"> <!-- tzh added full description --->
                                            <em>{{ specified_listing["officialDesc"] }}</em>
                                            <a @click="showFullDescription = false" style="font-weight: bold;">(Read Less)</a>
                                        </p>
                                    </div>
                                    <p v-else style="margin-bottom:0.2rem; padding-left:0.8rem !important;" class="mobile-rating-smaller-text-2">
                                        <em>{{ specified_listing["officialDesc"] }}</em>
                                    </p>    
                                </div>
                </div>
                <div class="row pt-2 container mobile-view-show text-black">
                <p class="text-start mb-1 col-10" style="white-space: nowrap; overflow:hidden;text-overflow: ellipsis; font-size:15px; font-weight:bold;">
                                                        <span v-if="specified_listing.drinkType === 'Whiskey / Whisky'">
                                                            <span style="color: #2c3e50;" class="text-decoration-none">Whisky | </span>
                                                        </span>
                                                        <span v-else>{{ specified_listing["drinkType"] }} | </span>
                                                        <span style="color: #2c3e50;" class="text-decoration-none">{{ specified_listing["typeCategory"] }} | </span>
                                                        <span style="color: #2c3e50;" class="text-decoration-none">{{ specified_listing["abv"] }} | </span>
                                                        <span style="color: #2c3e50;" class="text-decoration-none">{{ specified_listing["originCountry"] }}</span>
                </p>
                <div class="col-2 d-flex justify-content-end make-bookmark-bigger" >
                        <BookmarkIcon 
                            v-if="user" 
                            :user="user" 
                            :listing="specified_listing" 
                            :overlay="false"
                            size="30"
                            @icon-clicked="handleIconClick" />
                </div>
                </div>                                    
                <!-- more information (category, age, country of origin, abv, list buttons & bookmark) -->
                <div class="row pt-4 container mobile-view-hide">
                    <div class="col-7 col-lg-7">
                        <div class="row">
                            <!-- category -->
                            <div class="col-6 col-lg-3 text-start mobile-view-hide text-color-black">
                                <h5 class="text-body-secondary" style="margin-bottom:0;"> <b> {{ specified_listing["typeCategory"] }} </b> </h5>
                                <p class="mb-2"> <u> Category </u> </p>
                                
                            </div>
                            <!-- age --> 
                            <div class="col-6 col-lg-3 text-start mobile-view-hide text-color-black">
                                <!-- for wine listings -->
                                <div v-if="specified_listing['drinkType'] == 'Wine'">
                                    <h5 class="text-body-secondary" style="margin-bottom:0;"> <b>  {{ specified_listing["age"] }} </b> </h5>
                                    <p class="mb-2"> <u> Vintage </u> </p> <!-- to change this to calculate the age -->
                                    
                                </div>
                                <!-- for all other listings  -->
                                <div v-else>
                                    <h5 class="text-body-secondary" style="margin-bottom:0;"> <b>  {{ specified_listing["age"] }} </b> </h5>
                                    <p class="mb-2"> <u> Age </u> </p> 
                                    
                                </div>
                            </div>
                            <!-- country of origin -->
                            <div class="col-6 col-lg-4 text-start mobile-view-hide text-color-black">
                                <h5 class="text-body-secondary" style="margin-bottom:0;"> <b> {{ specified_listing["originCountry"] }} </b> </h5>
                                <p class="mb-2"> <u> Country of Origin </u> </p>
                                
                            </div>
                            <!-- abv -->
                            <div class="col-6 col-lg-2 text-start mobile-view-hide text-color-black">
                                <h5 class="text-body-secondary" style="margin-bottom:0;"> <b> {{ specified_listing["abv"] }} </b> </h5>
                                <p class="mb-1"> <u> ABV </u> </p>
                                
                            </div>
                        </div>
                    </div>
                    
                    <!-- have tried button -->
                    <div class="col-2 col-lg-2 p-0">
                        <!-- <div v-if="user && Object.keys(user.drinkLists).length > 0" v-html="checkDrinkLists(specified_listing).buttons.haveTried" class="d-grid" @click="addToTriedList"> </div> -->
                        <!-- CP edits: Removed the if logic so public users can also view and click -->
                        <div v-html="checkDrinkLists(specified_listing).buttons.haveTried" class="d-grid" @click="addToTriedList"> </div>
                    </div>
                    <!-- want to try button -->
                    <div class="col-2 col-lg-2 p-0">
                        <!-- <div v-if="user && Object.keys(user.drinkLists).length > 0" v-html="checkDrinkLists(specified_listing).buttons.wantToTry" class="d-grid" @click="addToWantList"> </div> -->
                        <!-- CP edits: Removed the if logic so public users can also view and click -->
                        <div v-html="checkDrinkLists(specified_listing).buttons.wantToTry" class="d-grid" @click="addToWantList"> </div>
                    </div>
                    <!-- bookmark button -->
                    <div class="col-1 col-lg-1 text-center d-flex justify-content-start make-bookmark-bigger" >
                        <!-- CP edits: removed v-if logic for public users to view and click -->
                        <BookmarkIcon 
                            :user="user" 
                            :listing="specified_listing" 
                            :overlay="false"
                            size="30"
                            @icon-clicked="handleIconClick" />

                    </div>
                    
                </div>

                <!-- more information (average rating, would recommend, would drink again) -->
                <div class="row pt-3 container">
                    <!-- xyz -->
                    <div class="col-12 col-lg-7">
                        <div class="row">
                            <!-- average rating -->
                            <div class="col-4 text-start mobile-col-3 mobile-pe-0 text-color-black">
                                
                                <h3 class="mobile-rating-smaller-text text-body-secondary rating-text" style="margin-bottom:0;"> 
                                    <b>{{ specificReviewRating }}</b>
                                    <svg xmlns="http://www.w3.org/2000/svg" width="30" height="1em" fill="currentColor" class="bi bi-star-fill-black" viewBox="0 0 16 16">
                                        <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
                                    </svg>
                                </h3>
                                <p class="mb-2 mobile-view-hide mobile-rating-smaller-text-2"> <u> Average Rating </u> </p>
                                <p class="mb-2 mobile-view-show mobile-rating-smaller-text-2"> <u> Rating </u> </p>
                            </div>
                            <!-- would recommend -->
                            <div class="col-4 text-start mobile-col-3 mobile-ps-0 mobile-pe-0 text-color-black">
                                <h3 class="mobile-rating-smaller-text text-body-secondary rating-text" style="margin-bottom:0;"> <b> {{ willRecommend }}% </b> </h3>
                                <p class="mb-2 mobile-rating-smaller-text-2"> <u> Would Recommend </u> </p>
                                
                            </div>
                            <!-- would drink again -->
                            <div class="col-4 text-start mobile-col-3 mobile-ps-0 text-color-black">
                                    <h3 class="mobile-rating-smaller-text text-body-secondary rating-text" style="margin-bottom:0;"> <b> {{ willDrinkAgain }}% </b> </h3>
                                    <p class="mb-2 mobile-rating-smaller-text-2"> <u> Would Drink Again </u> </p>
                                    
                            </div>
                            <div class="mobile-col-3 mobile-view-show">
                                            <div v-if="userType == 'user' && userID !== 'defaultUser'" class="padding-for-addyourreviewbutton-large-screen mobile-view-show">
                                                <div v-if="!inEdit" class="d-grid gap-2">
                                                    <button class="btn primary-btn-less-round-blue btn-lg" data-bs-toggle="modal" data-bs-target="#reviewModal" style="font-weight:bold;">  <!--tzh added -blue -->
                                                        <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-plus" viewBox="0 0 16 16">
                                                            <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4"/>
                                                        </svg>
                                                    </button>
                                                </div>
                                                <div v-else class="d-grid gap-2">
                                                    <button class="btn primary-btn-less-round-blue btn-lg mobile-rating-smaller-text-2">   <!--tzh added -blue -->
                                                        Review added
                                                    </button>
                                                </div>
                                            </div>
                                            <div v-else-if="userType == 'user'" class="col-5 mobile-view-hide">
                                                <div class="d-grid gap-2">
                                                    <router-link :to="{ path: '/login' }" class="reverse-clickable-text">
                                                        <button class="btn primary-btn-less-round-blue btn-lg mobile-rating-smaller-text-2">   <!--tzh added -blue -->
                                                            Login to leave Review
                                                        </button>

                                                    </router-link>
                                                </div>
                                            </div>
                                    
                            </div>
                        </div>
                    </div>

                    <!-- Delete listing modal -->
                    <div class="modal fade" id="deleteListingModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                        <div class="modal-dialog">
                            
                            <!-- DELETE SUCCESS -->
                            <div class="text-success fst-italic fw-bold fs-3 modal-content" v-if='successDeleteListing'>
                                <span>Your listing has successfully been deleted!</span>
                                <div class="modal-footer">
                                    <button type="button" @click="reloadRouteHome" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                </div>
                            </div>
                            <!-- DELETE ERROR -->
                            <div class="text-danger fst-italic fw-bold fs-3 modal-content" v-if="errorDeleteListing"> 
                                <div v-if="errorDeleteMessage" class="row"> 
                                    <span >An error occurred while attempting to delete, please try again!</span>
                                    <br>
                                    <button class="btn primary-btn btn-sm" @click="reloadRoute">
                                        <span class="fs-5 fst-italic"> Retry your delete request here! </span>
                                    </button>
                                </div>
                                
                                <span v-if="listingNotExist">There is no review by you for this bottle listing!</span>
                                <br>

                            
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                </div>
                            </div>

                            <!-- DELETE IN PROGRESS MODAL -->
                            <div v-if="deletingListing" class="modal-content">
                                <div class="modal-header" style="background-color: #535C72">
                                    <h5 class="modal-title" id="deleteListing" style="color: white;">Delete Listing</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                </div>
                                <div class="modal-body">
                                    Are you sure you want to delete this listing?
                                </div>
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                    <button type="button" class="btn btn-danger" @click="deleteListings(specified_listing)">Delete Listing</button>
                                </div>
                            </div>
                        </div>
                    </div>
                    <!-- END of delete review modal -->


                    <!-- add your review -->
                    <!-- Display Add review or Review already added accordingly to whether user already left review -->
                    <div v-if="userType == 'user' && userID !== 'defaultUser'" class="col-5 padding-for-addyourreviewbutton-large-screen mobile-view-hide">
                        <div v-if="!inEdit" class="d-grid gap-2">
                            <button class="btn primary-btn-less-round-blue btn-lg" data-bs-toggle="modal" data-bs-target="#reviewModal" style="font-weight:bold;"> 
                                <!---<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-plus" viewBox="0 0 16 16">
                                    <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4"/>
                                </svg>-->
                                + Add Your Review
                            </button>
                        </div>
                        <div v-else class="d-grid gap-2">
                            <button class="btn primary-btn-less-round btn-lg"> 
                                Review already added
                            </button>
                        </div>

                    </div>
                    <div v-if="userID == 'defaultUser'" class="col-5 mobile-view-hide">
                        <div class="d-grid gap-2">
                            <router-link :to="{ path: '/login' }" class="reverse-clickable-text">
                                <button class="btn primary-btn-less-round btn-lg"> 
                                    Login to leave a Review
                                </button>

                            </router-link>
                        </div>
                    </div>
                </div>

                <!-- popular flavorTag -->
                <div class="row pt-3 mobile-pt-2 container">
                    <div class="text-start mb-2 mobile-mb-0 text-color-black">
                        
                        <!-- flavor tag -->
                        <span v-for="(count, tag) in sorted_flavorTagCounts" :key="tag" class="badge rounded-pill me-2" :style="{ backgroundColor: '#' + tag.split('#')[1] }">{{ tag.split('#')[0] }}</span>
                        <p class="mb-2 mobile-rating-smaller-text-2"> <u> Most Popular Flavour Tags </u> </p>
                    </div>
                </div>

                <!-- popular observationTag -->
                <div class="row pt-3 container mobile-pt-2">
                    <div class="text-start mb-2 mobile-mb-0 text-color-black">
                        
                        <!-- flavor tag -->
                        <span v-for="(count, tag) in sorted_observationTagCounts" :key="tag" class="badge rounded-pill me-2" style="background-color: grey" >{{ tag }}</span>
                        <p class="mb-2 mobile-rating-smaller-text-2"> <u> Most Popular Action Tags </u> </p>
                    </div>
                </div>
                    
                <!-- Modal -->
                <div v-if="userID != 'defaultUser'" class="modal fade" id="reviewModal" tabindex="-1" aria-labelledby="reviewModalLabel" aria-hidden="true" data-bs-backdrop="static">
                    <div class="modal-dialog modal-lg">
                        <div class="text-success fst-italic fw-bold fs-3 modal-content" v-if='successSubmission'>
                            <span v-if="!inEdit">Your review has successfully been submitted!</span>
                            <span v-else>Your review has successfully been updated!</span>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" @click="reloadRoute" data-bs-dismiss="modal">Close</button>
                            </div>
                        </div>

                        <div class="text-danger fst-italic fw-bold fs-3 modal-content" v-if="errorSubmission"> 
                            <div v-if="errorMessage" class = "row"> 
                                <span v-if="!inEdit">An error occurred while attempting to submit, please try again!</span>
                                <span v-else>An error occurred while attempting to update, please try again!</span>
                                <br>
                                <button class="btn primary-btn btn-sm" @click="reset">
                                    <span class="fs-5 fst-italic"> Retry your submission here! </span>
                                </button>
                            </div>
                            <div v-if="duplicateEntry">
                                <span v-if="!inEdit">You've already submitted a review for this bottle listing!</span>
                                <span v-else>There is no review for this bottle listing!</span>
                            </div>
                            <br>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                            </div>
                        </div>
                        <!-- tzh xyz -->
                        <div v-if='addingReview' class="modal-content">
                            <!-- change modal header colour -->
                            <div class="modal-header" style="background-color: #535C72">
                                <!-- V-if to edit or add review -->
                                <h5 v-if="!inEdit" class="modal-title" id="reviewModalLabel" style="color: white;">Add Your Review</h5>
                                <h5 v-else class="modal-title" id="reviewModalLabel" style="color: white;">Edit Your Review</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>

                            <!-- This is where modal starts for review-->
                            <div class="modal-body px-4">
                                <!-- row 0: expression name for mobile only -->
                                <div class="row mobile-view-show ">
                                    <p class="text-body-secondary text-start"><b> {{ specified_listing["listingName"] }} </b></p>
                                </div>
                                <!-- row 1: language, location -->
                                <div class="row mobile-view-hide">
                                    <!-- language-->
                                    <div class="col-6 col-md-12 justify-content-start mb-3">
                                        <p class = 'text-start mb-2 fw-bold'>Language<span class="text-danger">*</span></p>
                                        <div class="input-group">                                                    
                                            <select v-model="selectedLanguage" class="form-select" id="inputGroupSelect01">
                                                <!-- Add in the languages here -->
                                                <option v-for="language in languages" v-bind:key="language['_id']">{{ language['language'] }}</option>
                                            </select>
                                        </div>
                                        <div v-if="nullSelectedLanguage" class ="col-md-12">
                                            <p class='text-danger text-start mb-2 fw-bold'>Please select a language</p>
                                        </div>
                                    </div>

                                </div>



                                <!-- row 4A: add photo, friends, location-->
                                <div class="row " >
                                    <div class="col-3 mobile-col-4">
                                        <input class="form-control mb-2" @change="onFileChange" type="file" id="reviewPhoto" style="display: none;">
                                        <label for="reviewPhoto" >
                                            <div class="mobile-review-svg-button">
                                                <svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="0 0 24 24" fill="none" stroke="#000000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><path d="M20.4 14.5L16 10 4 20"></path> <circle cx="19" cy="19" r="3" fill="black"></circle><line x1="18" y1="19" x2="20" y2="19" stroke="white" stroke-width="1"></line><line x1="19" y1="18" x2="19" y2="20" stroke="white" stroke-width="1"></line></svg>
                                            </div>
                                        </label>
                                        <div class = "row">
                                            <img :src="selectedImage || (image64 )" alt="" id="output" class="py-2 review-preview-photo">
                                        </div>
                                        <div class="row justify-content-start mb-2">
                                            <div class="col-md-4 text-start">
                                                <button v-if="image64!==null" class="btn tertiary-square-btn mb-1" @click="clearPhoto">Clear Photo</button>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-9 mobile-col-8">
                                        
                                        <div class="col-12 justify-content-start">
                                            
                                            <div class="form-group mb-2 mobile-mt-0 mt-3">
                                                <div v-if="showFriendTagList.length > 0" class="form-label pb-2 text-start"> 
                                                Tagged Friends: 
                                                    <div class="row">
                                                        <div class="col">
                                                            <div class="d-flex flex-wrap gap-2">
                                                                <div v-for="friend in showFriendTagList" v-bind:key="friend.id" class="mb-0 pb-0">
                                                                    <button @click='removeFriendTag(friend)' class="btn secondary-square-btn"> {{ friend.username }} </button> 
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                                <!-- <input type="text" class="form-control" id="friendTag"> -->
                                                <input list="followList" v-model="friendTag" class="form-control input-with-icon" id="friendTag" placeholder="Tag friends" v-on:keyup="updateFriendTag">
                                                <datalist id="followList">
                                                    <option v-for="user in followList" :key="user.id" :value="user.username">
                                                        {{user.username}}
                                                    </option>
                                                </datalist>  
                                                <div class="text-start mt-1">                                            
                                                    <button v-if="selectedFriendTag!==null" class="btn tertiary-square-btn mt-1" @click="tagSpecificFriend">Tag This Friend</button>
                                                </div>  
                                                <p v-show="friendTag.length > 0" class="text-start mb-1 text-danger" id="friendTagError"></p>
                                            </div>

                                            <div class="form-group mb-2">
                                                
                                                <div class="input-group mb-2">
                                                    <GMapAutocomplete
                                                        placeholder="Add location"
                                                        @place_changed="setPlace"
                                                        class="form-control input-with-icon"
                                                        ref="autocomplete"
                                                        :value="selectedLocation"
                                                    >
                                                    </GMapAutocomplete>
                                                </div>
                                                <div>
                                                    <p v-show="tagLocation.length > 0" class="text-start mb-1 text-danger" id="tagLocationError"></p>
                                                </div>
                                                <div class="row">
                                                    <div class="col-6 col-md-12 d-flex justify-content-start">
                                                        <button v-if="selectedLocation!==''" class="btn text-start mb-1" style="background-color: #535C72;color: white;" @click="clearLocation">Clear Selection</button>
                                                    </div>
                                                    
                                                </div>
                                            </div>
                                        </div>


                                    </div>
                                </div>  

                                <!-- row 3: review -->
                                <div class="row">
                                    <div class = 'col justify-content-start mb-3'>
                                        <div class = "col-md-12">
                                            <p class='text-start mb-2 fw-bold'>Review<span class="text-danger">*</span></p>
                                            <textarea v-model="reviewDesc" class="form-control" id="reviewTextarea" rows="3" placeholder="Min 20 characters"></textarea>
                                        </div>
                                        <div v-if="reviewDescError!==''" class ="col-md-12">
                                            <p class='text-danger text-start mb-2 fw-bold'>{{ reviewDescError }}</p>
                                        </div>
                                    </div>
                                </div>

                                  
                              
                                <!-- row 4: buttons (would recommend, would buy again) -->
                                <div class="row">
                                    <div class = 'col justify-content-start mb-3 text-start'>
                                        <div class = "col-md-12">
                                            <div class="form-check form-check-inline">
                                                <input class="form-check-input" type="checkbox" id="inlineCheckbox1" v-model="wouldRecommend" value="option1">
                                                <label class="form-check-label text-start fw-bold" for="inlineCheckbox1">Would Recommend</label>
                                            </div>
                                            <div class="form-check form-check-inline">
                                                <input class="form-check-input" type="checkbox" id="inlineCheckbox2" v-model="wouldBuyAgain" value="option2">
                                                <label class="form-check-label text-start fw-bold" for="inlineCheckbox2">Would Buy Again</label>
                                            </div>                                                                                                   
                                        </div>                                         
                                    </div>
                                </div>
                                

                                <!-- row 5: extend review -->
                                <div class="row">
                                    <!-- Buttons to expand -->
                                    <div v-if="!extendReview" class = 'col justify-content-start mb-3 text-start'>
                                        <div class = "col-md-12 text-center">
                                            <button class="btn primary-btn-less-round btn-sm" @click="controlModal"> 
                                                Extend Review <span style="color: white;">&#9660;</span>
                                            </button>                                                                  
                                        </div>                                         
                                    </div>
                                    <!-- Button to collapse -->
                                    <div v-if="extendReview" class = 'col justify-content-start mb-3 text-start'>
                                        <div class = "col-md-12 text-center">
                                            <button class="btn primary-btn-less-round btn-sm" @click="controlModal"> 
                                                Condense Review <span style="color: white;">&#9650;</span>
                                            </button>                                                                  
                                        </div>                                         
                                    </div>
                                </div>

                                <!-- row 6: section breaker (horizontal line) -->
                                <div class="row">
                                    <!-- Dashed line -->
                                    <div class = 'col justify-content-start mb-1 text-start'>
                                        <div class = "col-md-12 text-center">
                                            <p class="dotted-line">
                                            </p>
                                        </div>
                                    </div>
                                </div>

                                

                                <!-- TOGGLEABLE SECTION -->
                                <div v-if="extendReview">

                                    <!-- row 7: colours -->
                                    <div class="row">
                                        <div class="col-6 col-md-12 justify-content-start">
                                            <p class = 'text-start mb-2 fw-bold'>Colour</p>
                                        </div>
                                    </div>

                                    <!-- row 7A: selected colours  -->
                                    <div class="row">
                                        <div v-if="selectedColour=== ''" class="col-md-2"></div>
                                            <div v-else-if="selectedColour.includes('#')" class="col-md-1">
                                                <button class="btn text-start mb-1" :style="{ 
                                                                width: '30px', 
                                                                height: '30px', 
                                                                backgroundColor: selectedColour, 
                                                                color: selectedColour, 
                                                                borderRadius: '0', 
                                                                borderColor:'grey', 
                                                                borderWidth:'1px'
                                                            }"></button>
                                            </div>
                                            <div v-else class="col-md-1">
                                                <button class="btn text-start mb-1" :style="{ width: '30px', height: '30px', borderRadius: '0', borderColor:'grey', borderWidth:'1px', backgroundImage: `linear-gradient(to bottom right, ${specialColours[selectedColour][0]}, ${specialColours[selectedColour][1]}`}"></button>
                                            </div>
                                            <div v-if="selectedColour!== ''" class="col-md-4">
                                                <button @click="clearColour" class="btn text-start mb-1" style="background-color: #535C72;color: white;">Clear Selection</button>
                                            </div>
                                    </div>

                                    <!-- row 7B: all colours -->
                                    <div class="row justify-content-start mb-1 text-start">
                                        <!-- normal colours-->
                                        <div class="col-7 mobile-col-9">
                                            <button @click="displaySelectColour(colour)" v-for="(colour, i) in colours.slice(0, 14)" :key="i" :value="colour" class="btn" data-bs-toggle="button"
                                                    :style="{ 
                                                        width: '30px', 
                                                        height: '30px', 
                                                        backgroundColor: colour, 
                                                        color: colour, 
                                                        borderRadius: '0', 
                                                        borderColor:'grey', 
                                                        borderWidth:'1px'
                                                    }">                                
                                            </button>
                                        </div>
                                        <!-- Special gradient -->
                                        <div class="col-md-5 col-12">
                                            <button @click="displaySelectColour(key)" v-for="(value, key) in specialColours" :key="key" type="button" :value="key" class="btn" data-bs-toggle="button" :style="{ width: '30px', height: '30px', borderRadius: '0', borderColor:'grey', borderWidth:'1px', backgroundImage: `linear-gradient(to bottom right, ${value[0]}, ${value[1]}`}">                                
                                            </button>
                                        </div>
                                    </div>

                                    <!-- row 8: aroma, taste and finish -->
                                    <div class="row pt-2">
                                        <div class = 'col justify-content-start mb-3'>
                                            <div class="form-group mb-3">
                                                <p class='text-start mb-2 fw-bold'>Aroma</p>
                                                <input v-model="aroma" type="text" class="form-control" id="aroma">
                                            </div>
                                            <div class="form-group mb-3">
                                                <p class='text-start mb-2 fw-bold'>Taste</p>
                                                <input v-model="taste" type="text" class="form-control" id="taste">
                                            </div>
                                            <div class="form-group mb-2">
                                                <p class='text-start mb-2 fw-bold'>Finish</p>
                                                <input v-model="finish" type="text" class="form-control" id="finish">
                                            </div>
                                        </div>
                                    </div>

                                </div> <!-- end of v-if check for extendReview -->

                                <!-- row 9: rating -->
                                <div class="row">
                                    <div class="col-md-5 mb-3"> 
                                        <div class="row align-items-center text-start">
                                            <p class='text-star mb-1 fw-bold'>Rating<span class="text-danger">*</span></p>
                                            <label for="customRange2" class="form-label"> Selected: {{ rating }} 
                                            </label>
                                            <div class="col-auto">
                                                <label for="customRange" class="form-label fw-bold">1</label>
                                            </div>
                                            <div class="col">
                                                <input v-model="rating" type="range" class="form-range" min="1" max="10" step="0.1" id="customRange">
                                            </div>
                                            <div class="col-auto">
                                                <label for="customRange" class="form-label fw-bold">10</label>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <!-- row 10: flavour tags -->
                                <div class="row">
                                    <div class="form-group mb-3 text-start">
                                        <p class="text-start mb-1 fw-bold">Flavour Tags</p> 
                                        <div v-if="selectedFlavourTags.length > 0" class="form-label pb-2"> 
                                            Selected flavour tags: 
                                            <div class="row">
                                                <div class="col">
                                                    <div class="d-flex flex-wrap gap-2">
                                                        <div v-for="flavourTag in selectedFlavourTags" v-bind:key="flavourTag" class="mb-0 pb-0">
                                                            
                                                            <button v-if="flavourTag == '<deleted>'" :style="{ color:'white', backgroundColor: '#030303' }" class="btn"> {{ flavourTag }} </button> 
                                                            <button v-else :style="{ color:'white', backgroundColor: '#' + flavourTag.split('#')[1] }" class="btn"> {{ flavourTag.split("#")[0] }} </button> 
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        Select flavour tags:
                                        <br>
                                        <button class="btn mb-2 me-2" @click="toggleBox(family)" v-for="family in flavourTags" v-bind:key="family['_id']" :style="{ color:'white', backgroundColor: family['hexcode'], borderColor:family['hexcode'], borderWidth:'1px' }">{{ family['familyTag'] }}</button>
                                        <!-- This is the container/dropdown box for the subtags -->
                                        <div v-for="family in flavourTags" :key="family['_id']">
                                            <div v-if="family.showBox" class="rounded p-3" :style="{border: '3px solid ' + family['hexcode'] }">
                                                <div class="row">
                                                    <div class="col-3 mobile-px-1" v-for="(element, index) in family.subTag2" :key="index">
                                                        <button @click="toggleFlavourSelection(element.subTag, family['hexcode'],element.id)" class="btn mb-2 sub-flavour-tags mobile-px-1" :style="{ backgroundColor: selectedFlavourTags.includes(element.subTag+family['hexcode']) ? 'grey' :family['hexcode'], borderColor: family['hexcode'] }">{{ element.subTag }}</button>
                                                    </div>                        
                                                </div>
                                            </div>
                                        </div>
                                        <!-- End of dropdown -->
                                    </div>
                                </div>

                                <!-- row 11: observation tags -->
                                <div class="row">
                                    <div class="form-group mb-3 text-start">
                                        <p class="text-start mb-1 fw-bold">Action Tags</p>
                                        <div v-if="selectedObservations.length > 0" class="form-label pb-2"> 
                                            Selected action tags: 
                                            <div class="row">
                                                <div class="col">
                                                    <div class="d-flex flex-wrap gap-2">
                                                        <div v-for="observationTag in selectedObservations" v-bind:key="observationTag" class="mb-0 pb-0">
                                                            <button style="background-color: lightgrey;" class="btn"> {{ observationTag.split("#")[0] }} </button> 
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        Select action tags: 
                                        <br>
                                        <!-- Buttons for the first 8 observations -->
                                        <button v-for="observation in observationTags.slice(0, 8)" @click="toggleObservationSelection(observation)" v-bind:key="observation" class="btn mb-2 me-2" data-bs-toggle="button" :style="{ color: selectedObservations.includes(observation) ? 'white' : 'black',
                                                                                                                                                                                                                                    backgroundColor: selectedObservations.includes(observation) ? '#747D92' : 'lightgrey', 
                                                                                                                                                                                                                                    borderColor:'grey', 
                                                                                                                                                                                                                                    borderWidth:'1px' }">
                                            {{ observation }}
                                        </button>
                                        <!-- Buttons for additional observations (shown only when extendObservation is true) -->
                                        <div v-if="extendObservation">
                                            <button v-for="observation in observationTags.slice(8)" @click="toggleObservationSelection(observation)" v-bind:key="observation" class="btn mb-2 me-2" :style="{ color: selectedObservations.includes(observation) ? 'white' : 'black',
                                                                                                                                                                                                                                    backgroundColor: selectedObservations.includes(observation) ? '#747D92' : 'lightgrey', 
                                                                                                                                                                                                                                    borderColor:'grey', 
                                                                                                                                                                                                                                    borderWidth:'1px' }">
                                                {{ observation }}
                                            </button>
                                        </div>
                                        <!-- Button to toggle between View All and View Less -->
                                        <button @click="toggleObservations" class="btn mt-2" style="color:black; background-color:white; border-color:black; border-width: 1px;" v-if="!extendObservation">
                                            View All
                                        </button>
                                        <button @click="toggleObservations" class="btn mt-2" style="color:black; background-color:white; border-color:black; border-width: 1px;" v-else>
                                            View Less
                                        </button>
                                    </div>
                                </div>

                            </div>
                            
                            <!-- End of modal body -->
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                <button v-if="!inEdit" type="button" @click="addReview" class="btn primary-square">Submit Review</button>
                                <button v-else type="button" @click="editReview" class="btn primary-btn">Update Review</button>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- END OF MODAL -->

                
                <!-- reviews -->
                <!-- TODO  EDIT MODAL IF NOT DOING COMPONENT-->
                <div class="container no-right-padding-large-screen">
                    <hr> 
                    
                    <!-- photos posted by other users -->
                    <div class="row text-start" style="padding-left:1.5em;">
                        <div class="col">
                            <div class="justify-content-start row">
                                <!-- [if] user has not added a review yet, add new photo -->
                                <div v-if="userType == 'user' && userID !== 'defaultUser' && !inEdit" class="row">
                                    <!-- (1) add button -->
                                    <div class="mobile-col-3 col-sm-6 col-md-4 col-lg-2 mobile-px-1">
                                        <div data-bs-toggle="modal" data-bs-target="#reviewModal">
                                            <svg xmlns="http://www.w3.org/2000/svg"  fill="#83A9E8" class="bi bi-plus-lg review-image" viewBox="0 0 16 16"> <!--tzh changed currentColor to 83A9E8-->
                                                <path fill-rule="evenodd" d="M8 2a.5.5 0 0 1 .5.5v5h5a.5.5 0 0 1 0 1h-5v5a.5.5 0 0 1-1 0v-5h-5a.5.5 0 0 1 0-1h5v-5A.5.5 0 0 1 8 2"/>
                                            </svg>
                                        </div>
                                    </div>
                                    <!-- (2) to (6) other photos -->
                                    <div v-for="review in filteredReviewsWithImages.slice(0,5)" v-bind:key="review" class="mobile-col-3 col-sm-8 col-md-6 col-lg-2 mobile-px-1">
                                        <img :src=" (review['photo'] || defaultPhoto)" alt="" class="review-image" >
                                    </div>
                                </div>
                                <!-- [else] user has added a review -->
                                <!-- (1) to (6) display all photos -->
                                <div v-else class="row">
                                    <div v-for="review in filteredReviewsWithImages" v-bind:key="review" class="mobile-col-3 col-sm-8 col-md-6 col-lg-2 p-0 mobile-px-1">
                                        <img :src="(review['photo'] || defaultPhoto)" alt="" class="review-image" >
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <hr>

                    <div class="row mb-3" v-for="review in filteredReviews" v-bind:key="review.id">


                        <!-- user reviews -->
                        
                            <div class="col-9 xcol-lg-8">
                                <div class="row">
                                    <div class="text-start mb-2 ">
                                    <div class="row">    
                                        <!-- profile photo -->
                                        <div class="col-12 col-lg-1 mobile-col-2" style="text-align: left;">
                                            <router-link :to="`/profile/user/${review.userID}`">
                                                <img :src="(getPhotoFromReview(review) || defaultProfilePhoto)" alt="" class="profile-image">
                                            </router-link>
                                        </div>
                                        <div class="col-10 pe-0 mobile-fs-7 mobile-ps-4">
                                            <!-- username -->
                                            <router-link :to="`/profile/user/${review.userID}`" style="color: inherit">
                                                <b>
                                                    @{{ getUsernameFromReview(review) }}
                                                </b>
                                            </router-link>

                                            <!-- rating -->
                                            &nbsp;rated {{ review['rating'] }}
                                            
                                            <!-- star icon -->
                                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-star-fill me-1" viewBox="0 0 16 16">
                                                <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
                                            </svg>
                                            
                                            <!-- location -->
                                            
                                            <span v-if="review.location !== '' && checkVenue(review.address)">
                                                <a style="color: inherit" > 
                                                    at
                                                    <router-link :to="'/profile/venue/' + checkVenue(review.address)" style="color: inherit">
                                                        <b>{{ getVenueNameFromID(review.location) }}</b>
                                                    </router-link>
                                                </a>
                                            </span>

                                            <span v-else-if="review.location">
                                                at 
                                                <a :href="'https://www.google.com/maps/search/' + review.location" style="color: inherit" target="_blank"> 
                                                    <b>{{ review.location }}</b>
                                                </a>
                                            </span>

                                            <!-- tagged friends -->
                                            <span v-if="review.taggedUsers != null && review.taggedUsers.length > 0"> drank with {{ review.taggedUsers.length }} others </span>

                                            <!-- user title -->
                                            <span v-if="checkModFromUserID(review.userID)" class="badge rounded-pill ms-3 mobile-ms-0 mobile mt-1" style="color: black; background-color: white;">Moderator</span>
                                            
                                            <!-- Insert Edit modal here -->
                                            <div class="mt-2 mobile-mt-1">
                                                <button v-if="review.userID === parseInt(userID)"  class="btn btn-warning me-1 py-1  mobile-fs-7" @click="setUpdateID(review)" data-bs-toggle="modal" data-bs-target="#reviewModal">Edit</button>
                                                <button v-if="review.userID === parseInt(userID) || correctModerator" class="btn btn-danger py-1  mobile-fs-7" @click="setDeleteID(review)" data-bs-toggle="modal" data-bs-target="#deleteReview">Delete</button>
                                            </div>
                                        </div>    
                                    </div>
                                    </div>
                                    <div class="text-start mb-2">
                                        {{ review['reviewDesc'] }}
                                    </div>
                                    
                                    <!-- flavour tag -->
                                    <div class="text-start mb-2">
                                        <!-- flavor tag -->
                                            <span v-for="(tag, index) in review.flavourTag" :key="index" class="badge rounded-pill me-2" :style="{ backgroundColor: getTagColor(parseInt(tag)) }">{{ getTagName(parseInt(tag)) }}</span>
                                            <span v-for="(tag, index) in review.observationTag" :key="index" class="badge rounded-pill me-2" style="background-color: grey;">{{ tag }}</span>
                                    </div>
                                    <div style="display: inline;" class="text-start">
                                        <!-- voting -->
                                        <svg v-if="!JSON.stringify(review.userVotes.upvotes).includes(JSON.stringify(userID))" @click="voteReview(review, 'upvote')" xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-caret-up" viewBox="0 0 16 16">
                                            <path d="M3.204 11h9.592L8 5.519zm-.753-.659 4.796-5.48a1 1 0 0 1 1.506 0l4.796 5.48c.566.647.106 1.659-.753 1.659H3.204a1 1 0 0 1-.753-1.659"/>
                                        </svg>
                                        <svg v-else @click="voteReview(review, 'unupvote')" xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-caret-up-fill" viewBox="0 0 16 16">
                                            <path d="m7.247 4.86-4.796 5.481c-.566.647-.106 1.659.753 1.659h9.592a1 1 0 0 0 .753-1.659l-4.796-5.48a1 1 0 0 0-1.506 0z"/>
                                        </svg>
                                        <span class="mx-2">{{ review.userVotes.upvotes.length - review.userVotes.downvotes.length }}</span>
                                        <svg v-if="!JSON.stringify(review.userVotes.downvotes).includes(JSON.stringify(userID))" @click="voteReview(review, 'downvote')" xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-caret-down me-3" viewBox="0 0 16 16">
                                            <path d="M3.204 5h9.592L8 10.481zm-.753.659 4.796 5.48a1 1 0 0 0 1.506 0l4.796-5.48c.566-.647.106-1.659-.753-1.659H3.204a1 1 0 0 0-.753 1.659"/>
                                        </svg>
                                        <svg v-else @click="voteReview(review, 'undownvote')" xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-caret-down-fill me-3" viewBox="0 0 16 16">
                                            <path d="M7.247 11.14 2.451 5.658C1.885 5.013 2.345 4 3.204 4h9.592a1 1 0 0 1 .753 1.659l-4.796 5.48a1 1 0 0 1-1.506 0z"/>
                                        </svg>
                                        <a href="#" class="text-decoration-underline text-secondary" data-bs-toggle="modal" data-bs-target="#detailedReviewModal" @click="updateDetailedReview(review)">Detailed Review ></a>
                                    </div>

                                    <!-- Delete review modal -->
                                    <div class="modal fade" id="deleteReview" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                                        <div class="modal-dialog">
                                            
                                            <!-- DELETE SUCCESS -->
                                            <div class="text-success fst-italic fw-bold fs-3 modal-content" v-if='successDelete'>
                                                <span>Your review has successfully been deleted!</span>
                                                <div class="modal-footer">
                                                    <button type="button" @click="reloadRoute" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                                </div>
                                            </div>
                                            <!-- DELETE ERROR -->
                                            <div class="text-danger fst-italic fw-bold fs-3 modal-content" v-if="errorDelete"> 
                                                <div v-if="errorDeleteMessage" class="row"> 
                                                    <span >An error occurred while attempting to delete, please try again!</span>
                                                    <br>
                                                    <button class="btn primary-btn btn-sm" @click="reset">
                                                        <span class="fs-5 fst-italic"> Retry your delete request here! </span>
                                                    </button>
                                                </div>
                                                
                                                <span v-if="notExist">There is no review by you for this bottle listing!</span>
                                                <br>

                                            
                                                <div class="modal-footer">
                                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                                </div>
                                            </div>

                                            <!-- DELETE IN PROGRESS MODAL -->
                                            <div v-if="deletingReview" class="modal-content">
                                                <div class="modal-header" style="background-color: #535C72">
                                                    <h5 class="modal-title" id="deleteReview" style="color: white;">Delete Review</h5>
                                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                                </div>
                                                <div class="modal-body">
                                                    Are you sure you want to delete your review?
                                                </div>
                                                <div class="modal-footer">
                                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                                    <button type="button" class="btn btn-danger" @click="deleteReview">Delete Review</button>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <!-- END of delete review modal -->
                                </div>
                                <!-- detailed review modal start -->
                                <div class="modal fade" id="detailedReviewModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                                    <div class="modal-dialog">
                                        <div class="modal-content">
                                        <div class="modal-header">
                                            <h1 class="modal-title fs-5" id="exampleModalLabel">{{ specified_listing["listingName"] }} Review</h1>
                                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                        </div>
                                        <div class="modal-body text-start">
                                            <!-- username -->
                                            <div class="row">
                                                <div class="col-3">
                                                    <b>Username</b>
                                                </div>
                                                <div class="col-9">
                                                    <b>
                                                        @<router-link :to="`/profile/user/${detailedReview.userID}`" style="text-decoration-color: #535C72;">
                                                            <span class="default-clickable-text">
                                                                {{ getUsernameFromReview(detailedReview) }}
                                                            </span>
                                                        </router-link>
                                                    </b>
                                                </div>
                                            </div>
                                            <!-- rating -->
                                            <div class="row mt-2">
                                                <div class="col-3">
                                                    <b>Rating</b>
                                                </div>
                                                <div class="col-9">
                                                    {{ detailedReview.rating }}
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-star-fill me-3" viewBox="0 0 16 16">
                                                        <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
                                                    </svg>
                                                </div>
                                            </div>
                                            <!-- review -->
                                            <div class="row mt-2">
                                                <div class="col-3">
                                                    <b>Review</b>
                                                </div>
                                                <div class="col-9">
                                                    {{ detailedReview.reviewDesc }}
                                                </div>
                                            </div>
                                            <!-- location -->
                                            <div class="row mt-2">
                                                <div class="col-3">
                                                    <b>Location</b>
                                                </div>
                                                <div class="col-9">
                                                    <span v-if="detailedReview.location !== '' && checkVenue(detailedReview.location)">
                                                        <a style="color: inherit" >
                                                            <router-link :to="'/profile/venue/' + checkVenue(detailedReview.location)" style="color: inherit">
                                                                <b>{{ detailedReview.location }}</b>
                                                            </router-link>
                                                        </a>
                                                    </span>

                                                    <span v-else-if="detailedReview.location !== ''">
                                                        <a :href="'https://www.google.com/maps/search/' + detailedReview.location" style="color: inherit" target="_blank"> 
                                                            <b>{{ detailedReview.location }}</b>
                                                        </a>
                                                    </span>
                                                    <span v-else>-</span>
                                                </div>
                                            </div>
                                            <!-- feedback -->
                                            <div class="row mt-2">
                                                <div class="col-3">
                                                    <b>Feedback</b>
                                                </div>
                                                <div class="col-9">
                                                    <div v-if="detailedReview.willRecommend || detailedReview.wouldBuyAgain">
                                                        <div v-if="detailedReview.willRecommend">Would Recommend</div>
                                                        <div v-if="detailedReview.wouldBuyAgain">Would Buy Again</div>
                                                    </div>
                                                    <div v-else>-</div>
                                                </div>
                                            </div>
                                            <!-- more information -->
                                            <hr>
                                            <h5 class="text-center">More Information</h5>
                                            <hr>
                                            <!-- colour -->
                                            <div class="row mt-2">
                                                <div class="col-3">
                                                    <b>Colour</b>
                                                </div>
                                                <div class="col-9">
                                                    <div v-if="detailedReview.colour" :style="{ width: '24px', height: '24px', backgroundColor: detailedReview.colour }"></div>
                                                    <div v-else>-</div>
                                                </div>
                                            </div>
                                            <!-- aroma -->
                                            <div class="row mt-2">
                                                <div class="col-3">
                                                    <b>Aroma</b>
                                                </div>
                                                <div class="col-9">
                                                    <div v-if="detailedReview.aroma">
                                                        {{ detailedReview.aroma }}
                                                    </div>
                                                    <div v-else>-</div>
                                                </div>
                                            </div>
                                            <!-- aroma -->
                                            <div class="row mt-2">
                                                <div class="col-3">
                                                    <b>Taste</b>
                                                </div>
                                                <div class="col-9">
                                                    <div v-if="detailedReview.taste">
                                                        {{ detailedReview.taste }}
                                                    </div>
                                                    <div v-else>-</div>
                                                </div>
                                            </div>
                                            <!-- finish -->
                                            <div class="row mt-2">
                                                <div class="col-3">
                                                    <b>Finish</b>
                                                </div>
                                                <div class="col-9">
                                                    <div v-if="detailedReview.finish">
                                                        {{ detailedReview.finish }}
                                                    </div>
                                                    <div v-else>-</div>
                                                </div>
                                            </div>
                                            <!-- tags -->
                                            <hr>
                                            <h5 class="text-center">Tags</h5>
                                            <hr>
                                            <!-- friend tag -->
                                            <div class="row mt-2">
                                                <div class="col-3">
                                                    <b>Friend Tags</b>
                                                </div>
                                                <div class="col-9">
                                                    <span v-for="(user, index) in detailedReview.taggedUsers" :key="index">
                                                        <b>
                                                            @<router-link :to="`/profile/user/${user}`" style="text-decoration-color: #535C72;">
                                                                <span class="default-clickable-text">
                                                                    {{ getUsernameFromId(parseInt(user)) }}
                                                                </span>
                                                            </router-link>
                                                        </b>
                                                    </span>
                                                </div>
                                            </div>
                                            <!-- flavour tag -->
                                            <div class="row mt-2">
                                                <div class="col-3">
                                                    <b>Flavour Tags</b>
                                                </div>
                                                <div class="col-9">
                                                    <span v-for="(tag, index) in detailedReview.flavourTag" :key="index" class="badge rounded-pill me-2" :style="{ backgroundColor: getTagColor(parseInt(tag)) }">{{ getTagName(parseInt(tag)) }}</span>
                                                </div>
                                            </div>
                                            <!-- observation tag -->
                                            <div class="row mt-2">
                                                <div class="col-3">
                                                    <b>Action Tags</b>
                                                </div>
                                                <div class="col-9">
                                                    <span v-for="(tag, index) in detailedReview.observationTag" :key="index" class="badge rounded-pill me-2" style="background-color: grey;">{{ tag }}</span>
                                                </div>
                                            </div>


                                        </div>
                                        <div class="modal-footer">
                                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                            <!-- <button type="button" class="btn btn-primary">Save changes</button> -->
                                        </div>
                                        </div>
                                    </div>
                                </div>
                                <!-- modal end -->
                            </div>
                            <!-- review photo -->
                            <div class="col-2 xcol-lg-3 text-end mobile-view-hide">
                                <!-- review photo -->
                                <div data-bs-toggle="modal" :data-bs-target="`#reviewImageModal${getUsernameFromReview(review)}`" style=" cursor: pointer;"> 
                                    <img :src="(review['photo'] || defaultPhoto)" alt="" class="review-image" style="width: 125px; height: 125px">
                                </div>
                            </div>
                            <div class="col-3 xcol-lg-3 text-start mobile-view-show px-0">
                                <!-- review photo -->
                                <div data-bs-toggle="modal" :data-bs-target="`#reviewImageModal${getUsernameFromReview(review)}`" style=" cursor: pointer;"> 
                                    <img :src="(review['photo'] || defaultPhoto)" alt="" class="review-image" style="width: 125px; height: 125px">
                                </div>
                            </div>

                        <div  class="modal fade" :id="`reviewImageModal${getUsernameFromReview(review)}`" tabindex="-1" aria-labelledby="reviewModalLabel" aria-hidden="true">
                            <div class="modal-dialog modal-lg d-flex align-items-center" style="height: 100vh;">
                                <div class="modal-content">
                                    <div class="modal-body p-4">
                                        <img :src="(review['photo'] || defaultPhoto)" alt="" style="width:100%; height:auto;" >
                                    </div>    
                                </div>
                            </div>
                        </div>

                    <hr>
                    </div>
                
            </div> <!-- end of producer information -->


            </div>
            <!-- where to buy & where to try & 88 bamboo's review -->
            <div class="col-sm-12 col-md-9 col-lg-3 mobile-view-hide">
                <!-- where to buy -->
                <div class="row">
                    <div class="square primary-square-green rounded p-3 mb-3 text-start" style="height: 250px;">
                        <!-- header text -->
                        <div class="square-inline text-start">
                            <h4 class="mr-auto"> Where to Buy </h4>
                        </div>
                        <!-- body -->
                        <div style="height: 85%;">
                            <div class="text-start pt-2 overflow-auto" style="max-height: 100%;">
                                <!-- [function] where to buy -->
                                <div v-for="producer in producerListings" v-bind:key="producer">
                                    <router-link :to="{ path: '/profile/producer/' + producer }" class="reverse-clickable-text">
                                        <p> {{ getProducerName(producer) }} </p>
                                    </router-link>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- not sure what this line supposed to do -->
                <!-- {{ drinkList }} -->
            
                <!-- where to try -->
                <div class="row">
                    <div class="square primary-square-green rounded p-3 mb-3 text-start" style="height: 250px;">
                        <!-- header text -->
                        <div class="square-inline text-start">
                            <h4 class="mr-auto"> Where to Try </h4>
                        </div>
                        <!-- body -->
                        <div style="height: 85%;">
                            <div class="text-start pt-2 overflow-auto" style="max-height: 100%;">
                                <!-- [function] where to try -->
                                <!-- [if] user does not allow location -->
                                <div v-if="nearestBars.length == 0" >
                                    <div v-for="venue in venueListings" v-bind:key="venue.id">
                                        <router-link :to="{ path: '/profile/venue/' + venue.id }" class="reverse-clickable-text">
                                            <p class="mb-1"> {{ venue.venueName }} </p>
                                        </router-link>
                                    </div>
                                </div>
                                <!-- [else] user allows location -->
                                <div v-else>
                                    <div v-for="(distance, venueID) in nearestBars" v-bind:key="venueID">
                                        <router-link :to="{ path: '/profile/venue/' + venueID }" class="reverse-clickable-text">
                                            <p class="mb-4"> 
                                                <u> {{ getVenueNameFromID(venueID) }}  </u>
                                                <br>
                                                <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" fill="currentColor" class="bi bi-geo-alt-fill" viewBox="0 0 16 16">
                                                    <path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10m0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6"/>
                                                </svg>
                                                Distance: {{ venueDetails[venueID]["distance"] }}
                                                <br>
                                                <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" fill="currentColor" class="bi bi-clock" viewBox="0 0 16 16">
                                                    <path d="M8 3.5a.5.5 0 0 0-1 0V9a.5.5 0 0 0 .252.434l3.5 2a.5.5 0 0 0 .496-.868L8 8.71z"/>
                                                    <path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16m7-8A7 7 0 1 1 1 8a7 7 0 0 1 14 0"/>
                                                </svg>
                                                Duration: {{ venueDetails[venueID]["duration"] }}
                                            </p>
                                        </router-link>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- 88 bamboo's review -->
                <div class="row">
                    <div class="square primary-square-green-outline xsecondary-square rounded p-3 mb-3">
                        <!-- header text -->
                        <div class="py-2 text-start">
                            <h4> 88 Bamboo's Review </h4>
                            <a v-if="isHttpValid(specified_listing['reviewLink'])" :href="specified_listing['reviewLink']" class="text-left default-text-no-background row">
                                <div class="row">
                                    <div class="col-lg-4 col-md-6 col-sm-12">
                                        {{ getOGImage(specified_listing['reviewLink']) }}
                                        <!-- [if] there is a cover image for the post-->
                                        <img v-if="ogImage != null" :src="ogImage[specified_listing.reviewLink]" alt="OG Image" style="width: 80px; height: 80px;">
                                        <!-- [else] there is no cover image for the post (put 88 bamboo's logo) -->                    
                                        <img v-else src="https://88bamboo.co/cdn/shop/files/88B_New_Logo_-_white_face_transparent_background_180x.png?v=1655894111" style="width: 80px; height: 80px;">                                   
                                    </div>
                                    <div class="col-lg-8 col-md-12">
                                        {{ deepDiveLinkFormatted }}
                                    </div>
                                </div>
                            </a>
                            <div v-else>
                                <div class="text-body-secondary">
                                    <div class="fst-italic">
                                        No reviews available for this listing.
                                        For other 88 Bamboo reviews, 
                                        <a href="https://88bamboo.co/blogs/news" class="default-text-no-background">click here</a>.
                                    </div>
                                </div>
                            </div>

                        </div>
                        <div class="py-2"></div>
                    </div>
                </div>
            </div>
        </div>
        <BookmarkModal 
            v-if="user" 
            :user="user" 
            :listings="listings" 
            :listingID="bookmarkListingID" />
    
        </div> <!-- end of your drinks shelf & brands you follow -->

    
    

</template>

<!-- ---------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<!-- JavaScript -->
<script>
    import NavBar from '@/components/NavBar.vue';
    // import ReviewModal from '@/components/EditReview.vue'
    import BookmarkIcon from '@/components/BookmarkIcon.vue';
    import BookmarkModal from '@/components/BookmarkModal.vue';
    
    export default {
        // setup(){

        // },
        // components:{ReviewModal},
        components: {
            NavBar,
            BookmarkIcon, 
            BookmarkModal
        },
        data() {
            return {
                dataLoaded: false,
                listingExists: true,
                // data from database
                countries: [],
                listings: [],
                producers: [],
                reviews: [],
                users: [],
                venues: [],
                venuesAPI: [],
                drinkTypes: [],
                requestListings: [],
                requestEdits: [],
                modRequests: [],
                acctype:null,

                // search
                search: false,
                searchInput: '',
                searchTerm: '',
                searchResults: [],
                filteredListings: [],
                filteredReviews:[],
                filteredReviewsWithImages: [],


                // specified listing listing_id used for createReview
                listing_id: null,
                specified_listing: {},
                specificReviewRating:"",
                willRecommend: null,
                willDrinkAgain: null,

                // to toggle moderator lock
                inToggle: true,
                toggleSuccess: false,
                toggleError: false,

                // user
                userType: "",

                // specified producer
                producer_id: null,
                correctProducer: false,

                // check whether user is moderator, whether correct type and whether listing allows mod
                correctModerator: false,

                // where to buy
                producerListings: [],

                // where to try
                venueListings: [],

                // all venue drinks
                allVenueDrinks: [],
                venuesWithMenu: [],

                // customization for drinkLists buttons
                // [TODO] get drink list of user, for now is hardcoded

                drinkList:  {
                                "haveTried": [""],
                                "wantToTry": [""]
                            },
                haveTried: false,
                wantToTry: false,
                

                // for sorted flavorTags and observationTags
                sorted_flavorTagCounts: [],
                sorted_observationTagCounts: [],

                // For creating review
                languages:[],
                selectedLanguage:"English",
                nullSelectedLanguage:false,
                reviewDesc:"",
                rating: 5,
                colours: [],
                specialColours: {},
                selectedColour:"",
                image64: null,
                selectedImage: "",
                photo: null,
                observationTags: [],
                selectedObservations:[],
                flavourTags: [],
                subTags: [],
                selectedFlavourTags:[],
                finalSelectedFlavourTags:[],
                aroma:"",
                taste:"",
                finish:"",
                wouldRecommend:false,
                wouldBuyAgain:false,
                extendReview:false,
                locationOptions: [], // Your list of options
                locationSearchTerm: "",
                tagLocation:"",
                selectedLocation: "",
                selectedLocationAddress:"",
                selectedLocationId: "",
                extendObservation: false,
                loggedIn:false,
                userID: "defaultUser",
                reviewDescError:'',
                reviewResponseCode:'',
                addingReview: true,
                successSubmission: false,
                errorMessage: false,
                duplicateEntry: false,
                errorSubmission:false,
                followList:[],
                friendTag:'',
                selectedFriendTag:null,
                friendTagList:[],
                showFriendTagList:[],

                // To delete review
                deleteID :null,
                successDelete:false,
                deletingReview:true,
                errorDelete:false,
                errorDeleteMessage:false,

                // To delete listing
                deleteListingCode: null,
                successDeleteListing:false,
                deletingListing:true,
                errorDeleteListing:false,
                // errorDeleteMessage:false,
                listingNotExist:false,

                // To edit review
                inEdit:false,
                specificReview:[],

                // to view detailed review
                detailedReview: {},
                
                // matched user
                matchedUser: {},

                deepDiveLinkFormatted: "",

                // for bookmark
                user: null,
                userBookmarks: [],

                // for bookmark component
                bookmarkListingID: {},
                defaultPhoto: "https://drinkximages.s3.us-east-1.amazonaws.com/images/2d4d94bc-313e-4621-9a15-4bfbf77958de.jpg",
                defaultProfilePhoto: "https://drinkximages.s3.us-east-1.amazonaws.com/images/27e129b8-2d6e-44a3-8c14-d78c815b8056.jpg",

                
                // nearest Bars based on current location
                nearestBars: [],
                currentLocation: {lat: 0, lng: 0},
                venueDetails: {},

                // for the review cover image
                ogImage: {},

                // for review location
                locationOnWebsite:true,
                isActive: {
                    find: true,
                    add: false
                },

                // to check if venue exsist
                addressDict: null,
                // truncation of official description <!-- tzh added  --->
                showFullDescription: false
        
        };


        },
        mounted() {
            try {
                    // Get the query string parameters (listing ID) from the URL
                    this.listing_id = this.$route.params.listingID;
                    if (this.listing_id == null) {
                        // redirect to page
                        this.$router.push('/');
                    }
                    // Check if listing exists in database
                    this.checkListingExists();
                } 
                catch (error) {
                    console.error(error);
                }
        },
        computed: {
            filteredOptions() {
            let tempLocation = this.locationOptions.filter(option =>
                option.name.toLowerCase().includes(this.locationSearchTerm.toLowerCase())
            );
            tempLocation.sort((a,b)=>{
                return a.name.localeCompare(b.name)
            })
            return tempLocation
            },
        },
        methods: {
            // fetch specific listing data
            created() {

            },

            // load data from database
            async loadData() {
                    // countries
                    // _id, originCountry
                        // try {
                        //         const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getCountries`);
                        //         this.countries = response.data;
                        //     } 
                        //     catch (error) {
                        //         console.error(error);
                        // }
                    // reviews
                    // _id, userID, reviewTarget, date, rating, reviewDesc, taggedUsers, reviewTitle, reviewType, flavorTag, photo
                        try {
                            const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getReviews`);
                            this.reviews = response.data;
                            this.detailedReview = this.reviews[0];
                        }
                        catch (error) {
                            console.error(error);
                            this.dataLoaded = null;
                        }
                    // flavourTags
                    // _id, hexcode, familyTag, subtag, showbox
                    try {
                                const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getFlavourTags`);
                                this.flavourTags = response.data.map(item => {
                                    return { ...item, showBox: false };
                                })                            } 
                        catch (error) {
                            console.error(error);
                            this.dataLoaded = null;
                        }
                    // subTags
                    // _id, familyTagId, subtag
                    try {
                                const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getSubTags`);
                                this.subTags = response.data
                                this.flavourTags.forEach(flavourTag => {
                                    // Filter subtags belonging to the current flavor tag
                                    const subTagsForFlavourTag = this.subTags.filter(subTag => subTag.familyTagId === flavourTag.id);
                                    // Extract required information from subtags
                                    const subTagsInfo = subTagsForFlavourTag.map(subTag=> ({
                                        id: subTag.id,
                                        subTag: subTag.subTag
                                    }));
                                    // Assign subtag information to flavor tag object
                                    flavourTag.subTag2 = subTagsInfo;
                                });
                            } 
                        catch (error) {
                            console.error(error);
                            this.dataLoaded = null;
                        }
                    // observationTags
                    // observationTag
                        try {
                            const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getObservationTags`);
                            for (let observationTag of response.data) {
                                this.observationTags.push(observationTag.observationTag);
                            }
                        } 
                        catch(error){
                            console.error(error);
                            this.dataLoaded = null;
                        }
                    
                    // colours
                    // hexcode
                        try {
                            const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getColours`);
                            for (let colour of response.data) {
                                this.colours.push(colour.hexcode);
                            }
                        } 
                        catch(error){
                            console.error(error);
                            this.dataLoaded = null;
                        }
                    // specialColours
                        try {
                            const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getSpecialColours`);
                            this.specialColours = response.data.reduce((obj, item) => {
                                obj[item.colour] = item.hexList;
                                return obj;
                            }, {});
                        } 
                        catch(error){
                            console.error(error);
                            this.dataLoaded = null;
                        }
                    
                    // venues
                    // _id, venueName, venueDesc, originCountry, address, openingHours
                        try {
                            const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getVenues`);
                            this.venues = response.data;
                            this.locationOptions = response.data.map(item => ({name: item.venueName, id:item.id, address:item.address}));
                            this.addressDict = this.venues.reduce((dict, venue) => {
                                dict[venue.address] = venue.id;
                                return dict;
                            }, {});
                            this.getVenuesWithMenu(); // extract venues with menu
                        } 
                        catch (error) {
                            console.error(error);
                            this.dataLoaded = null;
                        }
                // listings
                // _id, listingName, producerID, bottler, originCountry, drinkType, typeCategory, age, abv, reviewLink, officialDesc, sourceLink, photo
                    try {
                        const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getListings`);
                        this.listings = response.data;
                        this.filteredListings = this.listings; // originally, make filtered listings the entire collection of listings
                        this.specified_listing = this.listings.find(listing => listing.id == this.listing_id); // find specified listing
                        this.producer_id = this.specified_listing.producerID // find specified producer
                        this.whereToBuy(); // find where to buy specified listing
                        this.whereToTry(); // find where to try specified listing [RE-ENABLE WHEN VENUES HAVE MENU ATTRIBUTE]
                        this.filteredReviews = this.getReviewsForListing(this.specified_listing);
                        this.getFilteredReviewsWithImages() // to get only those filtered reviews with photos
                        this.getFlavorTagCounts(); // to get the flavor tag counts
                        this.getObservationTagCounts(); // to get the observation tag counts
                        this.specificReview = this.getLoggedUserReview();
                        this.formatDeepDiveLink();
                    } 
                    catch (error) {
                        console.error(error);
                        this.dataLoaded = null;
                    }
                // languages
                // _id, language
                    try {
                        const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getLanguages`);
                        this.languages = response.data.sort((a,b)=>{
                            return a.language.localeCompare(b.language)
                            })
                    } 
                    catch (error) {
                        console.error(error);
                        this.dataLoaded = null;
                    }
                // producers
                // _id, producerName, producerDesc, originCountry, statusOB, mainDrinks
                try {
                        const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getProducers`);
                        this.producers = response.data;
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
                        this.user = this.users.find(user => user.id == this.userID)
                        if (this.user) {
                            this.userBookmarks = this.user.drinkLists
                            let triedDrinks=[]
                            let wantToTryDrinks=[]
                            this.followList = this.users.filter(user => {
                                return this.user.followLists.users.some(item => parseInt(item) === user.id);
                            });
                            if(this.specificReview.length >0){
                                this.showFriendTagList = this.friendTagList.map(id => {
                                    const user = this.users.find(user => user.id === id);
                                    return {
                                        username: user.username,
                                        id: id
                                    };
                                });
                            }
                            if (this.user.drinkLists && Object.keys(this.user.drinkLists).length > 0) {
                                for (let drink of this.user.drinkLists["Drinks I Have Tried"]["listItems"]) {
                                    let triedDrink = this.listings.find(listing => listing.id === parseInt(drink))?.listingName;
                                    if (triedDrink) {
                                        triedDrinks.push(triedDrink)
                                    }
                                }
                                for (let drink of this.user.drinkLists["Drinks I Want To Try"]["listItems"]) {
                                    let wantDrinkName = this.listings.find(listing => listing.id === parseInt(drink))?.listingName;   
                                    if (wantDrinkName) {
                                        wantToTryDrinks.push(wantDrinkName)
                                    }
                                }
                            }
                            this.drinkList = {
                                haveTried: triedDrinks,
                                wantToTry: wantToTryDrinks
                            }
                            
                        }
                        
                        
                    } 
                    catch (error) {
                        console.error(error);
                        this.dataLoaded = null;
                    }
                
                // venuesAPI
                // _id, venueName, venueDesc, originCountry
                // try {
                //         const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getVenuesAPI`);
                //         this.venuesAPI = response.data;
                //     } 
                //     catch (error) {
                //         console.error(error);
                //     }
                // drinkTypes
                // _id, drinkType, typeCategory
                    // try {
                    //     const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getDrinkTypes`);
                    //     this.drinkTypes = response.data;
                    // } 
                    // catch (error) {
                    //     console.error(error);
                    // }
                // requestListings
                // _id, listingName, producerNew, producerID, bottler, originCountry, drinkType, typeCategory, age, abv, reviewLink, sourceLink, brandRelation, reviewStatus, userID, photo
                    // try {
                    //         const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getRequestListings`);
                    //         this.requestListings = response.data;
                    //     } 
                    // catch (error) {
                    //     console.error(error);
                    // }
                // requestEdits
                // _id, duplicateLink, editDesc, sourceLink, brandRelation, listingID, userID, reviewStatus
                    // try {
                    //         const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getRequestEdits`);
                    //         this.requestEdits = response.data;
                    //     } 
                    // catch (error) {
                    //     console.error(error);
                    // }
                // modRequests
                // _id, userID, drinkType, modDesc
                    // try {
                    //         const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getModRequests`);
                    //         this.modRequests = response.data;
                    //     } 
                    // catch (error) {
                    //     console.error(error);
                    // }
                this.specificReviewRating = this.getRatings(this.specified_listing)
                this.willRecommend = this.getWillRecommend(this.specified_listing)
                this.willDrinkAgain = this.getWillDrinkAgain(this.specified_listing)

                if (this.userID == this.producer_id && this.userType == "producer") {
                    this.correctProducer = true;
                }

                // Check if logged in, then check if moderator is allowed to edit listing
                if(this.userID!='defaultUser' && this.userType=='user'){
                    if((this.user.modType.includes(this.specified_listing.drinkType) && this.specified_listing.allowMod)|| this.user.isAdmin){
                        this.correctModerator = true
                    }else{
                        this.correctModerator = false
                    }
                }else{
                    this.correctModerator=false
                }

                // Set dataLoaded to true if all data is loaded
                if (this.dataLoaded != null) {
                    this.dataLoaded = true;
                }
            
            },

            // view which producers have specified listing
            whereToBuy() {
                this.producerListings = this.listings
                    .filter(listing => listing["id"] == this.specified_listing["id"])
                    .map(listing => listing["producerID"]);
            },

            // extract venues with menu
            getVenuesWithMenu() {
                this.venuesWithMenu = this.venues.filter(venue => venue["menu"].length > 0);
            },

            // view which venues have specified listing, sort by alphabetical order of venue name
            whereToTry() {

                for (let venue of this.venuesWithMenu) {
                    let allMenuItems = venue["menu"]
                    let allSectionMenus = allMenuItems.reduce((acc, menuItem) => {
                        return acc.concat(menuItem.sectionMenu);
                    }, []);

                    let allListingsIDs = allSectionMenus.reduce((acc, menuItem) => {
                        return acc.concat(menuItem.itemID); 
                    }, []);

                    let uniqueListingsIDs = [...new Set(allListingsIDs.map(item => item["id"]))];
                    if (uniqueListingsIDs.includes(this.specified_listing["id"])) {
                        this.venueListings.push(venue);
                    }
                }

                if (this.currentLocation.lat != 0 | this.currentLocation.lng != 0){
                    const apiKey = process.env.VUE_APP_GOOGLE_MAPS_API_KEY;
                    // const apiKey = 'AIzaSyD5aukdDYDbnc8BKjFF_YjApx-fUe515Hs'; // Replace with your Google Places API key
                    // const maxDistance = 5000
                    // create an object to store the distance of each venue from the current location
                    let venueDistances = {};
                    
                    this.venueListings.forEach(async (venue) => {
                        const address = encodeURIComponent(venue.address);
                        const response = await this.$axios.get(`https://maps.googleapis.com/maps/api/geocode/json?address=${address}&key=${apiKey}`);
                        const { results } = response.data;
                        console.log(results)
                        if (results.length > 0) {
                            const { lat, lng } = results[0].geometry.location;
                            venue.coordinates = { lat, lng };

                            let origins = `${this.currentLocation.lat},${this.currentLocation.lng}`
                            let destinations = `${venue.coordinates.lat},${venue.coordinates.lng}`

                            try {
                                const response2 = await this.$axios.get(`${process.env.VUE_APP_API_URL}/editListing/getDistance/` + origins + '/' + destinations + '/' + apiKey);
                                const responseData = response2.data.data
                                const rows = responseData.rows;
                                console.log(rows)
                                if (rows.length > 0 && rows[0].elements.length > 0) {
                                    const distance = rows[0].elements[0].distance
                                    const duration = rows[0].elements[0].duration

                                    const distance_text = distance.text;
                                    const distance_value = distance.value;
                                    const duration_text = duration.text;

                                    // to store the distance value only
                                    venueDistances[venue.id] = distance_value

                                    // to store other info
                                    this.venueDetails[venue.id] = {
                                        distance: distance_text,
                                        duration: duration_text
                                    }
                                }
                            } catch (error) {
                                console.error('Error in getDistance request:', error);
                            }
                        }
                        // if (venue.distance != null && venue.distance != undefined && venue.distance < maxDistance){
                        //     this.nearestBars.push(venue.venueName)    
                        //     console.log(this.nearestBars)
                        // }

                        // sort the venues by distance
                        let nearestBars = this.sortDistanceValues(venueDistances)
                        this.nearestBars = nearestBars

                
                    });
                        
                        
               
                    
                }

            },

            // get producerName for a listing based on producerID
            getProducerName(producerID) {
                const producer = this.producers.find((producer) => {
                    return producer["id"] == producerID;
                });
                // ensures that producer is found before accessing "producerName"
                if (producer) {
                    const producerName = producer["producerName"];
                    return producerName;
                }
                else {
                    return null;
                }
            },

            // get VenueName for a listing based on producerID
            getVenueName(venueID) {
                const venue = this.venues.find((venue) => {
                    return venue["id"] == venueID;
                });
                // ensures that venue is found before accessing "venueName"
                if (venue) {
                    const venueName = venue["venueName"];
                    return venueName;
                }
                else {
                    return null;
                }
            },

            getVenueNameFromID(venueID) {
                const venue = this.venues.find((venue) => {
                    return venue["id"] == venueID;
                });
                if (venue) {
                    return venue["venueName"];
                }
            },

            // check if user has already added listing to shelf, add colour to button accordingly
            checkDrinkLists(listing) {
                const haveTried = this.drinkList.haveTried.includes(listing.listingName);
                const wantToTry = this.drinkList.wantToTry.includes(listing.listingName);

                const haveTriedButton = `
                <button type="button" class="btn custom-drink-list-btn rounded-0 ${haveTried ? 'disabled' : ''}">
                    Have tried
                </button>
                `;

                const wantToTryButton = `
                <button type="button" class="btn custom-drink-list-btn rounded-0 ${wantToTry ? 'disabled' : ''}">
                    Want to try
                </button>
                `;

                return {
                    buttons: {
                        haveTried: haveTriedButton,
                        wantToTry: wantToTryButton,
                    }
                }
            },

            // get ratings for a listing
            getRatings(listing) {
                const ratings = this.reviews.filter((rating) => {
                try {
                    return rating["reviewTarget"] == listing['id'];
                }
                catch(error){console.error(error)}
                });
                // if there are no ratings
                if (ratings.length == 0) {
                    return "-";
                }
                // else there are ratings
                const averageRating = ratings.reduce((total, rating) => {
                    return total + rating["rating"];
                }, 0) / ratings.length;
                return averageRating.toFixed(2);
            },

            // get will drink again for a listing
            getWillRecommend(listing) {
                const ratings = this.reviews.filter((rating) => {
                try {
                    return rating["reviewTarget"] == listing['id'];
                }
                catch(error){console.error(error)}
                });
                // if there are no ratings
                if (ratings.length == 0) {
                    return "-";
                }
                // else there are ratings
                const numberRecommend = ratings.reduce((total, rating) => {
                    return total + (rating["willRecommend"] ? 1 : 0);
                }, 0);
                const averageRecommend = (numberRecommend / ratings.length) * 100;
                return averageRecommend.toFixed(2);
            },

            // get will drink again for a listing
            getWillDrinkAgain(listing) {
                const ratings = this.reviews.filter((rating) => {
                try {
                    return rating["reviewTarget"] == listing['id'];
                }
                catch(error){console.error(error)}
                });
                // if there are no ratings
                if (ratings.length == 0) {
                    return "-";
                }
                // else there are ratings
                const numberDrinkAgain = ratings.reduce((total, rating) => {
                    return total + (rating["wouldBuyAgain"] ? 1 : 0);
                }, 0);
                const averageDrinkAgain = (numberDrinkAgain / ratings.length) * 100;
                return averageDrinkAgain.toFixed(2);
            },

            // add user's uploaded photo to database (TO BE IMPLEMENTED)
            addPhoto() {
                alert("This feature is not yet implemented.");
            },

            getReviewsForListing(listing) {
                const reviews = this.reviews.filter((review) => {
                    return review["reviewTarget"] == listing.id;
                });
                return reviews;
            },
            getLoggedUserReview(){
                const specificReview = this.filteredReviews.filter((review) => {
                    return review["userID"] == this.userID;
                });
                if(specificReview.length!=0){
                    this.inEdit=true
                    this.selectedLanguage= specificReview[0].language
                    this.selectedColour= specificReview[0].colour
                    this.reviewDesc= specificReview[0].reviewDesc
                    this.wouldRecommend= specificReview[0].willRecommend
                    this.wouldBuyAgain= specificReview[0].wouldBuyAgain
                    this.aroma= specificReview[0].aroma
                    this.taste= specificReview[0].taste
                    this.finish= specificReview[0].finish
                    this.rating= specificReview[0].rating
                    // reconcile id with flavourtags
                    // this.selectedFlavourTags= specificReview[0].flavourTag
                    if(specificReview[0].flavourTag!=null){
                        specificReview[0].flavourTag.forEach(subtag=>{
                            const subTag = this.subTags.find(subTag => parseInt(subtag)===subTag.id)         
                            if(subTag){
                                const familyTag = this.flavourTags.find(family=>subTag.familyTagId===family.id)
                                if(familyTag){
                                    const hexcode = familyTag.hexcode
                                    const subtagInfo = subTag.subTag
                                    this.selectedFlavourTags.push(subtagInfo+ hexcode)
                                }
                            }else{
                                this.selectedFlavourTags.push("<deleted>")
                            }
                        })
                    }
                    this.finalSelectedFlavourTags = specificReview[0].flavourTag
                    if(specificReview[0].taggedUsers !=null){
                        this.friendTagList = specificReview[0].taggedUsers.map(userId => parseInt(userId));
                    }
                    this.selectedObservations= specificReview[0].observationTag
                    this.image64= specificReview[0].photo
                    let selectedLocation = []
                    if(specificReview[0].location != null){
                        selectedLocation = this.locationOptions.filter((location)=>{
                            return location['id'] == specificReview[0].location
                        })
                    }
                    if(selectedLocation.length !=0){
                        this.selectedLocation = selectedLocation[0].name
                        // this.selectedLocationaddress=selectedLocation[0].address 
                    }
                }

                return specificReview
            },

            getUsernameFromReview(review) {
                const user = this.users.find((user) => {
                    return user["id"] == review["userID"];
                });
                if (user) {
                    return user["username"];
                }
            },

            getUsernameFromId(id) {
                const user = this.users.find((user) => {
                    return user["id"] == id;
                });
                if (user) {
                    return user["username"];
                }
            },

            getPhotoFromReview(review) {
                const user = this.users.find((user) => {
                    return user["id"] == review["userID"];
                });
                if (user) {
                    return user["photo"];
                }
            },
            checkModFromUserID(userID){
                const user = this.users.find((user) => {
                    return user["id"] == userID;
                });
                if (user) {
                    return user["modType"].length > 0;
                }
            },

            displaySelectColour(colour){
                this.selectedColour = colour
            },
            // function to display submitted image
            onFileChange(event){
                const file = event.target.files[0];
                const reader = new FileReader();

                reader.onloadend = async () => {
                    this.selectedImage = reader.result
                    const base64String = reader.result.replace('data:', '').replace(/^.+,/, '');
                    this.image64 = base64String;
                };
                reader.readAsDataURL(file);
            },

            // Function to add review
            addReview(){
                // TODO Combine with editReview because using the same variables
                

                // let errorPhrase = "Your completion is incomplete"
                // form validation
                if(this.reviewDesc.length < 20){
                    this.reviewDescError ="Character count is less than 20, please write more for a more detailed review."
                    alert("Submission has error, please fill in the required fields properly")
                    return "Submission error"
                }
                else{
                    this.reviewDescError = ''
                }
                if(this.selectedLanguage ==''){
                    this.nullSelectedLanguage = true
                    alert("Submission has error, please fill in the required fields properly")
                    return "Submission error"
                }
                let createdDate = new Date().toISOString();
                if (this.reviewDesc !== "") {
                    this.reviewDesc = this.reviewDesc.trim();
                }
                if (this.photo !== null) {
                    this.photo = this.photo.trim();
                }
                if (this.aroma !== "") {
                    this.aroma = this.aroma.trim();
                }
                if (this.taste !== "") {
                    this.taste = this.taste.trim();
                }
                if (this.finish !== "") {
                    this.finish = this.finish.trim();
                }
                let submitAPI = `${process.env.VUE_APP_API_URL}/createReview/createReview`
                let submitData = {
                    "userID" : this.userID,
                    "reviewTarget" :this.listing_id,
                    "rating" : Number(this.rating),
                    "reviewDesc": this.reviewDesc,
                    "reviewType": "Listing",
                    "flavourTag" : this.finalSelectedFlavourTags,
                    "photo" : this.image64,
                    "colour" : this.selectedColour,
                    "language" : this.selectedLanguage,
                    "aroma" : this.aroma,
                    "taste" : this.taste,
                    "finish" : this.finish,
                    "location" :this.selectedLocation,
                    "address":this.selectedLocationAddress,
                    "willRecommend": this.wouldRecommend,
                    "taggedUsers": this.friendTagList,
                    "wouldBuyAgain": this.wouldBuyAgain,
                    "observationTag": this.selectedObservations,
                    "createdDate": createdDate,
                    "userVotes": {
                        "downvotes":[],
                        "upvotes":[]
                    }
                    
                }
                this.writeReview(submitAPI, submitData)
                
            },

            editReview(){
                if(this.reviewDesc.length < 20){
                    this.reviewDescError ="Character count is less than 20, please write more for a more detailed review."
                    alert("Submission has error, please fill in the required fields properly")
                    return "Submission error"
                }
                if(this.selectedLanguage ==''){
                    this.nullSelectedLanguage = true
                    alert("Submission has error, please fill in the required fields properly")
                    return "Submission error"
                }
                if (this.reviewDesc !== "") {
                    this.reviewDesc = this.reviewDesc.trim();
                }
                if (this.photo !== null) {
                    this.photo = this.photo.trim();
                }
                if (this.aroma !== "") {
                    this.aroma = this.aroma.trim();
                }
                if (this.taste !== "") {
                    this.taste = this.taste.trim();
                }
                if (this.finish !== "") {
                    this.finish = this.finish.trim();
                }
                let submitAPI = `${process.env.VUE_APP_API_URL}/editReview/updateReview/` + this.specificReview[0].id
                let submitData = {
                    "userID" : this.userID,
                    "reviewTarget" :this.listing_id,
                    "rating" : Number(this.rating),
                    "reviewDesc": this.reviewDesc,
                    "reviewType": "Listing",
                    "flavourTag" : this.finalSelectedFlavourTags,
                    "photo" : this.image64,
                    "colour" : this.selectedColour,
                    "language" : this.selectedLanguage,
                    "aroma" : this.aroma,
                    "taste" : this.taste,
                    "finish" : this.finish,
                    "location" :this.selectedLocation,
                    "address":this.selectedLocationAddress,
                    "taggedUsers": this.friendTagList,
                    "willRecommend": this.wouldRecommend,
                    "wouldBuyAgain": this.wouldBuyAgain,
                    "observationTag": this.selectedObservations,
                    "createdDate": this.specificReview[0].createdDate
                }
                this.updateReview(submitAPI, submitData)
            },

            async updateReview(submitAPI, submitData){
                const response = await this.$axios.put(submitAPI, submitData)
                .then((response)=>{
                    this.reviewResponseCode = response.data.code
                })
                .catch((error)=>{
                    console.error(error);
                    this.reviewResponseCode = error.response.data.code
                });
                if(this.reviewResponseCode==200){
                    this.successSubmission=true; // Display success message
                    this.addingReview=false; // Hide submission in progress message
                }else{
                    this.errorSubmission=true; // Display error message
                    this.addingReview=false; // Hide submission in progress message
                    if(this.reviewResponseCode==400){
                        this.duplicateEntry = true // Display duplicate entry message
                    }else{
                        this.errorMessage = true // Display generic error message
                    }
                }
                return response
            },

            async writeReview(submitAPI, submitData){
                
                const response = await this.$axios.post(submitAPI, submitData)
                .then((response)=>{
                    this.reviewResponseCode = response.data.code
                })
                .catch((error)=>{
                    console.error(error);
                    this.reviewResponseCode = error.response.data.code
                });
                if(this.reviewResponseCode==201){
                    this.successSubmission=true; // Display success message
                    this.addingReview=false; // Hide submission in progress message
                }else{
                    this.errorSubmission=true; // Display error message
                    this.addingReview=false; // Hide submission in progress message
                    if(this.reviewResponseCode==400){
                        this.duplicateEntry = true // Display duplicate entry message
                    }else{
                        this.errorMessage = true // Display generic error message
                    }
                }
                return response
            },

            // Function to expand/contract the modal
            controlModal(){
                if(this.extendReview){
                    this.extendReview = false
                }
                else{
                    this.extendReview = true
                }
            },

            filterOptions(event) {
                const selectedOption = this.filteredOptions.find(option => option.name === event.target.value);
                this.selectedLocationId = selectedOption.id;
            },
            
            toggleBox(family) {
                let tempShowBox = family.showBox
                this.flavourTags.forEach(item => {
                    item.showBox = false;
                });
                family.showBox = !tempShowBox; // Toggle the visibility of the box
            },

            toggleObservations(){
                this.extendObservation = !this.extendObservation
            },

            toggleObservationSelection(observation) {
                const index = this.selectedObservations.indexOf(observation);
                if (index === -1) {
                    // Observation is not selected, so add it to the array
                    this.selectedObservations.push(observation);
                } else {
                    // Observation is selected, so remove it from the array
                    this.selectedObservations.splice(index, 1);
                }
            },

            toggleFlavourSelection(flavour, hexcode, id) {
                const index = this.selectedFlavourTags.indexOf(flavour+hexcode);
                if (index === -1) {
                    // Observation is not selected, so add it to the array
                    this.selectedFlavourTags.push(flavour+hexcode);
                    this.finalSelectedFlavourTags.push(id)
                } else {
                    // Observation is selected, so remove it from the array
                    this.selectedFlavourTags.splice(index, 1);
                    this.finalSelectedFlavourTags.splice(index, 1);
                }
            },

            clearColour(){
                this.selectedColour = ''
            },

            clearLocation(){
                this.tagLocation = ''
                this.selectedLocation = ''
                if(!this.locationOnWebsite){
                    this.$refs.autocomplete.$el.value = "";
                    
                }
                
            },

            clearPhoto(){
                this.image64 = null
                this.selectedImage = ""
                document.getElementById('reviewPhoto').value = '';
            },

            async deleteReview(){
                let deleteAPI = `${process.env.VUE_APP_API_URL}/deleteReview/deleteReview/` + this.deleteID
                const response = await this.$axios.delete(deleteAPI)
                .then((response)=>{
                    this.deleteReviewCode = response.data.code
                })
                .catch((error)=>{
                    console.error(error);
                    this.deleteReviewCode = error.response.data.code
                });
                if(this.deleteReviewCode==200){
                    this.successDelete=true; // Display success message
                    this.deletingReview=false; // Hide submission in progress message
                }else{
                    this.errorDelete=true; // Display error message
                    this.deletingReview=false; // Hide submission in progress message
                    if(this.reviewResponseCode==400){
                        this.notExist = true // Display duplicate entry message
                    }else{
                        this.errorDeleteMessage = true // Display generic error message
                    }
                }
                return response
                
            },

            setDeleteID(review){
                this.deleteID = review.id
            },

            setUpdateID(review){
                this.updateID = review.id
            },

            async voteReview(review, vote){
                if (vote == "upvote") {
                    review.userVotes.upvotes.push(this.userID);
                    review.userVotes.downvotes = review.userVotes.downvotes.filter(vote => vote !== this.userID);
                } else if (vote == "downvote") {
                    review.userVotes.downvotes.push(this.userID);
                    review.userVotes.upvotes = review.userVotes.upvotes.filter(vote => vote !== this.userID);
                } else if (vote == "unupvote") {
                    review.userVotes.upvotes = review.userVotes.upvotes.filter(vote => vote !== this.userID);
                } else if (vote == "undownvote") {
                    review.userVotes.downvotes = review.userVotes.downvotes.filter(vote => vote !== this.userID);
                }

                try {
                    await this.$axios.post(`${process.env.VUE_APP_API_URL}/editReview/voteReview`, 
                        {
                            reviewID: review.id,
                            userVotes: review.userVotes,
                            action: vote
                        }, {
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    });
                } catch (error) {
                    console.error(error);
                }
            },


            // view detailed review
            updateDetailedReview(review) {
                this.detailedReview = review;
            },

            reloadRoute() {
                this.$router.go(); // Reloads the current route
            },

            reloadRouteHome() {
                this.$router.push('/'); // Navigate to root 
            },
            getTagName(tag) {
                const subTag = this.subTags.find(subTag=>subTag.id === tag)
                if(subTag){
                    const familyTag = this.flavourTags.find(family=>subTag.familyTagId===family.id)
                    if(familyTag){
                        const hexcode = familyTag.hexcode
                        const subtagInfo = subTag.subTag
                        const tagInfo = subtagInfo + hexcode
                        const tagParts = tagInfo.split("#");
                        return tagParts[0];
                    }
                }else{
                    return "<deleted tag>"
                }
            },
            getTagColor(tag) {
                const subTag = this.subTags.find(subTag=>subTag.id === tag)
                if(subTag){
                    const familyTag = this.flavourTags.find(family=>subTag.familyTagId===family.id)
                    if(familyTag){
                        const hexcode = familyTag.hexcode
                        const subtagInfo = subTag.subTag
                        const tagInfo = subtagInfo + hexcode
                        const tagParts = tagInfo.split("#");
                        return "#" + tagParts[1];
                    }
                }else{
                    return "#" + "030303"
                }
            },

            formatDeepDiveLink() {
                if(this.specified_listing["reviewLink"]!= null){
                    let unformattedLink = this.specified_listing["reviewLink"];
                    // extract segment after the last "/"
                    const segment = unformattedLink.substring(unformattedLink.lastIndexOf("/") + 1);
                    // split the segment by "-"
                    const words = segment.split("-");
                    // capitalize the first letter of each word
                    const capitalizedWords = words.map(word => word.charAt(0).toUpperCase() + word.slice(1));
                    // join the words back together with spaces
                    this.deepDiveLinkFormatted = capitalizedWords.join(" ");
                }
            }, 
            
            resetToggle(){
                if(!this.toggleSuccess){
                    this.specified_listing.allowMod = !this.specified_listing.allowMod
                }
                this.toggleSuccess=false
                this.toggleError=false
                this.inToggle=true
            },

            async updateToggle(){
                let responseCode = "";
                this.inToggle=false;
                let submitData = {
                            "listingName": this.specified_listing.listingName,
                            "allowMod": this.specified_listing.allowMod,
                }
                const response = await this.$axios.post(`${process.env.VUE_APP_API_URL}/editListing/updateListingMod/` + this.listing_id, submitData)
                .then((response)=>{
                    responseCode = response.data.code
                })
                .catch((error)=>{
                    console.error(error);
                    responseCode = error.response.data.code
                });

                if(responseCode == 200){
                    this.toggleSuccess = true
                }else{
                    this.toggleError = true
                }

                return response
            },
            async addToTriedList(){
                
                // CP edits: Check if user is logged in
                if (this.userID == "defaultUser") {
                    // Redirect to login page
                    this.$router.push('/login');
                    return;
                }
                
                let responseCode = "";
                
                let submitData = {
                            "date": new Date(),
                            "listingID": this.specified_listing.id,
                            "userID": this.userID,
                            
                }
                await this.$axios.put(`${process.env.VUE_APP_API_URL}/addToList/addToTried/`, submitData)
                    .then((response) => {
                        responseCode = response.data.code;
                    })
                    .catch((error) => {
                        console.error(error);
                        responseCode = error.response.data.code;
                    });

                if (responseCode == 200) {
                    console.log("Success")
                    window.location.reload();
                } else {
                    console.log("Fail");
                }
            },
            async addToWantList(){

                // CP edits: Check if user is logged in
                if (this.userID == "defaultUser") {
                    // Redirect to login page
                    this.$router.push('/login');
                    return;
                }

                let responseCode = "";
                
                let submitData = {
                            "date": new Date(),
                            "listingID": this.specified_listing.id,
                            "userID": this.userID,
                            
                }
                await this.$axios.put(`${process.env.VUE_APP_API_URL}/addToList/addToWant/`, submitData)
                    .then((response) => {
                        responseCode = response.data.code;
                    })
                    .catch((error) => {
                        console.error(error);
                        responseCode = error.response.data.code;
                    });

                if (responseCode == 210) {
                    console.log("Success")
                    window.location.reload();
                } else {
                    console.log("Fail");
                }
            },
            
            getFilteredReviewsWithImages() {
                let allReviews = this.filteredReviews
                let reviewsWithImages = allReviews.filter(review => review.photo !== null)
                // if reviewsWithImages more than 6, get the first 6
                if (reviewsWithImages.length > 6) {
                    this.filteredReviewsWithImages = reviewsWithImages.slice(0, 6)
                } else {
                    this.filteredReviewsWithImages = reviewsWithImages
                }
            },

            // from filtered reviews, create a dictionary with the count of each observation tag
            getFlavorTagCounts() {
                let allReviews = this.filteredReviews
                let flavorTags = []
                for (let review of allReviews) {
                    for (let tag of review.flavourTag) {
                        // convert ID into the string instead, make life easier
                        // flavorTags.push(tag)
                        const subTag = this.subTags.find(subTag=>subTag.id === tag.id)
                        if(subTag){
                            const familyTag = this.flavourTags.find(family=>subTag.familyTagId === family.id)
                            if(familyTag){
                                const hexcode = familyTag.hexcode
                                const subtagInfo = subTag.subTag
                                flavorTags.push(subtagInfo + hexcode)
                            }
                        }
                    }
                }
                let flavorTagCounts = {}
                for (let tag of flavorTags) {
                    if (tag in flavorTagCounts) {
                        flavorTagCounts[tag] += 1
                    } else {
                        flavorTagCounts[tag] = 1
                    }
                }
                // sort flavorTagCounts by value
                let sorted_flavorTagCounts = Object.fromEntries(
                    Object.entries(flavorTagCounts).sort(([,a],[,b]) => b-a)
                );
                // get top 5 flavor tags if there are more than 5
                if (Object.keys(sorted_flavorTagCounts).length > 5) {
                    let top5 = Object.keys(sorted_flavorTagCounts).slice(0, 5)
                    this.sorted_flavorTagCounts = {}
                    for (let tag of top5) {
                        this.sorted_flavorTagCounts[tag] = sorted_flavorTagCounts[tag]
                    }
                } else {
                    this.sorted_flavorTagCounts = sorted_flavorTagCounts
                }
            },

            // from filtered reviews, create a dictionary with the count of each flavour tag
            getObservationTagCounts() {
                let allReviews = this.filteredReviews
                let observationTags = []
                for (let review of allReviews) {
                    for (let tag of review.observationTag) {
                        observationTags.push(tag)
                    }
                }
                let observationTagCounts = {}
                for (let tag of observationTags) {
                    if (tag in observationTagCounts) {
                        observationTagCounts[tag] += 1
                    } else {
                        observationTagCounts[tag] = 1
                    }
                }
                // sort observationTagCounts by value
                let sorted_observationTagCounts = Object.fromEntries(
                    Object.entries(observationTagCounts).sort(([,a],[,b]) => b-a)
                );
                // get top 5 flavor tags if there are more than 3
                if (Object.keys(sorted_observationTagCounts).length > 3) {
                    let top3 = Object.keys(sorted_observationTagCounts).slice(0, 3)
                    this.sorted_observationTagCounts = {}
                    for (let tag of top3) {
                        this.sorted_observationTagCounts[tag] = sorted_observationTagCounts[tag]
                    }
                } else {
                    this.sorted_observationTagCounts = sorted_observationTagCounts
                }
            },
            // for bookmark component
            handleIconClick(data) {
                if (data == 'login') {
                    this.$router.push('/login');
                }
                else {
                    this.bookmarkListingID = data
                }
            },

            // Get current location using browser's Geolocation API
            getCurrentLocation() {
            
            navigator.geolocation.getCurrentPosition(
                position => {
                this.currentLocation.lat = position.coords.latitude;
                this.currentLocation.lng = position.coords.longitude;
                
                },
                error => {
                console.error(error);
                // Handle error gracefully
                }
            );
            },
            
            updateFriendTag(){
                let friendTagError = document.getElementById("friendTagError")
                // find listing based on bottle name
                let user = this.followList.find(user => user.username === this.friendTag)
                if (user) {
                    this.selectedFriendTag = user
                    friendTagError.innerHTML = ""
                }
                else {
                    this.selectedfriendTag = null
                    friendTagError.innerHTML = "Please enter a valid username"
                }
            },

            tagSpecificFriend(){
                if (this.selectedFriendTag !== null && !this.friendTagList.includes(this.selectedFriendTag.id)) {
                    this.friendTagList.push(this.selectedFriendTag.id);
                    this.showFriendTagList.push({username:this.selectedFriendTag.username,id:this.selectedFriendTag.id})
                    this.friendTag=''
                    this.selectedFriendTag=null
                }
            },

            removeFriendTag(friend){
                this.showFriendTagList = this.showFriendTagList.filter(item => item.username !== friend.username);
                this.friendTagList = this.friendTagList.filter(item => item !== friend.id);
            },

            sortDistanceValues(distanceObject) {
                let sortedDistanceValues = Object.fromEntries(
                    Object.entries(distanceObject).sort(([,a],[,b]) => a-b)
                );
                return sortedDistanceValues;
            },

            // For review tag location

            changeLocationInput(status){
                this.selectedLocation = ''
                if (status == "add") {
                    this.isActive['add'] = true
                    this.isActive['find'] = false
                    this.locationOnWebsite = false
                }
                else if (status == "find") {
                    this.isActive['add'] = false
                    this.isActive['find'] = true
                    this.locationOnWebsite = true
                }
            },

            setPlace(place){
                this.selectedLocation=place.name
                this.selectedLocationAddress=place.formatted_address
            },

            // return place id

            checkVenue(place){
                // Querying MongoDB venues collection to check if a place exists
                
                // // Querying MongoDB venues collection to check if a place exists
                // if (this.filteredOptions.hasOwnProperty(place)) {
                //     // Place exists as a key in filtered options
                //     console.log("Place exists");
                // } else {
                //     // Place does not exist as a key in filtered options
                //     console.log("Place does not exist");
                // }
                // const selectedPlace = this.filteredOptions.find(option => option.name === place);
                // if(selectedPlace){
                //     return selectedPlace.id;
                // }
                // else{
                //     return false;
                // }
                
                if (place in this.addressDict){

                    // have to get the id of the address
                    return this.addressDict[place];
                }
                else{
                    return null;
                }



            },

            // to get webscrapped image data
            getOGImage(url) {
                if (url != null) {
                    this.$axios({
                        url: url.startsWith('https://88bamboo.co/') ? url.replace('https://88bamboo.co/', '/api/') : url,
                        method: "get",
                        headers: {
                        accept: "*/*",
                        },
                    })
                    .then((res) => {
                        const html = res.data;
                        const regex = /<meta property="og:image" content="([^"]+)">/;
                        const match = html.match(regex);
                        const img_url = match ? match[1] : null;
                        this.ogImage[url] = img_url;
                        console.log(img_url)
                    })
                    .catch((err) => {
                        console.log(err);
                    });
                }
                
            },

            isHttpValid(url) {
                try {
                    const newUrl = new URL(url);
                    return newUrl.protocol === 'http:' || newUrl.protocol === 'https:';
                } 
                catch (err) {
                    return false;
                }
            },

            navigateAndReload(to) {
                // Navigate to the specified route
                this.$router.push(to).then(() => {
                    // After navigation is complete, reload the window
                    window.location.reload(true);
                });
            },

            // delete bottle listing
            async deleteListings(listing) {
                let deleteAPI = `${process.env.VUE_APP_API_URL}/editListing/deleteListing/` + listing.id
                const response = await this.$axios.delete(deleteAPI)
                .then((response)=>{
                    this.deleteListingCode = response.data.code
                })
                .catch((error)=>{
                    console.error(error);
                    this.deleteListingCode = error.response.data.code
                });
                if(this.deleteListingCode==201){
                    this.successDeleteListing=true; // Display success message
                    this.deletingListing=false; // Hide submission in progress message

                }else{
                    this.errorDeleteListing=true; // Display error message
                    this.deletingListing=false; // Hide submission in progress message
                    if(this.deleteListingCode==400){
                        this.listingNotExist = true // Display duplicate entry message
                    }else{
                        this.errorDeleteMessage = true // Display generic error message
                    }

                }
                return response
            },

            // Check whether listing exists
            async checkListingExists() {
                try {
                    const listing = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getListing/`+ this.listing_id);
                    if (listing.data.length !== 0) {
                        this.loadData();
                        // Load local storage variables
                        const accID = localStorage.getItem("88B_accID");
                        if(accID !== null){
                            this.userID = localStorage.getItem('88B_accID')
                        }
                        //     this.loggedIn = true
                        // }
                        const accType = localStorage.getItem("88B_accType");
                        if(accType !==null){
                            this.userType = accType
                        }
                        this.getCurrentLocation();
                    }
                    else {
                        this.dataLoaded = null;
                        this.listingExists = false;
                    }
                }
                catch (error) {
                    console.error(error);
                    this.dataLoaded = null;
                }
            },

            updateTagLocation(){
                // get error message element
                let tagLocationError = document.getElementById("tagLocationError")
                // find listing based on bottle name
                let locationTag = this.locationOptions.find(location => location.name === this.tagLocation)
                if (locationTag) {
                    this.selectedLocation = locationTag.name
                    tagLocationError.innerHTML = ""
                }
                else {
                    this.selectedLocation = ""
                    tagLocationError.innerHTML = "Please enter a valid location, if not location will be left empty"
                }
            },
        }
    };
</script>