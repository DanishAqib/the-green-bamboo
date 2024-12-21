<!-- Component for submitting new listings (both requests + actual) -->
<!--
    formType: req (request), power (actual)
    formMode: new, edit, dup (duplicate)
-->

<!--
    TODO:
    - "Return" button may bring user back to same page, but with form cleared. Prevent that by returning to last notable page. (optional)
    - Consider another backend check to ensure that submitter is authorized to submit listing in specified mode, with valid producerID for producers.
    - Should we save the form data for easier retry when invoking reset()? Should reset() just hard refresh the page?
-->

<template>
    <div class="container pt-3">

        <!-- Display when data is still loading / form is being submitted -->
        <div class="text-info-emphasis fst-italic fw-bold fs-5" v-if="submitForm || !dataLoaded">
            <span v-if="!dataLoaded">Loading form, please wait...</span>
            <span v-if="submitForm">The form is being submitted, please hold on!</span>
            <br><br>
            <div class="spinner-border" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
        </div>
        
        <!-- Display when bottle listing is successfully submitted -->
        <div class="text-success fst-italic fw-bold fs-3" v-if="successSubmission"> 
            <div v-if="formType == 'req'">
                <span v-if="formMode == 'new'">The request has successfully been submitted!</span>
                <span v-if="formMode == 'edit'">The edit request has successfully been submitted!</span>
                <span v-if="formMode == 'dup'">The duplicate report has successfully been submitted!</span>
            </div>
            <div v-if="formType == 'power'">
                <span v-if="formMode == 'new' && requestRemoval == false">The bottle listing has successfully been created!</span>
                <span v-if="formMode == 'edit' && requestRemoval == false">The bottle listing has successfully been edited!</span>
                <span v-if="requestRemoval == true">The request has successfully been removed!</span>
            </div>
            <br>
            <button class="btn primary-btn btn-sm" @click="reset" v-if="formMode == 'new'">
                <span class="fs-5 fst-italic"> Submit another bottle listing here! </span>
            </button>
            <button class="btn primary-btn btn-sm" @click="goBack" v-if="formMode != 'new'">
                <span class="fs-5 fst-italic"> Return to previous page </span>
            </button>
            <router-link :to="'/request/view'" class="mx-1">
                <button class="btn primary-btn btn-sm">
                    <span class="fs-5 fst-italic"> View Requests </span>
                </button>
            </router-link>
            <router-link :to="'/'" class="mx-1">
                <button class="btn primary-btn btn-sm">
                    <span class="fs-5 fst-italic"> Go to Home page </span>
                </button>
            </router-link>
        </div>
        
        <!-- Display when bottle listing submission encounters an error -->
        <div class="text-danger fst-italic fw-bold fs-3" v-if="errorSubmission"> 
            <span v-if="errorMessage">An error occurred while attempting to submit, please try again!</span>
            <span v-if="invalidListing">Your request is not linked to a valid listing, please try again!</span>
            <span v-if="duplicateEntry">The bottle listing you are trying to submit already exists.</span>
            <br>
            <button class="btn primary-btn btn-sm" @click="reset">
                <span class="fs-5 fst-italic"> Retry your submission here! </span>
            </button>
        </div>

        <!-- Form Container -->
        <div class="row" v-if="fillForm">
            
            <!-- spacer -->
            <div class="col-xl-3 col-lg-2 col-md-1"></div>
            
            <!-- Main Form Area -->
            <div class="col-xl-6 col-lg-8 col-md-10">

                <!-- Form Title -->
                <div class="d-grid gap-2">
                    <div v-if="formType == 'req'">
                        <p class="fw-bold fs-1" v-if="formMode == 'new'">Request New Bottle Listing</p>
                        <p class="fw-bold fs-1" v-if="formMode == 'edit'">Propose Edit to Bottle Listing</p>
                        <p class="fw-bold fs-1" v-if="formMode == 'dup'">Report Duplicate Bottle Listing</p>
                    </div>
                    <div v-if="formType == 'power'">
                        <p class="fw-bold fs-1" v-if="formMode == 'new'">Create New Bottle Listing</p> 
                        <p class="fw-bold fs-1" v-if="formMode == 'edit'">Edit Bottle Listing</p>
                    </div>
                </div>
                
                <!-- [REQ EDIT/DUP] Show Linked Bottle Listing Information -->
                <div class="card mb-3 text-start" v-if="formType == 'req' && (formMode == 'edit' || formMode == 'dup')">
                    <div class="card-header fst-italic">
                        <span v-if="formMode == 'edit'">Proposing an edit to:</span>
                        <span v-if="formMode == 'dup'">Listing to be reported:</span>
                    </div>
                    <div class="card-body">
                        <div class="container">
                            <div class="row">
                                <!-- photo -->
                                <div class="col-4 image-container">
                                    <!-- <img :src=" 'data:image/jpeg;base64,' + ( targetListing.photo || defaultPhoto )" style="width: 200px; height: 200px;"> -->
                                    <img :src="( targetListing.photo || defaultPhoto )" style="width: 200px; height: 200px;">
                                </div>
                                <!-- other listing info -->
                                <div class="col-8 ps-5">
                                    <span class="card-title fw-bold fs-5">{{ targetListing.listingName }}</span>
                                    <br>
                                    <span class="card-text">{{ targetListing.drinkType }}<span v-if="targetListing.typeCategory"> / {{ targetListing.typeCategory }}</span></span>
                                    <br>
                                    <span class="card-text fst-italic">{{ targetListing.officialDesc }}</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="card-footer text-body-secondary">
                        <!-- Link to Bottle Listing Page -->
                        <!-- [RE-ROUTE FLAG] '/listing/view/' -->
                        <router-link :to="'/listing/view/' + this.$route.params.listingID" class="text-decoration-none">
                            <span>View Listing Details</span>
                        </router-link>
                    </div>
                </div>

                <!-- [POWER EDIT] Show Edit / Duplicate Request Information -->
                <div class="card mb-3 text-start" v-if="formType == 'power' && formMode == 'edit' && prevListing">
                    <div class="card-header fst-italic">
                        <span>Linked Request Information:</span>
                    </div>
                    <div class="card-body">
                        <span class="card-title fw-bold fs-5" v-if="modifyRequest['duplicateLink'].trim()">Duplicate Report</span>
                        <span class="card-title fw-bold fs-5" v-else>Suggested Edits</span>
                        <br>
                        <span class="card-text fst-italic">{{ modifyRequest.editDesc }}</span>
                    </div>
                    <div class="card-footer text-body-secondary">
                        <span v-if="modifyRequest['duplicateLink'].trim()">Duplicate Link: {{ modifyRequest.duplicateLink }}</span>
                        <span v-else>Source Link: {{ modifyRequest.sourceLink }}</span>
                    </div>
                </div>

                <!-- Form Fields -->
                <form v-on:submit.prevent="submitFunction" id="frm">

                    <!-- Form: Propose Edit / Report Duplicate -->
                    <div v-if="formType == 'req' && (formMode == 'edit' || formMode == 'dup')">
                        
                        <!-- [REQ EDIT/DUP] Input: Proposed Edits / Duplicate Report Information -->
                        <div class="form-group mb-3">
                            <p class="text-start mb-1" v-if="formMode == 'edit'">What edits do you propose? <span class="text-danger">*</span></p>
                            <p class="text-start mb-1" v-if="formMode == 'dup'">Reason for duplicate report: <span class="text-danger">*</span></p>
                            <textarea v-if="userType == 'user'" rows=3 class="form-control" v-model="form['editDesc']" id="editDesc" placeholder="Enter your comments..."></textarea>
                            <textarea v-if="userType == 'producer'" rows=1 class="form-control" placeholder="This listing is produced by my distillery." disabled></textarea>
                            <p class="text-start mt-1" v-if="userType == 'producer'">* For other edit suggestions, please ensure that you are logged in as a user</p>
                        </div>

                        <!-- [REQ EDIT] Input: Link to source -->
                        <div class="form-group mb-3" v-if="formMode == 'edit'">
                            <p class="text-start mb-1">Link to source, if applicable.</p>
                            <input type="text" class="form-control" v-model="form['sourceLink']" id="sourceLink" placeholder="Enter source link">
                        </div>

                        <!-- [REQ DUP] Input: Link to duplicate -->
                        <div class="form-group mb-3" v-if="formMode == 'dup'">
                            <p class="text-start mb-1">Link to duplicate listing <span class="text-danger">*</span></p>
                            <input type="text" class="form-control" v-model="form['duplicateLink']" id="duplicateLink" placeholder="Enter duplicate link">
                        </div>
                    </div>

                    <!-- Form: Listing Details -->
                    <div v-if="formType == 'power' || formMode == 'new'">

                        <!-- Input: Bottle Name -->
                        <div class="form-group mb-3">
                            <p class="text-start mb-1">Name of Bottle <span class="text-danger">*</span></p>
                            <input type="text" v-model="form['listingName']" class="form-control" id="bottleName" placeholder="Enter Bottle Name">
                        </div>

                        <!-- Input: drinkType (eg. Whiskey) + typeCategory (eg. Single Malt) -->
                        <div class="row">
                            <div class="col-md-6 mb-3">
                                <p class="text-start mb-1">Drink Type <span class="text-danger">*</span></p>
                                <div class="input-group">
                                    <select class="form-select" id="drinkTypeSelect" v-model="tempDrinkType" @change="getDrinkCategoryList">
                                        <option v-for="taste in drinkCategoriesList" :key="taste" :value="taste">
                                        {{ taste }}
                                        </option>
                                    </select>
                                </div>
                            </div>
                        
                            <div class="col-md-6 mb-3">
                                <p class="text-start mb-1">Drink Category</p>

                                <!-- For drink types that have serveral categories to choose from -->
                                <div class="input-group" v-if="tempTypeCategoryList.length > 1">
                                    <select class="form-select" id="inputGroupSelect01" v-model="tempTypeCategory">
                                        <option v-for="cat in tempTypeCategoryList.sort()" :key="cat" :value="cat" >
                                            {{ cat }}
                                        </option>
                                    </select>
                                </div>
                                
                                <!-- If there are no categories to select, display disabled dummy selection field -->
                                <div class="input-group" v-else>
                                    <select class="form-select" disabled>
                                        <option selected>-</option>
                                    </select>
                                </div>

                            </div>
                        </div>

                        <!-- [POWER] Input: Drink Description -->
                        <div class="form-group mb-3" v-if="formType == 'power'">
                            <p class="text-start mb-1">Official Description <span class="text-danger">*</span></p>
                            <textarea rows=3 class="form-control" v-model="form['officialDesc']" id="officialDesc" placeholder="Enter description of bottle"></textarea>
                        </div>

                        <!-- Input: Link to website or source (optional for actual listing, mandatory for request) -->
                        <div class="form-group mb-3">
                            <p class="text-start mb-1">Link to website or source <span class="text-danger" v-if="formType == 'req'">*</span></p>
                            <input type="text" class="form-control" v-model="form['sourceLink']" id="sourceLink" placeholder="Enter source link">
                        </div>

                        <!-- Input: Link to 88 Bamboo review -->
                        <div class="form-group mb-3">
                            <p class="text-start mb-1">Link to 88 Bamboo review</p>
                            <input type="text" class="form-control" v-model="form['reviewLink']" id="reviewLink" placeholder="Enter review link">
                        </div>

                        <!-- Input: Photo file -->
                        <div class="form-group mb-3">
                            <p class="text-start mb-1">Photo of bottle</p>
                            <button type="button" class="btn primary-btn btn-sm d-flex mb-1" @click="() => { this.form['photo'] = ''; this.selectedImage = '';}">Reset to Default Photo</button>
                            <!-- <img :src="'data:image/jpeg;base64,' + (this.form['photo'] || defaultPhoto)" class="rounded d-flex mb-3" alt="" style="width: 100px; height: 100px; object-fit: cover;"> -->
                            <img :src="selectedImage || (this.form['photo'] || defaultPhoto)" class="rounded d-flex mb-3" alt="" style="width: 100px; height: 100px; object-fit: cover;">
                            <input class="form-control" type="file" id="formFile" @change="handleFileSelect">
                        </div>

                        <!-- Input: Producer Name -->
                        <!-- [IF] Producer is creating listing, lock Producer selection -->
                        <div class="form-group mb-3" v-if="isProducer != false">
                            <p class="text-start mb-1">Producer Name <span class="text-danger">*</span></p>
                            <select class="form-select" disabled>
                                <option selected>{{ isProducer }}</option>
                            </select>
                        </div>
                        <!-- [ELSE] Dropdown menu tied to producerID, show producerNew textbox only if "Other" selected (no producerID). -->
                        <!-- set name only, then before submitting request, put the id, save computation -->
                        <div class="form-group mb-3" v-else>
                            <p class="text-start mb-1">New Producer Name <span class="text-danger">*</span></p>
                            <input list="producer-names" v-model="form['producerNew']" class="form-control" id="bottleName" placeholder="Enter Producer Name" @input="getProducerID">
                            <datalist id="producer-names">
                                <option v-for="producer in producerList" :key="producer.producerName" :value="producer.producerName">
                                    {{ producer.producerName }}
                                </option>
                            </datalist>
                        </div>

                        <!-- Input: Independent Bottler Check -->
                        <p class="text-start mb-1">Is this bottle by an independent bottler? <span class="text-danger">*</span></p>
                        <!-- Toggleable Switch -->
                        <div class="text-start mb-3">
                            <div class="form-check form-switch form-check-inline">
                                <input class="form-check-input" type="checkbox" role="switch" id="IBCheck" name="IBCheck" v-model="indOperator">
                                <label class="form-check-label" for="IBCheck" v-if="indOperator">Yes</label>
                                <label class="form-check-label" for="IBCheck" v-if="!indOperator">No</label>
                            </div>
                        </div>
                        <!-- (ONLY IF above toggled to "Yes") Input Text for Independent Bottler -->
                        <div class="form-group mb-3" v-if="indOperator">
                            <p class="text-start mb-1">If yes, who is the independent bottler? <span class="text-danger">*</span></p>
                            <input type="text" class="form-control" v-model="form['bottler']" :disabled="!indOperator" id="bottlerName" placeholder="Enter Bottler Name">
                        </div>

                        <!-- Input: Country of Origin -->
                        <div class="form-group mb-3">
                            <div class=" mb-3">
                                <p class="text-start mb-1">Country of Origin <span class="text-danger" v-if="formType == 'power'">*</span></p>
                                <div class="input-group">
                                    <select class="form-select" id="countrySelect" v-model="form['originCountry']">
                                        <option v-for="country in countries" :key="country" :value="country">
                                        {{ country }}
                                        </option>
                                    </select>
                                </div>
                            </div>
                        </div>

                        <!-- Input: Alcohol Strength (% ABV) + Alcohol Age / Vintage (years old / Year Bottled) -->
                        <div class="row mb-3">
                            <div class="form-group col-6">
                                <p class="text-start mb-1">Strength <span class="text-danger" v-if="formType == 'power'">*</span></p>
                                <div class="form-group row">
                                    <div class="col-6 pe-1">
                                        <input type="number" v-model="form['abv']" class="form-control" id="abv" min="0" max="100" step="0.1">
                                    </div>
                                    <label for="abv" class="col-6 col-form-label ps-1 text-start">% ABV</label>
                                </div>
                            </div>
                            <div class="form-group col-6">
                                <p class="text-start mb-1" v-if="tempDrinkType == 'Wine (Grape wine)'">Vintage (Year Bottled)</p>
                                <p class="text-start mb-1" v-else>Age</p>
                                <div class="form-group row">
                                    <div class="col-6 pe-1">
                                        <input type="number" v-model="form['age']" class="form-control" id="age" min="0">
                                    </div>
                                    <label for="age" class="col-6 col-form-label ps-1 text-start" v-if="tempDrinkType != 'Wine (Grape wine)'">years old</label>
                                </div>
                            </div>
                        </div>

                    </div>

                    <!-- [REQ] Input: Relationship with Brand -->
                    <p class="text-start mb-1" v-if="formType == 'req'">Your Relationship with the Brand <span class="text-danger">*</span></p>
                    <div class="text-start mb-3" v-if="formType == 'req'">
                        <div class="form-check form-check-inline" v-if="userType == 'user'">
                            <input class="form-check-input" type="radio" v-model="form['brandRelation']" :value="'Customer'" name="brandRelationCustomer" id="brandRelationCustomer">
                            <label class="form-check-label" for="brandRelationCustomer">Customer</label>
                        </div>
                        <div class="form-check form-check-inline">
                            <input class="form-check-input" type="radio" v-model="form['brandRelation']" :value="'Employee'" name="brandRelationEmployee" id="brandRelationEmployee">
                            <label class="form-check-label" for="brandRelationEmployee">Employee</label>
                        </div>
                        <div class="form-check form-check-inline" v-if="userType == 'user'">
                            <input class="form-check-input" type="radio" v-model="form['brandRelation']" :value="'Public Relations'" name="brandRelationPR" id="brandRelationPR">
                            <label class="form-check-label" for="brandRelationPR">Public Relations</label>
                        </div>
                        <div class="form-check form-check-inline" v-if="userType == 'user'">
                            <input class="form-check-input" type="radio" v-model="form['brandRelation']" :value="'Distributor'" name="brandRelationDist" id="brandRelationDist">
                            <label class="form-check-label" for="brandRelationDist">Distributor</label>
                        </div>
                        <div class="form-check form-check-inline" v-if="userType == 'user'">
                            <input class="form-check-input" type="radio" v-model="form['brandRelation']" :value="'Others'" name="brandRelationOther" id="brandRelationOther">
                            <label class="form-check-label" for="brandRelationOther">Others</label>
                        </div>
                    </div>

                    <!-- Error Handling -->
                    <div v-if="errors.length > 0">
                        <div class="alert alert-danger" role="alert">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-exclamation-triangle" viewBox="0 0 16 16">
                            <path d="M7.938 2.016A.13.13 0 0 1 8.002 2a.13.13 0 0 1 .063.016.146.146 0 0 1 .054.057l6.857 11.667c.036.06.035.124.002.183a.163.163 0 0 1-.054.06.116.116 0 0 1-.066.017H1.146a.115.115 0 0 1-.066-.017.163.163 0 0 1-.054-.06.176.176 0 0 1 .002-.183L7.884 2.073a.147.147 0 0 1 .054-.057zm1.044-.45a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566z"/>
                            <path d="M7.002 12a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 5.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995z"/>
                            </svg>
                            <h5> Error </h5>
                            <li v-for="error in errors" :key="error"> {{ error }} </li>
                        </div>
                    </div>
                    
                    <!-- Submission Buttons -->
                    <div v-if="formType == 'req'">
                        <button type="button" class="btn btn-secondary mx-1 mb-3" @click="goBack">Return</button>
                        <button type="submit" class="btn primary-square-btn-green mx-1 mb-3" v-if="formMode == 'new'">Submit Listing Request</button>  <!--tzh added -green-->
                        <button type="submit" class="btn primary-square-btn-green mx-1 mb-3" v-if="formMode == 'edit'">Submit Edit Request</button> <!--tzh added -green-->
                        <button type="submit" class="btn primary-square-btn-green mx-1 mb-3" v-if="formMode == 'dup'">Submit Duplicate Report</button> <!--tzh added -green-->
                        
                    </div>
                    <div v-if="formType == 'power'">
                        <button type="button" class="btn btn-secondary mx-1 mb-3" @click="goBack">Return</button>
                        <button type="submit" class="btn primary-square-btn-green mx-1 mb-3" v-if="formMode == 'new'">Create New Listing</button>  <!--tzh changed secondary-btn to primary-square-btn-green-->
                        <button type="submit" class="btn primary-square-btn-green mx-1 mb-3" v-if="formMode == 'edit'">Save Listing Edits</button> <!--tzh changed secondary-btn to primary-square-btn-green-->

                        <button type="button" class="btn btn-danger rounded-pill mx-1 mb-3" v-if="prevListing" @click="updateRequestStatus('reject')">Reject Request</button>
                        
                    </div>
                
                </form>

            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "SubmitListingNew",
        props: {
            formType: String,
            formMode: String
        },
        data () {
            return {
                // Default Photo

                defaultPhoto: "https://drinkximages.s3.us-east-1.amazonaws.com/images/2d4d94bc-313e-4621-9a15-4bfbf77958de.jpg",
                // User
                userType: "",
                // Flags
                dataLoaded: false,
                submitForm: false,
                successSubmission: false,
                errorSubmission: false,
                fillForm: false,
                requestRemoval: false,

                // Error-specific flags
                errorMessage: false,
                invalidListing: false,
                duplicateEntry: false,
                errors: [],

                // Pre-loaded data
                targetListing: {},
                isProducer: false,
                prevListing: false,
                modifyRequest: {},
                types: [],

                // Form model variables
                tempDrinkType: "",
                tempTypeCategory: "",
                tempProducer: "",
                indOperator: true,

                // Form data variables
                drinkCategories: [],
                drinkCategoriesList: [],
                tempTypeCategoryList: [],
                producerList: [],
                countries: [],
                selectedImage:"",

                form: {
                    "editDesc": "",
                    "sourceLink": "",
                    "duplicateLink": "",
                    "listingName": "",
                    "officialDesc": "",
                    "reviewLink": "",
                    "producerNew": "", // mutually exclusive with producerID  (exactly one of them will be blank)
                    "bottler": "",
                    "originCountry": "",
                    "abv": "",
                    "age": "",
                    "brandRelation": "Others",

                    "userID": "",
                    "producerID": "", // mutually exclusive with producerNew (exactly one of them will be blank)
                    "listingID": "",
                    "photo": "",
                },
            };
        },
        mounted() {

            // Get userID
            this.form['userID'] = localStorage.getItem('88B_accID');
            this.userType = localStorage.getItem('88B_accType');
            if (this.userType == "producer") {
                this.form.brandRelation = "Employee"
                this.form.editDesc = "This listing is produced by my distillery."
            }

            // Check if route params "requestID" is present
            if (this.$route.params.requestID != "" && this.$route.params.requestID != undefined) {
                this.prevListing = true;
            }

            // Power user check
            if (this.formType == "power") {
                this.checkPower();
            } else {
                // Load data
                this.loadData();
            }
        },
        methods:{
            // Function to check if user is a power user
            async checkPower() {
                let powerValid = false;

                // Check if user is a producer
                if (localStorage.getItem('88B_accType') == "producer") {
                    powerValid = true;
                }
                // If user is a user, check power
                else if (localStorage.getItem('88B_accType') == "user") {
                    try {
                        const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getUser/` + this.form['userID']);
                        if (Array.isArray(response.data) && response.data.length == 0) {
                            throw "User not found!";
                        }
                        this.types = response.data["modType"];

                        // Check for data deformation - reject if non-array type is found
                        if (Array.isArray(this.types) == false) {
                            this.types = [];
                        }

                        if (this.types.length > 0) {
                            powerValid = true;
                        }
                        if (response.data["isAdmin"] == true) {
                            this.types = [];
                            powerValid = true;
                        }
                    } 
                    catch (error) {
                        console.error(error);
                    }
                }

                // Resolve power check
                if (powerValid) {
                    this.loadData();
                } else {
                    alert("This page is only accessible to producers and power users! Please log in as a producer or power user to access this page.")
                    this.$router.push({path: '/login'});
                }
            },
            
            // Function to load form data
            async loadData(){

                // Only run when listing detail form is required
                if (this.formType == "power" || this.formMode == "new") {

                    // populate "countries" form data variable
                    try {
                        const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getCountries`);
                        for (let country of response.data) {
                            this.countries.push(country.originCountry);
                        }
                        this.countries = this.countries.sort();
                    } 
                    catch (error) {
                        console.error(error);
                    }

                    // populate "drinkCategories" + "drinkCategoriesList" form data variable
                    try {
                        const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getDrinkTypes`);
                        this.drinkCategories = response.data;
                        for (let drink of this.drinkCategories) {
                            if (this.types.length === 0 || this.types.includes(drink.drinkType)) {
                                this.drinkCategoriesList.push(drink.drinkType);
                            }
                        }
                        this.drinkCategoriesList = this.drinkCategoriesList.sort();
                    } 
                    catch (error) {
                        console.error(error);
                    }

                    // populate "producerList" form data variable
                    try {
                        const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getProducers`);
                        this.producerList = response.data;
                        this.producerList.sort((a,b)=>{
                            return a.producerName.localeCompare(b.producerName)
                        })
                        // Check if user is a producer
                        if (localStorage.getItem('88B_accType') == "producer") {
                            this.isProducer = this.producerList.find(producer => producer.id == this.form['userID']).producerName;
                            this.form['producerID'] = this.form['userID'];
                        }
                    } 
                    catch (error) {
                        console.error(error);
                    }

                }
                // Only run when editing listing / proposing edit / reporting duplicate (listingID is present in route params)
                if (this.formMode == "edit" || this.formMode == "dup") {
                    this.form["listingID"] = this.$route.params.listingID;

                    // Get target listing
                    try {
                        const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getListing/` + this.$route.params.listingID);
                        if (Array.isArray(response.data) && response.data.length == 0) {
                            throw "Listing not found!";
                        }
                        this.targetListing = response.data;

                        if (this.formType == "power") {
                            this.populateForm(this.targetListing);
                            this.form["officialDesc"] = this.targetListing.officialDesc;
                        }
                    } 
                    catch (error) {
                        console.error(error);
                    }
                }

                // Only run when route params "requestID" is present (modifying previously submitted request / auto-filling form with request data)
                if (this.prevListing) {

                    // [REQ / POWER NEW] Retrieve previously submitted new listing request data
                    if (this.formMode == "new") {
                        try {
                            const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getRequestListing/` + this.$route.params.requestID);
                            if (Array.isArray(response.data) && response.data.length == 0) {
                                throw "Request not found!";
                            }
                            let previousData = await response.data;
                            this.checkUserPermissions(previousData);

                            // If user is a producer, check if request producerID is the same as user producerID
                            if (this.isProducer != false) {
                                if (previousData.producerID != this.form['userID']) {
                                    alert("This request is specified for a different producer!");
                                    this.$router.go(-1);
                                }
                            }

                            this.populateForm(previousData);
                            this.form["brandRelation"] = previousData.brandRelation;
                        }
                        catch (error) {
                            console.error(error);
                        }
                    }

                    // [REQ EDIT/DUP + POWER EDIT] Retrieve previously submitted request edit/duplicate data
                    if (this.formMode == "edit" || this.formMode == "dup") {
                        try {
                            const response = await this.$axios.get(`${process.env.VUE_APP_API_URL}/getData/getRequestEdit/` + this.$route.params.requestID);
                            if (Array.isArray(response.data) && response.data.length == 0) {
                                throw "Request not found!";
                            }
                            let previousData = response.data;
                            this.checkUserPermissions(previousData);

                            // For request mode
                            if (this.formType == "req") {

                                // If set to duplicate mode, but duplicate link is not present, redirect to edit mode
                                if (this.formMode == "dup" && !previousData["duplicateLink"].trim()) {
                                    alert("This request is not a duplicate report!\nRedirecting to edit mode...\nNOTE: Please reload the page after redirection.");
                                    // [RE-ROUTE FLAG] this.$router.replace({path: '/request/modify/edit/' + this.$route.params.listingID + '/' + this.$route.params.requestID});
                                    this.$router.replace({path: '/request/modify/edit/' + this.$route.params.listingID + '/' + this.$route.params.requestID});
                                }

                                // If set to edit mode, but duplicate link is present, redirect to duplicate mode
                                if (this.formMode == "edit" && previousData["duplicateLink"].trim()) {
                                    alert("This request is not a proposed edit!\nRedirecting to duplicate mode...\nNOTE: Please reload the page after redirection.");
                                    // [RE-ROUTE FLAG] this.$router.replace({path: '/request/modify/duplicate/' + this.$route.params.listingID + '/' + this.$route.params.requestID});
                                    this.$router.replace({path: '/request/modify/duplicate/' + this.$route.params.listingID + '/' + this.$route.params.requestID});
                                }

                                // Fill form with previous data
                                this.form['listingID'] = previousData['listingID'];
                                this.form['editDesc'] = previousData['editDesc'];
                                this.form['sourceLink'] = previousData['sourceLink'];
                                this.form['duplicateLink'] = previousData['duplicateLink'];
                                this.form['brandRelation'] = previousData['brandRelation'];
                                
                            }

                            // For actual listing mode
                            if (this.formType == "power") {

                                // Check if retrieved request is for the correct listing
                                if (previousData.listingID != this.$route.params.listingID) {
                                    alert("The linked request is not for the linked listing!\nRemoving request link...");
                                    // [RE-ROUTE FLAG] this.$router.push({path: '/listing/edit/' + this.$route.params.listingID});
                                    this.$router.push({path: '/listing/edit/' + this.$route.params.listingID});
                                }

                                this.modifyRequest = previousData;
                            }
                        }
                        catch (error) {
                            console.error(error);
                        }
                    }
                }

                this.dataLoaded = true;
                this.fillForm = true;
            },
            // Function to check user editing permissions
            checkUserPermissions(checkData) {
                if (this.formType == "req") {
                    // Check if user is the owner of the request
                    if (checkData.userID != this.form['userID']) {
                        alert("You can only edit requests that you have submitted!");
                        this.$router.go(-1);
                    }

                    // Check if request is already reviewed
                    if (checkData.reviewStatus != false) {
                        alert("Your request is already under review, and can no longer be edited!\nPlease submit a new request!");
                        this.$router.go(-1);
                    }
                }
            },
            // Function to populate form with previous data
            populateForm(previousData) {
                
                this.tempDrinkType = previousData.drinkType;
                this.getDrinkCategoryList();
                this.tempTypeCategory = previousData.typeCategory;

                this.form["sourceLink"] = previousData.sourceLink;
                this.form["listingName"] = previousData.listingName;
                this.form["reviewLink"] = previousData.reviewLink;
                this.form["originCountry"] = previousData.originCountry;
                this.form["producerID"] = previousData.producerID;
                this.form["photo"] = previousData.photo;

                // Check if producerID is blank
                if (this.form["producerID"] == "" || this.form["producerID"] == null) {
                    this.form["producerNew"] = previousData.producerNew;
                    // The code below... is it necessary?
                    if (this.formMode != "new") {
                        if (this.formType == "req") {
                            // In request mode, fill in producerNew
                            this.form["producerNew"] = previousData.producerNew;
                            this.tempProducer = "Other";
                        } else if (this.formType == "power") {
                            // In actual listing mode, fill in tempProducer
                            this.tempProducer = previousData.producerNew;
                        }
                    }
                } else {
                    this.form["producerNew"] = this.producerList.find(producer => producer.id == previousData.producerID).producerName;
                }

                // If independent bottler, fill in bottler
                if (previousData.bottler != "OB") {
                    this.indOperator = true;
                    this.form["bottler"] = previousData.bottler;
                } else {
                    this.indOperator = false;
                }

                // If abv has % sign, remove it. Change abv to number.
                if (toString(previousData.abv).includes("%")) {
                    this.form["abv"] = parseFloat(previousData.abv.slice(0, -1));
                } else {
                    this.form["abv"] = previousData.abv;
                }

                // If age has value, change age to number.
                if (previousData.age) {
                    this.form["age"] = parseInt(previousData.age);
                }
            },

            // Helper function to reset form (by refreshing page)
            reset(){
                if (this.successSubmission == true && this.prevListing == true) {
                    // Remove requestID router param from current path
                    let newPath = this.$route.path.split("/").slice(0, -1).join("/");
                    window.location.replace(newPath);
                }
                else {
                    this.$router.go(0);
                }
            },
            // Helper function to return to previous page
            goBack() {
                this.$router.go(-1)
            },
            // Helper function to get drink category list for selected drink type ("tempDrinkType")
            getDrinkCategoryList() {
                this.tempTypeCategoryList = this.drinkCategories.find(cat => cat.drinkType == this.tempDrinkType).typeCategory;
                this.tempTypeCategory = "";
            },
            // Helper function to handle file selection for photo
            handleFileSelect(event){
                try {
                    const file = event.target.files[0];
                    const reader = new FileReader;
                    
                    reader.onload = () => {
                        this.selectedImage = reader.result
                        const base64String = reader.result.split(',')[1];
                        this.form["photo"] = base64String
                    };
                    
                    reader.readAsDataURL(file);
                }
                catch (error) {
                    // console.error(error);
                }
            },
            // Helper function to get producerID from tempProducer
            getProducerID() {
                let producer = this.producerList.find(producer => producer.producerName == this.form['producerNew'])
                if (producer) {
                    this.form['producerID'] = producer.id;
                }
                else {
                    this.form['producerID'] = ""
                }
            },

            // Function to submit form
            async submitFunction(){
                this.errors = [];
                
                // Form Validation for Edit/Duplicate Request
                if (this.formType == "req" && (this.formMode == "edit" || this.formMode == "dup")) {

                    // Validate Edit Description
                    if (!this.form["editDesc"].trim()) {
                        this.errors.push("Please enter your comments.");
                    }

                    // Validate Duplicate Link
                    if (this.formMode == "dup" && !this.form["duplicateLink"].trim()) {
                        this.errors.push("Please enter the duplicate listing link.");
                    }
                }
                // Form Validation for Listing Details
                else {

                    // Validate Bottle Name
                    if (!this.form["listingName"].trim()) {
                        this.errors.push("Bottle Name is required.");
                    }

                    // Validate Drink Type
                    if (!this.tempDrinkType.trim()) {
                        this.errors.push("Drink Type is required.");
                    }

                    // Validate Independent Bottler Name (if OB, will be handled by database writing method)
                    if (!this.form["bottler"].trim() && this.indOperator == true) {
                        this.errors.push("Name of independent bottler is required.");
                    }

                    // Validation ONLY FOR REQUEST
                    if (this.formType == "req") {

                        // Validate Source Link
                        if (!this.form["sourceLink"].trim()) {
                            this.errors.push("Link to website or source is required.");
                        }

                        // Validate Producer Name
                        if (this.form['producerID']) {
                            // If producerID is blank, check if producerNew is blank
                            if (!this.form["producerNew"]) {
                                this.errors.push("Producer Name is required.");
                            }
                        } else {
                            // Check if producerNew is blank
                            if (!this.form["producerNew"].trim()) {
                                this.errors.push("Producer Name is required.");
                            }
                        }

                    }

                    // Validation ONLY FOR ACTUAL LISTING
                    if (this.formType == "power") {

                        // Validate Official Description
                        if (!this.form["officialDesc"] || !this.form["officialDesc"].trim()) {
                            this.errors.push("Official Description is required.");
                        }

                        // Validate Producer ID
                        if (!this.form["producerID"]) {
                            this.errors.push("Producer ID is required: Create new producer first!");
                        }

                        // Validate Country of Origin
                        if (!this.form["originCountry"].trim()) {
                            this.errors.push("Country of Origin is required.");
                        }

                        // Validate Alcohol Strength (% ABV)
                        if (!this.form["abv"].toString().trim()) {
                            this.errors.push("Alcohol Strength is required.");
                        }
                        
                    }
                    
                }

                if (this.errors.length > 0) {
                    // If errors, alert user and return
                    return "Submission Incomplete"
                } else {
                    // If no errors, pass corresponding API into database writing method
                    let submitAPI = ""
                    let submitData = {}
                    
                    // Request Listing Mode
                    if (this.formType == "req") {

                        // Request Creation Mode
                        if (this.formMode == "new") {
                            submitAPI = `${process.env.VUE_APP_API_URL}/requestListing/requestListing`
                            submitData = {
                                "sourceLink": this.form["sourceLink"].trim(),
                                "listingName": this.form["listingName"].trim(),
                                "reviewLink": this.form["reviewLink"].trim(),
                                "producerNew": this.form["producerNew"].trim(),
                                "bottler": this.form["bottler"].trim(),
                                "originCountry": this.form["originCountry"].trim(),
                                "abv": this.form["abv"].toString().trim(),
                                "age": this.form["age"].toString().trim(),
                                "brandRelation": this.form["brandRelation"],

                                "userID": this.form["userID"],
                                "producerID": this.form["producerID"],
                                "photo": this.form["photo"],

                                "drinkType": this.tempDrinkType.trim(),
                                "typeCategory": this.tempTypeCategory.trim(),
                                "reviewStatus": false,
                            }

                            if (this.prevListing) {
                                submitAPI = `${process.env.VUE_APP_API_URL}/requestListing/requestListingModify/` + this.$route.params.requestID
                            }
                        }

                        // Request Edit / Duplicate Mode
                        else if (this.formMode == "edit" || this.formMode == "dup") {
                            submitAPI = `${process.env.VUE_APP_API_URL}/requestListing/requestEdits`
                            submitData = {
                                "editDesc": this.form["editDesc"].trim(),
                                "sourceLink": this.form["sourceLink"].trim(),
                                "duplicateLink": this.form["duplicateLink"].trim(),
                                "brandRelation": this.form["brandRelation"],

                                "userID": this.form["userID"],
                                "listingID": this.form["listingID"],
                                "reviewStatus": false,
                            }

                            if (this.prevListing) {
                                submitAPI = `${process.env.VUE_APP_API_URL}/requestListing/requestEditsModify/` + this.$route.params.requestID;
                            }
                        }

                        else {
                            // Catching statement for invalid mode
                            alert("There was an issue with submission. Try to reopen the page after saving your inputs!")
                            return "Invalid Mode"
                        }

                    } else if (this.formType == "power") {

                        submitData = {
                            "sourceLink": this.form["sourceLink"].trim(),
                            "listingName": this.form["listingName"].trim(),
                            "officialDesc": this.form["officialDesc"].trim(),
                            "reviewLink": this.form["reviewLink"].trim(),
                            "bottler": this.form["bottler"].trim(),
                            "originCountry": this.form["originCountry"].trim(),
                            "abv": this.form["abv"].toString().trim(),
                            "age": this.form["age"].toString().trim(),
                            
                            "producerID": this.form["producerID"],
                            "photo": this.form["photo"],

                            "drinkType": this.tempDrinkType.trim(),
                            "typeCategory": this.tempTypeCategory.trim(),
                        }

                        // Listing Creation Mode
                        if (this.formMode == "new") {
                            submitAPI = `${process.env.VUE_APP_API_URL}/createListing/createListing`
                        }

                        // Listing Edit Mode
                        else if (this.formMode == "edit") {
                            submitAPI = `${process.env.VUE_APP_API_URL}/editListing/updateListing/` + this.$route.params.listingID
                        }

                        else {
                            // Catching statement for invalid mode
                            alert("There was an issue with submission. Try to reopen the page after saving your inputs!")
                            return "Invalid Mode"
                        }

                    } else {
                        // Catching statement for invalid mode
                        alert("There was an issue with submission. Try to reopen the page after saving your inputs!")
                        return "Invalid Mode"
                    }

                    if (this.formType == "power" || this.formMode == "new") {
                        // If not independent bottler, set bottler to "OB"
                        if (this.indOperator == false) {
                            submitData["bottler"] = "OB"
                        }

                        // If abv has value, add % sign
                        if (submitData["abv"]) {
                            submitData["abv"] = submitData["abv"].toString() + "%"
                        }
                    }

                    // Update request status
                    if (this.prevListing && this.formType == "power") {
                        this.updateRequestStatus("approve")
                    }

                    this.writeListing(submitAPI, submitData)
                }
            },

            // Function to write listing to database
            async writeListing(submitAPI, submitData) {

                this.fillForm = false; // Hide form
                this.submitForm = true; // Display submission in progress message
                let responseCode = "";

                const response = await this.$axios.post(submitAPI, submitData)
                .then((response)=>{
                    responseCode = response.data.code
                })
                .catch((error)=>{
                    responseCode = error.response.data.code
                });

                // [Replace with Backend Fix] Response Code Transformation for Edit Listing
                if (this.formType == "power" && this.formMode == "edit") {
                    if (responseCode == 200) {
                        responseCode = 201
                    }
                    if (responseCode == 420 || responseCode == 440) {
                        responseCode = 400
                    }
                }
                
                if (responseCode == 201) {
                    this.successSubmission = true; // Display success message
                    this.submitForm = false; // Hide submission in progress message
                } else {
                    this.errorSubmission = true; // Display error message
                    this.submitForm = false; // Hide submission in progress message
                    
                    if (responseCode == 400) {
                        if (this.formMode == "new") {
                            this.duplicateEntry = true // Display duplicate entry message
                        } else {
                            this.invalidListing = true // Display invalid listing error message
                        }
                    } else if (responseCode == 410) {
                        this.duplicateEntry = true // Display duplicate entry message
                    } else {
                        this.errorMessage = true // Display generic error message
                    }
                }
                return response
            },

            // Function to update request status
            async updateRequestStatus(status) {

                let responseCode = "";
                let submitAPI = `${process.env.VUE_APP_API_URL}/requestListing/requestReviewStatus/` + this.$route.params.requestID;
                let submitData = {};

                // Set up submission data
                if (this.formMode == "new") {
                    submitData = {
                        "targetCollection": "requestListings",
                        "reviewStatus": false,
                    }
                }
                else if (this.formMode == "edit") {
                    submitData = {
                        "targetCollection": "requestEdits",
                        "reviewStatus": false,
                    }
                }
                else {
                    // Catching statement for invalid mode
                    alert("There was an issue with submission. Try to reopen the page after saving your inputs!")
                    return "Invalid Mode"
                }

                // Set new review status
                if (status == "reject") {

                    this.fillForm = false; // Hide form
                    this.submitForm = true; // Display submission in progress message
                    submitData["reviewStatus"] = null;

                }
                else if (status == "approve") {
                    submitData["reviewStatus"] = true;
                }

                const response = await this.$axios.post(submitAPI, submitData)
                .then((response)=>{
                    responseCode = response.data.code
                })
                .catch((error)=>{
                    responseCode = error.response.data.code
                });
                
                if (responseCode == 201) {
                    if (status == "reject") {
                        this.successSubmission = true; // Display success message
                        this.requestRemoval = true; // Display request removal message
                        this.submitForm = false; // Hide submission in progress message
                    }
                } else {
                    this.errorSubmission = true; // Display error message
                    this.fillForm = false; // Hide form
                    this.submitForm = false; // Hide submission in progress message
                    this.errorMessage = true // Display generic error message
                }
                return response

            },

        }
    }
</script>