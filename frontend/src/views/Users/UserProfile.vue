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

    <div v-if="displayUser && dataLoaded" class="userprofile mt-5 mobile-mt-3">

        <div class="container text-start">
            <div class="row">
                <!-- user profile -->
                <div class="col-12 col-md-4 mb-3">

                    <div class="container">

                        <!-- basic information -->
                        <div class="row">
                            <!-- profile picture -->
                            <div class="col-4 text-start pe-0">
                                <!-- <img :src=" 'data:image/jpeg;base64,' + (displayUser.photo || defaultProfilePhoto)" alt="" class="rounded-circle-no-bg border border-dark profile-img" style="height:auto; width:100%; "> -->
                                <img :src="selectedImage || (displayUser.photo || defaultProfilePhoto)" alt="" class="rounded-circle-no-bg border border-dark profile-img" style="height:auto; width:100%; ">
                            </div>                        
                            <!-- user name -->
                            <div class="col-8">
                                <h3 class="mb-0" >{{ displayUser.displayName }}</h3> 
                                <b>@{{ displayUser.username }}</b> 
                                <br/>
                                {{ drinkCount }} Drinks Tasted 
                                <br/>
                                <button v-if="displayUser && displayUser.modType && (displayUser.modType.length > 0 || displayUser.isAdmin)"
                                    data-bs-toggle="modal" data-bs-target="#moderatormodal" class="btn btn-warning hover-button p-1" 
                                    style="border-radius: 20px; font-size: 0.8rem;">
                                    ★ Certified Moderator
                                </button> 
                            </div>
                        </div>

                        <!-- additional information -->
                        <div class="mt-3">
                            <div class="row">
                                <div class="col-5">
                                    <b>Member Since</b>
                                </div>
                                <div class="col-7 text-end">
                                    {{ joinDate }}
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-5">
                                    <b>Drink of Choice</b>
                                </div>
                                <div class="col-7 text-end">
                                    <span v-if="drinkChoice.length == 0"><i>None</i></span>
                                    <span v-else>{{ drinkChoice }}</span>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-5">
                                    <b> Points Earned </b>
                                </div>
                                <div class="col-7 text-end">
                                    <span> {{ totalPoints }} pts </span>
                                </div>
                            </div>
                        </div>

                        <!-- buttons -->
                        <div class="row mt-3">
                            <button v-if="ownProfile && user" type="button" class="btn tertiary-btn-blue-outline xprimary-btn-outline-not-round" data-bs-toggle="modal" data-bs-target="#editProfileModal" style="font-weight:bold;">Edit Profile</button>
                            <button v-else-if="following && user" type="button" class="btn primary-btn-outline-less-round" @click="editFollow('unfollow')">Following</button>
                            <button v-else-if="user" type="button" class="btn primary-btn-less-round" @click="editFollow('follow')"  style="font-weight:bold;">+ Follow User</button>
                            <router-link v-if="ownProfile && user" :to="{ path: '/dashboard/user' }" class="btn primary-btn-less-round-blue xsecondary-btn-not-rounded rounded-0 mt-3" style=" font-weight: bold;">
                                View My Analytics
                            </router-link>
                            <span style="position: relative; display: inline-block" class="m-0 p-0">
                                <div v-if="!ownProfile && displayUser.modType != []" class="speech-bubble">{{ displayUser.modType ? displayUser.modType.join(', ') : 'None' }}</div>
                                <button v-if="user && user.isAdmin" class="btn tertiary-btn reverse-clickable-text mt-3" style="width: 100%" type="button" data-bs-toggle="modal" data-bs-target="#addModeratorModal">Add/Remove Moderator Rights</button>
                            </span>
                            
                        
                            <button v-if="ownProfile && user" type="button" class="btn secondary-btn-less-round mt-3" data-bs-toggle="modal" data-bs-target="#changePasswordModal">Change/Reset Password</button>
                        </div>

                        <!-- join as a moderator modal start -->
                        <div class="modal fade" id="moderatormodal" tabindex="-1" aria-labelledby="moderatorModalLabel" aria-hidden="true" data-bs-backdrop="static">

                            <div class="modal-dialog xmodal-lg d-flex align-items-center" style="height: 100vh;">

                            <div class="modal-content">

                            <div v-if="drinkChoice.length == 0" class="modal-body px-4">
                            
                                <button v-if="!ownProfile && displayUser.modType != []" data-bs-toggle="modal" data-bs-target="#moderatormodal" class="btn btn-warning hover-button p-1 mb-3" style="border-radius: 20px; font-size: 0.8rem;">★ Certified Moderator</button> 
                                <button v-if="user && user.isAdmin" data-bs-toggle="modal" data-bs-target="#moderatormodal" class="btn btn-warning hover-button p-1 mb-3" style="border-radius: 20px; font-size: 0.8rem;">★ Certified Moderator</button>
                                <button type="button" class="btn-close uninvert" data-bs-dismiss="modal" aria-label="Close" style="margin-left:63%;"></button>
                                <p><b>{{ displayUser.displayName }} is a Drink X moderator.</b></p> 
                                <p><b><em>Moderators help shape the drinks community and ensure drink reviews remain fun, useful and respectful!</em></b></p>
                                <b><a v-if="user && !user.isAdmin" href="#" class="mt-3" data-bs-toggle="modal" data-bs-target="#applyModerator" style="color: black">Want to be a moderator? Apply here!</a></b>   
                            </div>
                            <div v-else class="modal-body px-4">
                                <div style="display: flex; justify-content: space-between; ">
                                    <div style="display: inline-block;">
                                        <button v-if="!ownProfile && displayUser.modType != []" data-bs-toggle="modal" data-bs-target="#moderatormodal" class="btn btn-warning hover-button p-1 mb-3" style="border-radius: 20px; font-size: 0.8rem;">★ Certified Moderator</button> 
                                        <button v-if="user && user.isAdmin" data-bs-toggle="modal" data-bs-target="#moderatormodal" class="btn btn-warning hover-button p-1 mb-3" style="border-radius: 20px; font-size: 0.8rem;">★ Certified Moderator</button>
                                    </div>
                                    <div style="display: flex; justify-content: flex-end;">
                                        <button type="button" class="btn-close uninvert" data-bs-dismiss="modal" aria-label="Close" ></button>
                                    </div>
                                </div>   
                                <p><b>{{ displayUser.displayName }} is a moderator of the following communities:</b></p> 
                                <p>{{ drinkChoice }}</p>
                                <p><b><em>Moderators help shape the drinks community and ensure drink reviews remain fun, useful and respectful!</em></b></p>        
                                
                                <b><a v-if="user && !user.isAdmin" href="#" class="mt-3" data-bs-toggle="modal" data-bs-target="#applyModerator" style="color: black">Want to be a moderator? Apply here!</a></b>                    
                            </div>
                            

                            </div>


                            </div>

                        </div>

                        

                        <!-- join as a moderator modal end -->

                        <!-- Add/Remove modal start -->
                        <!-- Mod addition modal -->
                        <div class="modal fade" id="addModeratorModal" data-bs-backdrop="static" tabindex="-1" aria-labelledby="addModeratorLabel" aria-hidden="true">
                            <div class="modal-dialog">
                                <div class="modal-content">
                                    <div class="modal-header" style="background-color: #535C72">
                                        <h1 class="modal-title fs-5" id="addModeratorLabel" style="color: white;">Add Moderator</h1>
                                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>

                                    <!-- Success remove mod modal body -->
                                    <div v-if="successRemoveMod" class="modal-body text-center text-success fst-italic fw-bold fs-3">
                                        <span>User has successfully been removed as moderator!</span>
                                    </div>
                                    <!-- Error remove mod modal body -->
                                    <div v-if="errorRemoveMod" class="modal-body text-center text-danger fst-italic fw-bold fs-3">
                                        <span>There is an error removing user as moderator, please try again!</span>
                                    </div>
                                    <!-- Success add mod modal body -->
                                    <div v-if="successAddMod" class="modal-body text-center text-success fst-italic fw-bold fs-3">
                                        <span>User has successfully been added as moderator!</span>
                                    </div>
                                    <!-- Error add mod modal body -->
                                    <div v-if="errorAddMod" class="modal-body text-center text-danger fst-italic fw-bold fs-3">
                                        <span>There is an error adding user as moderator, please try again!</span>
                                    </div>
                                    <!-- Initial select mode, add or remove moderator -->
                                    <div v-if="chooseMod==''" class="modal-body">
                                        <button class="btn tertiary-btn reverse-clickable-text m-1" type="button" @click="addModMode">
                                            Add a moderator
                                        </button>      
                                        <button class="btn tertiary-btn reverse-clickable-text m-1" type="button" @click="removeModMode">
                                            Remove a moderator
                                        </button>      
                                    </div>

                                    <!-- Initial select user to promote -->
                                    <div v-if="chooseMod=='add' && !doubleConfirmMod && !(successAddMod||errorAddMod||successRemoveMod||errorRemoveMod)" class="modal-body">                                    
                                        <div class="form-group mb-3">
                                            <p class="text-start mb-1"> Choose drink type that user can moderate: <span class="text-danger">*</span></p>
                                            <p v-html="formattedModTypes" class="text-start mb-1"></p>
                                            <input list="addableDrinkType" v-model="promotedType" class="form-control" id="promotedType" placeholder="Enter drink type" v-on:change="updateDrinkType">
                                            <datalist id="addableDrinkType">
                                                <option v-for="drinkType in addableDrinkType" :key="drinkType.id" :value="drinkType.drinkType">
                                                    {{drinkType.drinkType}}
                                                </option>
                                            </datalist>
                                            <p v-show="promotedType.length > 0" class="text-start mb-1 text-danger" id="promotedTypeError"></p>
                                        </div>
                                        <p class="text-start mb-1 text-danger" id="alreadyModError"></p>
                                    </div>

                                    <div v-if="chooseMod=='remove' && !doubleConfirmMod && !(successAddMod||errorAddMod||successRemoveMod||errorRemoveMod)" class="modal-body">                                    
                                        <div class="form-group mb-3">
                                            <p class="text-start mb-1"> Choose drink type for user to remove moderator rights: <span class="text-danger">*</span></p>
                                            <p v-html="formattedModTypes" class="text-start mb-1"></p>
                                            <input list="removableDrinkType" v-model="removedType" class="form-control" id="removedType" placeholder="Enter drink type" v-on:change="updateRemovedDrinkType">
                                            <datalist id="removableDrinkType">
                                                <option v-for="drinkType in removableDrinkType" :key="drinkType.id" :value="drinkType.drinkType">
                                                    {{drinkType.drinkType}}
                                                </option>
                                            </datalist>
                                            <p v-show="promotedType.length > 0" class="text-start mb-1 text-danger" id="removedTypeError"></p>
                                        </div>
                                        <p class="text-start mb-1 text-danger" id="notModError"></p>
                                    </div>

                                    <!-- confirm mod to promote -->
                                    <div v-if="chooseMod=='add' && doubleConfirmMod && !(successAddMod||errorAddMod||successRemoveMod||errorRemoveMod)" class="modal-body">
                                        <p class="text-start mb-1"> Do you really want to add <strong>{{ displayUser.username }}</strong> as a moderator for <strong>{{ promotedType }}</strong>? <span class="text-danger">*</span></p>
                                    </div>
                                    <div v-if="chooseMod=='remove' && doubleConfirmMod && !(successAddMod||errorAddMod||successRemoveMod||errorRemoveMod)" class="modal-body">
                                        <p class="text-start mb-1"> Do you really want to remove <strong>{{ displayUser.username }}</strong> as a moderator for <strong>{{ removedType }}</strong>? <span class="text-danger">*</span></p>
                                    </div>

                                    <!-- Initial confirm mod to promote to promote footer -->
                                    <div v-if="(chooseMod=='add' || chooseMod=='remove') && !doubleConfirmMod && !(successAddMod||errorAddMod||successRemoveMod||errorRemoveMod)" class="modal-footer">
                                        <button type="button" @click="selectMode" class="btn btn-secondary">Return</button>
                                        <button v-if="chooseMod=='add'" type="button" @click="doubleConfirm" class="btn btn-primary">Add Moderator</button>
                                        <button v-if="chooseMod=='remove'" type="button" @click="doubleConfirm" class="btn btn-primary">Remove Moderator</button>
                                    </div>

                                    <!-- Double confirm mod to promote footer -->
                                    <div v-if="(chooseMod=='add' || chooseMod=='remove') && doubleConfirmMod && !(successAddMod||errorAddMod||successRemoveMod||errorRemoveMod)" class="modal-footer">
                                        <button v-if="chooseMod=='add'" type="button" @click="addModMode" class="btn btn-secondary">Return</button>
                                        <button v-if="chooseMod=='remove'" type="button" @click="removeModMode" class="btn btn-secondary">Return</button>
                                        <button type="button" @click="confirmModifyModerator" class="btn btn-primary">Confirm Moderator</button>
                                    </div>

                                    <!-- successaddmod and erroraddmod footer -->
                                    <div v-if="successAddMod||errorAddMod||successRemoveMod||errorRemoveMod" class="modal-footer">
                                        <button type="button" @click="selectMode" class="btn btn-secondary">Return</button>
                                        <button type="button" @click="selectMode" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!-- Add/Remove moderator modal end -->


                        <!-- editProfileModal start -->
                        <div v-if="user" class="modal fade" id="editProfileModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                            <div class="modal-dialog modal-dialog-centered modal-lg">
                                <div class="modal-content">
                                <div class="modal-header">
                                    <h1 class="modal-title fs-5" id="exampleModalLabel">Edit Profile</h1> 
                                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                </div>
                                <div class="modal-body text-center">
                                    <!-- edit profile photo -->
                                    <div class="edit-profile-pic">
                                        <div class="row mb-3">
                                            <div class="col-4 text-start ps-5" style="margin: auto;">
                                                Image Preview
                                            </div>
                                            <div class="col-8">
                                                <!-- <img :src="selectedImage || 'data:image/jpeg;base64,' + (user.photo || defaultProfilePhoto)" alt="" class="rounded-circle-no-bg border border-dark profile-img" id="output" style="height:auto; width:100%; "> -->
                                                <img :src="selectedImage || (user.photo || defaultProfilePhoto)" alt="" class="rounded-circle-no-bg border border-dark profile-img" id="output" style="height:auto; width:100%; ">
                                            </div>
                                        </div>
                                        <div class="row mb-3">
                                            <div class="col-4 text-start ps-5" style="margin: auto;">
                                                Edit Image
                                            </div>
                                            <div class="col-8">
                                                <input class="form-control" id="file" type="file" @change="loadFile" ref="fileInput"/>
                                            </div>
                                        </div>
                                    </div>
                                    
                                    <!-- change drink of choice -->
                                    <div class="edit-drink-choice">
                                        <div class="row">
                                            <div class="col-4 text-start ps-5" style="margin: auto;">
                                                Drink Choice
                                            </div>
                                            <div class="col-8 text-start">
                                                <!-- checkbox to choose drinks -->
                                                <div v-for="(type, index) in drinkType" :key="index" class="m-1" style="display: inline-block">
                                                    <input type="checkbox" class="btn-check" :id="index" autocomplete="off" v-model="selectedDrinks" :value="type">
                                                    <label v-if="selectedDrinks.includes(type)" class="btn primary-btn-less-round" :for="index" style="color: whitesmoke; background-color: #535C72; border: 4px solid #535C72;">{{type}}</label>
                                                    <label v-else class="btn primary-btn-outline-less-round" :for="index">{{type}}</label>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal" @click="cancelChanges">Close</button>
                                    <button type="button" class="btn btn-primary" @click="saveChangesDetails" data-bs-dismiss="modal">Save changes</button>
                                </div>
                                </div>
                            </div>
                        </div>
                        <!-- editProfileModal end -->

                        <!-- applyModerator start -->
                        <div v-if="user" class="modal fade" id="applyModerator" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                            <div class="modal-dialog modal-lg modal-dialog-centered">
                                <div class="modal-content" >
                                    <div class="modal-header" style="background-color: #535C72"> <!-- style="background-color: #DDC8A9;"-->
                                        <p class="modal-title fs-5" style="color: white;">
                                        <b>Apply to be a moderator!</b>
                                        </p>
                                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>
                                    <div class="modal-body  px-5"> <!--text-center-->
                                        <div class="row">

                                            <div style="max-width:110px;">
                                                <svg v-if="photo == ''" xmlns="http://www.w3.org/2000/svg" style="height:auto; width:100%; " class="rounded-circle-no-bg border border-dark profile-img" >
                                                    <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0"/>
                                                    <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8m8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1"/>
                                                </svg>
                                                <!-- <img v-else :src="'data:image/png;base64,'+ photo" style="height:auto; width:100%;" class="rounded-circle-no-bg border border-dark profile-img" > -->
                                                <img v-else :src="photo" style="height:auto; width:100%;" class="rounded-circle-no-bg border border-dark profile-img" >
                                            </div>
                                            <div style="max-width:170px;" class="px-0">
                                                <button class="btn btn-warning hover-button p-1" style="border-radius: 20px; font-size: 0.8rem;">★ Certified Moderator</button> 
                                            </div>
                                        </div>


                                        <p class="fs-5"><b>Help shape the drinks community and share your expertise as a moderator! Just some quick questions:</b></p>
                                        <!--- <a href="#" class="m-2" style="font-style: italic; color: inherit">Click here to learn more about being a moderator</a>-->
                                        
                                        <div class="px-3">
                                            <h6 class="m-3 mx-0">What drinks category would you like to moderate for?</h6>
                                            <select class="form-select w-50 mx-auto" style="border: 2px solid #535C72;" aria-label="Default select example" v-model="modCat">
                                                <option v-for="(type, index) in filteredDrinkType" :key="index" :value="type">{{type}}</option>
                                            </select>
                                            <h6 class="m-3 mx-0">Why do you want to be a Drink X moderator? What's your experience with this drink category?</h6>
                                            <div class="mb-3">
                                                <textarea class="form-control Xw-50 mx-auto" style="border: 2px solid #535C72;" id="exampleFormControlTextarea1" rows="3" v-model="modDesc"></textarea>
                                            </div>
                                        </div>
                                        <btn class="btn secondary-btn-border " data-bs-dismiss="modal" @click="submitModeratorApplication" style="margin-right: 40%;margin-left:40%;"><b>Apply Now!</b></btn>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!-- applyModerator end -->

                        <!-- Change Password start -->
                        <div v-if="user" class="modal fade" id="changePasswordModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
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
                                            <p>Click on "Send Pin" and key in the OTP sent to your email:</p>
                                            <div class = "input-group">
                                                <input type='text' class="form-control" placeholder="Enter OTP" v-model="resetPin">
                                                <button :disabled="isButtonDisabled" class="btn btn-primary" type="button" id="resendPin" @click="sendResetPin">Send Pin</button>
                                            </div>
                                            <!-- <p v-show="isButtonDisabled" class="text-start mb-1 text-success" id="sendPinSuccess"></p> -->
                                            <p v-show="isButtonDisabled" class="text-start mb-1 text-success" id="sendPinSuccess"></p>
                                            <p v-show="isButtonDisabled" class="text-start mb-1 text-danger" id="sendPinError"></p>
                                            <p v-show="verifyErrorMessage.length>0" class="text-start mb-1 text-danger">{{ verifyErrorMessage }}</p>
                                        </div>  
                                        <div v-if="confirmResetPassword && !(passwordError||passwordSuccess||resettingPassword)">
                                            <b>Are you sure you want to reset your password? A new password will be sent to you.</b>
                                        </div>
                                        <div v-if="confirmResetPassword && resettingPassword && !(passwordError||passwordSuccess)">
                                            <b>Please wait while password is being resetted.</b>
                                        </div>
                                        
                                        <!-- if password change/reset is successful -->
                                        <p v-if="passwordSuccess" class="text-success fst-italic fw-bold fs-3">Password {{ changingPassword }} is successful!</p>
                                        <p v-if="passwordSuccess && confirmResetPassword" class="text-success fst-italic fw-bold fs-3">An email has been sent to you containing the password.</p>
                                        
                                        <!-- if password change/reset faces error -->
                                        <p v-if="passwordError" class ="text-danger fst-italic fw-bold fs-3">There is an error during password {{ changingPassword }}, please try again!</p>
                                        <p v-if="passwordMismatch" class ="text-danger fst-italic fw-bold fs-3">Old password do not match, please try again</p>
                                    </div>

                                    <div class="modal-footer">
                                        <!-- To return to previous select change password or reset password -->
                                        <button v-if="changingPassword!='' && !resettingPassword && !passwordSuccess" type="button" @click="selectPasswordMode" class="btn btn-secondary">Return</button>

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
                        <!-- Change password end -->


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
                                    <div class="mobile-col-3 col-12 col-sm-4 col-md-6 col-xl-4 p-2 mobile-pt-0 mobile-pb-0 mobile-pe-2 mobile-mb-2 " v-for="drinkTypeDetails in matchedDrinkTypes" :key="drinkTypeDetails.id">
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
                                        <img :src="(getBadgeInfo(badge)?.badgePhoto)" 
                                            alt="" class="rounded-circle-white-bg border border-dark badge-img">
                                        <!-- badge description -->
                                        <p class="pt-1" style="line-height: 1;"> 
                                            <small> 
                                                <b> {{ getBadgeInfo(badge)?.badgeDesc }} </b>
                                            </small> 
                                        </p>
                                    </div>
                                </div>
                            </div>
                            
                            <div>
                                <a href="#" style="color: black">Learn more about badges.</a>
                            </div>

                        </div>
                        
                    </div>

                </div>

                <!-- reviews and lists -->
                <div class="col-12 col-md-8">

                    <!-- reviews button -->
                    <button 
                        class="btn mx-1 fw-bold no-hover"
                        :class="{ 'primary-btn-green active-toggle-button-user-profile': activeTab === 'reviews', 'primary-btn-green-thin-outline inactive-toggle-button-user-profile': activeTab !== 'reviews' }"
                        @click="switchTab('reviews')"> 
                        Reviews 
                    </button>
                    <button 
                        class="btn mx-1 fw-bold no-hover"
                        :class="{ 'primary-btn-green active-toggle-button-user-profile': activeTab !== 'reviews', 'primary-btn-green-thin-outline inactive-toggle-button-user-profile': activeTab === 'reviews' }"
                        @click="switchTab('lists')"> 
                        <span v-if="ownProfile">My Drink List</span>
                        <span v-if="!ownProfile">Drink List</span> 
                    </button>

                    <div class="tab-content container mt-2 mobile-px-0" >
                        <!-- reviews tab -->
                        <div v-if="activeTab == 'reviews'" id="reviews">
                            <h3 class="text-body-secondary text-start pt-4"> 
                                <b> Recent Reviews </b> 
                            </h3>
                            <div v-if="Object.keys(recentReviews).length > 0">
                                <div v-for="(review, index) in recentReviews.slice(0, 5)" :key="index">  
                                    <div style="display: flex" class="row">
                                        <div class="col-3 mobile-col-3 mobile-pe-0">
                                            <!-- <img :src="'data:image/png;base64,' + (review.photo || defaultDrinkImage)" alt="" class="rounded bottle-img "> me-3 -->
                                            <img :src="(review.photo || defaultDrinkImage)" alt="" class="rounded bottle-img ">
                                            <p class="fs-4 mobile-fs-5 fw-bold rating-text text-center mobile-mb-1" >
                                                {{ review.rating }}
                                                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-star-fill " viewBox="0 0 16 16">
                                                    <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
                                                </svg>
                                            </p>
                                        </div>
                                        <div class="col-9 mobile-col-9 mobile-ps-2">
                                            <a :href="'/listing/view/' + review.reviewTarget" style="text-decoration: none; color: #223957;">
                                                <p class="fs-5 mobile-fs-7 mb-1 mobile-mb-0_5" ><b>{{ getListingName(review.reviewTarget) }}</b></p>
                                            </a>
                                            <!-- flavor tag -->
                                                
                                                <span v-for="(tag, index) in review.flavorTag" :key="index" class="mobile-view-hide badge rounded-pill-user-profile me-2 mb-1 mobile-me-0_5 mobile-mb-0_5 " :style="{ backgroundColor: getTagColor(tag) }"> {{ getTagName(tag) }}</span>
                                                <span v-for="(tag, index) in review.observationTag" :key="index" class="mobile-view-hide badge rounded-pill-user-profile me-2 mb-1 mobile-me-0_5 mobile-mb-0_5" style="background-color: grey;">{{ tag }}</span>

                                                <span v-for="(tag, index) in review.flavorTag?.slice(0, 2)" :key="index" class="mobile-view-show badge rounded-pill-user-profile me-2 mb-1 mobile-me-0_5 mobile-mb-0_5 " :style="{ backgroundColor: getTagColor(tag) }"> {{ getTagName(tag) }}</span>
                                                <span v-for="(tag, index) in review.observationTag.slice(0, 1)" :key="index" class="mobile-view-show badge rounded-pill-user-profile me-2 mb-1 mobile-me-0_5 mobile-mb-0_5" style="background-color: grey;">{{ tag }}</span>                                        
                                            <p class="mobile-fs-7">
                                                <b>{{ review.reviewTitle }}</b> <br v-if="review.reviewTitle">
                                                {{ review.reviewDesc }}
                                            </p>
                                            
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div v-else class="container m-2">
                                No reviews yet. To explore more drinks in the home page, 
                                <router-link to="/" style="color: inherit;">click here</router-link>. 
                            </div>

                            <ListingRowDisplayUserProfile 
                                :listingArr="favouriteListings" 
                                displayName="Favourite Listings" 
                                :user="user" 
                                :listing="listing" 
                                columnWidth="165px"
                                @icon-clicked="handleIconClick"/>

                            <ListingRowDisplayUserProfile 
                                :listingArr="recentActivity" 
                                displayName="Recent Activity" 
                                :user="user" 
                                :listing="listing" 
                                columnWidth="165px"
                                @icon-clicked="handleIconClick"/>



                        </div>

                        <!-- lists tab -->
                        <div v-if="activeTab == 'lists'" id="lists">
                            <button v-if="ownProfile" type="button" class="btn fw-bold primary-btn-less-round-blue xprimary-btn-outline-less-round mb-3" data-bs-toggle="modal" data-bs-target="#createNewListModal" >Create New List</button>

                            <!-- create new list modal -->
                            <div class="modal fade" id="createNewListModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                                <div class="modal-dialog modal-dialog-centered">
                                    <div class="modal-content">
                                    <div class="modal-header">
                                        <h1 class="modal-title fs-5" id="exampleModalLabel">Create New List</h1>
                                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>
                                    <div class="modal-body">
                                        <div class="mb-3">
                                            <label for="basic-url" class="form-label">List Name</label>
                                            <div class="input-group mb-3">
                                                <input v-model="newListName" type="text" class="form-control" placeholder="List Name" aria-label="Username" aria-describedby="basic-addon1">
                                            </div>
                                            <div v-if="newListNameError" class="text-danger text-sm">
                                                *{{ newListNameError }}
                                            </div>
                                        </div>

                                        <div class="mb-3">
                                            <label for="basic-url" class="form-label">List Description</label>
                                            <div class="input-group mb-3">
                                                <textarea v-model="newListDesc" type="text" class="form-control" placeholder="List Description (Optional)" aria-label="Username" aria-describedby="basic-addon1" rows="5"></textarea>
                                            </div>
                                        </div>

                                    </div>
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                        <button type="button" class="btn btn-primary" @click="addNewList">Save changes</button>
                                    </div>
                                    </div>
                                </div>
                            </div>
                            
                            <!-- display all lists -->
                            <div v-for="(bookmarkList, name, index) in displayUserBookmarks" :key="name" style="display: flex" class="row mb-3">
                                <div class="col-3 mobile-col-4 mobile-pe-0" >
                                    <!-- <img :src=" 'data:image/png;base64,' + ( getListingFromID(bookmarkList.listItems[0]).photo || defaultDrinkImage )" alt="" class="bottle-img me-3"> xyz -->
                                    <img :src="( getListingFromID(bookmarkList.listItems[0])?.photo || defaultDrinkImage )" alt="" class="bottle-img me-3">
                                </div>
                                <div  class="col-9 mobile-col-8 mobile-ps-1" > <!-- style="height: 150px; display: flex; flex-direction: column;" -->
                                    <h5 class="mt-1" @click="viewList(name)" style="cursor: pointer"> {{ name }} </h5>
                                    <span v-if="bookmarkList.listItems.length > 1"> {{ bookmarkList.listItems.length }} items in list </span>
                                    <span v-else> {{ bookmarkList.listItems.length }} item in list </span>
                                    <div style="max-height: 48px; overflow-y: auto; font-style: italic;">
                                        {{ bookmarkList.listDesc }}
                                    </div>
                                    <div style="display: flex; margin-top: auto;" class="mb-1">
                                        <b><a class="me-4 mobile-view-hide" @click="viewList(name)" href="#" style="color: #535C72;">View List</a></b>
                                        <b><a class="me-4 mobile-view-show" @click="viewList(name)" href="#" style="color: #535C72;">View</a></b>
                                        <b><a v-if="ownProfile && !(name == 'Drinks I Have Tried' || name == 'Drinks I Want To Try')" class="mobile-view-hide me-2" href="#" style="color: #535C72;" data-bs-toggle="modal" :data-bs-target="`#editListModal${index}`" @click="resetEditList(name, bookmarkList.listDesc)">Edit List</a></b>
                                        <b><a v-if="ownProfile && !(name == 'Drinks I Have Tried' || name == 'Drinks I Want To Try')"  class="mobile-view-hide " href="#" style="color: #535C72;" data-bs-toggle="modal" :data-bs-target="`#deleteListModal${index}`">Delete List</a></b>
                                        <b><a v-if="ownProfile && !(name == 'Drinks I Have Tried' || name == 'Drinks I Want To Try')" class="mobile-view-show me-2" href="#" style="color: #535C72;" data-bs-toggle="modal" :data-bs-target="`#editListModal${index}`" @click="resetEditList(name, bookmarkList.listDesc)">Edit</a></b>
                                        <b><a v-if="ownProfile && !(name == 'Drinks I Have Tried' || name == 'Drinks I Want To Try')" class="mobile-view-show" href="#" style="color: #535C72;" data-bs-toggle="modal" :data-bs-target="`#deleteListModal${index}`">Delete</a></b>
                                        
                                    </div>
                                </div>

                                <!-- edit list modal start -->
                                <div class="modal fade" :id="`editListModal${index}`" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                                    <div class="modal-dialog modal-dialog-centered">
                                    <div class="modal-content">
                                    <div class="modal-header">
                                        <h1 class="modal-title fs-5" id="exampleModalLabel">Edit List</h1>
                                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>
                                    <div class="modal-body">
                                        <div class="mb-3">
                                            <label for="basic-url" class="form-label">List Name</label>
                                            <div class="input-group mb-3">
                                                <input v-model="editListName" type="text" class="form-control" :placeholder="name" aria-label="Username" aria-describedby="basic-addon1">
                                            </div>
                                            <div v-if="editListNameError" class="text-danger text-sm">
                                                *{{ editListNameError }}
                                            </div>
                                        </div>

                                        <div class="mb-3">
                                            <label for="basic-url" class="form-label">List Description</label>
                                            <div class="input-group mb-3">
                                                <textarea v-model="editListDesc" type="text" class="form-control" :placeholder="bookmarkList.listDesc" aria-label="Username" aria-describedby="basic-addon1" rows="5"></textarea>
                                            </div>
                                        </div>

                                    </div>
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                        <button type="button" class="btn btn-primary" @click="editList(name)">Save changes</button>
                                    </div>
                                    </div>
                                </div>
                                </div>
                                <!-- modal end -->

                                <!-- delete list modal start -->
                                <div class="modal fade" :id="`deleteListModal${index}`" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                                    <div class="modal-dialog modal-dialog-centered">
                                        <div class="modal-content">
                                            <div class="text-end mt-2 me-2">
                                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                            </div>

                                            <div class="text-center">
                                                <img src="../../../Images/Others/cancel.png" alt="" class="rounded-circle border border-dark text-center" style="width: 100px; height: 100px;">
                                                <h3>Are you sure?</h3>
                                                <br>
                                                <p>Do you really want to delete <b><i>{{ name }}</i></b>? </p>
                                            </div>
                                            <div style="display: inline" class="text-center mb-4">
                                                <button type="button" class="btn btn-secondary me-3" data-bs-dismiss="modal">Cancel</button>
                                                <button type="button" class="btn btn-danger" data-bs-dismiss="modal" @click="deleteList(name)">Delete</button>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <!-- modal end -->
                            </div>
                        </div>

                        <!-- individual list tab -->
                        <div v-if="activeTab == 'list' && displayUser.drinkLists" id="list">

                            <!-- list name, back to lists & add drink to list & share button -->
                            <div class="row mb-4 mobile-mt-4">
                                <div class="col-5 mobile-col-7">
                                    <h3>{{currentList}}</h3>
                                </div>
                                <div class="col-7 mobile-col-5 text-end d-flex justify-content-end">
                                    <button v-if="ownProfile" type="button" class="btn primary-btn-outline-less-round drinklist" data-bs-toggle="modal" data-bs-target="#exampleModal">
                                        <svg xmlns="http://www.w3.org/2000/svg"  fill="currentColor" class="bi bi-plus-square mb-1 me-1 funnel-svg-dimensions" viewBox="0 0 16 16">
                                        <path d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2z"/>
                                        <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4"/>
                                        </svg>
                                        <span class="mobile-view-hide" >Add Drink</span>
                                    </button>
                                    <button @click="updateCurrentURL" type="button" class="btn primary-btn-outline-less-round ms-3 drinklist" data-bs-toggle="modal" data-bs-target="#shareListModal">
                                        <svg  xmlns="http://www.w3.org/2000/svg"  fill="currentColor" class="bi bi-share mb-1 me-1 funnel-svg-dimensions" viewBox="0 0 30 30">
                                            <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
                                            <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
                                            <g id="SVGRepo_iconCarrier"> 
                                            <path d="M0 25.472q0 2.368 1.664 4.032t4.032 1.664h18.944q2.336 0 4-1.664t1.664-4.032v-8.192l-3.776 3.168v5.024q0 0.8-0.544 1.344t-1.344 0.576h-18.944q-0.8 0-1.344-0.576t-0.544-1.344v-18.944q0-0.768 0.544-1.344t1.344-0.544h9.472v-3.776h-9.472q-2.368 0-4.032 1.664t-1.664 4v18.944zM5.696 19.808q0 2.752 1.088 5.28 0.512-2.944 2.24-5.344t4.288-3.872 5.632-1.664v5.6l11.36-9.472-11.36-9.472v5.664q-2.688 0-5.152 1.056t-4.224 2.848-2.848 4.224-1.024 5.152zM32 22.080v0 0 0z"></path> 
                                            </g>
                                        </svg>
                                        <span class="mobile-view-hide">Share List</span>
                                    </button>
                                    <button @click="viewList('lists')" type="button" class="btn primary-btn-outline-less-round ms-3 drinklist">
                                        <svg xmlns="http://www.w3.org/2000/svg"  fill="currentColor" class="bi bi-arrow-left-circle mb-1 me-1 funnel-svg-dimensions" viewBox="0 0 16 16">
                                        <path fill-rule="evenodd" d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8m15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0m-4.5-.5a.5.5 0 0 1 0 1H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5z"/>
                                        </svg>
                                        <span class="mobile-view-hide">Back to Lists</span>
                                    </button>

                                    <!-- Share Menu Modal (QR Code) -->
                                    <div class="modal fade" id="shareListModal" tabindex="-1" aria-labelledby="shareListModalLabel" aria-hidden="true">
                                        <div class="modal-dialog">
                                            <div class="modal-content">
                                                <div class="modal-header">
                                                    <h1 class="modal-title fs-5" id="shareMenuModalLabel"> Drink List QR Code </h1>
                                                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                                </div>
                                                <div class="modal-body">
                                                    <div class="centered">
                                                        <qr-code v-bind:text="currentURL" ref="qrCode"></qr-code>
                                                    </div>
                                                    <div class="input-group pt-3">
                                                        <input type="text" class="form-control" aria-label="Link" aria-describedby="button-addon2" v-bind:value="currentURL" disabled>
                                                        <button class="btn btn-outline-secondary" type="button" id="button-addon2" @click="copyToClipboard(currentURL)">
                                                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-clipboard" viewBox="0 0 16 16">
                                                                <path d="M4 1.5H3a2 2 0 0 0-2 2V14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V3.5a2 2 0 0 0-2-2h-1v1h1a1 1 0 0 1 1 1V14a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V3.5a1 1 0 0 1 1-1h1z"/>
                                                                <path d="M9.5 1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-3a.5.5 0 0 1-.5-.5v-1a.5.5 0 0 1 .5-.5zm-3-1A1.5 1.5 0 0 0 5 1.5v1A1.5 1.5 0 0 0 6.5 4h3A1.5 1.5 0 0 0 11 2.5v-1A1.5 1.5 0 0 0 9.5 0z"/>
                                                            </svg>
                                                        </button>
                                                    </div>
                                                    <p class="text-start pt-2" v-if="clipboardItem"> 
                                                        <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-check" viewBox="0 0 16 16">
                                                            <path d="M10.97 4.97a.75.75 0 0 1 1.07 1.05l-3.99 4.99a.75.75 0 0 1-1.08.02L4.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093 3.473-4.425z"/>
                                                        </svg>
                                                        Copied to clipboard!
                                                    </p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                </div>
                            </div>

                            <!-- add drink modal -->
                            <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                                <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                                    <div class="modal-content">
                                    <div class="modal-header">
                                        <h5>Add Drink to List: {{currentList}}</h5>
                                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>
                                    <div class="modal-body" style="height: 400px;">
                                        <!-- search -->
                                        <div>
                                            <!-- search bar  -->
                                            <div class="input-group mb-3">
                                                <input type="text" class="form-control" placeholder="Search for drink" aria-label="Recipient's username" aria-describedby="button-addon2" v-model="drinkSearch" @keyup="searchResult">
                                            </div>
                                            <!-- search results -->
                                            <div class="overflow-auto" :style="{ height: drinksToAdd.length > 0 ? '200px' : '300px' }">
                                                <div class="form-check" v-for="(drinkName, index) in drinkSearchResults" :key="index">
                                                    <input class="form-check-input" type="checkbox" :value="drinkName" :id="'drinkCheckbox' + index" v-model="drinksToAdd">
                                                    <label class="form-check-label" :for="'drinkCheckbox' + index">
                                                        {{ drinkName }}
                                                    </label>
                                                </div>
                                            </div>
                                        </div>
                                        <!-- selected results -->
                                        <div v-if="drinksToAdd.length > 0" class="mt-2">
                                            <hr>
                                            <div class="overflow-auto" style="height: 75px">
                                                <b>Selected Drinks: </b>
                                                {{ drinksToAdd.join(', ') }}
                                            </div>
                                        </div>

                                    </div>
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-primary" @click="addDrinkToList(currentList)">Add to List</button>
                                    </div>
                                    </div>
                                </div>
                            </div>

                            <!-- list details -->
                            <div class="row mb-3" v-for="(listingID, index) in displayUser.drinkLists[currentList].listItems" :key="index">
                                <div class="col-10 pe-0" style="display: flex">
                                    <!-- <img :src=" 'data:image/png;base64,' + ( getListingFromID(listingID[1]).photo || defaultDrinkImage )" alt="" style="width:130px; height:130px;" class="bottle-img me-3"> -->
                                    <img :src=" ( getListingFromID(listingID)?.photo || defaultDrinkImage )" alt="" style="width:130px; height:130px;" class="bottle-img me-3">
                                    <div style="min-height: 150px; display: flex; flex-direction: column;">
                                        <a :href="'/listing/view/' + listingID" style="text-decoration: none; color: inherit;">
                                            <h4>{{ getListingFromID(listingID)?.listingName }}</h4>
                                        </a>
                                        <p style="display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden;"> {{ getListingFromID(listingID)?.officialDesc }} </p>
                                        <div v-if="ownProfile" style="display: flex; margin-top: auto" class="mb-0">
                                            <a href="#" style="text-decoration: none; color: #535C72;" data-bs-toggle="modal" :data-bs-target="`#deleteFromListModal${index}`">
                                                <!-- cross icon -->
                                                <svg class=mb-1 xmlns="http://www.w3.org/2000/svg" height="16" width="12" viewBox="0 0 384 512">
                                                    <!--! Font Awesome Free 6.5.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc. -->
                                                    <path d="M342.6 150.6c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L192 210.7 86.6 105.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L146.7 256 41.4 361.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L192 301.3 297.4 406.6c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3L237.3 256 342.6 150.6z"/>
                                                </svg>
                                                Delete from list
                                            </a>
                                        </div>

                                    </div>
                                </div>
                                <div class="col-2 text-center ps-0">
                                    <h2>
                                        {{ getAverageReview(listingID) }}
                                        <svg class="mb-2" xmlns="http://www.w3.org/2000/svg" height="18" width="20.25" viewBox="0 0 576 512">
                                            <!--! Font Awesome Free 6.5.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc. -->
                                            <path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L433.6 328.4l26.2 155.6c1.5 9-2.2 18.1-9.7 23.5s-17.3 6-25.3 1.7l-137-73.2L151 509.1c-8.1 4.3-17.9 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l26.2-155.6L31.1 218.2c-6.5-6.4-8.7-15.9-5.9-24.5s10.3-14.9 19.3-16.3l153.2-22.6L266.3 13.5C270.4 5.2 278.7 0 287.9 0zm0 79L235.4 187.2c-3.5 7.1-10.2 12.1-18.1 13.3L99 217.9 184.9 303c5.5 5.5 8.1 13.3 6.8 21L171.4 443.7l105.2-56.2c7.1-3.8 15.6-3.8 22.6 0l105.2 56.2L384.2 324.1c-1.3-7.7 1.2-15.5 6.8-21l85.9-85.1L358.6 200.5c-7.8-1.2-14.6-6.1-18.1-13.3L287.9 79z"/>
                                        </svg>
                                    </h2>
                                </div>

                                <!-- delete from list modal start -->
                                <div class="modal fade" :id="`deleteFromListModal${index}`" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                                    <div class="modal-dialog modal-dialog-centered">
                                        <div class="modal-content">
                                            <div class="text-end mt-2 me-2">
                                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                            </div>

                                            <div class="text-center mx-2">
                                                <img src="../../../Images/Others/cancel.png" alt="" class="rounded-circle border border-dark text-center" style="width: 100px; height: 100px;">
                                                <h3>Are you sure?</h3>
                                                <br>
                                                <p>Do you really want to delete <b><i>{{ getListingFromID(listingID)?.listingName }}</i></b> from <b><i>{{ currentList }}</i></b>? </p>
                                            </div>
                                            <div style="display: inline" class="text-center mb-4">
                                                <button type="button" class="btn btn-secondary me-3" data-bs-dismiss="modal">Cancel</button>
                                                <button type="button" class="btn btn-danger" data-bs-dismiss="modal" @click="deleteFromList(currentList, listingID)">Delete</button>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <!-- modal end -->
                            </div>
                        
                        </div>
                    </div>

                </div>
            </div>
            <BookmarkModal 
                v-if="user" 
                :user="user" 
                :listings="listings" 
                :listingID="bookmarkListingID" />
            
        </div>
        


    
    </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue';
