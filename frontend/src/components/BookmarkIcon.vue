<!-- Component for drinks display. Used in all profile pages. -->

<!-- Include this code in script tag of the parent component  

handleIconClick(data) {
    this.bookmarkListingID = data
},

 -->

<template>
    <!-- CP edits: added v-if div to ensure when public user click on bookmark icon, it does not throw out an error.-->
    <div v-if="user">
        <svg v-if="checkBookmarkStatus(listing.id)" xmlns="http://www.w3.org/2000/svg" :width="size" :height="size" fill="#83A9E8" class="bi bi-bookmark-fill" :class="{ 'overlay-icon': overlay }" viewBox="0 0 16 16"
            data-bs-toggle="modal" data-bs-target="#bookmarkModal" @click="iconClicked"> <!--tzh changed currentColor to 83A9E8-->
            <path d="M2 2v13.5a.5.5 0 0 0 .74.439L8 13.069l5.26 2.87A.5.5 0 0 0 14 15.5V2a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2"/>
        </svg>
        <svg v-else xmlns="http://www.w3.org/2000/svg" :width="size" :height="size" fill="#83A9E8" class="bi bi-bookmark" :class="{ 'overlay-icon': overlay }" viewBox="0 0 16 16"
            data-bs-toggle="modal" data-bs-target="#bookmarkModal" @click="iconClicked">
            <path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.777.416L8 13.101l-5.223 2.815A.5.5 0 0 1 2 15.5zm2-1a1 1 0 0 0-1 1v12.566l4.723-2.482a.5.5 0 0 1 .554 0L13 14.566V2a1 1 0 0 0-1-1z"/>
        </svg>
    </div>

    <div v-else>
        <svg xmlns="http://www.w3.org/2000/svg" :width="size" :height="size" fill="currentColor" class="bi bi-bookmark" :class="{ 'overlay-icon': overlay }" viewBox="0 0 16 16"
            @click="iconClicked">
            <path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.777.416L8 13.101l-5.223 2.815A.5.5 0 0 1 2 15.5zm2-1a1 1 0 0 0-1 1v12.566l4.723-2.482a.5.5 0 0 1 .554 0L13 14.566V2a1 1 0 0 0-1-1z"/>
        </svg>
    </div>
    
</template>

<script>
    export default {
        name: "BookmarkModal",
        props: {
            user: Object,
            listing: Object,
            overlay: Boolean,
            size: String,
        },
        data() {
            return {
                userID: '',
                userBookmarks: {},
            }
        },
        mounted() {
            if (this.user) {
                this.userID = this.user.id;
                this.userBookmarks = this.user.drinkLists;
            }
        },
        methods: {
            // checks if listing is in user bookmark list
            checkBookmarkStatus(listingID) {
                for (const category of Object.values(this.userBookmarks)) {
                    if (category.listItems) {
                        if (category.listItems.some(item => parseInt(item) === listingID)) {
                            return true;
                        }
                    }
                }
            },
            iconClicked() {           
                if (this.user) {
                    this.$emit('icon-clicked', this.listing.id);
                }
                else {
                    this.$emit('icon-clicked', 'login');
                }
                
            },

            

        }
    }
</script>