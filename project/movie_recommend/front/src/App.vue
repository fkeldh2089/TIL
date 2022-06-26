<template>
  <v-app id="app">
    <nav-bar></nav-bar>
    <hr />
    <router-view></router-view>
    <footer-bar></footer-bar>
  </v-app>
</template>

<script>
  import NavBar from '@/components/NavBar.vue'
  import FooterBar from '@/components/FooterBar.vue'

  import { mapActions } from 'vuex'

  export default {
    name: 'App',
    components: { NavBar, FooterBar },
    methods: {
      ...mapActions(['fetchCurrentUser'])
    },
    created() {
      this.fetchCurrentUser()
    }
  }
</script>

<style></style>