import ListingRowDisplayUserProfile from '@/components/ListingRowDisplayUserProfile.vue';
import BookmarkModal from '@/components/BookmarkModal.vue';



// toggling between lists and list details
export default {
    components: {
        NavBar, 
        ListingRowDisplayUserProfile, 
        BookmarkModal
    },
    data() {
        return {
            dataLoaded: false,
            currentURL: "",
            // default images
            defaultProfilePhoto: "https://drinkximages.s3.us-east-1.amazonaws.com/images/27e129b8-2d6e-44a3-8c14-d78c815b8056.jpg",       
            defaultDrinkImage: "https://drinkximages.s3.us-east-1.amazonaws.com/images/2d4d94bc-313e-4621-9a15-4bfbf77958de.jpg",   
            
            //personal profile image
            photo: '',
            profileURL: '/login',
            onProfile: false,

            // user details
            loggedIn: false,
            userID: "",
            user: {},
            userBookmarks: {},
            ownProfile: false,

            // user being viewed
            displayUserID: null,
            displayUser: {},
            drinkChoice: "",
            drinkCount: 0,
            joinDate: "",
            following: false,

            // data from database
            listings: [],
            producers: [],
            venues: [],
            reviews: [],
            reversedReviews: [],
            users: [],
            drinkCategories: [],
            drinkTypes: [],
            badges: [],
            drinkType: [],
            subTags: null,
            flavourTags: null,

            filteredDrinkType: [],

            // data for tab
            showCurrentContent: true, 
            activeTab: 'reviews',

            // image upload
            selectedImage: null,
            selectedDrinks: [],
            image64: null,

            // display user drink activity
            favouriteListings: {},
            recentActivity: {},
            recentReviews: {},

            // create list
            currentList: "",
            newListName: "",
            newListDesc: "",
            newListNameError: "",

            // edit list
            editListName: "",
            editListDesc: "",
            editListNameError: "",

            // add or edit drink from list
            drinksToAdd: [],
            drinkSearch: "",
            drinkSearchResults: [],

            // mod request
            modType: "",
            modDesc: "",

            // for bookmark component
            bookmarkListingID: {},

            // flags and variables for adding moderator
            successAddMod:false,
            successRemoveMod:false,
            errorRemoveMod:false,
            errorAddMod:false,
            addableDrinkType:[],
            removableDrinkType:[],
            promotedType:"",
            removedType:"",
            selectedPromotedType:null,
            selectedRemoveType:null,
            chooseMod:"",
            doubleConfirmMod:false,

            // flags and variables for changing/resetting password
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
    computed: {
        formattedModTypes() {
            // Join the modType array elements with commas and spaces
            if(this.displayUser.modType.length === 0){
                return "This user is currently not a moderator!"
            }
            else{
                return "This user is currently a moderator for <b>" + this.displayUser.modType.join(', ') +"</b>!";
            }
        },
    },
    mounted() {

        // Obtain user's profile picture + set profile URL
        if (localStorage.getItem('88B_accID') != null) {

        this.accType = localStorage.getItem('88B_accType');
        let accID = localStorage.getItem('88B_accID');
        let url = `${process.env.VUE_APP_API_URL}/getData/get`;

        if (this.accType == 'user') {
            url = url + 'User/' + accID;
            this.loadData(url);

            this.profileURL = '/profile/user/'+accID;
            this.dashboardURL = '/dashboard/user';
            this.dashboardWord = 'Drink';
        } 
        else if (this.accType == 'producer') {
            url = url + 'Producer/' + accID;
            this.loadData(url);

            this.profileURL = '/profile/producer/' + accID;
            this.dashboardURL = '/Producers/ProducersDashboard/' + accID;
            this.dashboardWord = 'Brand';
            
        } 
        else if (this.accType == 'venue') {
            url = url + 'Venue/' + accID;
            this.loadData(url);

            this.profileURL = '/profile/venue';
            this.dashboardURL = '/dashboard/venue';
            this.dashboardWord = 'Venue';
        }

        // check if current page is profile page
        if (this.$route.path.split('/')[1] == 'profile') {
            this.onProfile = true;
        }

        // check if current page is create listing page
        if (this.$route.path.split('/').length >= 3 && this.$route.path.split('/')[2] == 'create') {
            this.onCreate = true;
        }

        // check if current page is request page
        if (this.$route.path.split('/')[1] == 'request') {
            this.onRequest = true;
        }
        }

        // get local storage
        const accID = localStorage.getItem("88B_accID");
        if(accID !== null){
            this.userID = localStorage.getItem('88B_accID')
            this.loggedIn = true
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

        // get list name from URL
        try {
            if (this.$route.params.listName) {
                this.currentList = this.$route.params.listName;
                this.activeTab = 'list';
            } else {
                this.currentList = "";
            
            }
        }
        catch (error) {
            console.error(error);
        }

    },
    methods: {
        // load data from database
        async loadData(url) {
            //profile picture
            if (url){
                try {
                    const response = await this.$axios.get(url);
                    this.photo = response.data["photo"];

                if (this.accType == 'user') {
                    if (response.data.isAdmin) {
                        this.isAdmin = true;
                    }
                    if (Array.isArray(response.data.modType) && response.data.modType.length > 0) {
                        this.isModerator = true;
                    }
                }
            } 
            catch (error) {
                console.error(error);
            }
            }

            // Listings
            try {
                const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getListings`);
                this.listings = response.data;
                // originally, make filteredListings the entire collection of listings
                this.filteredListings = this.listings;
            } 
            catch (error) {
                console.error(error);
                this.dataLoaded = null;
            }
            // Reviews
            try {
                const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getReviews`);
                this.reviews = response.data;
                this.reversedReviews = this.reviews.reverse();
                this.recentReviews = this.reversedReviews.filter(review => review.userID === parseInt(this.displayUserID) && review.reviewType === 'Listing');
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
            // Users
            try {
                const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getUsers`);
                this.users = response.data;
                this.user = this.getUser(this.userID);
                this.displayUser = this.getUser(this.displayUserID);
                
                if (this.userID === this.displayUserID) {
                    this.ownProfile = true;
                }
                else {
                    this.ownProfile = false;
                }

                this.drinkChoice = this.getDrinkOfChoice();
                this.drinkCount = this.getDrinkCount();
                if (this.user) {
                    // join date
                    const dateString = this.user.joinDate;
                    const dateParts = dateString.split('-');
                    const year = dateParts[0];
                    const month = new Date(dateString).toLocaleString('default', { month: 'long' });
                    this.joinDate = `${month} ${year}`;
                    this.selectedDrinks = this.user.choiceDrinks;
                    this.userBookmarks = this.user.drinkLists;
                    this.following = JSON.stringify(this.user.followLists.users).includes(JSON.stringify(this.displayUserID));

                } else {
                    const dateString = this.displayUser.joinDate;
                    const dateParts = dateString.split('-');
                    const year = dateParts[0];
                    const month = new Date(dateString).toLocaleString('default', { month: 'long' });
                    this.joinDate = `${month} ${year}`;
                }

                this.userDrinkChoice = this.getDrinkOfChoice(this.user);
                this.displayUserDrinkChoice = this.getDrinkOfChoice(this.displayUser);
                this.displayUserBookmarks = this.displayUser.drinkLists;
                this.getUserFavourite();
                this.getRecentActivity();

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
            // mod requests
            try {
                const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getModRequests`);
                this.modRequests = response.data;
                this.modRequestsType = this.modRequests
                    .filter(request => request.userID === this.userID && request.reviewStatus === true)
                    .map(request => request.drinkType);
            } 
            catch (error) {
                console.error(error);
                this.dataLoaded = null;
            }
            // drinkCategories
            try {
                const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getDrinkTypes`);
                this.drinkTypes = response.data;
                // retrieve the drink type and put them into an array
                this.drinkType = this.drinkTypes.map(category => category.drinkType);
                if (this.user && this.drinkTypes) {
                    this.filteredDrinkType =  this.drinkType.filter(type => !this.user.modType.includes(type));
                    if (this.modRequestsType.length > 0) {
                        this.filteredDrinkType = this.filteredDrinkType.filter(type => !this.modRequestsType.includes(type));
                    }
                }
                if(this.displayUser){
                    let currentMod = this.displayUser.modType
                    this.removableDrinkType = this.drinkTypes.filter(drinkType=>{
                        return currentMod.includes(drinkType.drinkType);
                    })
                    this.addableDrinkType = this.drinkTypes.filter(drinkType=>{
                        return !currentMod.includes(drinkType.drinkType);
                    })
                }

                // ==== for badges ====
                this.getTopCategoriesReviewed();
                this.getMatchedDrinkType();
                this.calculateTotalBadges();

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
                })
            } 
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

            // Set data loaded flag
            if (this.dataLoaded !== null) {
                this.dataLoaded = true;
            }
        },

        // ------------------- User Profile -------------------
        // get user from user ID
        getUser(id) {
            return this.users.find(user => user.id === parseInt(id));
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
        getDrinkOfChoice() {
            if (this.ownProfile) {
                return this.user.choiceDrinks.join(", ");
            }
            else {
                return this.displayUser.choiceDrinks.join(", ");
            }
        },

        // ------------------- Edit User Profile -------------------
        // read uploaded image
        async loadFile(event) {
            const file = event.target.files[0];
            const reader = new FileReader();

            reader.onloadend = async () => {
                this.selectedImage = reader.result;
                const base64String = reader.result.replace('data:', '').replace(/^.+,/, '');

                this.image64 = base64String;

            };
            reader.readAsDataURL(file);
        
        },
        // save changes to user profile
        async saveChangesDetails() {
            if (this.image64 == null) {
                this.image64 = this.user["profile_picture"];
            }
            
            try {
                console.log(this.image64)
                const response = await this.$axios.post(`${process.env.VUE_APP_API_URL}/editProfile/editDetails`, 
                    {
                        userID: this.userID,
                        image64: this.image64,
                        drinkChoice: this.selectedDrinks,
                    }, {
                    headers: {
                        'Content-Type': 'application/json'
                    }
                });
                console.log(response.data);
            } catch (error) {
                console.error(error);
            }

            // window.location.reload();
        },
        // reset edit profile form
        cancelChanges() {
            this.selectedDrinks = this.user.choiceDrinks;
            this.selectedImage = null;
            this.$refs.fileInput.value = '';
        }, 

        // ------------------- User Bookmarks -------------------
        // checks if an item has been bookmarked
        checkBookmarkStatus(listingID) {
            // check if listingID is in user bookmark
            for (const category of Object.values(this.userBookmarks)) {
                if (category.listItems) {
                    if (category.listItems.some(item => item === parseInt(listingID))) {
                        return true;
                    }
                }
            }
        },
        getListingFromID(listingID) {
            return this.listings.find(listing => listing.id === parseInt(listingID));
        },

        // return oid from name of drink listing
        getListingID(listingName) {
            const listing = this.listings.find(listing => listing.listingName === listingName);
            return listing.id;
        },
        // return search items for bookmarking
        searchResult() {
            this.drinkSearchResults = this.listings
                .filter(listing => listing.listingName.toLowerCase().includes(this.drinkSearch.toLowerCase()))
                .filter(listing => !this.checkBookmarkStatus(listing.id))
                .map(listing => listing.listingName);
        },
        // bookmark item through search
        async addDrinkToList(listName) {
            for (const drink of this.drinksToAdd) {
                let addListingId = this.getListingID(drink);
                let itemExist = this.userBookmarks[listName].listItems.find(item => item === addListingId);
                if (!itemExist) {
                    this.userBookmarks[listName].listItems.push(addListingId);
                }
            }

            try {
                const response = await this.$axios.post(`${process.env.VUE_APP_API_URL}/editProfile/updateBookmark`, 
                    {
                        userID: this.userID,
                        bookmark: this.userBookmarks,
                    }, {
                    headers: {
                        'Content-Type': 'application/json'
                    }
                });
                console.log(response.data);
            } catch (error) {
                console.error(error);
            }
            
           window.location.reload();
        },
        // add new list
        async addNewList() {
            if (this.userBookmarks[this.newListName]) {
                this.newListNameError = "List name already exists";
                return;
            } else if (this.newListName === "") {
                this.newListNameError = "List name cannot be empty";
                return;
            }
            
            this.newListNameError = "";
            this.userBookmarks[this.newListName] = {};
            this.userBookmarks[this.newListName].listDesc = this.newListDesc;
            this.userBookmarks[this.newListName].listItems = [];

            try {
                const response = await this.$axios.post(`${process.env.VUE_APP_API_URL}/editProfile/updateBookmark`, 
                    {
                        userID: this.userID,
                        bookmark: this.userBookmarks,
                    }, {
                    headers: {
                        'Content-Type': 'application/json'
                    }
                });
                console.log(response.data);
            } catch (error) {
                console.error(error);
            }
            
            window.location.reload();

        },
        // delete drink from list
        async deleteFromList(listName, listingID) {
            // param: objectId
            const index = this.userBookmarks[listName].listItems.indexOf(listingID);
            this.userBookmarks[listName].listItems.splice(index, 1);

            try {
                const response = await this.$axios.post(`${process.env.VUE_APP_API_URL}/editProfile/updateBookmark`, 
                    {
                        userID: this.userID,
                        bookmark: this.userBookmarks,
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
        // delete list
        async deleteList(listName) {
            // delete the list from the user's bookmark list
            delete this.userBookmarks[listName];

            try {
                const response = await this.$axios.post(`${process.env.VUE_APP_API_URL}/editProfile/updateBookmark`, 
                    {
                        userID: this.userID,
                        bookmark: this.userBookmarks,
                    }, {
                    headers: {
                        'Content-Type': 'application/json'
                    }
                });
                console.log(response.data);
            } catch (error) {
                console.error(error);
            }

            window.location.reload();
        }, 
        // reset form details
        resetEditList(listName, listDesc) {
            this.editListName = listName;
            this.editListDesc = listDesc;
            this.editListNameError = "";
        },
        // edit list details
        async editList(currentListName) {
            if (this.editListName === "") {
                this.editListNameError = "List name cannot be empty";
                return;
            } else if (this.editListName !== currentListName && this.userBookmarks[this.editListName]) {
                this.editListNameError = "List name already exists";
                return;
            }

            this.listNameError = "";

            if (this.editListName !== currentListName) {
                this.userBookmarks[this.editListName] = {};
                this.userBookmarks[this.editListName].listDesc = this.editListDesc;
                this.userBookmarks[this.editListName].listItems = this.userBookmarks[currentListName].listItems;
                delete this.userBookmarks[currentListName];
            } 
            
            this.userBookmarks[this.editListName].listDesc = this.editListDesc;

            try {
                const response = await this.$axios.post(`${process.env.VUE_APP_API_URL}/editProfile/updateBookmark`, 
                    {
                        userID: this.userID,
                        bookmark: this.userBookmarks,
                    }, {
                    headers: {
                        'Content-Type': 'application/json'
                    }
                });
                console.log(response.data);
            } catch (error) {
                console.error(error);
            }

            window.location.reload();

        }, 

        // ------------------- Moderator Application -------------------
        // submit moderator application
        async submitModeratorApplication() {
            try {
                const response = await this.$axios.post(`${process.env.VUE_APP_API_URL}/editModRequests/submitModRequest`, 
                    {
                        userID: this.userID,
                        drinkType: this.modCat,
                        modDesc: this.modDesc,
                    }, {
                    headers: {
                        'Content-Type': 'application/json'
                    }
                });
                console.log(response.data);
                if (response.data.code == 201) {
                    alert("Moderator application submitted successfully!");
                }
            } catch (error) {
                console.error(error);
            }
            const index = this.filteredDrinkType.indexOf(this.modCat);
            if (index !== -1) {
                this.filteredDrinkType.splice(index, 1);
            }
            this.modCat = "";
            this.modDesc = "";
        },
        
        // ------------------- User Drink Activity -------------------
        // check if review is for listing
        async checkReviewType(listingID) {
            const review = this.reviews.find(review => review.listingID === listingID);
            return review.reviewType == "Listing"
        },
        // get listing name from listing ID
        getListingName(listingID) {
            if (this.listings) {
                return this.listings.find(listing => listing.id === listingID).listingName;
            }
        },
        // get user's favourite listings
        getUserFavourite() {
            const favouriteListingReviews = this.reviews
                .filter(review => review.reviewType === "Listing" && 
                    review.userID === this.displayUserID &&
                    review.rating >= 5)
                .sort((a, b) => b.rating - a.rating);

            const favouriteListingIds = favouriteListingReviews
                .map(review => review.reviewTarget)

            this.favouriteListings = this.listings
                .filter(listing => favouriteListingIds.includes(listing.id))
                .sort((a, b) => {
                    // Get the indices of the IDs in favouriteIdList
                    const indexA = favouriteListingIds.indexOf(a.id);
                    const indexB = favouriteListingIds.indexOf(b.id);
                    
                    // Sort based on the indices in favouriteIdList
                    return indexA - indexB;
                })
                .slice(0, 5);
        },
        // get user's recent activity
        getRecentActivity() {

            // // reviews
            let userReviews = this.reviews
                .filter(review => review.reviewType === "Listing" && 
                    review.userID === this.displayUserID)
                .map(review => {
                    review.listingID = review.reviewTarget;
                    return review;
                });

            // bookmarks
            let allUserBookmarks = Object.values(this.userBookmarks).map(item => item.listItems).flat();
            let allUserBookmarksDict = allUserBookmarks.map(listingID => ({listingID}));

            // combine reviews and bookmarks
            let userActivity = userReviews.concat(allUserBookmarksDict);

            this.recentActivity = userActivity
                .reverse()
                .filter((item, index, self) =>
                    index === self.findIndex((t) => (
                    t.listingID === item.listingID
                    ))
                )
                .map(item => {
                    item = this.listings.find(listing => listing.id === parseInt(item.listingID));
                    return item;
                })
                .slice(0, 5);

        }, 
        getListingPhoto(listingID) {
            const listing = this.listings.find(listing => listing.id === listingID);
            return listing.photo;
        },
        getTagName(tag) {
            if (!this.subTags || !this.flavourTags) {
                return "";
            }
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
                if (!familyTag || !subTag) {
                    return "";
                }
            }else{
                return "<deleted>"
            }

        },
        getTagColor(tag) {
            if (!this.subTags || !this.flavourTags) {
                return "";
            }
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
                if (!familyTag || !subTag) {
                    return "";
                }
            }else{
                return "#" + "030303"
            }
            
        },

        // ------------------- User Follow -------------------
        // follow or unfollow user
        async editFollow(action) {
            if (action === "unfollow") {
                this.following = false;
            } else {
                this.following = true
            }
            try {
                const response = await this.$axios.post(`${process.env.VUE_APP_API_URL}/editProfile/updateFollowLists`, 
                    {
                        userID: this.userID,
                        action: action,
                        target: "users",
                        followerID: this.displayUserID,
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

        // others
        // get average review
        getAverageReview(listingID) {
            // param: objectId
            const reviews = this.reviews.filter(review => review.reviewTarget === listingID);
            if (reviews.length > 0) {
                const totalRating = reviews.reduce((acc, review) => acc + review.rating, 0);
                return (totalRating / reviews.length).toFixed(1);
            }
            return "-";
        },

        // ------------------- UI -------------------
        // review and drink list toggle
        viewList(name) {
            if (name == "lists") {
                this.activeTab = 'lists';
                this.$router.push('/profile/user/' + this.displayUserID);
            } else {
                this.activeTab = 'list';
                this.currentList = name;
                this.$router.push('/profile/user/' + this.displayUserID + '/' + name);
            }
        },
        switchTab(tab) {
            this.activeTab = tab;
            this.$router.push('/profile/user/' + this.displayUserID);
        },

        // drink list sharing
        updateCurrentURL() {
            this.currentURL = window.location.href;
        },

        copyToClipboard(text) {
            navigator.clipboard.writeText(text)
            .then(() => {
                this.clipboardItem = true;
                setTimeout(() => {
                    this.clipboardItem = false;
                }, 3000);
            })
            .catch(err => {
                console.error('Failed to copy text: ', err);
            });
        },
        
        // for bookmark component
        handleIconClick(data) {
            this.bookmarkListingID = data
        },
        updateDrinkType(){
            // get error message element
            let promotedTypeError = document.getElementById("promotedTypeError")
            // find listing based on bottle name
            let drinkType = this.addableDrinkType.find(drinkType => drinkType.drinkType === this.promotedType)
            if (drinkType) {
                this.selectedPromotedType = drinkType
                promotedTypeError.innerHTML = ""
            }
            else {
                this.selectedPromotedType = null
                promotedTypeError.innerHTML = "Please enter a valid drink type"
            }
        },
        updateRemovedDrinkType(){
            // get error message element
            let removedTypeError = document.getElementById("removedTypeError")
            // find listing based on bottle name
            let drinkType = this.removableDrinkType.find(drinkType => drinkType.drinkType === this.removedType)
            if (drinkType) {
                this.selectedRemoveType = drinkType
                removedTypeError.innerHTML = ""
            }
            else {
                this.selectedRemoveType = null
                removedTypeError.innerHTML = "Please enter a valid drink type"
            }
        },
        doubleConfirm(){
            if(this.chooseMod == 'add'){
                let errorMessage = ''
                if(this.selectedPromotedType == null){
                    errorMessage+="Please enter a valid drink type!\n"
                }
                if(errorMessage!=''){
                    alert(errorMessage)
                    return null
                }
                let alreadyModError = document.getElementById("alreadyModError")
                if(this.displayUser.modType.includes(this.selectedPromotedType.drinkType)){
                    alreadyModError.innerHTML = "This user is already a moderator for this drink type"
                    return null
                }else{
                    alreadyModError.innerHTML = ""
                }
            }
            if(this.chooseMod =='remove'){
                let errorMessage = ''
                if(this.selectedRemoveType == null){
                    errorMessage+="Please enter a valid drink type!\n"
                }
                if(errorMessage!=''){
                    alert(errorMessage)
                    return null
                }
                let notModError = document.getElementById("notModError")
                if(!this.displayUser.modType.includes(this.selectedRemoveType.drinkType)){
                    notModError.innerHTML = "This user is not a moderator for this drink type"
                    return null
                }else{
                    notModError.innerHTML = ""
                }
            }
            this.doubleConfirmMod = true
        },
        addModMode(){
            this.chooseMod = 'add'
            this.doubleConfirmMod = false
        },
        removeModMode(){
            this.chooseMod = 'remove'
            this.doubleConfirmMod = false
        },
        selectMode(){
            this.chooseMod = ''
            this.doubleConfirmMod = false
            this.resetErrors()
        },
        resetErrors(){
            this.successAddMod = false
            this.successRemoveMod =false
            this.errorAddMod = false
            this.errorRemoveMod = false
            this.selectedPromotedType = null
            this.selectedRemoveType = null
            this.promotedType = ''
            this.removedType = ''
        },
        async confirmModifyModerator(){
            try {
                let submitURL = ''
                let submitData = {}
                if(this.chooseMod=='remove'){
                    submitURL = `${process.env.VUE_APP_API_URL}/editProfile/removeModType`
                    submitData={
                        userID: this.displayUser.id,
                        removeModType: this.selectedRemoveType.drinkType,
                    }
                }
                if(this.chooseMod=='add'){
                    submitURL = `${process.env.VUE_APP_API_URL}/editProfile/updateModType`
                    submitData = {
                        userID: this.displayUser.id,
                        newModType: this.selectedPromotedType.drinkType,
                    }
                }
                await this.$axios.post(submitURL, submitData, {
                    headers: {
                        'Content-Type': 'application/json'
                    }
                }).then(response => {
                    // Handle the response here
                    if(response.data.code == 201){
                        if(this.chooseMod == 'remove'){
                            this.successRemoveMod = true
                            let modToDowngrade = this.displayUser.modType.findIndex(obj => obj === this.selectedRemoveType.drinkType);
                            if (modToDowngrade !== -1) {
                                this.displayUser.modType.splice(modToDowngrade, 1);
                            }
                            let currentMod = this.displayUser.modType
                            this.removableDrinkType = this.drinkTypes.filter(drinkType=>{
                                return currentMod.includes(drinkType.drinkType);
                            })
                            this.addableDrinkType = this.drinkTypes.filter(drinkType=>{
                                return !currentMod.includes(drinkType.drinkType);
                            })
                        }
                        if(this.chooseMod == 'add'){
                            this.successAddMod = true
                            this.confirmModerator = false
                            this.displayUser.modType.push(this.selectedPromotedType.drinkType)
                            let currentMod = this.displayUser.modType
                            this.removableDrinkType = this.drinkTypes.filter(drinkType=>{
                                return currentMod.includes(drinkType.drinkType);
                            })
                            this.addableDrinkType = this.drinkTypes.filter(drinkType=>{
                                return !currentMod.includes(drinkType.drinkType);
                            })
                                }
                            }
                });
            } catch (error) {
                console.error(error);
                if(this.chooseMod == 'add'){
                    this.errorAddMod = true
                }
                if(this.chooseMod == 'remove'){
                    this.errorRemoveMod = true
                }
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
            let oldHash = this.hashPassword(this.user.username, this.oldPassword)
            let newHash = this.hashPassword(this.user.username, this.newPassword)
            let submitURL = `${process.env.VUE_APP_API_URL}/authcheck/editPassword/` + this.user.id 
            let submitData = {
                oldHash: oldHash.toString(),
                newHash: newHash.toString(),
                userType: "user",
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
            // clear all message
            let sendPinSuccess = document.getElementById("sendPinSuccess")
            let sendPinError = document.getElementById("sendPinError")

            sendPinSuccess.innerHTML = ""
            sendPinError.innerHTML = ""
            this.verifyErrorMessage = ""

            // call api to send pin
            this.isButtonDisabled = true;
                setTimeout(() => {
                    this.isButtonDisabled = false;
                }, 60000);
            let submitURL = `${process.env.VUE_APP_API_URL}/authcheck/sendResetPin/` + this.user.id
            let submitData = {
                userType: "user",
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
                sendPinSuccess.innerHTML = "OTP has been sent!"
                sendPinError.innerHTML = ""
            }
            else{
                sendPinSuccess.innerHTML = ""
                sendPinError.innerHTML = "Error sending OTP, please try again in 60 seconds"
            }
        },

        async verifyOTP(){
            // remove trailing and leading spaces
            this.resetPin = this.resetPin.trim()

            // remove send pin messages
            let sendPinSuccess = document.getElementById("sendPinSuccess")
            sendPinSuccess.innerHTML = ""

            // call api to verify the pin
            let submitURL = `${process.env.VUE_APP_API_URL}/authcheck/verifyPin/` + this.user.id
            let submitData ={
                userType:"user",
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
            let submitURL = `${process.env.VUE_APP_API_URL}/authcheck/resetPassword/` + this.user.id
            let submitData = {
                userType:"user",
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
            this.pointSystem.tagLocation[0] = this.recentReviews.reduce((sum, review) => {
                if (review.location) {
                    return sum + 1;
                }
                return sum;
            }, 0);
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

    },
};
</script>