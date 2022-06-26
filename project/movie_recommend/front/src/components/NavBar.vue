<template>
<v-card
    color="grey lighten-4"
    flat
    height="50px"
    tile
    fixed
  >
    <v-toolbar
      dense
    >
      <v-toolbar-title>
        <router-link to="/" tag="span" style="cursor: pointer">
          <img src="@/assets/mylogo.png" style="height: 3rem" alt="">
        </router-link>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items v-if="!isLoggedIn" class="hidden-xs-only">
        <v-btn
          v-for="item in menuItems1"
          :key="item.title"
          :to="item.path">
          {{ item.title }}
        </v-btn>
      </v-toolbar-items>
      <v-toolbar-items v-if="isLoggedIn" class="hidden-xs-only">
        <v-btn
          v-for="item in menuItems2"
          :key="item.title"
          :to="item.path">
          {{ item.title }}
        </v-btn>
        <v-btn
          :to="{ name: 'profile', params: { username } }"
        >
          profile
        </v-btn>
      </v-toolbar-items>
    </v-toolbar>
  </v-card>
</template>

<script>
  import { mapGetters } from 'vuex'

  export default {
    name: 'NavBar',
    data(){
      return {
        menuItems1: [
            { title: 'Home', path: '/',},
            { title: 'Search', path: '/movies',},
            { title: 'Log In', path: '/login',}
        ],
        menuItems2: [
              { title: 'Home', path: '/',},
              { title: 'Search', path: '/movies',},
        ]
      }
    },
    computed: {
      ...mapGetters(['isLoggedIn', 'currentUser']),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
    },
  }
</script>

<style></style>
