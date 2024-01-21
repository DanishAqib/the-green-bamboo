import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

// TODO: Re-route paths to correct views, such as / path to BottleListings.vue
// TODO: Discuss with team about path names and how to organize them

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/LoginView.vue')
  },
  {
    path: '/search',
    name: 'search',
    component: () => import('../views/SearchView.vue')
  },
  {
    path: '/Users/Bottle-Listings',
    name: 'usersbottlelistings',
    component: () => import('../views/Users/BottleListings.vue')
  },  
  {
    path: '/userprofile',
    name: 'userprofile',
    component: () => import('../views/UserProfile.vue')
  },
  {
    path: '/Producers/Bottle-Listings',
    name: 'producersbottlelistings',
    component: () => import('../views/Producers/BottleListings.vue')
  },  
  {
    path: '/Producer/Producer-Listings',
    name: 'producerlistings',
    component: () => import('../views/Producers/ProducerListings.vue')
  },  
  {
    path: '/Producer/Producer-Create-Listing',
    name: 'producercreatelistings',
    component: () => import('../views/Producers/CreateListing.vue')
  },  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
