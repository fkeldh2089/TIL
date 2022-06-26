<template>
  <v-app id="inspire">
    <account-error-list v-if="authError"></account-error-list>
    <v-main class="blue-grey lighten-4">
      <!-- Login Component -->
      <v-container style="max-width: 450px" fill-height>
        <v-layout align-center row wrap>
          <v-flex xs12>
            <v-card>
              <div class="pa-10">
                <h1 style="text-align: center" class="mb-10">Login</h1>
                <form @submit.prevent="signup(credentials)">
                  <v-text-field
                    v-model="credentials.username"
                    id="username" required
                    label="username"
                    prepend-inner-icon="mdi-account"
                  ></v-text-field>
                  <v-text-field
                    v-model="credentials.password1"
                    type="password" id="password1" required
                    prepend-inner-icon="mdi-lock"
                    label="Password1"
                  >
                  </v-text-field>
                  <v-text-field
                    v-model="credentials.password2"
                    type="password" id="password2" required
                    prepend-inner-icon="mdi-lock"
                    label="Password2"
                  >
                  </v-text-field>
                  <v-btn
                    type="submit"
                    color="blue lighten-1 text-capitalize"
                    depressed
                    large
                    block
                    dark
                    class="mb-3"
                  >
                    Sign Up
                  </v-btn>
                </form>
              </div>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'SignupView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password1: '',
          password2: '',
        }
      }
    },
    
    computed: {
      ...mapGetters(['authError'])
    },
    
    methods: {
      ...mapActions(['signup'])
    },
  }
</script>

<style></style>
