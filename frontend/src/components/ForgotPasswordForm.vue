<template>
    <div>
        <!-- Header -->
        <h1>Reset Password</h1>

        <!-- Instructions -->
        <p class="px-5 pt-3">Please enter your email to get the One Time Pin (OTP) to reset your password. Do note that the OTP is only valid for an hour.</p>



        <!-- 1st Stage: Input box to fill in email -->
        <input type="text" v-if="resetStage == 'email'" v-model="email" placeholder="Enter your email here" class="rounded p-2" required>
        <!-- Error message if email is not in valid format -->
        <p v-if="email.length > 0 && !emailIsValid" class="text-danger">Please enter a valid email address</p>
        <!-- Error message if email is not valid -->
        <p v-if="resetStage == 'email' && userNotFound" class="text-danger">User not found</p>
        <!-- Error message if sending email encounters error -->
        <p v-if="resetStage == 'email' && sendPinError" class="text-danger">{{sendPinError}}</p>
        <!-- Success message if OTP is sent -->
        <p v-if="resetStage == 'otp' && sendPinSuccess" class="text-success">{{sendPinSuccess}}</p>



        <!-- 2nd Stage: Input box to enter OTP -->
        <input type="text" v-if="resetStage == 'otp'" v-model="resetPin" placeholder="Enter OTP here" class="rounded p-2" required>
        <!-- Error message if OTP is wrong, expired or encounter error -->
        <p v-if="resetStage == 'otp' && verifyErrorMessage" class="text-danger">{{verifyErrorMessage}}</p>



        <!-- 3rd Stage: Input boxes to enter new password -->
        New password: <br>
        <input type="password" v-if="resetStage == 'password'" v-model="newPassword" placeholder="Enter new password" class="rounded p-2" required> <br>
        Confirm new password: <br>
        <input type="password" v-if="resetStage == 'password'" v-model="confirmPassword" placeholder="Confirm new password" class="rounded p-2" required>
        <!-- Loading message -->
        <!-- Error message if both password do not match -->
        <p v-if="resetStage == 'password' && newPassword != confirmPassword" class="text-danger">Passwords do not match</p>
        <!-- Success message -->
        <p v-if="resetStage == 'password' && resetSuccessMsg" class="text-success">{{resetSuccessMsg}}</p>



        <div class="d-flex justify-content-center align-items-center gap-3 py-3">
            <!-- Cancel Button to return to login page -->
            <button @click="returnToLogin" class="btn btn-link text-decoration-none text-black hover-text">Cancel</button>

            <!-- Button to send OTP and reset password-->
            <button v-if="resetStage == 'email'" @click="checkUser" :disabled="isButtonDisabled" class="btn secondary-btn-border-thick btn-md px-3">Send OTP</button>

            <!-- Button to verify OTP -->
            <button v-if="resetStage == 'otp'" @click="verifyOTP" class="btn secondary-btn-border-thick btn-md px-3">Verify OTP</button>

            <!-- Button to reset password -->
            <button v-if="resetStage == 'password' && newPassword == confirmPassword" @click="resetPassword" :disabled="isButtonDisabled" class="btn secondary-btn-border-thick btn-md px-3">Reset Password</button>
        </div>
    </div>  

</template>

<style scoped>
/* !important is used to override the default bootstrap styling */
.hover-text:hover {
    text-decoration: underline !important;
    color: #0d6efd !important;
}
</style>

<script>

export default {
    data() {

        return {
            isButtonDisabled: false,
            resetStage: "email", // 3 stages in chronological order: email, otp, password

            // email stage variables
            email: "",
            id: null,
            userType: null,
            userName: null,
            userNotFound: false,

            // otp stage variables
            sendPinSuccess: "",
            sendPinError: "",
            resetPin: "",
            verifyErrorMessage: "",
            

            // password stage variables
            newPassword: "",
            confirmPassword: "",
            resetSuccessMsg: "",

        }
    },
    computed: {
        // Computed property to check if email is valid
        emailIsValid() {
            return this.email.match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/);
        },
    },

    methods: {
        // Function to check if user exists and retrieve the user id, f user exists, call the sendResetPin function
        async checkUser(){
            // call api to check if user exists
            let submitURL = `${process.env.VUE_APP_API_URL}/getData/getUserByEmail/` + this.email
            await this.$axios.get(submitURL)
                .then((response)=>{
                    this.id = response.data.id
                    this.userType = response.data.type
                    this.userName = response.data.username

                    this.resetStage = "otp"
                    // If user exists, send Reset Pin
                    this.sendResetPin()
                })
                .catch((error)=>{
                    console.error(error);
                    this.userNotFound = true
                });
        },

        // Function to send reset pin after user enters email
        async sendResetPin(){
            // call api to send pin
            this.isButtonDisabled = true;
                setTimeout(() => {
                    this.isButtonDisabled = false;
                }, 60000);
            let submitURL = `${process.env.VUE_APP_API_URL}/authcheck/sendResetPin/` + this.id
            let submitData = {
                userType: this.userType,
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
                this.sendPinSuccess = "OTP has been sent!"
            }
            else{
                this.sendPinError = "Error sending OTP, please try again in 60 seconds"
                this.resetStage = "email"
            }
        },

        // Function to verify OTP
        async verifyOTP(){
            // call api to verify the pin
            let submitURL = `${process.env.VUE_APP_API_URL}/authcheck/verifyPin/` + this.id
            let submitData ={
                userType:this.userType,
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
                this.resetStage = "password"
                this.verifyErrorMessage = ""
                this.isButtonDisabled = false;
            }
            else if(responseCode == 400){
                this.verifyErrorMessage = "OTP is wrong or expired."
            }else{
                this.verifyErrorMessage = "An error verifying the OTP. Please resend OTP or try again."
            }
        },

        // Function to reset password
        async resetPassword(){

            // Check if both passwords match
            if(this.newPassword != this.confirmPassword){
                return
            }

            // Disable button to prevent multiple clicks
            this.isButtonDisabled = true;

            // call api to reset password
            let submitURL = `${process.env.VUE_APP_API_URL}/authcheck/resetPasswordLogin`
            let submitData ={
                id:this.id,
                username:this.userName,
                userType:this.userType,
                password:this.confirmPassword
            }

            await this.$axios.post(submitURL,submitData)
                .then((response)=>{
                    this.resetSuccessMsg = response.data.message

                    // Wait for 3 seconds before returning to login page
                    setTimeout(() => {
                        this.returnToLogin()
                    }, 5000);
                })
                .catch((error)=>{
                    console.error(error);
                });
        },

        // Function to return to login page
        returnToLogin() {
            this.$emit('returnToLogin', true);  // Correct syntax for emitting the event
        }
    },
};
</script>