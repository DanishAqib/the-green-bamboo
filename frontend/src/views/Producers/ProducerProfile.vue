<!-- HTML -->
<template>
    <NavBar />

    <!-- Display when data is still loading -->
    <div class="text-info-emphasis fst-italic fw-bold fs-5 pt-5" v-if="dataLoaded == false">
        <span>Loading profile, please wait...</span>
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

    <div class="container pt-5 ps-lg-0 mobile-pt-4" v-if="dataLoaded">
        <div class="row">
            <!-- producer information -->
            <div class="col-xl-9 col-12 no-margin p-lg-0">
                <!-- header -->
                <div class="row">
                    <!-- image -->
                    <div class="col-lg-3 col-12 mb-lg-0 mb-3 image-container text-start mobile-col-5">
                        <!-- [if] editing -->
                        <div v-if="editing" style="position: relative; text-align: center;">
                            <!-- image -->
                            <img :src="selectedImage || (specified_producer_original_photo || defaultProfilePhoto)" 
                                alt="" style="width: 150px; height: 150px; z-index: 1; opacity: 50%">
                            <!-- change option -->
                            <label for="file1" class="btn primary-light-dropdown" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); z-index: 2;">Choose File</label>
                            <input id="file1" type="file" v-on:change="loadFile" ref="fileInput" style="width: 0px; height: 0px;">
                            <!-- reset image option -->
                            <button class="btn primary-light-dropdown m-1" @click="selectedImage = '';  specified_producer_original_photo= specified_producer['photo']; image64 = null">Revert</button>
                            <!-- remove image option -->
                            <button class="btn primary-light-dropdown m-1" @click="selectedImage = ''; specified_producer_original_photo=''; image64 = ''">Remove</button>
                        </div>
                        <!-- [else] not editing  TZH removed style="width: 200px; height: 200px; z-index: 1;" from img tag-->
                        <div v-else>
                            
                            <img :src="selectedImage || (specified_producer['photo'] || defaultProfilePhoto)" 
                                alt="" class="producer-bottle-listing-page-image" >
                        </div>
                    </div>
                    <!-- details -->
                    <div class="col-lg-9 col-12 text-start padding-for-followthisbusinessbutton-large-screen mobile-col-7 mobile-ps-0 mobile-pe-0">
                        <div class="container text-start pe-lg-0">
                            <!-- country  -->
                            <div class="row ">
                                <div class="col-8 pe-0 ps-0">
                                    <!-- [if] editing -->
                                    <div v-if="editing">
                                        <label for="originCountryInput "> Country of Origin </label>
                                        <input type="text" class="form-control mb-3" id="originCountryInput" aria-describedby="originCountry" v-model="edit_originCountry">
                                    </div>
                                    <!-- [else] not editing -->
                                    <div v-else>
                                        <h5  class="text-body-secondary mobile-view-hide"> {{ specified_producer["originCountry"] }} </h5>
                                        <h6  class="text-body-secondary mobile-view-show mb-0"> {{ specified_producer["originCountry"] }} </h6>
                                    </div>
                                </div>
                                <!-- claim this business / add listing & edit profile -->
                                <div class="col-4 mobile-view-hide">
                                    <!-- [if] user type is producer / admin -->
                                    <span v-if="correctProducer || isAdmin" class="row"> 
                                        <!-- add listing-->
                                        <div v-if="correctProducer && editing == false" class="col d-grid no-padding">
                                            <!-- if not editing -->
                                            <button type="button" class="btn tertiary-btn rounded-0 reverse-clickable-text">
                                                <router-link :to="`/listing/create`" class="reverse-clickable-text">
                                                    Add Listing
                                                </router-link>
                                            </button>
                                        </div>
                                        <!-- edit profile -->
                                        <div class="col d-grid no-padding">
                                            <!-- [if] not editing -->
                                            <button v-if="editing == false" type="button" class="btn tertiary-btn-blue-outline rounded-0 reverse-clickable-text" v-on:click="editProfile()">
                                                Edit Profile
                                            </button>
                                            <!-- [else] if editing -->
                                            <button v-else type="button" class="btn btn-success rounded-0 reverse-clickable-text" v-on:click="saveEdit()">
                                                Save
                                            </button>
                                        </div>
                                    </span>
                                    <!-- [else] user type is NOT producer -->
                                    <div v-else> 
                                        <p v-if="!specified_producer['claimStatus']" class="text-body-secondary no-margin text-decoration-underline fst-italic text-end" @click="claimProducerAccount"> Claim This Business </p>
                                    </div>
                                </div>
                            </div>
                            <!-- producer -->
                            <div class="row">
                                <!-- [if] editing -->
                                <div v-if="editing">
                                    <label for="producerNameInput"> Producer Name </label>
                                    <input type="text" class="form-control mb-3" id="producerNameInput" aria-describedby="producerDesc" v-model="edit_producerName">
                                </div>
                                <!-- [else] not editing -->
                                <div v-else class="ps-0 pe-0">
                                    <h3  class="text-body-secondary mobile-view-hide"> <b> {{ specified_producer["producerName"] }} </b> </h3>
                                    <h4  class="text-body-secondary mobile-view-show pe-0 ps-0 mb-0"> <b> {{ specified_producer["producerName"] }} </b> </h4>
                                </div>
                            </div>
                            <!-- description -->
                            <div class="row scrollable">
                                <div class="col-12 pe-lg-0 ps-0">
                                    <!-- [if] editing -->
                                    <div v-if="editing">
                                        <label for="producerDescInput"> Producer Description </label>
                                        <textarea type="text" class="form-control mb-3" id="producerDescInput" aria-describedby="producerDesc" v-model="edit_producerDesc"> </textarea>
                                    </div>
                                    <!-- [else] not editing -->
                                    <div v-else class="ps-0 pe-0">
                                        <div v-if="specified_producer.producerDesc.length > 150">
                                            <p v-if="!showFullProducerDescription" class="text-body-secondary fs m-0 mobile-rating-smaller-text-2"> 
                                                {{ specified_producer["producerDesc"].slice(0,150) + (specified_producer["producerDesc"].length > 150 ? '...' : '') }} 
                                                <a @click="showFullProducerDescription = true" style="font-weight: bold;">(Read More)</a>
                                            </p>
                                            <p v-else class="text-body-secondary fs m-0 mobile-rating-smaller-text-2"> 
                                                {{ specified_producer["producerDesc"] }} 
                                                <a @click="showFullProducerDescription = false" style="font-weight: bold;">(Read Less)</a>
                                            </p>
                                        </div>
                                        <p v-else class="text-body-secondary fs m-0 mobile-rating-smaller-text-2"> 
                                            {{ specified_producer["producerDesc"] }} 
                                        </p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- more information (expressions, reviews) -->
                <div class="row mt-3 mobile-mt-1">
                    <div class="col-7 d-flex justify-content-start mobile-pe-0">
                        <!-- toggle latest updates-->
                        <button v-if="showListings == false" class="btn active-toggle-button mx-1 mobile-rating-smaller-text-2 mobile-ps-1 mobile-pe-1 mobile-toggle-button-producer-profile" v-on:click="showAllReviews()"> Brand Overview </button>
                        <button v-else class="btn inactive-toggle-button mx-1 mobile-rating-smaller-text-2 mobile-ps-1 mobile-pe-1 mobile-toggle-button-producer-profile" v-on:click="showAllReviews()"> Brand Overview </button>
                        <!-- toggle expressions view-->
                        <button v-if="showListings == true" class="btn active-toggle-button mx-1 mobile-rating-smaller-text-2 mobile-ps-1 mobile-pe-1 mobile-toggle-button-producer-profile" v-on:click="showAllListings()"> {{ allDrinksCount }} Expressions (View All) </button>
                        <button v-else class="btn inactive-toggle-button mx-1 mobile-rating-smaller-text-2 mobile-ps-1 mobile-pe-1 mobile-toggle-button-producer-profile" v-on:click="showAllListings()"> {{ allDrinksCount }} Expressions (View All) </button>
                        
                        
                            
                            <!-- reviews hidden for now
                            <div class="col-md-6 col-12 text-start">
                                <div class="row">
                                    <div class="col-2">
                                        <h4 class="text-body-secondary rating-text mb-2"> 
                                            <b> {{ allReviewsCount }}  </b> 
                                        </h4>
                                    </div>
                                     <div class="col-10">
                                        <h4 class="text-body-secondary rating-text mb-2"> 
                                            <u v-on:click="showAllReviews()"> Reviews </u> 
                                        </h4>
                                    </div>
                                </div>
                            </div>
                                -->

                            
                        
                    </div>
                  
                    <!-- follow this business -->
                    <div class="col-5 justify-content-end padding-for-followthisbusinessbutton-large-screen" v-if="userType == 'user'" >
                            <div v-if="!following" class="d-grid gap-2">
                                <button class="btn primary-btn-less-round-blue btn-lg mobile-view-show fs-6" @click="editFollow('follow')" style="font-weight:bold;" >+ Follow</button> <!--tzh added -blue -->
                                <button class="btn primary-btn-less-round-blue btn-lg mobile-view-hide" @click="editFollow('follow')" style="font-weight:bold;" >  <!--tzh added -blue -->
                                    <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-plus" viewBox="0 0 16 20">
                                        <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4"/>
                                    </svg>
                                    Follow this business
                                </button>
                            </div>
                            <div v-else class="d-grid gap-2">
                                <button class="btn primary-btn-less-round-blue btn-lg" @click="editFollow('unfollow')" style="font-weight: bold;">  <!--tzh changed primary-btn-outline-less-round to primary-btn-less-round-blue -->
                                    Following
                                </button>
                            </div>
                    </div>
                        
                    
                    
                </div>
                <div class="padding-for-hr-below-followthisbusinessbutton-large-screen">
                    <hr>
                </div>
                <!-- main page (hide all listings) -->
                <div v-if="showListings == false" class="padding-for-latestupdatesNmostpopularcontainer-large-screen">

                    <!-- [if] account is claimed -->
                    <div v-if="claimStatus">

                        <!-- latest updates -->
                        <div class="row">
                            <!-- header -->
                            <div class="col-12">
                                <p class="text-body-secondary text-start fs-4 fw-bold m-0 mobile-fs-6">Latest Updates from {{ specified_producer["producerName"] }}</p>
                            </div>
                        </div>

                        <div class="row" v-if="hasUpdates">
                            <div class="row">
                                <div class="col-xl-8 col-md-6 col-12">
                                    <p class="text-decoration-underline text-start fs-5 m-0 pb-3 mobile-fs-6">Posted on: {{ this.formatDate(latestUpdate.date) }}</p>
                                </div>
                                <div v-if="correctProducer || isAdmin" class="col-xl-4 col-md-6 col-12 text-end">
                                    <!-- edit & delete button -->
                                    <button v-if="correctProducer && (editingLatestUpdate == false)" type="button" class="btn btn-warning rounded-0" @click="editUpdate(latestUpdate, 'latest')"> Edit </button>
                                    <button v-if="correctProducer && editingLatestUpdate" type="button" class="btn btn-success rounded-0 reverse-clickable-text" @click="saveUpdateEdit(latestUpdate, 'latest')"> Save Changes </button>
                                    <button v-if="correctProducer && editingLatestUpdate" type="button" class="btn btn-warning rounded-0 reverse-clickable-text ms-1" @click="cancelUpdate(latestUpdate, 'latest')"> Cancel </button>
                                    <button v-if="correctProducer && (editingLatestUpdate == false)" type="button" class="btn btn-danger rounded-0 ms-1" @click="deleteUpdate(latestUpdate)"> Delete </button>
                                </div>
                            </div>

                            <!-- information -->
                            <div class="row">
                                <!-- profile photo & post timestamp & # of likes -->
                                <div class="col-lg-2 col-md-3 col-4">
                                    <!-- image -->
                                    <div class="image-container">
                                        <!-- [if] editing -->
                                        <div v-if="editingLatestUpdate" style="position: relative; text-align: center;">
                                            <!-- image -->
                                            <img :src="selectedLatestUpdateImage || (latestUpdate['photo'] || defaultPhoto)" 
                                                alt="" style="width: 128px; height: 128px; z-index: 1; opacity: 50%">
                                            <!-- change option -->
                                            <label for="file2" class="btn primary-light-dropdown" style="position: absolute; top: 30%; left: 50%; transform: translate(-50%, -50%); z-index: 2;">Choose</label>
                                            <input id="file2" type="file" v-on:change="loadLatestUpdateFile" ref="fileInput2" style="width: 0px; height: 0px;">
                                            <!-- reset image option -->
                                            <button class="btn primary-light-dropdown m-1" @click="selectedLatestUpdateImage = latestUpdate['photo']; image64LatestUpdate = null">Revert</button>
                                            <!-- remove image option -->
                                            <button class="btn primary-light-dropdown m-1" @click="selectedLatestUpdateImage = defaultPhoto; image64LatestUpdate = ''">Remove</button>
                                        </div>
                                        <!-- [else] not editing tzh removed style="width: 128px; height: 128px; z-index: 1;" from img tag -->
                                        <div v-else>
                                            <img :src="selectedLatestUpdateImage || (latestUpdate['photo'] || defaultPhoto)" 
                                                alt="" class="producer-profile-latest-updates-image" >
                                        </div>
                                    </div>

                                    <!-- # of likes -->
                                    <div class="row pt-2"> 
                                        <div class="col-6 text-end">
                                            <!-- [if] liked -->
                                            <div v-if="likeStatus" class="d-inline-block" v-on:click="unlikeUpdates(latestUpdate.id)">
                                                <svg xmlns="http://www.w3.org/2000/svg"  fill="red" class="bi bi-heart-fill producer-profile-latest-updates-heart" viewBox="0 0 16 16">
                                                    <path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314"/>
                                                </svg>
                                            </div>
                                            <!-- [else] not liked -->
                                            <div v-else class="d-inline-block" v-on:click="likeUpdates(latestUpdate.id)">
                                                <svg xmlns="http://www.w3.org/2000/svg"  fill="currentColor" class="bi bi-heart producer-profile-latest-updates-heart" viewBox="0 0 16 16">
                                                    <path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.920 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143q.090.083.176.171a3 3 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15"/>
                                                </svg>
                                            </div>
                                        </div>
                                        <div class="col-6 text-start mobile-fs-6 ">
                                            <p class="text-body-secondary fs-5 mobile-fs-6 m-0"> {{ updateLikesCount }} </p>
                                        </div>
                                    </div>
                                </div>
                                <!-- description -->
                                <div class="col-xl-10 col-md-9 col-8 mobile-ps-0 mobile-pe-0">
                                    <div class="text-start p-text-lg mobile-rating-smaller-text-2"> 
                                        <p v-if="editingLatestUpdate == false">
                                            {{latestUpdate['text']}}
                                        </p>
                                        <p v-else>
                                            <label for="latestUpdateText"> Update Text </label>
                                            <textarea class="form-control mb-3" id="latestUpdateText" aria-describedby="latestUpdateText" v-model="edit_latestUpdateText"></textarea>
                                        </p>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- no other updates -->
                        <div v-else>
                            <p class="fs-5 fst-italic m-0 text-start"> {{ specified_producer["producerName"] }} has not posted any updates! </p>
                        </div>

                        <!-- reply / send to producer -->
                        <div v-if="correctProducer" class="row pt-3">
                            <!-- [if] user type is producer -->
                            <div class="input-group centered">
                                <input class="search-bar form-control rounded fst-italic" type="text" placeholder="Say hi to your patrons!" v-model="updateText">

                                <label for="file3" class="btn p-0 ms-2">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-camera" viewBox="0 0 16 16">
                                        <path d="M15 12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1h1.172a3 3 0 0 0 2.12-.879l.83-.828A1 1 0 0 1 6.827 3h2.344a1 1 0 0 1 .707.293l.828.828A3 3 0 0 0 12.828 5H14a1 1 0 0 1 1 1zM2 4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2h-1.172a2 2 0 0 1-1.414-.586l-.828-.828A2 2 0 0 0 9.172 2H6.828a2 2 0 0 0-1.414.586l-.828.828A2 2 0 0 1 3.172 4z"/>
                                        <path d="M8 11a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5m0 1a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7M3 6.5a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0"/>
                                    </svg>
                                </label>
                                <input id="file3" type="file" v-on:change="loadUpdateFile" style="width: 0px; height: 0px;" ref="fileInput3">

                                <button v-on:click="addUpdates" class="btn send-icon p-0 mx-1">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-send" viewBox="0 0 16 16">
                                        <path d="M15.854.146a.5.5 0 0 1 .11.54l-5.819 14.547a.75.75 0 0 1-1.329.124l-3.178-4.995L.643 7.184a.75.75 0 0 1 .124-1.33L15.314.037a.5.5 0 0 1 .54.11ZM6.636 10.07l2.761 4.338L14.13 2.576zm6.787-8.201L1.591 6.602l4.339 2.76z"/>
                                    </svg>
                                </button>
                            </div>

                            <!-- New Update Preview -->
                            <div v-if="updateText.length > 0 || updateImage64" class="border border-secondary rounded mt-3">

                                <!-- Header / Clear Button -->
                                <div class="row my-2">
                                    <div class="col-10">
                                        <p class="text-start text-body-secondary fs-5 fw-bold m-0">New Update Preview:</p>
                                    </div>
                                    <div class="col-2 d-flex justify-content-end align-items-center">
                                        <button type="button" class="btn-close" aria-label="Clear New Update Draft" @click="updateText = ''; updateImage64 = ''"></button>
                                    </div>
                                </div>

                                <div class="row mb-3">
                                    <!-- Photo / Clear Photo -->
                                    <div class="col-xl-2 col-md-3">
                                        <div style="position: relative; text-align: center; width: 128px; height: 128px;">
                                            <img :src=" updateImage64 ? 'data:image/jpeg;base64,' + updateImage64:defaultPhoto" alt="" style="width: 128px; height: 128px;">
                                            <!-- <img :src=" (updateImage64 || defaultPhoto)" alt="" style="width: 128px; height: 128px;"> -->
                                            <button type="button" class="btn-close" @click="updateImage64 = ''" style="position: absolute; top: 10%; left: 90%; transform: translate(-50%, -50%); z-index: 2;"></button>
                                        </div>
                                    </div>
                                    <!-- Description -->
                                    <div class="col-xl-10 col-md-9">
                                        <p class="text-start p-text-lg">{{ updateText }}</p>
                                    </div>
                                </div>

                            </div>

                        </div>

                        <!-- view more updates -->
                        <div class="row" v-if="hasUpdates">

                            <!-- Toggle Button -->
                            <button v-if="remainingUpdates.length > 0"
                                type="button" 
                                class="btn tertiary-text text-decoration-underline pt-2 no-margin border border-0" 
                                data-bs-toggle="collapse" 
                                data-bs-target="#collapseMoreUpdates" 
                                aria-expanded="false" 
                                aria-controls="collapseMoreUpdates" 
                                @click="checkToShowRemainingUpdates()">
                                 View <span v-if="showRemainingUpdates">less ↑</span><span v-else>more updates ↓</span> 
                            </button>
                            <p v-else></p>
                            <!-- show remaining updates when "view more" is clicked -->
                            <div class="collapse" id="collapseMoreUpdates">

                                <!-- check if there are any updates 
                                <p v-if="remainingUpdates.length > 0" class="text-body-secondary fs-5 fw-bold m-0 mobile-fs-6 mobile-mb-2">Viewing {{ remainingUpdates.length }} more updates ↓</p>
                                <p v-else class="fs-5 fst-italic m-0 mobile-fs-6 mobile-mb-2">There are no more updates to view!</p>
                                -->
                                <!-- for each update -->
                                <div v-for="update in remainingUpdates" v-bind:key="update.id">
                                    <div class="row">
                                        <div class="row">
                                            <div class="col-xl-8 col-md-6 col-12">
                                                <p class="text-start text-decoration-underline fs-5 m-0 pb-3 mobile-fs-6">Posted on: {{ this.formatDate(update.date) }}</p>
                                            </div>

                                            <div v-if="correctProducer || isAdmin" class="col-xl-4 col-md-6 col-12 text-end">
                                                <!-- edit & delete button -->
                                                <button v-if="correctProducer && (editingRemainingUpdate == false || editingRemainingUpdateID != update.id)" type="button" class="btn btn-warning rounded-0" @click="editUpdate(update, 'remaining')"> Edit </button>
                                                <button v-if="correctProducer && editingRemainingUpdateID == update.id" type="button" class="btn btn-success rounded-0 reverse-clickable-text" @click="saveUpdateEdit(update, 'remaining')"> Save </button>
                                                <button v-if="correctProducer && editingRemainingUpdateID == update.id" type="button" class="btn btn-warning rounded-0 reverse-clickable-text ms-1" @click="cancelUpdate(update, 'remaining')"> Cancel </button>
                                                <button v-if="correctProducer && (editingRemainingUpdate == false || editingRemainingUpdateID != update.id)" type="button" class="btn btn-danger rounded-0 ms-1" @click="deleteUpdate(update)"> Delete </button>
                                            </div>
                                        </div>

                                        <!-- other info -->
                                        <div class="col-lg-2 col-md-3 col-4">
                                            <!-- photo & # of likes -->
                                            <div class="image-container">
                                                <!-- image -->
                                                <!-- [if] editing -->
                                                <div v-if="editingRemainingUpdateID == update.id" style="position: relative; text-align: center;">
                                                    <!-- image -->
                                                    <!-- <img :src="selectedRemainingUpdateImage || 'data:image/jpeg;base64,' + (update['photo'] || defaultPhoto)" 
                                                        alt="" style="width: 128px; height: 128px; z-index: 1; opacity: 50%"> -->
                                                    <img :src="selectedRemainingUpdateImage || (update['photo'] || defaultPhoto)" 
                                                        alt="" style="width: 128px; height: 128px; z-index: 1; opacity: 50%">
                                                    <!-- change option -->
                                                    <label for="file4" class="btn primary-light-dropdown" style="position: absolute; top: 30%; left: 50%; transform: translate(-50%, -50%); z-index: 2;">Choose</label>
                                                    <input id="file4" type="file" v-on:change="loadRemainingUpdateFile" ref="fileInput4" style="width: 0px; height: 0px;">
                                                    <!-- reset image option -->
                                                    <button class="btn primary-light-dropdown m-1" @click="selectedRemainingUpdateImage = ''; image64RemainingUpdate = null">Revert</button>
                                                    <!-- remove image option -->
                                                    <button class="btn primary-light-dropdown m-1" @click="selectedRemainingUpdateImage = defaultPhoto; image64RemainingUpdate = ''">Remove</button>
                                                </div>
                                                <!-- [else] not editing -->
                                                <div v-else-if="editingRemainingUpdate == false || editingRemainingUpdateID != update.id">
                                                    <!-- <img :src="'data:image/jpeg;base64,' + (update['photo'] || defaultPhoto)" 
                                                        alt="" class="producer-profile-latest-updates-image"> -->
                                                    <img :src="(update['photo'] || defaultPhoto)" 
                                                        alt="" class="producer-profile-latest-updates-image">
                                                </div>
                                            </div>
                                            <!-- # of likes -->
                                            <div class="row pt-2"> 
                                                <div class="col-6 text-end">
                                                    <!-- [if] liked -->
                                                    <div v-if="remainingLikeStatus[update.id]" class="d-inline-block"  v-on:click="unlikeUpdates(update.id)">
                                                        <svg xmlns="http://www.w3.org/2000/svg"  fill="red" class="bi bi-heart-fill producer-profile-latest-updates-heart" viewBox="0 0 16 16">
                                                            <path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314"/>
                                                        </svg>
                                                    </div>
                                                    <!-- [else] not liked -->
                                                    <div v-else class="d-inline-block" v-on:click="likeUpdates(update.id)">
                                                        <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="bi bi-heart producer-profile-latest-updates-heart" viewBox="0 0 16 16">
                                                            <path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.920 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143q.090.083.176.171a3 3 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15"/>
                                                        </svg>
                                                    </div>
                                                </div>
                                                <div class="col-6 text-start">
                                                    <p class="text-body-secondary fs-5 m-0 mobile-fs-6"> {{ updateLikesCount }} </p>
                                                </div>
                                            </div>
                                        </div>

                                        <!-- description -->
                                        <div class="col-xl-10 col-md-9 col-8 mobile-ps-0 mobile-pe-0">
                                            <!-- description -->
                                            <div class="text-start p-text-lg mobile-rating-smaller-text-2"> 
                                                <p v-if="editingRemainingUpdate == false || editingRemainingUpdateID != update.id">
                                                    {{update['text']}}
                                                </p>
                                                <p v-else-if="editingRemainingUpdateID == update.id">
                                                    <label for="remainingUpdateText"> Update Text </label>
                                                    <textarea class="form-control" id="remainingUpdateText" aria-describedby="remainingUpdateText" v-model="edit_remainingUpdateText[update.id]"></textarea>
                                                </p>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                            </div>

                        </div>

                    </div>

                    <!-- [else] account is not claimed -->
                    <div v-else>
                        <div class="row text-center py-2" style="background-color:#DDC8A9;">
                            <p class="fw-bold fs-3 pt-3" style="font-style: italic; ">
                                Do you own this business?
                            </p>
                            <p> Sign up for a producer account to share your latest updates with your fans! </p>
                            <!-- spacer -->
                            <div class="col-4"></div>
                            <!-- button -->
                            <button type="submit" class="col-4 btn secondary-btn-border-thick mb-3" @click="claimProducerAccount"> Claim This Business </button>
                            <!-- spacer -->
                            <div class="col-4"></div>
                        </div>
                    </div>

                    <hr>

                    <!-- view Q&A for mobile -->
                    <div class="row mobile-view-show ps-2 pe-2">
                        <!-- Toggle Button active-toggle-producer-QnA-->
                        <button v-if="showQnA"
                            type="button" 
                            class="active-toggle-producer-QnA tertiary-text pt-2 pb-2 border" 
                            data-bs-toggle="collapse" 
                            data-bs-target="#collapseQnA" 
                            aria-expanded="false" 
                            aria-controls="collapseQnA" 
                            style="font-weight:bold;"
                            @click="checkToShowQnA()">Q&As for {{ specified_producer["producerName"] }} ↑</button>
                        <button v-else
                            type="button" 
                            class="primary-btn-less-round-green tertiary-text pt-2 pb-2 border" 
                            data-bs-toggle="collapse" 
                            data-bs-target="#collapseQnA" 
                            aria-expanded="false" 
                            aria-controls="collapseQnA" 
                            style="font-weight:bold;"
                            @click="checkToShowQnA()">Q&As for {{ specified_producer["producerName"] }} ↓</button>
                    <!-- show Q&A when button is clicked -->
                    <div class="collapse pe-0 ps-0" id="collapseQnA">
                    <!-- q&a -->
                        <br>
                            <div class="col-xl-12 col-lg-4 col-md-6 col-12">
                                <div class="square primary-square-green rounded p-3 mb-3"> <!--tzh added -green-->
                                    <!-- header text -->
                                    <div class="square-inline text-start">
                                        <!-- [if] user type producer -->
                                        <div v-if="correctProducer" class="mr-auto"> 
                                            <h4> Q&A for You! </h4> 
                                            <div v-if="claimStatus">
                                                <router-link :to="{ path: '/Producers/ProducersQA/' + producer_id}" class="default-text-no-background">
                                                    <p class="reverse-text no-margin text-decoration-underline text-start pb-2"> View All </p>
                                                </router-link> 
                                            </div>
                                        </div>
                                        <!-- [else] user type is NOT producer -->
                                        <h4 v-else class="mr-auto"> Q&As for {{ specified_producer["producerName"] }} </h4>
                                    </div>

                                    <!-- [if] account is claimed -->
                                    <div v-if="claimStatus">
                                        <!-- show buttons for answered & unanswered questions -->
                                        <div v-if="correctProducer" class="row text-center px-2">
                                            <div class="col-6 d-grid gap-0 no-padding">
                                                <button type="button" class="btn tertiary-btn-qa rounded-0 reverse-clickable-text">
                                                    <a class="reverse-clickable-text" v-on:click="showAnswered()">
                                                        Answered
                                                    </a>
                                                </button>
                                            </div>
                                            <div class="col-6 d-grid gap-0 no-padding">
                                                <button type="button" class="btn tertiary-btn-qa rounded-0 reverse-clickable-text">
                                                    <a class="reverse-clickable-text" v-on:click="showUnanswered()">
                                                        Unanswered
                                                    </a>
                                                </button>
                                            </div>
                                        </div>
                                        <!-- body -->
                                        <div class="text-start pt-2">
                                            <!-- responses to q&a -->
                                            <div id="carouselExample" class="carousel slide">
                                                <div class="carousel-inner px-4">
                                                    <!-- [if] user type is producer -->
                                                    <div v-if="correctProducer">
                                                        <!-- show answered questions -->
                                                        <div v-if="answerStatus">
                                                            <div class="carousel-item" v-for="(qa, index) in answeredQuestions" v-bind:key="qa.id" v-bind:class="{ 'active': index === 0 }">
                                                                <p> <b> Q: {{ qa["question"] }} </b> </p>
                                                                <!-- [if] not editing -->
                                                                <button v-if="correctProducer && (editingQA == false || editingQAID != qa.id)" type="button" class="btn btn-warning rounded-0 me-1" v-on:click="editQA(qa)">
                                                                    Edit answer
                                                                </button>
                                                                <!-- [else] if editing -->
                                                                <button v-if="correctProducer && editingQAID == qa.id" type="button" class="btn btn-success rounded-0 me-1" v-on:click="saveQAEdit(qa)">
                                                                    Save
                                                                </button>
                                                                <!-- [else] if editing -->
                                                                <button v-if="correctProducer && editingQAID == qa.id" type="button" class="btn btn-warning rounded-0 me-1" v-on:click="cancelQAEdit(qa)">
                                                                    Cancel
                                                                </button>
                                                                <!-- delete -->
                                                                <button type="button" class="btn btn-danger rounded-0" v-on:click="deleteQAEdit(qa)">
                                                                    Delete
                                                                </button>
                                                                <!-- spacer -->
                                                                <div class="mt-2"></div>
                                                                <p v-if="editingQA == false || editingQAID != qa.id"> A: {{ qa["answer"] }} </p>
                                                                <textarea v-else-if="editingQAID == qa.id" class="search-bar form-control rounded fst-italic question-box flex-grow-1" type="text" placeholder="Edit answer." v-model="edit_answer[qa.id]"></textarea>
                                                            </div>
                                                        </div>

                                                        <!-- show unanswered questions -->
                                                        <div v-else>
                                                                <div class="carousel-item" v-for="(qa, index) in unansweredQuestions" v-bind:key="qa.id" v-bind:class="{ 'active': index === 0 }">
                                                                <p> <b> Q: {{ qa["question"] }} </b> </p>
                                                                <div class="input-group centered">
                                                                    <div class="input-group centered pt-2">
                                                                        <textarea class="search-bar form-control rounded fst-italic question-box" type="text" placeholder="Respond to your fans latest questions." v-model="answer"></textarea>
                                                                        <div v-on:click="sendAnswer(qa)" class="send-icon ps-1">
                                                                            <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-send" viewBox="0 0 16 16">
                                                                                <path d="M15.854.146a.5.5 0 0 1 .11.54l-5.819 14.547a.75.75 0 0 1-1.329.124l-3.178-4.995L.643 7.184a.75.75 0 0 1 .124-1.33L15.314.037a.5.5 0 0 1 .54.11ZM6.636 10.07l2.761 4.338L14.13 2.576zm6.787-8.201L1.591 6.602l4.339 2.76z"/>
                                                                            </svg>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <!-- [else] user type is NOT producer -->
                                                    <div v-else>
                                                        <div class="carousel-item" v-for="(qa, index) in answeredQuestions" v-bind:key="qa.id" v-bind:class="{ 'active': index === 0 }">
                                                            <div>
                                                                <p> <b> Q: {{ qa["question"] }} </b> </p>
                                                                <p> A: {{ qa["answer"] }} </p>
                                                            </div>
                                                            <div class="input-group centered pt-2">
                                                                <textarea class="search-bar form-control rounded fst-italic question-box" type="text" placeholder="Ask your question!" v-model="question"></textarea>
                                                                <div v-on:click="sendQuestion" class="send-icon ps-1">
                                                                    <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-send" viewBox="0 0 16 16">
                                                                        <path d="M15.854.146a.5.5 0 0 1 .11.54l-5.819 14.547a.75.75 0 0 1-1.329.124l-3.178-4.995L.643 7.184a.75.75 0 0 1 .124-1.33L15.314.037a.5.5 0 0 1 .54.11ZM6.636 10.07l2.761 4.338L14.13 2.576zm6.787-8.201L1.591 6.602l4.339 2.76z"/>
                                                                    </svg>
                                                                </div>
                                                            </div>
                                                        </div>
                                                        <div v-if="answeredQuestions.length === 0" class="input-group centered pt-2">
                                                            <textarea class="search-bar form-control rounded fst-italic question-box" type="text" placeholder="Ask a question!" v-model="question"></textarea>
                                                            <div v-on:click="sendQuestion" class="send-icon ps-1">
                                                                <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-send" viewBox="0 0 16 16">
                                                                    <path d="M15.854.146a.5.5 0 0 1 .11.54l-5.819 14.547a.75.75 0 0 1-1.329.124l-3.178-4.995L.643 7.184a.75.75 0 0 1 .124-1.33L15.314.037a.5.5 0 0 1 .54.11ZM6.636 10.07l2.761 4.338L14.13 2.576zm6.787-8.201L1.591 6.602l4.339 2.76z"/>
                                                                </svg>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                                <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
                                                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                                    <span class="visually-hidden">Previous</span>
                                                </button>
                                                <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
                                                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                                    <span class="visually-hidden">Next</span>
                                                </button>
                                            </div>
                                        </div>
                                        <div class="py-1"></div>
                                    </div>

                                    <!-- [else] account is not claimed -->
                                    <div v-else>
                                        <div class="row text-center mx-1 py-2 default-text-no-background" style="background-color:#DDC8A9;">
                                            <p class="fw-bold fs-3 pt-3" style="font-style: italic; ">
                                                Do you own this business?
                                            </p>
                                            <p> Sign up for a producer account to answer latest questions from your fans! </p>
                                            <!-- spacer -->
                                            <div class="col-2"></div>
                                            <!-- button -->
                                            <button type="submit" class="col-8 btn secondary-btn-border-thick mb-3" @click="claimProducerAccount"> Claim This Business </button>
                                            <!-- spacer -->
                                            <div class="col-2"></div>
                                        </div>
                                    </div>

                                </div>
                            </div>

                    </div>
                        
                    </div>
                    <hr>
                    <!-- most popular (highest ratings) -->
                    <ListingRowDisplayProducerProfile 
                        :listingArr="mostPopular" 
                        displayName="Most Popular" 
                        :user="user" 
                        :listing="listing" 
                        @icon-clicked="handleIconClick"/>

                    <!-- most discussed (most number of reviews) -->
                    <ListingRowDisplayProducerProfile 
                        :listingArr="mostDiscussed" 
                        displayName="Most Discussed" 
                        :user="user" 
                        :listing="listing" 
                        @icon-clicked="handleIconClick"/>
                    
                    <!-- recently added -->
                    <ListingRowDisplayProducerProfile 
                        :listingArr="recentlyAdded" 
                        displayName="Recently Added" 
                        :user="user" 
                        :listing="listing" 
                        @icon-clicked="handleIconClick"/>

    
                </div> <!-- end of main page (hide all listings) -->

                <!-- show all listings-->
                <div v-else >
                    <!-- search & sort by -->
                    <div class="row">
                        <!-- back button -->
                        <div class="col-1 centered mobile-view-hide">
                            <!-- back button -->
                            <span style="display: inline-block;">
                                <span class="pe-2">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-arrow-clockwise" viewBox="0 0 16 16" v-on:click="resetListings()">
                                        <path fill-rule="evenodd" d="M8 3a5 5 0 1 0 4.546 2.914.5.5 0 0 1 .908-.417A6 6 0 1 1 8 2z"/>
                                        <path d="M8 4.466V.534a.25.25 0 0 1 .41-.192l2.36 1.966c.12.1.12.284 0 .384L8.41 4.658A.25.25 0 0 1 8 4.466"/>
                                    </svg>
                                </span>
                            </span>
                        </div>
                        <!-- search -->
                        <div class="col-8 ps-0 pe-3 mobile-col-10 mobile-ps-3 mobile-pe-0">
                            <!-- [if] user type is producer -->
                            <div v-if="correctProducer || isAdmin" class="row">
                                <div class="col-3 d-grid no padding mobile-pe-0">
                                    <button type="button" class="btn primary-btn-outline-thick rounded-0 mobile-pe-2 mobile-ps-2" v-on:click="editCatalogue()">
                                        <a class="default-clickable-text mobile-fs-7 mobile-view-hide"> Edit catalogue </a> 
                                        <a class="default-clickable-text mobile-fs-7 mobile-view-show"> Edit </a> 
                                    </button>
                                </div>
                                <div class="col-3 d-grid no padding mobile-pe-0">
                                    <button type="button" class="btn primary-btn-outline-thick rounded-0 mobile-pe-2 mobile-ps-2">
                                        <router-link :to="`/listing/create`" class="default-clickable-text mobile-fs-7 mobile-view-hide">
                                            Add Listing
                                        </router-link>
                                        <router-link :to="`/listing/create`" class="default-clickable-text mobile-fs-7 mobile-view-show">
                                            Add
                                        </router-link>
                                    </button>
                                </div>
                                <div class="col-6 d-grid no padding mobile-pe-0">
                                    <input class="search-bar form-control rounded fst-italic mobile-view-hide" type="text" placeholder="Search for expressions" style="height: 50px;" v-model="searchExpressions" v-on:keyup.enter="searchForExpressions()">
                                    <input class="search-bar form-control rounded fst-italic mobile-view-show mobile-fs-7" type="text" placeholder="Search expressions" style="height: 50px;" v-model="searchExpressions" v-on:keyup.enter="searchForExpressions()">
                                </div>
                            </div>
                            <!-- [else] user type is NOT producer -->
                            <div v-else class="row">
                                <div v-if="canMod && !isAdmin" class="col-3 d-grid no padding">
                                    <button type="button" class="btn primary-btn-outline-thick rounded-0" v-on:click="editCatalogue()">
                                        <a class="default-clickable-text"> Edit catalogue </a> 
                                    </button>
                                </div>
                                <div v-if="canMod && !isAdmin" class="col-9 d-grid no padding">
                                    <input class="search-bar form-control rounded fst-italic" type="text" placeholder="Search for expressions" style="height: 50px;" v-model="searchExpressions" v-on:keyup.enter="searchForExpressions()">
                                </div>
                                <div v-else-if="!isAdmin" class="col-12 d-grid no padding">
                                    <input class="search-bar form-control rounded fst-italic" type="text" placeholder="Search for expressions" style="height: 50px;" v-model="searchExpressions" v-on:keyup.enter="searchForExpressions()">
                                </div>
                            </div>
                        </div>
                
                        <!-- sort by -->
                        <div class="col-3 padding-for-followthisbusinessbutton-large-screen mobile-col-2 mobile-ps-0">
                            <div class="d-grid gap-2 dropdown">
                                <button class="btn primary-light-dropdown-homepage btn-lg dropdown-toggle mobile-view-remove-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false" style="white-space: nowrap; overflow:hidden;text-overflow: ellipsis;">
                                    <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="mobile-view-show bi bi-sort-down funnel-svg-dimensions" viewBox="0 0 16 16"><path d="M3.5 2.5a.5.5 0 0 0-1 0v8.793l-1.146-1.147a.5.5 0 0 0-.708.708l2 1.999.007.007a.497.497 0 0 0 .7-.006l2-2a.5.5 0 0 0-.707-.708L3.5 11.293zm3.5 1a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 0 1h-7a.5.5 0 0 1-.5-.5M7.5 6a.5.5 0 0 0 0 1h5a.5.5 0 0 0 0-1zm0 3a.5.5 0 0 0 0 1h3a.5.5 0 0 0 0-1zm0 3a.5.5 0 0 0 0 1h1a.5.5 0 0 0 0-1z"></path></svg>
                                    <span class="mobile-view-hide">Sort: {{ sortSelection.category != '' ? sortSelection.category : 'by Category' }}</span>
                                </button>
                                <ul class="dropdown-menu">
                                    <li><span class="dropdown-item" @click="sortByCategory('')"> Clear Sort </span></li>
                                    <li><hr class="dropdown-divider"></li>
                                    <li v-for="category in sortCategoryList" :key="category">
                                        <span class="dropdown-item" @click="sortByCategory(category)"> {{ category }} </span>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <!-- scrollable expressions for desktop view TZH -->
                    <div class="row scrollable-expressions-none mobile-view-hide">
                        <!-- v-loop for each listing -->
                        <div class="container text-start">
                            <div v-for="listing in lazyListings" v-bind:key="listing.id" class="p-3 mobile-pb-0">
                                <div class="row">
                                    <!-- image  remove style="width: 150px; height: 150px;" from img tag-->
                                    <div class="col-lg-2 col-12 image-container text-center mx-auto mb-3 mb-lg-0 producer-profile-no-left-padding-large-screen mobile-col-3 mobile-mx-0 mobile-px-0 mobile-mb-0">
                                        <router-link :to="{ path: '/listing/view/' +listing.id}" class="default-text-no-background">
                                            <!-- <img :src=" 'data:image/jpeg;base64,' + (listing['photo'] || defaultPhoto)" class="producer-bottle-listing-page-bottle-image" > -->
                                            <img :src="(listing['photo'] || defaultPhoto)" class="producer-bottle-listing-page-bottle-image" >
                                        </router-link>
                                        <div class="row">
                                            <!-- edit listing -->
                                            <div class="col-1">
                                            <button v-if="(correctProducer || isAdmin) && editingListing" type="button" class="icon-btn">
                                                <router-link :to="`/listing/edit/${listing.id}`" style="color:black;">
                                                    <svg viewBox="0 0 24 24" fill="currentColor" class="bi bi-sort-down funnel-svg-dimensions" xmlns="http://www.w3.org/2000/svg"><path d="M21.1213 2.70705C19.9497 1.53548 18.0503 1.53547 16.8787 2.70705L15.1989 4.38685L7.29289 12.2928C7.16473 12.421 7.07382 12.5816 7.02986 12.7574L6.02986 16.7574C5.94466 17.0982 6.04451 17.4587 6.29289 17.707C6.54127 17.9554 6.90176 18.0553 7.24254 17.9701L11.2425 16.9701C11.4184 16.9261 11.5789 16.8352 11.7071 16.707L19.5556 8.85857L21.2929 7.12126C22.4645 5.94969 22.4645 4.05019 21.2929 2.87862L21.1213 2.70705ZM18.2929 4.12126C18.6834 3.73074 19.3166 3.73074 19.7071 4.12126L19.8787 4.29283C20.2692 4.68336 20.2692 5.31653 19.8787 5.70705L18.8622 6.72357L17.3068 5.10738L18.2929 4.12126ZM15.8923 6.52185L17.4477 8.13804L10.4888 15.097L8.37437 15.6256L8.90296 13.5112L15.8923 6.52185ZM4 7.99994C4 7.44766 4.44772 6.99994 5 6.99994H10C10.5523 6.99994 11 6.55223 11 5.99994C11 5.44766 10.5523 4.99994 10 4.99994H5C3.34315 4.99994 2 6.34309 2 7.99994V18.9999C2 20.6568 3.34315 21.9999 5 21.9999H16C17.6569 21.9999 19 20.6568 19 18.9999V13.9999C19 13.4477 18.5523 12.9999 18 12.9999C17.4477 12.9999 17 13.4477 17 13.9999V18.9999C17 19.5522 16.5523 19.9999 16 19.9999H5C4.44772 19.9999 4 19.5522 4 18.9999V7.99994Z" ></path>
                                                    </svg>
                                                </router-link>
                                            </button>
                                            <button v-else-if="editingListing && user.modType.includes(listing.drinkType) && listing.allowMod" type="button" class="icon-btn">
                                                <router-link :to="`/listing/edit/${listing.id}`" style="color:black;">
                                                    <svg viewBox="0 0 24 24" fill="currentColor" class="bi bi-sort-down funnel-svg-dimensions" xmlns="http://www.w3.org/2000/svg"><path d="M21.1213 2.70705C19.9497 1.53548 18.0503 1.53547 16.8787 2.70705L15.1989 4.38685L7.29289 12.2928C7.16473 12.421 7.07382 12.5816 7.02986 12.7574L6.02986 16.7574C5.94466 17.0982 6.04451 17.4587 6.29289 17.707C6.54127 17.9554 6.90176 18.0553 7.24254 17.9701L11.2425 16.9701C11.4184 16.9261 11.5789 16.8352 11.7071 16.707L19.5556 8.85857L21.2929 7.12126C22.4645 5.94969 22.4645 4.05019 21.2929 2.87862L21.1213 2.70705ZM18.2929 4.12126C18.6834 3.73074 19.3166 3.73074 19.7071 4.12126L19.8787 4.29283C20.2692 4.68336 20.2692 5.31653 19.8787 5.70705L18.8622 6.72357L17.3068 5.10738L18.2929 4.12126ZM15.8923 6.52185L17.4477 8.13804L10.4888 15.097L8.37437 15.6256L8.90296 13.5112L15.8923 6.52185ZM4 7.99994C4 7.44766 4.44772 6.99994 5 6.99994H10C10.5523 6.99994 11 6.55223 11 5.99994C11 5.44766 10.5523 4.99994 10 4.99994H5C3.34315 4.99994 2 6.34309 2 7.99994V18.9999C2 20.6568 3.34315 21.9999 5 21.9999H16C17.6569 21.9999 19 20.6568 19 18.9999V13.9999C19 13.4477 18.5523 12.9999 18 12.9999C17.4477 12.9999 17 13.4477 17 13.9999V18.9999C17 19.5522 16.5523 19.9999 16 19.9999H5C4.44772 19.9999 4 19.5522 4 18.9999V7.99994Z" ></path>
                                                    </svg>
                                                </router-link>
                                            </button>
                                            </div>
                                            <!-- delete listing -->
                                            <div class="col-1"> 
                                            <button v-if="deletingListing" type="button" class="icon-btn" v-on:click="deleteListings(listing)">
                                                <a>
                                                    <svg viewBox="0 0 24 24" fill="none" class="bi bi-sort-down funnel-svg-dimensions" xmlns="http://www.w3.org/2000/svg">
                                                        <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M18 6L17.1991 18.0129C17.129 19.065 17.0939 19.5911 16.8667 19.99C16.6666 20.3412 16.3648 20.6235 16.0011 20.7998C15.588 21 15.0607 21 14.0062 21H9.99377C8.93927 21 8.41202 21 7.99889 20.7998C7.63517 20.6235 7.33339 20.3412 7.13332 19.99C6.90607 19.5911 6.871 19.065 6.80086 18.0129L6 6M4 6H20M16 6L15.7294 5.18807C15.4671 4.40125 15.3359 4.00784 15.0927 3.71698C14.8779 3.46013 14.6021 3.26132 14.2905 3.13878C13.9376 3 13.523 3 12.6936 3H11.3064C10.477 3 10.0624 3 9.70951 3.13878C9.39792 3.26132 9.12208 3.46013 8.90729 3.71698C8.66405 4.00784 8.53292 4.40125 8.27064 5.18807L8 6" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path> </g>
                                                    </svg>
                                                </a>
                                            </button>
                                            </div>
                                        </div>
                                    </div>
                                    <!-- details -->
                                    <div class="col-lg-10 col-12 ps-3 mobile-col-7 mobile-pe-0 mobile-ps-1">
                                        <!-- expression name, have tried & want to try & bookmark buttons -->
                                        <div class="row">
                                            <!-- expression name - tzh removed pt-2 from row-->
                                            <div class="col-7 mobile-col-12 mobile-pe-0">
                                                <div class="row ">
                                                    <p class="default-text fs-5 mobile-fs-6" style="margin-bottom:0.3rem;"> 
                                                        <router-link :to="{ path: '/listing/view/' +listing.id }" class="default-text-no-background">
                                                            <u> <b> {{ listing["listingName"] }}  </b> </u>
                                                        </router-link>
                                                    </p> 
                                                </div>
                                            </div>
                                            
                                            <!-- have tried button -->
                                            <div class="col-2 pe-0 mobile-view-hide">
                                                <div v-html="checkDrinkLists(listing).buttons.haveTried" class="d-grid"> </div>
                                            </div>
                                            <!-- want to try button -->
                                            <div class="col-2 ps-0 mobile-view-hide">
                                                <div v-html="checkDrinkLists(listing).buttons.wantToTry" class="d-grid"> </div>
                                            </div>
                                            <!-- bookmark button -->
                                            <div class="col-1 text-start p-0 mobile-view-hide">
                                                <BookmarkIcon 
                                                    v-if="user && Object.keys(user).length > 0" 
                                                    :user="user" 
                                                    :listing="listing" 
                                                    :overlay="false"
                                                    size="30"
                                                    @icon-clicked="handleIconClick" />
                                            </div>
                                        </div>
                                        <div class="row">
                                             <!-- Bottler / Drink Type / Type Category / ABV / Country / Description - added by TZH -->
                                                <p class="text-start mb-1 mobile-fs-7" > 
                                                         {{ listing["bottler"] }} | {{ listing["drinkType"] }} | {{ listing["typeCategory"] }} | {{ listing["abv"] }} ABV | {{ listing["originCountry"] }} 
                                                </p>

                                            
                                            <!-- official description --->
                                            <div class="col-10 mobile-view-hide">
                                                <div class="row">
                                                    <div v-if="listing.officialDesc?.length > 142">
                                                        <p v-if="!showFullDescription[listing.id]" style="margin-bottom:0.2rem;"><!-- tzh added truncated description --->
                                                            <em>{{ listing["officialDesc"].slice(0, 142) + (listing["officialDesc"].length > 142 ? '...' : '') }}</em>
                                                            <a @click="showFullDescription[listing.id] = true" style="font-weight: bold;">(Read More)</a>
                                                        </p>
                                                        <p v-else style="margin-bottom:0.2rem;"> <!-- tzh added full description --->
                                                            <em>{{ listing["officialDesc"] }}</em>
                                                            <a @click="showFullDescription[listing.id] = false" style="font-weight: bold;">(Read Less)</a>
                                                        </p>
                                                    </div>
                                                    <div v-else>
                                                        <p style="margin-bottom:0.2rem;"> <!-- tzh added full description --->
                                                            <em>{{ listing["officialDesc"] }}</em>
                                                        </p>
                                                    </div>
                                                </div>
                                            </div>
                                            <!-- rating-->
                                            <div class="col-2 d-flex align-items-center ps-lg-3 mobile-view-hide">
                                                <p class="fs-3 fw-bold rating-text text-end d-flex align-items-center" style="margin-bottom:0.1rem;">
                                                    {{ getRatings(listing) }}
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-star-fill ms-1" viewBox="0 0 16 16">
                                                        <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
                                                    </svg>
                                                </p>
                                            </div>

                                            
                                            <div class="row">
                                                    
                                                    <div class="col-4 mobile-view-hide">
                                                        <router-link :to="{ path: '/listing/view/' + listing.id }" >
                                                            <button type="button" class="btn primary-btn-outline-thick p-1 px-2" style="font-size:90%;"> See User Reviews </button>
                                                        </router-link>
                                                    </div>
                                                     
                                                     <div class="col-4">
                                                       
                                                    </div>
                                                    
                                                    <div class="col-4">
                                                        
                                                    </div>
                                                </div>

                                        </div>
                                        <!-- release date -->
                                        <!-- NOTE: can exclude for now (no data) -->
                                        <!-- <div class="row pt-5"> 
                                            <h5> 
                                                <b> Release Date:</b>
                                                date
                                            </h5>
                                        </div> -->
                                    </div>
                                    <!--mobile view rating -->
                                    <div class="mobile-col-2 mobile-pe-0 mobile-ps-1">
                                        <div class="d-flex flex-column align-items-center ps-lg-3 mobile-view-show">
                                            <p class="fs-3 fw-bold rating-text text-end d-flex align-items-center mobile-fs-5" style="margin-bottom:0.1rem;">
                                                {{ getRatings(listing) }}
                                            </p>
                                            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-star-fill ms-2 me-2" viewBox="0 0 16 16">
                                                <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
                                            </svg>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- load more button -->
                            <div class="d-flex justify-content-center align-items-center" v-if="lazyListings.length < filteredListings.length">
                                <button class="btn primary-btn-less-round btn-lg mt-2 mb-3" @click="loadMoreListings">Load More</button>
                            </div>
                        </div>
                    </div> <!-- end of listings -->
                    <!-- non-scrollable expressions for mobile view TZH -->
                        <div class="row  mobile-view-show">
                        <!-- v-loop for each listing -->
                        <div class="container text-start">
                            <div v-for="listing in lazyListings" v-bind:key="listing.id" class="p-3 mobile-pb-0">
                                <div class="row">
                                    <!-- image  remove style="width: 150px; height: 150px;" from img tag-->
                                    <div class="col-lg-2 col-12 image-container text-center mx-auto mb-3 mb-lg-0 producer-profile-no-left-padding-large-screen mobile-col-3 mobile-mx-0 mobile-px-0 mobile-mb-0">
                                        <router-link :to="{ path: '/listing/view/' +listing.id}" class="default-text-no-background">
                                            <!-- <img :src=" 'data:image/jpeg;base64,' + (listing['photo'] || defaultPhoto)" class="producer-bottle-listing-page-bottle-image" > -->
                                            <img :src="(listing['photo'] || defaultPhoto)" class="producer-bottle-listing-page-bottle-image" >
                                        </router-link>
                                        <div class="row">
                                            <!-- edit listing -->
                                            <div class="col-1">
                                            <button v-if="(correctProducer || isAdmin) && editingListing" type="button" class="icon-btn">
                                                <router-link :to="`/listing/edit/${listing.id}`" style="color:black;" >
                                                    <svg width="25" height="25" viewBox="0 0 24 24" fill="currentColor" class="bi bi-sort-down" xmlns="http://www.w3.org/2000/svg"><path d="M21.1213 2.70705C19.9497 1.53548 18.0503 1.53547 16.8787 2.70705L15.1989 4.38685L7.29289 12.2928C7.16473 12.421 7.07382 12.5816 7.02986 12.7574L6.02986 16.7574C5.94466 17.0982 6.04451 17.4587 6.29289 17.707C6.54127 17.9554 6.90176 18.0553 7.24254 17.9701L11.2425 16.9701C11.4184 16.9261 11.5789 16.8352 11.7071 16.707L19.5556 8.85857L21.2929 7.12126C22.4645 5.94969 22.4645 4.05019 21.2929 2.87862L21.1213 2.70705ZM18.2929 4.12126C18.6834 3.73074 19.3166 3.73074 19.7071 4.12126L19.8787 4.29283C20.2692 4.68336 20.2692 5.31653 19.8787 5.70705L18.8622 6.72357L17.3068 5.10738L18.2929 4.12126ZM15.8923 6.52185L17.4477 8.13804L10.4888 15.097L8.37437 15.6256L8.90296 13.5112L15.8923 6.52185ZM4 7.99994C4 7.44766 4.44772 6.99994 5 6.99994H10C10.5523 6.99994 11 6.55223 11 5.99994C11 5.44766 10.5523 4.99994 10 4.99994H5C3.34315 4.99994 2 6.34309 2 7.99994V18.9999C2 20.6568 3.34315 21.9999 5 21.9999H16C17.6569 21.9999 19 20.6568 19 18.9999V13.9999C19 13.4477 18.5523 12.9999 18 12.9999C17.4477 12.9999 17 13.4477 17 13.9999V18.9999C17 19.5522 16.5523 19.9999 16 19.9999H5C4.44772 19.9999 4 19.5522 4 18.9999V7.99994Z" ></path>
                                                    </svg>
                                                </router-link>
                                            </button>
                                            <button v-else-if="editingListing && user.modType.includes(listing.drinkType) && listing.allowMod" type="button" class="icon-btn">
                                                <router-link :to="`/listing/edit/${listing.id}`" style="color:black;">
                                                    <svg width="25" height="25" viewBox="0 0 24 24" fill="currentColor" class="bi bi-sort-down " xmlns="http://www.w3.org/2000/svg"><path d="M21.1213 2.70705C19.9497 1.53548 18.0503 1.53547 16.8787 2.70705L15.1989 4.38685L7.29289 12.2928C7.16473 12.421 7.07382 12.5816 7.02986 12.7574L6.02986 16.7574C5.94466 17.0982 6.04451 17.4587 6.29289 17.707C6.54127 17.9554 6.90176 18.0553 7.24254 17.9701L11.2425 16.9701C11.4184 16.9261 11.5789 16.8352 11.7071 16.707L19.5556 8.85857L21.2929 7.12126C22.4645 5.94969 22.4645 4.05019 21.2929 2.87862L21.1213 2.70705ZM18.2929 4.12126C18.6834 3.73074 19.3166 3.73074 19.7071 4.12126L19.8787 4.29283C20.2692 4.68336 20.2692 5.31653 19.8787 5.70705L18.8622 6.72357L17.3068 5.10738L18.2929 4.12126ZM15.8923 6.52185L17.4477 8.13804L10.4888 15.097L8.37437 15.6256L8.90296 13.5112L15.8923 6.52185ZM4 7.99994C4 7.44766 4.44772 6.99994 5 6.99994H10C10.5523 6.99994 11 6.55223 11 5.99994C11 5.44766 10.5523 4.99994 10 4.99994H5C3.34315 4.99994 2 6.34309 2 7.99994V18.9999C2 20.6568 3.34315 21.9999 5 21.9999H16C17.6569 21.9999 19 20.6568 19 18.9999V13.9999C19 13.4477 18.5523 12.9999 18 12.9999C17.4477 12.9999 17 13.4477 17 13.9999V18.9999C17 19.5522 16.5523 19.9999 16 19.9999H5C4.44772 19.9999 4 19.5522 4 18.9999V7.99994Z" ></path>
                                                    </svg>
                                                </router-link>
                                            </button>
                                            </div>
                                            <!-- delete listing -->
                                            <div class="col-1">
                                            <button v-if="deletingListing" type="button" class="icon-btn" v-on:click="deleteListings(listing)">
                                                <a>
                                                    <svg width="25" height="25" viewBox="0 0 24 24" fill="none" class="bi bi-sort-down " xmlns="http://www.w3.org/2000/svg">
                                                        <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M18 6L17.1991 18.0129C17.129 19.065 17.0939 19.5911 16.8667 19.99C16.6666 20.3412 16.3648 20.6235 16.0011 20.7998C15.588 21 15.0607 21 14.0062 21H9.99377C8.93927 21 8.41202 21 7.99889 20.7998C7.63517 20.6235 7.33339 20.3412 7.13332 19.99C6.90607 19.5911 6.871 19.065 6.80086 18.0129L6 6M4 6H20M16 6L15.7294 5.18807C15.4671 4.40125 15.3359 4.00784 15.0927 3.71698C14.8779 3.46013 14.6021 3.26132 14.2905 3.13878C13.9376 3 13.523 3 12.6936 3H11.3064C10.477 3 10.0624 3 9.70951 3.13878C9.39792 3.26132 9.12208 3.46013 8.90729 3.71698C8.66405 4.00784 8.53292 4.40125 8.27064 5.18807L8 6" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path> </g>
                                                    </svg>
                                                </a>
                                            </button>
                                            </div>
                                        </div>
                                    </div>
                                    <!-- details -->
                                    <div class="col-lg-10 col-12 ps-3 mobile-col-7 mobile-pe-0 mobile-ps-1">
                                        <!-- expression name, have tried & want to try & bookmark buttons -->
                                        <div class="row">
                                            <!-- expression name - tzh removed pt-2 from row-->
                                            <div class="col-7 mobile-col-12 mobile-pe-0">
                                                <div class="row ">
                                                    <p class="default-text fs-5 mobile-fs-6" style="margin-bottom:0.3rem;"> 
                                                        <router-link :to="{ path: '/listing/view/' +listing.id }" class="default-text-no-background">
                                                            <u> <b> {{ listing["listingName"] }}  </b> </u>
                                                        </router-link>
                                                    </p> 
                                                </div>
                                            </div>
                                            
                                            <!-- have tried button -->
                                            <div class="col-2 pe-0 mobile-view-hide">
                                                <div v-html="checkDrinkLists(listing).buttons.haveTried" class="d-grid"> </div>
                                            </div>
                                            <!-- want to try button -->
                                            <div class="col-2 ps-0 mobile-view-hide">
                                                <div v-html="checkDrinkLists(listing).buttons.wantToTry" class="d-grid"> </div>
                                            </div>
                                            <!-- bookmark button -->
                                            <div class="col-1 text-start p-0 mobile-view-hide">
                                                <BookmarkIcon 
                                                    v-if="user && Object.keys(user).length > 0" 
                                                    :user="user" 
                                                    :listing="listing" 
                                                    :overlay="false"
                                                    size="30"
                                                    @icon-clicked="handleIconClick" />
                                            </div>
                                        </div>
                                        <div class="row">
                                             <!-- Bottler / Drink Type / Type Category / ABV / Country / Description - added by TZH -->
                                                <p class="text-start mb-1 mobile-fs-7" > 
                                                         {{ listing["bottler"] }} | {{ listing["drinkType"] }} | {{ listing["typeCategory"] }} | {{ listing["abv"] }} ABV | {{ listing["originCountry"] }} 
                                                </p>

                                            
                                            <!-- official description --->
                                            <div class="col-10 mobile-view-hide">
                                                <div class="row">
                                                    <div v-if="listing.officialDesc?.length > 142">
                                                        <p v-if="!showFullDescription[listing.id]" style="margin-bottom:0.2rem;"><!-- tzh added truncated description --->
                                                            <em>{{ listing["officialDesc"].slice(0, 142) + (listing["officialDesc"].length > 142 ? '...' : '') }}</em>
                                                            <a @click="showFullDescription[listing.id] = true" style="font-weight: bold;">(Read More)</a>
                                                        </p>
                                                        <p v-else style="margin-bottom:0.2rem;"> <!-- tzh added full description --->
                                                            <em>{{ listing["officialDesc"] }}</em>
                                                            <a @click="showFullDescription[listing.id] = false" style="font-weight: bold;">(Read Less)</a>
                                                        </p>
                                                    </div>
                                                    <div v-else>
                                                        <p style="margin-bottom:0.2rem;"> <!-- tzh added full description --->
                                                            <em>{{ listing["officialDesc"] }}</em>
                                                        </p>
                                                    </div>
                                                </div>
                                            </div>
                                            <!-- rating-->
                                            <div class="col-2 d-flex align-items-center ps-lg-3 mobile-view-hide">
                                                <p class="fs-3 fw-bold rating-text text-end d-flex align-items-center" style="margin-bottom:0.1rem;">
                                                    {{ getRatings(listing) }}
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-star-fill ms-1" viewBox="0 0 16 16">
                                                        <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
                                                    </svg>
                                                </p>
                                            </div>

                                            
                                            <div class="row">
                                                    
                                                    <div class="col-4 mobile-view-hide">
                                                        <router-link :to="{ path: '/listing/view/' + listing.id }" >
                                                            <button type="button" class="btn primary-btn-outline-thick p-1 px-2" style="font-size:90%;"> See User Reviews </button>
                                                        </router-link>
                                                    </div>
                                                     
                                                     <div class="col-4">
                                                       
                                                    </div>
                                                    
                                                    <div class="col-4">
                                                        
                                                    </div>
                                                </div>

                                        </div>
                                        <!-- release date -->
                                        <!-- NOTE: can exclude for now (no data) -->
                                        <!-- <div class="row pt-5"> 
                                            <h5> 
                                                <b> Release Date:</b>
                                                date
                                            </h5>
                                        </div> -->
                                    </div>
                                    <!--mobile view rating -->
                                    <div class="mobile-col-2 mobile-pe-0 mobile-ps-1">
                                        <div class="d-flex flex-column align-items-center ps-lg-3 mobile-view-show">
                                            <p class="fs-3 fw-bold rating-text text-end d-flex align-items-center mobile-fs-5" style="margin-bottom:0.1rem;">
                                                {{ getRatings(listing) }}
                                            </p>
                                            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-star-fill ms-2 me-2" viewBox="0 0 16 16">
                                                <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
                                            </svg>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- load more button -->
                            <div class="d-flex justify-content-center align-items-center" v-if="lazyListings.length < filteredListings.length">
                                <button class="btn primary-btn-less-round btn-lg mt-2 mb-3" @click="loadMoreListings">Load More</button>
                            </div>
                        </div>
                    </div> <!-- end of listings -->
                </div>

            </div> <!-- end of producer information -->
            
            <!-- view analytics & q&a for producer & 88 bamboo's deepdive -->
            <div class="col-xl-3 col-12 ps-lg-0">
                <div class="row">
                    <!-- view analytics -->
                    <div v-if="correctProducer">
                        <router-link :to="{ path: '/Producers/ProducersDashboard/' + producer_id}" class="col-12 d-grid gap-2 pb-3 default-clickable-text">
                            <button class="btn secondary-btn-not-rounded rounded-0" type="button" style=" font-weight: bold;"> View My Analytics </button>
                        </router-link> 

                        <router-link :to="{ path: '/business/settings'}" class="col-12 d-grid gap-2 pb-3 default-clickable-text">
                            <button class="btn secondary-btn-not-rounded rounded-0" type="button" style=" font-weight: bold;"> Settings </button>
                        </router-link> 

                        <!-- Button for change/reset password -->
                        <button type="button" class="btn secondary-btn-not-rounded rounded-0 mb-3 col-12 d-grid gap-2 default-clickable-text" data-bs-toggle="modal" data-bs-target="#changePasswordModal">Change/Reset Password</button>
                    </div>
                    <!-- q&a -->
                    <div class="col-xl-12 col-lg-4 col-md-6 col-12 mobile-view-hide">
                        <div class="square primary-square-green rounded p-3 mb-3"> <!--tzh added -green -->
                            <!-- header text -->
                            <div class="square-inline text-start">
                                <!-- [if] user type producer -->
                                <div v-if="correctProducer" class="mr-auto"> 
                                    <h4> Q&A for You! </h4> 
                                    <div v-if="claimStatus">
                                        <router-link :to="{ path: '/Producers/ProducersQA/' + producer_id}" class="default-text-no-background">
                                            <p class="reverse-text no-margin text-decoration-underline text-start pb-2"> View All </p>
                                        </router-link> 
                                    </div>
                                </div>
                                <!-- [else] user type is NOT producer -->
                                <h4 v-else class="mr-auto"> Q&As for {{ specified_producer["producerName"] }} </h4>
                            </div>

                            <!-- [if] account is claimed -->
                            <div v-if="claimStatus">
                                <!-- show buttons for answered & unanswered questions -->
                                <div v-if="correctProducer" class="row text-center px-2">
                                    <div class="col-6 d-grid gap-0 no-padding">
                                        <button type="button" class="btn tertiary-btn-qa rounded-0 reverse-clickable-text">
                                            <a class="reverse-clickable-text" v-on:click="showAnswered()">
                                                Answered
                                            </a>
                                        </button>
                                    </div>
                                    <div class="col-6 d-grid gap-0 no-padding">
                                        <button type="button" class="btn tertiary-btn-qa rounded-0 reverse-clickable-text">
                                            <a class="reverse-clickable-text" v-on:click="showUnanswered()">
                                                Unanswered
                                            </a>
                                        </button>
                                    </div>
                                </div>
                                <!-- body -->
                                <div class="text-start pt-2">
                                    <!-- responses to q&a -->
                                    <div id="carouselExample" class="carousel slide">
                                        <div class="carousel-inner px-4">
                                            <!-- [if] user type is producer -->
                                            <div v-if="correctProducer">
                                                <!-- show answered questions -->
                                                <div v-if="answerStatus">
                                                    <div class="carousel-item" v-for="(qa, index) in answeredQuestions" v-bind:key="qa.id" v-bind:class="{ 'active': index === 0 }">
                                                        <p> <b> Q: {{ qa["question"] }} </b> </p>
                                                        <!-- [if] not editing -->
                                                        <button v-if="correctProducer && (editingQA == false || editingQAID != qa.id)" type="button" class="btn btn-warning rounded-0 me-1" v-on:click="editQA(qa)">
                                                            Edit answer
                                                        </button>
                                                        <!-- [else] if editing -->
                                                        <button v-if="correctProducer && editingQAID == qa.id" type="button" class="btn btn-success rounded-0 me-1" v-on:click="saveQAEdit(qa)">
                                                            Save
                                                        </button>
                                                        <!-- [else] if editing -->
                                                        <button v-if="correctProducer && editingQAID == qa.id" type="button" class="btn btn-warning rounded-0 me-1" v-on:click="cancelQAEdit(qa)">
                                                            Cancel
                                                        </button>
                                                        <!-- delete -->
                                                        <button type="button" class="btn btn-danger rounded-0" v-on:click="deleteQAEdit(qa)">
                                                            Delete
                                                        </button>
                                                        <!-- spacer -->
                                                        <div class="mt-2"></div>
                                                        <p v-if="editingQA == false || editingQAID != qa.id"> A: {{ qa["answer"] }} </p>
                                                        <textarea v-else-if="editingQAID == qa.id" class="search-bar form-control rounded fst-italic question-box flex-grow-1" type="text" placeholder="Edit answer." v-model="edit_answer[qa.id]"></textarea>
                                                    </div>
                                                </div>

                                                <!-- show unanswered questions -->
                                                <div v-else>
                                                        <div class="carousel-item" v-for="(qa, index) in unansweredQuestions" v-bind:key="qa.id" v-bind:class="{ 'active': index === 0 }">
                                                        <p> <b> Q: {{ qa["question"] }} </b> </p>
                                                        <div class="input-group centered">
                                                            <div class="input-group centered pt-2">
                                                                <textarea class="search-bar form-control rounded fst-italic question-box" type="text" placeholder="Respond to your fans latest questions." v-model="answer"></textarea>
                                                                <div v-on:click="sendAnswer(qa)" class="send-icon ps-1">
                                                                    <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-send" viewBox="0 0 16 16">
                                                                        <path d="M15.854.146a.5.5 0 0 1 .11.54l-5.819 14.547a.75.75 0 0 1-1.329.124l-3.178-4.995L.643 7.184a.75.75 0 0 1 .124-1.33L15.314.037a.5.5 0 0 1 .54.11ZM6.636 10.07l2.761 4.338L14.13 2.576zm6.787-8.201L1.591 6.602l4.339 2.76z"/>
                                                                    </svg>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <!-- [else] user type is NOT producer -->
                                            <div v-else>
                                                <div class="carousel-item" v-for="(qa, index) in answeredQuestions" v-bind:key="qa.id" v-bind:class="{ 'active': index === 0 }">
                                                    <div>
                                                        <p> <b> Q: {{ qa["question"] }} </b> </p>
                                                        <p> A: {{ qa["answer"] }} </p>
                                                    </div>
                                                    <div class="input-group centered pt-2">
                                                        <textarea class="search-bar form-control rounded fst-italic question-box" type="text" placeholder="Ask your question!" v-model="question"></textarea>
                                                        <div v-on:click="sendQuestion" class="send-icon ps-1">
                                                            <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-send" viewBox="0 0 16 16">
                                                                <path d="M15.854.146a.5.5 0 0 1 .11.54l-5.819 14.547a.75.75 0 0 1-1.329.124l-3.178-4.995L.643 7.184a.75.75 0 0 1 .124-1.33L15.314.037a.5.5 0 0 1 .54.11ZM6.636 10.07l2.761 4.338L14.13 2.576zm6.787-8.201L1.591 6.602l4.339 2.76z"/>
                                                            </svg>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div v-if="answeredQuestions.length === 0" class="input-group centered pt-2">
                                                    <textarea class="search-bar form-control rounded fst-italic question-box" type="text" placeholder="Ask a question!" v-model="question"></textarea>
                                                    <div v-on:click="sendQuestion" class="send-icon ps-1">
                                                        <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-send" viewBox="0 0 16 16">
                                                            <path d="M15.854.146a.5.5 0 0 1 .11.54l-5.819 14.547a.75.75 0 0 1-1.329.124l-3.178-4.995L.643 7.184a.75.75 0 0 1 .124-1.33L15.314.037a.5.5 0 0 1 .54.11ZM6.636 10.07l2.761 4.338L14.13 2.576zm6.787-8.201L1.591 6.602l4.339 2.76z"/>
                                                        </svg>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
                                            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                            <span class="visually-hidden">Previous</span>
                                        </button>
                                        <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
                                            <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                            <span class="visually-hidden">Next</span>
                                        </button>
                                    </div>
                                </div>
                                <div class="py-1"></div>
                            </div>

                            <!-- [else] account is not claimed -->
                            <div v-else>
                                <div class="row text-center mx-1 py-2 default-text-no-background" style="background-color:#DDC8A9;">
                                    <p class="fw-bold fs-3 pt-3" style="font-style: italic; ">
                                        Do you own this business?
                                    </p>
                                    <p> Sign up for a producer account to answer latest questions from your fans! </p>
                                    <!-- spacer -->
                                    <div class="col-2"></div>
                                    <!-- button -->
                                    <button type="submit" class="col-8 btn secondary-btn-border-thick mb-3" @click="claimProducerAccount"> Claim This Business </button>
                                    <!-- spacer -->
                                    <div class="col-2"></div>
                                </div>
                            </div>

                        </div>
                    </div>
                    <!-- 88 bamboo's deepdive -->
                    <div class="col-xl-12 col-lg-4 col-md-6 col-12 mobile-view-hide">
                        <div class="square primary-square-green-outline rounded p-3 mb-3"> <!--tzh changed secondary-square to primary-square-green-outline -->
                            <!-- header text -->
                            <div class="py-2 text-start">
                                <h4> 88 Bamboo's Review </h4>
                                <a v-if="isHttpValid(specified_producer['producerLink'])" :href="specified_producer['producerLink']" class="text-left default-text-no-background row">
                                    <div class="row">
                                        <div class="col-md-5 col-3">
                                            {{ getOGImage(specified_producer['producerLink']) }}
                                            <!-- [if] there is a cover image for the post-->
                                            <img v-if="ogImage != null" :src="ogImage[specified_producer.producerLink]" alt="OG Image" style="width: 80px; height: 80px;">
                                            <!-- [else] there is no cover image for the post (put 88 bamboo's logo) -->                    
                                            <img v-else src="https://88bamboo.co/cdn/shop/files/88B_New_Logo_-_white_face_transparent_background_180x.png?v=1655894111" style="width: 80px; height: 80px;">                                   
                                        </div>
                                        <div class="col-md-7 col-9">
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

        </div> <!-- end of row -->

        <!-- Start of change/reset password modal -->
        <div v-if="correctProducer" class="modal fade" id="changePasswordModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header" style="background-color: #535C72">
                        <h1 class="modal-title fs-5" id="exampleModalLabel" style="color: white;">Change Password</h1>
                        <button type="button" @click="resetChangePassword" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <!-- Initial select mode, change or reset password -->
                    <div v-if="changingPassword==''" class="modal-body">
                        <button class="btn tertiary-btn reverse-clickable-text m-1" type="button" @click="changePasswordMode('change')">
                            Change Password
                        </button>      
                        <button class="btn tertiary-btn reverse-clickable-text m-1" type="button" @click="changePasswordMode('reset')">
                            Reset Password
                        </button>      
                    </div>
                    <div class="modal-body text-center">
                        <div v-if="changingPassword =='change' && !(confirmChangePassword||passwordError||passwordSuccess||passwordMismatch)">
                            <p class="text-start mb-1"> Old Password: <span class="text-danger">*</span></p>
                            <input type='password' v-model="oldPassword" class="form-control" id="oldPassword" placeholder="Enter Previous Password">
                            <p class="text-start mt-3 mb-1"> New Password: <span class="text-danger">*</span></p>
                            <input type='password' v-model="newPassword" class="form-control" id="newPassword" placeholder="Enter New Password">
                        </div>  
                        <div v-if="confirmChangePassword && !(passwordError||passwordSuccess||passwordMismatch)">
                            <b>Are you sure you want to change password?</b>
                        </div>
                        <div v-if="changingPassword =='reset' && !(confirmResetPassword||passwordError||passwordSuccess)">
                            <p>Please key in OTP sent to your email:</p>
                            <div class = "input-group">
                                <input type='text' class="form-control" placeholder="Enter OTP" v-model="resetPin">
                                <button :disabled="isButtonDisabled" class="btn btn-outline-secondary" type="button" id="resendPin" @click="sendResetPin">Send Pin</button>
                            </div>
                            <!-- <p v-show="isButtonDisabled" class="text-start mb-1 text-success" id="sendPinSuccess"></p> -->
                            <p v-show="isButtonDisabled" class="text-start mb-1 text-success" id="sendPinSuccess"></p>
                            <p v-show="isButtonDisabled" class="text-start mb-1 text-danger" id="sendPinError"></p>
                            <p v-show="verifyErrorMessage.length>0" class="text-start mb-1 text-danger">{{ verifyErrorMessage }}</p>
                        </div>  
                        
                        <!-- Confirm if want to reset password-->
                        <div v-if="confirmResetPassword && !(passwordError||passwordSuccess||resettingPassword)">
                            <b>Are you sure you want to reset your password? A new password will be sent to you.</b>
                        </div>
                        <div v-if="confirmResetPassword && resettingPassword && !(passwordError||passwordSuccess)">
                            <b>Please wait while password is being resetted.</b>
                        </div>

                        <!-- if password change/reset is successful -->
                        <p v-if="passwordSuccess" class="text-success fst-italic fw-bold fs-3">Password {{ changingPassword }} is successful</p>
                        <p v-if="passwordSuccess && confirmResetPassword" class="text-success fst-italic fw-bold fs-3">An email has been sent to you containing the password.</p>
                        
                        <!-- if password change/reset faces error -->
                        <p v-if="passwordError" class ="text-danger fst-italic fw-bold fs-3">There is an error during password {{ changingPassword }}, please try again!</p>
                        <p v-if="passwordMismatch" class ="text-danger fst-italic fw-bold fs-3">Old password do not match, please try again</p>
                    </div>

                    <div class="modal-footer">
                        <!-- To return to previous select change password or reset password -->
                        <button v-if="changingPassword!='' && !resettingPassword" type="button" @click="selectPasswordMode" class="btn btn-secondary">Return</button>

                        <!-- Close modal-->
                        <button v-if="!resettingPassword" type="button" @click="resetChangePassword" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>

                        <!-- Change password first confirmation and second confirmation -->
                        <button v-if="changingPassword == 'change' && !(confirmChangePassword||passwordError||passwordSuccess||passwordMismatch||resettingPassword)" type="button" @click="updatePassword" class="btn btn-primary">Change Password</button>
                        <button v-if="confirmChangePassword && !(passwordError||passwordSuccess||passwordMismatch||resettingPassword)" type="button" @click="confirmUpdatePassword" class="btn btn-primary">Update Password</button>
                        
                        <!-- Reset password first confirmation and second confirmation -->
                        <button v-if="changingPassword == 'reset' && !(confirmResetPassword||passwordError||passwordSuccess||resettingPassword)" type="button" @click="verifyOTP" class="btn btn-primary">Verify OTP</button>
                        <button v-if="confirmResetPassword && !(passwordError||passwordSuccess||resettingPassword)" type="button" @click="resetPassword" class="btn btn-primary">Reset Password</button>                        
                    
                    </div>
                </div>
            </div>
        </div>
        <!-- Change/reset password end -->

        <BookmarkModal 
            v-if="user" 
            :user="user" 
            :listings="listings" 
            :listingID="bookmarkListingID" />

    </div> <!-- end of main content -->

</template>

<!-- ---------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<!-- JavaScript -->
<script>
// import { all } from 'axios';
    import NavBar from '@/components/NavBar.vue';
    import ListingRowDisplayProducerProfile from '@/components/ListingRowDisplayProducerProfile.vue';
    import BookmarkIcon from '@/components/BookmarkIcon.vue';
    import BookmarkModal from '@/components/BookmarkModal.vue';



    export default {
        components: {
            NavBar,
            ListingRowDisplayProducerProfile,
            BookmarkIcon, 
            BookmarkModal
        },
        data() {
            return {
                dataLoaded: false,
                // data from database
                // countries: [],
                listings: [],
                lazyListings: [],
                // producers: [],
                reviews: [],
                // users: [],
                drinkTypes: [],
                requestListings: [],
                requestEdits: [],
                modRequests: [],
                producersProfileViews: [],

                // define user type here (defined on mounted() function)
                user_id: "", // 65b327d5687b64f8302d56ee | 65b327d5687b64f8302d56ef
                userType: "",
                correctProducer: false,
                claimStatus: false,
                user: null,

                // all drinks that producer has
                allDrinks: [],
                allDrinksCount: 0,
                drinkCounts: {},
                sortedDrinksCounts: {},
                mostDiscussed: [],
                recentlyAdded: [],

                // all reviews for producer's drinks
                allReviews: [],
                allReviewsCount: 0,
                drinkRatings: {},
                sortedAverageRatings: {},
                mostPopular: [],

                // check if user is editing
                editing: false,

                // edit image
                selectedImage: '', // changed image
                image64: null, // original image

                // edit other fields
                edit_producerName: '',
                edit_producerDesc: '',
                edit_originCountry: '',

                // search
                searchInput: '',
                searchExpressions: '',
                searchTerm: '',
                searchResults: [],
                filteredListings: [],

                // specified producer
                producer_id: null,
                specified_producer: {},
                specified_producer_original_photo: '',

                // flag for if mod can edit any listings
                canMod: false,

                // flag for admin
                isAdmin: false,

                // q&a
                question: '',
                answer: '',

                // status to indicate whether to show listings or not
                showListings: false,

                // customization for drinkLists buttons
                // [TODO] get drink list of user, for now is hardcoded
                drinkList:  {
                                "haveTried": ["Harmony Collection Inspired by Intense Arabica"],
                                "wantToTry": ["Catnip Gin No. 2", "Five Farms Irish Cream Liqueur"]
                            },
                haveTried: false,
                wantToTry: false,

                // to track if catalogue is being edited
                editingListing:false,
                deletingListing:false,

                // to fetch producer's latest updates
                hasUpdates: false,
                update_id: null,
                latestUpdate: {},
                updateLikes: [],
                likeStatus: false,
                updateLikesCount: 0,

                // to fetch producer's remaining updates
                showRemainingUpdates: false,
                remainingUpdates: [],
                remainingUpdateLikes: {},
                remainingLikeStatus: {},
                remainingLikesCount: {},

                // to get producer's answered questions
                showQnA: false,
                answeredQuestions: [],
                unansweredQuestions: [],
                answerStatus: true,

                // for producer to add new updates
                currDate: new Date().toISOString(),
                updateFileName: '', // name of file
                updateImage: '', // changed image
                updateImage64: null, // original image
                updateText: '',

                deepDiveLinkFormatted: "",

                // to check if user is following producer
                following: false,

                // for bookmark component
                bookmarkListingID: {},

                // for sort function
                sortSelection: {
                    category: ''
                },
                sortCategoryList: [
                                    'Alphabetical (A - Z)',
                                    'Alphabetical (Z - A)',
                                    'Date (Newest - Oldest)',
                                    'Date (Oldest - Newest)',
                                    'Ratings (Highest - Lowest)',
                                    'Ratings (Lowest - Highest)',
                                ],
                sortedListings: [],

                // for producer profile views
                producerProfileViewInfo: {},
                producerProfileID: null,

                // for editing update
                editingLatestUpdate: false,
                editingRemainingUpdate: false,
                editingRemainingUpdateID: "",
                edit_latestUpdateText: "",
                edit_remainingUpdateText: {},
                selectedLatestUpdateImage: "",
                image64LatestUpdate: null,
                selectedRemainingUpdateImage: "",
                image64RemainingUpdate: null,

                // for editing Q&A
                editingQA: false,
                edit_answer: {},
                editingQAID: "",

                // for the review cover image
                ogImage: {},

                // for change/reset password
                oldPassword:"",
                newPassword:"",
                changingPassword:"",
                confirmChangePassword: false,
                confirmResetPassword: false,
                passwordError: false,
                passwordSuccess: false,
                passwordMismatch: false,
                resetPin: "",
                isButtonDisabled: false,
                verifyErrorMessage:"",
                resettingPassword:false,

                // default producer photo
                defaultPhoto: "https://drinkximages.s3.us-east-1.amazonaws.com/images/2d4d94bc-313e-4621-9a15-4bfbf77958de.jpg",
                defaultProfilePhoto: "https://drinkximages.s3.us-east-1.amazonaws.com/images/27e129b8-2d6e-44a3-8c14-d78c815b8056.jpg",
                // for truncation of official bottle description <!-- tzh added  --->
                showFullDescription: {},
                //for truncation of producer description - tzh added
                showFullProducerDescription:false
            };
        },
        async mounted() {
            var userID = localStorage.getItem('88B_accID')
            if(userID != null){
                this.user_id = userID;
            }

            var userType = localStorage.getItem('88B_accType');
            if(userType != null){
                this.userType = userType;
            }

            await this.loadData();
        },
        methods: {
            // load data from database
            async loadData() {
                // Get the query string parameters (listing ID) from the URL
                this.producer_id = this.$route.params.producerID;
                    if (this.producer_id == null) {
                        // redirect to page
                        this.$router.push('/');
                    }
                    else {
                        // check if user_id same as producer_id
                        if (this.user_id == this.producer_id && this.userType == "producer") {
                            this.correctProducer = true;
                        }
                    }
                // producers
                // _id, producerName, producerDesc, originCountry, statusOB, mainDrinks
                try {
                        const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getProducer/${this.producer_id}`);
                        this.specified_producer = response.data
                        this.specified_producer_original_photo = this.specified_producer['photo']

                        if (this.specified_producer.stripeCustomerId) {    
                            this.claimStatus = false                        
                            // check for active subscription if last check status date before today
                            const claimStatusCheckDate = this.specified_producer['claimStatusCheckDate']
                            // if (claimStatusCheckDate) {
                            if ((claimStatusCheckDate?.split('T')[0] < new Date().toISOString().split('T')[0]) || !claimStatusCheckDate) {
                                console.log('checking subscription');
                                // check for active subscription
                                try {
                                    const response = await this.$axios.post(`${process.env.VUE_APP_API_URL}/payment/retrieve-latest-subscription`, {
                                        customerId: this.specified_producer.stripeCustomerId,
                                    }, {
                                        headers: {
                                            'Content-Type': 'application/json',
                                        }
                                    });
                                    this.subscription = response.data;
                                    console.log(this.subscription);
    
                                    if (this.subscription && this.subscription.status == "active") {
                                        this.claimStatus = true;
                                    } 
    
                                } catch (error) {
                                    if (error.response && error.response.status === 404) {
                                        console.error('Error retrieving subscription:', error);

                                    } else {
                                        console.error('Error retrieving subscription:', error);
                                        this.dataLoaded = null;
                                    }
                                }

                                // update claim status if different
                                if (this.specified_producer.claimStatus != this.claimStatus) {
                                    try {
                                        await this.$axios.post(`${process.env.VUE_APP_API_URL}/editProducerProfile/updateProducerClaimStatus`, 
                                            {
                                                businessId: this.producer_id,
                                                claimStatus: this.claimStatus,
                                            }, {
                                            headers: {
                                                'Content-Type': 'application/json'
                                            }
                                        });
                                    } catch (error) {
                                        console.error(error);
                                    }
                                }
    
                                // upqdate last check status date
                                try {
                                    await this.$axios.post(`${process.env.VUE_APP_API_URL}/editProducerProfile/updateProducerClaimStatusCheckDate`, 
                                        {
                                            businessId: this.producer_id,
                                            claimStatusCheckDate: new Date().toISOString(),
                                        }, {
                                        headers: {
                                            'Content-Type': 'application/json'
                                        }
                                    });
                                } catch (error) {
                                    console.error(error);
                                }
                            } else {
                                this.claimStatus = this.specified_producer.claimStatus // get claim status of producer
                            }
                        } else {
                            this.claimStatus = this.specified_producer.claimStatus // get claim status of producer
                        }


                        this.getLatestUpdates()
                        this.checkProducerAnswered()
                        this.formatDeepDiveLink()
                    } 
                    catch (error) {
                        console.error(error);
                        this.dataLoaded = null;
                    }
                // producer listings
                // _id, listingName, producerID, bottler, originCountry, drinkType, typeCategory, age, abv, reviewLink, officialDesc, sourceLink, photo
                    try {
                        const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getListingsByProducer/${this.producer_id}`);
                        this.listings = response.data;

                        this.getAllDrinks()
                        this.getCountsByType()
                        this.getTotalCounts()
                        this.getMostDiscussed()
                        this.getRecentlyAdded()
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
                        // get all reviews
                        this.getAllReviews()
                        this.getRatingsByType()
                        this.getAverageRatings()
                        this.getMostPopular()
                    }
                    catch (error) {
                        console.error(error);
                        this.dataLoaded = null;
                    }
                // users
                // _id, username, displayName, choiceDrinks, drinkLists, modType, photo
                    if (this.user_id) {
                        try {
                            const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getUser/${this.user_id}`);
                            this.user = response.data;
                            if (this.userType == "user") {
                                // this.user = this.users.find(user => user['id'] == this.user_id);
                                this.following = JSON.stringify(this.user.followLists.producers).includes(this.producer_id);
                                this.isAdmin = this.user.isAdmin // check if user is admin
                            }
                        } 
                        catch (error) {
                            console.error(error);
                            this.dataLoaded = null;
                        }
                    }
                // producersProfileViews
                // _id, producerID, views
                    try {
                        const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getProducersProfileViews`);
                        this.producersProfileViews = response.data;

                        if (this.producersProfileViews.length > 0) {
                            this.producerProfileViewInfo = this.producersProfileViews.find(view => view.producerId == this.producer_id);
                            if (this.producerProfileViewInfo) {
                                this.producerProfileID = this.producerProfileViewInfo.id;
                            }
                        }
                        this.getProfileViews()
                    }
                    catch (error) {
                        console.error(error);
                    }

                // check whether mod can edit any listing at all in the producer page
                if(this.user_id != "" && this.userType=="user"){                    
                    if(this.user.modType.length>0){
                        const editableListing = this.allDrinks.filter(listing => this.user.modType.includes(listing.drinkType) && listing.allowMod)
                        if(editableListing.length>0){
                            this.canMod = true
                        }
                    }
                }

                // Set dataLoaded to true
                if (this.dataLoaded != null) {
                    this.dataLoaded = true;
                }
            },

            // get all drinks that a producer has
            async getAllDrinks() {
                let allProducerDrinks = this.listings.filter(listing => listing.producerID == this.producer_id);
                this.allDrinks = allProducerDrinks;
                this.allDrinksCount = allProducerDrinks.length
            },

            // get all reviews that a producer has
            async getAllReviews() {
                let allProducerReviews = this.reviews.filter(review => {
                    let review_target = review.reviewTarget;
                    let all_drinks = this.allDrinks;
                    return all_drinks.some(drink => drink.id === review_target);
                });
                this.allReviews = allProducerReviews;
                this.allReviewsCount = allProducerReviews.length
            },

            // find drink name given reviewTarget
            findDrinkNameForReview(reviewTarget) {
                let drink_name = this.listings.find(listing => listing.id == reviewTarget).listingName;
                return drink_name;
            },

            // find drink name given listing
            findDrinkNameForListing(listing) {
                let drink_name = listing.listingName;
                return drink_name;
            },

            // get compiled dictionary of ratings of each type of drink
            getRatingsByType() {
                let allProducerDrinkRatings = {};
                this.allReviews.forEach(review => {
                    let drink_name = this.findDrinkNameForReview(review.reviewTarget);
                    let rating = review["rating"];
                    allProducerDrinkRatings[drink_name] = allProducerDrinkRatings[drink_name] || [];
                                                            allProducerDrinkRatings[drink_name].push(rating);
                });
                this.drinkRatings = allProducerDrinkRatings;
            },

            // get compiled dictionary of count of each type of drink
            getCountsByType() {
                let allProducerDrinkCounts = {};
                this.allDrinks.forEach(listing => {
                    let drink_name = this.findDrinkNameForListing(listing);
                    allProducerDrinkCounts[drink_name] = allProducerDrinkCounts[drink_name] ? 
                                                            allProducerDrinkCounts[drink_name] + 1 : 1;
                });
                this.drinkCounts = allProducerDrinkCounts;
            },

            // get average ratings for each listing
            getAverageRatings() {
                const averageRatings = {};
                for (const [drink, ratings] of Object.entries(this.drinkRatings)) {
                    const filteredRatings = ratings.filter(value => value !== "-").map(Number);
                    if (filteredRatings.length > 0) {
                        const averageRating = filteredRatings.reduce((sum, rating) => sum + rating, 0) / filteredRatings.length;
                        averageRatings[drink] = averageRating;
                    }
                }
                const sortedProducerAverageRatings = Object.fromEntries(Object.entries(averageRatings)
                                                        .sort((a, b) => b[1] - a[1]));
                this.sortedAverageRatings = sortedProducerAverageRatings;
            },

            // get total counts for each listing
            getTotalCounts() {
                const drinkCountsArray = Object.entries(this.drinkCounts);
                drinkCountsArray.sort((a, b) => b[1] - a[1]);
                const sortedProducerDrinkCounts = Object.fromEntries(drinkCountsArray);
                this.sortedDrinksCounts = sortedProducerDrinkCounts;
            },

            // get the most popular drinks
            getMostPopular() {
                // get the average ratings
                const averageRatings = this.sortedAverageRatings;
                // get the first 5 items from the average ratings
                let firstFiveItems = Object.entries(averageRatings).slice(0, 5);
                firstFiveItems = firstFiveItems.map(item => {
                    const listing = this.listings.find(listing => listing.listingName === item[0]);
                    return listing ? [...item, listing.id] : item;
                });
                // if firstFiveItems is less than 5, get the remaining from this.allDrinks
                if (firstFiveItems.length < 5) {
                    this.allDrinks.forEach(drink => {
                        if (!firstFiveItems.some(item => item[0] == drink.listingName)) {
                            let drinkName = drink.listingName;
                            let drinkCount = this.drinkCounts[drink.listingName];
                            let drinkID = drink.id
                            firstFiveItems.push([drinkName, drinkCount, drinkID]);
                        }
                    });
                }
                firstFiveItems = firstFiveItems.slice(0,5)
                this.mostPopular = firstFiveItems;
                this.mostPopular = this.mostPopular.map(item => {
                    return this.listings.find(listing => listing.id == item[2]);
                });
            },

            // get the most discussed drinks
            getMostDiscussed() {
                // get the drink counts
                const drinkCounts = this.sortedDrinksCounts;
                // get the first 5 items from the drink counts
                let firstFiveItems = Object.entries(drinkCounts).slice(0, 5);
                firstFiveItems = firstFiveItems.map(item => {
                    const listing = this.listings.find(listing => listing.listingName === item[0]);
                    return listing ? [...item, listing.id] : item;
                });
                // if firstFiveItems is less than 5, get the remaining from this.allDrinks
                if (firstFiveItems.length < 5) {
                    this.allDrinks.forEach(drink => {
                        if (!firstFiveItems.some(item => item[0] == drink.listingName)) {
                            let drinkName = drink.listingName;
                            let drinkCount = this.drinkCounts[drink.listingName];
                            let drinkID = drink.id
                            firstFiveItems.push([drinkName, drinkCount, drinkID]);
                        }
                    });
                }
                firstFiveItems = firstFiveItems.slice(0,5)
                this.mostDiscussed = firstFiveItems;
                this.mostDiscussed = this.mostDiscussed.map(item => {
                    return this.listings.find(listing => listing.id == item[2]);
                });
            },

            // get most recently added drinks
            getRecentlyAdded() {
                const firstFiveItems = this.allDrinks.slice(0, 5);
                this.recentlyAdded = firstFiveItems;
            },

            // get photo from drink
            getPhotoFromDrink(drinkName) {
                let photo = ""
                for (const i in this.listings) {
                    let listingName = this.listings[i].listingName;
                    if (drinkName == listingName) {
                        photo = this.listings[i].photo;
                    }
                }
                return photo;
            },

            // show all listings that a producer has
            showAllListings() {
                this.showListings = true;
                this.filteredListings = this.allDrinks; // initially set filtered drinks to all drinks
                this.lazyListings = this.filteredListings.slice(0, 10);
            },

            // show all reviews that a producer has
            showAllReviews() {
                this.showListings = false;
            },

            // get ratings for a listing
            getRatings(listing) {
                const ratings = this.reviews.filter((rating) => {
                    return rating["reviewTarget"] == listing['id'];
                });
                // if there are no ratings
                if (ratings.length == 0) {
                    return "-";
                }
                // else there are ratings
                const averageRating = ratings.reduce((total, rating) => {
                    return total + rating["rating"];
                }, 0) / ratings.length;
                // round to 1 decimal place
                const roundedRating = Math.round(averageRating * 10) / 10;
                return roundedRating;
            },

            // check if user has already added listing to shelf, add colour to button accordingly
            checkDrinkLists(listing) {
                const haveTried = this.drinkList.haveTried.includes(listing.listingName);
                const wantToTry = this.drinkList.wantToTry.includes(listing.listingName);

                const haveTriedButton = `
                <button type="button" class="btn custom-drink-list-btn rounded-0 ${haveTried ? 'disabled' : ''}" style="font-size:80%;">
                    Have tried
                </button>
                `;

                const wantToTryButton = `
                <button type="button" class="btn custom-drink-list-btn rounded-0 ${wantToTry ? 'disabled' : ''}" style="font-size:80%;">
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

            // for searching for expressions
            searchForExpressions() {
                // flag to check if there are search inputs
                const searchExpressions = this.searchExpressions.toLowerCase();
                this.searchTerm = this.searchExpressions;

                // get all listings to search from
                const listings = this.allDrinks;

                // if there is something searched
                const searchResults = listings.filter((listing) => {
                    const expressionName = listing["listingName"].toLowerCase();
                    return expressionName.includes(searchExpressions);
                });

                // if nothing found
                if (searchResults.length == 0) {
                    this.filteredListings = [];
                    this.lazyListings = [];
                } 
                else {
                    this.filteredListings = searchResults;
                    this.lazyListings = this.filteredListings.slice(0, 10);
                }

                // if there is nothing searched
                if (this.searchExpressions == '') {
                    this.resetListings();
                }
            },

            // for resetting listings (show full listings)
            resetListings() {
                this.searchExpressions = '';
                this.filteredListings = this.allDrinks;
                this.lazyListings = this.filteredListings.slice(0, 10);
                this.sortByCategory("")
            },

            // when user click on "edit profile"
            editProfile() {
                // set editing status to true
                this.editing = true;

                // set the current details to the edit details
                this.edit_producerName = this.specified_producer["producerName"];
                this.edit_producerDesc = this.specified_producer["producerDesc"];
                this.edit_originCountry = this.specified_producer["originCountry"];
            },

            // edit profile photo
            async loadFile(event) {
                try {
                    const file = event.target.files[0];
                
                    const reader = new FileReader();

                    reader.onloadend = async () => {
                        this.selectedImage = reader.result;
                        const base64String = reader.result.replace('data:', '').replace(/^.+,/, '');

                        this.image64 = base64String;

                    };
                    reader.readAsDataURL(file);
                } 
                catch (error) {
                    console.error(error);
                }
            
            },

            // save edits when producer finishes editing profile
            async saveEdit() {
                // set editing status to false
                this.editing = false;

                // check if image is uploaded
                console.log(this.image64);
                // if (this.image64 == null) {
                //     // set default image
                //     console.log(this.specified_producer)
                //     this.image64 = this.specified_producer["photo"];
                // }
                
                try {
                    const response = await this.$axios.post(`${process.env.VUE_APP_API_URL}/editProducerProfile/editDetails`, 
                        {
                            producerID: this.producer_id,
                            image64: this.image64,
                            producerName: this.edit_producerName,
                            producerDesc: this.edit_producerDesc,
                            originCountry: this.edit_originCountry
                        },
                        {
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    });
                    console.log(response.data);
                } 
                catch (error) {
                    console.error(error);
                }

                // force page to reload
                window.location.reload();
            },

            // send questions that users ask to producers
            async sendQuestion () {
                try {
                    const response = await this.$axios.post(`${process.env.VUE_APP_API_URL}/editProducerProfile/sendQuestions`, 
                        {
                            producerID: this.producer_id,
                            question: this.question,
                            answer: "",
                            date: this.currDate,
                            userID: this.user_id
                        },
                        {
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    });
                    alert("Your question has been successfully sent!");
                    console.log(response.data);
                } 
                catch (error) {
                    console.error(error);
                    alert("An error occurred while attempting to send your question, please try again!");
                }

                // force page to reload
                window.location.reload();
            },

            // send answer that producers give to users
            async sendAnswer (qa) {
                let q_and_a_id = qa.id;
                try {
                    const response = await this.$axios.post(`${process.env.VUE_APP_API_URL}/editProducerProfile/sendAnswers`, 
                        {
                            producerID: this.producer_id,
                            questionsAnswersID: q_and_a_id,
                            answer: this.answer,
                        },
                        {
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    });
                    console.log(response.data);
                } 
                catch (error) {
                    console.error(error);
                }

                // force page to reload
                window.location.reload();
            },

            // for user to edit their catalogue
            // check user type:producer, admin or mod and set accordingly
            editCatalogue () {
                if(this.correctProducer || this.isAdmin){
                    this.deletingListing=true
                    this.editingListing=true
                }else if(this.canMod){
                    this.editingListing=true
                }
            },

            // delete bottle listing
            async deleteListings(listing) {

                try {
                    const response = await this.$axios.delete(`${process.env.VUE_APP_API_URL}/editListing/deleteListing/${listing.id}`);
                    console.log(response.data);
                } 
                catch (error) {
                    console.error(error);
                }

                // force page to reload
                window.location.reload();

            },

            // format date
            formatDate(dateTimeString) {
                let datePart = dateTimeString.split("T")[0];
                // splitting the date into year, month, and day
                let [year, month, day] = datePart.split("-");
                // formatting the date
                let formattedDate = `${day}/${month}/${year}`;
                return formattedDate;
            },

            // format date
            formatTime(dateTimeString) {
                let timePart = dateTimeString.split("T")[1].split(".")[0];
                // splitting the time into hours, minutes, and seconds
                let [hours, minutes, seconds] = timePart.split(":");
                // formatting the time
                let formattedTime = `${hours}:${minutes}:${seconds}`;
                return formattedTime;
            },

            // get producer's latest updates
            getLatestUpdates() {
                let updatesList = this.specified_producer["updates"];

                if (updatesList.length > 0) {
                    this.hasUpdates = true
                    let latestUpdate = updatesList[updatesList.length - 1];

                    // check that there is more than 1 update
                    if (updatesList.length > 1) {
                        // for remaining updates
                        this.remainingUpdates = updatesList.slice(0, updatesList.length - 1);
                        // sort remaining updates in descending order by date
                        this.remainingUpdates.sort((a, b) => {
                            return new Date(b.date) - new Date(a.date);
                        });
                        for (let update of this.remainingUpdates) {
                            let remainingUpdateLike = update["likes"];
                            this.remainingUpdateLikes[update['id']] = remainingUpdateLike
                            try {
                                this.remainingLikesCount[update['id']] = this.remainingUpdateLikes[update['id']].length;
                            }
                            catch {
                                this.remainingLikesCount[update['id']] = 0;
                            }
                            this.checkLiked('remaining');
                        }
                    }

                    // for latest update ONLY
                    this.latestUpdate = latestUpdate
                    // add likes
                    this.updateLikes = latestUpdate["likes"];
                    try {
                        this.updateLikesCount = this.updateLikes.length;
                    }
                    catch {
                        this.updateLikesCount = 0;
                    }
                    this.checkLiked('latest');
                }
            },

            // get producer's answered questions (to be displayed to the users/venues)
            checkProducerAnswered() {
                let answeredQuestions = this.specified_producer["questionsAnswers"];
                if (answeredQuestions.length > 0) {
                    for (let qa in answeredQuestions) {
                        let answer = answeredQuestions[qa]["answer"];
                        if (answer != "") {
                            this.answeredQuestions.push(answeredQuestions[qa]);
                        }
                        else {
                            this.unansweredQuestions.push(answeredQuestions[qa]);
                        }
                    }
                }
            },

            // change status of producer's answer to true
            showAnswered() {
                this.answerStatus = true;
            },

            // change status of producer's answer
            showUnanswered() {
                this.answerStatus = false;
            },

            // upload update photo
            async loadUpdateFile(event) {
                const file = event.target.files[0];
                this.updateFileName = file.name;
                const reader = new FileReader();

                reader.onloadend = async () => {
                    this.updateImage = reader.result;
                    const base64String = reader.result.replace('data:', '').replace(/^.+,/, '');

                    this.updateImage64 = base64String;
                };
                reader.readAsDataURL(file);
            },

            // for producer to add updates
            async addUpdates() {
                try {
                    const response = await this.$axios.post(`${process.env.VUE_APP_API_URL}/editProducerProfile/addUpdates`, 
                        {
                            producerID: this.producer_id,
                            date: this.currDate,
                            text: this.updateText,
                            image64: this.updateImage64,
                        },
                        {
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    });
                    console.log(response.data);
                } 
                catch (error) {
                    console.error(error);
                }

                // force page to reload
                window.location.reload();
            },

            // check if user liked the post
            checkLiked(status) {
                if (status == 'latest') {
                    for (let i in this.updateLikes) {
                        if ((this.updateLikes[i].userId == this.user_id) && this.updateLikes[i].userType == this.userType) {
                            this.likeStatus = true;
                        }
                    }
                }
                else if (status == 'remaining') {
                    for (let i in this.remainingUpdateLikes) {
                        for (let j in this.remainingUpdateLikes[i]) {
                            if (this.remainingUpdateLikes[i][j] == this.user_id) {
                                this.remainingLikeStatus[i] = true;
                            }
                        }
                    }
                }
            },

            // like updates
            async likeUpdates(updateID) {
                try {
                    const response = await this.$axios.post(`${process.env.VUE_APP_API_URL}/editProducerProfile/likeUpdates`, 
                        {
                            producerID: this.producer_id,
                            updateID: updateID,
                            userID: this.user_id,
                            userType: this.userType
                        },
                        {
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    });
                    console.log(response.data);
                } 
                catch (error) {
                    console.error(error);
                }

                // force page to reload
                window.location.reload();
            },

            // unlike updates
            async unlikeUpdates(updateID) {
                try {
                    const response = await this.$axios.post(`${process.env.VUE_APP_API_URL}/editProducerProfile/unlikeUpdates`, 
                        {
                            producerID: this.producer_id,
                            updateID: updateID,
                            userID: this.user_id,
                            userType:this.userType
                        },
                        {
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    });
                    console.log(response.data);
                } 
                catch (error) {
                    console.error(error);
                }

                // force page to reload
                window.location.reload();
            },

            // to format deepdive link
            formatDeepDiveLink() {
                let unformattedLink = this.specified_producer["producerLink"];
                if (!unformattedLink) return;
                
                // extract segment after the last "/"
                const segment = unformattedLink.substring(unformattedLink.lastIndexOf("/") + 1);
                // split the segment by "-"
                const words = segment.split("-");
                // capitalize the first letter of each word
                const capitalizedWords = words.map(word => word.charAt(0).toUpperCase() + word.slice(1));
                // join the words back together with spaces
                this.deepDiveLinkFormatted = capitalizedWords.join(" ");
            }, 

            // to follow and unfollow producers
            async editFollow(action) {
                if (action === "unfollow") {
                    this.following = false;
                } else {
                    this.following = true
                }
                try {
                    const response = await this.$axios.post(`${process.env.VUE_APP_API_URL}/editProfile/updateFollowLists`, 
                        {
                            userID: this.user_id,
                            action: action,
                            target: "producers",
                            followerID: this.producer_id,
                        }, {
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    });
                    console.log(response.data);
                } catch (error) {
                    console.error(error);
                }
                
            }, 
            claimProducerAccount() {
                let accountDetails = {
                    userID: this.producer_id,
                    businessType: "producer",
                    businessName: this.specified_producer.producerName,
                    businessDesc: this.specified_producer.producerDesc,
                    businessLink: this.$route.fullPath,
                    originCountry: this.specified_producer.originCountry,
                }
                this.$router.push({
                    path: '/BusinessSignup', 
                    query: accountDetails
                });
            },
            // to check if all updates should be shown
            checkToShowRemainingUpdates() {
                if (this.showRemainingUpdates == true) {
                    this.showRemainingUpdates = false;
                } 
                else {
                    this.showRemainingUpdates = true;
                }
            },
            // to check if producer QnA should be shown
            checkToShowQnA() {
                if (this.showQnA == true) {
                    this.showQnA = false;
                } 
                else {
                    this.showQnA = true;
                }
            },
            // for bookmark component
            handleIconClick(data) {
                this.bookmarkListingID = data
            },

            sortResults() {
                let category = this.sortSelection.category;
                // #1: Alphabetical (A - Z)
                if (category == 'Alphabetical (A - Z)') {
                    this.filteredListings.sort((a, b) => {
                        return a.listingName.localeCompare(b.listingName);
                    });
                    this.lazyListings = this.filteredListings.slice(0, 10);
                }

                // #2: Alphabetical (Z - A)
                else if (category == 'Alphabetical (Z - A)') {
                    this.filteredListings.sort((a, b) => {
                        return b.listingName.localeCompare(a.listingName);
                    });
                    this.lazyListings = this.filteredListings.slice(0, 10);
                }

                // #3: Date (Newest - Oldest)
                else if (category == 'Date (Newest - Oldest)') {
                    this.filteredListings.sort((a, b) => {
                        return new Date(b.addedDate) - new Date(a.addedDate);
                    });
                    this.lazyListings = this.filteredListings.slice(0, 10);
                }

                // [DEFAULT] #4: Date (Oldest - Newest)
                else if (category == '' || category == 'Date (Oldest - Newest)') {
                    this.filteredListings.sort((a, b) => {
                        return new Date(a.addedDate) - new Date(b.addedDate);
                    });
                    this.lazyListings = this.filteredListings.slice(0, 10);
                }

                // #5: Ratings (Highest - Lowest)
                else if (category == 'Ratings (Highest - Lowest)') {
                    this.filteredListings.sort((a, b) => {
                        return this.getRatingsSearch(b) - this.getRatingsSearch(a);
                    });
                    this.lazyListings = this.filteredListings.slice(0, 10);
                }

                // #6: Ratings (Lowest - Highest)
                else if (category == 'Ratings (Lowest - Highest)') {
                    this.filteredListings.sort((a, b) => {
                        return this.getRatingsSearch(a) - this.getRatingsSearch(b);
                    });
                    this.lazyListings = this.filteredListings.slice(0, 10);
                }
            },

            // Sort Support Function (Category)
            sortByCategory(category) {
                // Check if the selected filter is the same as the current filter
                if (this.sortSelection.category == category) {
                    return;
                }
                else {
                    this.sortSelection.category = category
                    this.sortResults();
                }
            },

            // get ratings (search function) --> main difference is if there are no ratings, return 0 instead of "-" so that it can be sorted
            getRatingsSearch(listing) {
                const ratings = this.reviews.filter((rating) => {
                    return rating["reviewTarget"] == listing['id'];
                });
                // if there are no ratings
                if (ratings.length == 0) {
                    return 0;
                }
                // else there are ratings
                const averageRating = ratings.reduce((total, rating) => {
                    return total + rating["rating"];
                }, 0) / ratings.length;
                // round to 1 decimal place
                const roundedRating = Math.round(averageRating * 10) / 10;
                return roundedRating;
            },

            // for producer to track page views
            getProfileViews() {
                // ensure that it is not the producer viewing their own page
                if (this.user_id != this.producer_id) {
                    // get current date
                        let currDate = this.currDate

                    // check if currDate exists in the producerProfileViewInfo
                    let dateExists = (this.producerProfileViewInfo?.date == currDate) || false;

                    // if current date already exists, increment the count
                    if (dateExists) {

                        // get current view
                        let viewsID = this.producerProfileViewInfo.id;
                        try {
                            const response = this.$axios.post(`${process.env.VUE_APP_API_URL}/editProducerProfile/addProfileCount`, 
                                {
                                    producerID: this.producerProfileID,
                                    viewsID: viewsID,
                                },
                                {
                                headers: {
                                    'Content-Type': 'application/json'
                                }
                            });
                            console.log(response.data);
                        } 
                        catch (error) {
                            console.error(error);
                        }
                    } 

                    // if current date does not exist, add a new view
                    else {
                        try {
                            this.$axios.post(`${process.env.VUE_APP_API_URL}/editProducerProfile/addNewProfileCount`, 
                                {
                                    producerID: this.producer_id,
                                    date: currDate,
                                },
                                {
                                headers: {
                                    'Content-Type': 'application/json'
                                }
                            });
                        } 
                        catch (error) {
                            console.error(error);
                        }
                    } 
                }
            },

            // when user click on edit update
            editUpdate(update, status) {
                // set editing status to true
                if (status == "latest") {
                    this.editingLatestUpdate = true;
                    // set the current details to the edit details
                    this.edit_latestUpdateText = update.text
                }
                else if (status == "remaining") {
                    this.editingRemainingUpdateID = update.id;
                    this.editingRemainingUpdate = true;
                    // set the current details to the edit details
                    this.edit_remainingUpdateText[update.id] = update.text
                }
            },

            // edit update photo
            async loadLatestUpdateFile(event) {
                try {
                    const file = event.target.files[0];
                    const reader = new FileReader();

                    reader.onloadend = async () => {
                        this.selectedLatestUpdateImage = reader.result;
                        const base64String = reader.result.replace('data:', '').replace(/^.+,/, '');
                        this.image64LatestUpdate = base64String;

                    };
                    reader.readAsDataURL(file);
                } 
                catch (error) {
                    console.error(error);
                }
            
            },

            // edit remaining photo
            async loadRemainingUpdateFile(event) {
                try {
                    const file = event.target.files[0];
                    const reader = new FileReader();

                    reader.onloadend = async () => {
                        this.selectedRemainingUpdateImage = reader.result;
                        const base64String = reader.result.replace('data:', '').replace(/^.+,/, '');
                        this.image64RemainingUpdate = base64String;

                    };
                    reader.readAsDataURL(file);
                } 
                catch (error) {
                    console.error(error);
                }
            
            },

            // edit update
            saveUpdateEdit(update, status) {
                if (status == "latest") {
                    this.editingLatestUpdate = false;
                    // check if image is uploaded
                    if (this.image64LatestUpdate == null) {
                        // set default image
                        this.image64LatestUpdate = update["photo"];
                    }
                    // send to backend
                    try {
                        const response = this.$axios.post(`${process.env.VUE_APP_API_URL}/editProducerProfile/editUpdate`, 
                            {
                                producerID: this.producer_id,
                                updateID: update.id,
                                update: this.edit_latestUpdateText,
                                image64: this.image64LatestUpdate,
                            },
                            {
                                headers: {
                                    'Content-Type': 'application/json'
                                }
                            });
                        console.log(response.data);
                    } 
                    catch (error) {
                        console.error(error);
                    }
                }
                else if (status == "remaining") {
                    this.editingRemainingUpdate = false;
                    let newUpdate = this.edit_remainingUpdateText[update.id];
                    console.log(update)
                    // check if image is uploaded
                    if (this.image64RemainingUpdate == null) {
                        // set default image
                        this.image64RemainingUpdate = update["photo"];
                    }
                    // send to backend
                    try {
                        const response = this.$axios.post(`${process.env.VUE_APP_API_URL}/editProducerProfile/editUpdate`, 
                            {
                                producerID: this.producer_id,
                                updateID: update.id,
                                update: newUpdate,
                                image64: this.image64RemainingUpdate,
                            },
                            {
                            headers: {
                                'Content-Type': 'application/json'
                            }
                        });
                        console.log(response.data);
                    } 
                    catch (error) {
                        console.error(error);
                    }
                }

                // force page to reload
                window.location.reload();
            },

            // delete update
            deleteUpdate(update) {

                try {
                    const response = this.$axios.post(`${process.env.VUE_APP_API_URL}/editProducerProfile/deleteUpdate`, 
                        {
                            producerID: this.producer_id,
                            updateID: update.id,
                        },
                        {
                            headers: {
                                'Content-Type': 'application/json'
                            }
                        });
                    console.log(response.data);
                } 
                catch (error) {
                    console.error(error);
                }

                // force page to reload
                window.location.reload();

            },

            // cancel update
            cancelUpdate(update, status) {
                // set editing status to true
                if (status == "latest") {
                    this.editingLatestUpdate = false;
                    this.edit_latestUpdateText = ""
                }
                else if (status == "remaining") {
                    this.editingRemainingUpdateID = ""
                    this.editingRemainingUpdate = false;
                    this.edit_remainingUpdateText[update.id] = ""
                }
            },

            // for editing Q&A answers
            editQA(qa) {
                this.editingQA = true;
                // set the current details to the edit details
                this.edit_answer[qa.id] = qa.answer
                this.editingQAID = qa.id;
            }, 
            
            saveQAEdit(qa) {
                // set editing status to false
                this.editingQA = false;
                let q_and_a_id = qa.id;

                this.$axios.post(`${process.env.VUE_APP_API_URL}/editProducerProfile/editQA`, 
                    {
                        producerID: this.producer_id,
                        questionsAnswersID: q_and_a_id,
                        answer: this.edit_answer[qa.id],
                    },
                    {
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    })
                    .then((response) => {
                        console.log(response.data);
                        window.location.reload();
                    })
                    .catch((error) => {
                        // Handle the error
                        console.error(error);
                    });
            },

            deleteQAEdit(qa) {
                let q_and_a_id = qa.id;
                try {
                    const response = this.$axios.post(`${process.env.VUE_APP_API_URL}/editProducerProfile/deleteQA`, 
                        {
                            producerID: this.producer_id,
                            questionsAnswersID: q_and_a_id,
                            answer: "",
                        },
                        {
                            headers: {
                                'Content-Type': 'application/json'
                            }
                        });
                    console.log(response.data);
                } 
                catch (error) {
                    console.error(error);
                }

                // force page to reload
                window.location.reload();
            },

            // cancel Q&A edit
            cancelQAEdit(qa) {
                this.editingQA = false;
                this.edit_answer[qa.id] = "";
                this.editingQAID = "";
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

            // To handle change and reset password
            changePasswordMode(mode){
                this.changingPassword = mode
            },
            selectPasswordMode(){
                if(this.confirmChangePassword||this.confirmResetPassword){
                    this.passwordError = false
                    this.passwordMismatch = false
                    this.passwordSuccess = false
                    this.confirmChangePassword = false
                    this.confirmResetPassword = false
                    this.verifyErrorMessage = ""
                }
                else{
                    this.changingPassword = ""
                }
            },
            resetChangePassword(){
                if(this.passwordError||this.passwordSuccess||this.passwordMismatch){
                    this.passwordError = false
                    this.passwordMismatch = false
                    this.passwordSuccess = false
                    this.confirmChangePassword = false
                    this.confirmResetPassword = false
                    this.changingPassword = ""
                    this.verifyErrorMessage = ""
                }
            },
            updatePassword(){
                if(this.oldPassword=="" || this.newPassword==""){
                    alert("One of the passwords is empty, please check again")
                    return null
                }
                this.confirmChangePassword = true
            },
            // Function to hash password
            // create unique hash based on username and password
            hashPassword(username, password) {
                const combinedString = username.toString() + password;
                let hash = 0;

                for (let i = 0; i < combinedString.length; i++) {
                    const char = combinedString.charCodeAt(i);
                    hash = (hash << 5) - hash + char;
                    hash |= 0; // convert to 32-bit integer
                }

                return hash;
            },
            async confirmUpdatePassword(){
                let oldHash = this.hashPassword(this.specified_producer.producerName, this.oldPassword)
                let newHash = this.hashPassword(this.specified_producer.producerName, this.newPassword)
                let submitURL = `${process.env.VUE_APP_API_URL}/authcheck/editPassword/` + this.specified_producer.id 
                let submitData = {
                    oldHash: oldHash.toString(),
                    newHash: newHash.toString(),
                    userType: "producer",
                }
                // Send request over
                let responseCode = ''
                await this.$axios.post(submitURL,submitData)
                    .then((response)=>{
                        responseCode = response.data.code
                    })
                    .catch((error)=>{
                        console.error(error);
                        responseCode = error.response.data.code
                    });
                if(responseCode==201){
                    this.passwordSuccess=true; // Display success message
                }else if(responseCode==401){
                    this.passwordMismatch = true // Display duplicate entry message
                }else{
                    this.passwordError = true // Display generic error message
                }
            },

            async sendResetPin(){
            // call api to send pin
            this.isButtonDisabled = true;
                setTimeout(() => {
                    this.isButtonDisabled = false;
                }, 60000);
            let submitURL = `${process.env.VUE_APP_API_URL}/authcheck/sendResetPin/` + this.specified_producer.id
            let submitData = {
                userType: "producer",
            }
            let responseCode = ''
            await this.$axios.post(submitURL,submitData)
                .then((response)=>{
                    responseCode = response.data.code
                })
                .catch((error)=>{
                    console.error(error);
                    responseCode = error.response.data.code
                });
            let sendPinSuccess = document.getElementById("sendPinSuccess")
            let sendPinError = document.getElementById("sendPinError")
            if(responseCode == 201){
                sendPinSuccess.innerHTML = "OTP has been sent!"
                sendPinError.innerHTML = ""
            }
            else{
                sendPinSuccess.innerHTML = ""
                sendPinError.innerHTML = "Error sending OTP, please try again in 60 seconds"
            }
        },

        async verifyOTP(){
            // call api to verify the pin
            let submitURL = `${process.env.VUE_APP_API_URL}/authcheck/verifyPin/` + this.specified_producer.id
            let submitData ={
                userType:"producer",
                pin:this.resetPin
            }
            let responseCode = ''
            await this.$axios.post(submitURL,submitData)
                .then((response)=>{
                    responseCode = response.data.code
                })
                .catch((error)=>{
                    console.error(error);
                    responseCode = error.response.data.code
                });
            if(responseCode == 201){
                this.confirmResetPassword = true
                this.verifyErrorMessage = ""
            }
            else if(responseCode == 400){
                this.verifyErrorMessage = "OTP is wrong or expired."
            }else{
                this.verifyErrorMessage = "An error verifying the OTP. Please resend OTP or try again."
            }
            
        },

        async resetPassword(){
            this.resettingPassword=true
            let submitURL = `${process.env.VUE_APP_API_URL}/authcheck/resetPassword/` + this.specified_producer.id
            let submitData = {
                userType:"producer",
                pin:this.resetPin
            }
            // Send request over
            let responseCode = ''
            await this.$axios.post(submitURL,submitData)
                .then((response)=>{
                    responseCode = response.data.code
                })
                .catch((error)=>{
                    console.error(error);
                    responseCode = error.response.data.code
                });
            console.log(responseCode)
            this.resettingPassword= false
            if(responseCode==201){
                this.passwordSuccess=true; // Display success message
            }else{
                this.passwordError = true // Display generic error message
            }
        },

        loadMoreListings() {
            const listingsLength = this.lazyListings.length;
            this.lazyListings = this.filteredListings.slice(0, listingsLength + 10);
        },

        }
    };

    


</script>