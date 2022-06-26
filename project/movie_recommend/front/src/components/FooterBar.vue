<template>
  <v-footer
    color="grey lighten-2"
    padless
    fixed
  >
    <v-row
      justify="space-around"
      no-gutters
    >
      <v-btn
        color="white"
        text
        rounded
        class="my-2"
        :to="{ name: 'main'}"
      >
        main
      </v-btn>
      <v-btn
        color="white"
        text
        rounded
        class="my-2"
        :to="{ name: 'movies'}"
      >
        search
      </v-btn>
      <v-btn
        color="white"
        text
        rounded
        class="my-2"
        :to="{ name: 'profile', params: { username } }"
      >
        profile
      </v-btn>
    </v-row>
  </v-footer>
</template>
<script>
  export default {

  }
</script>