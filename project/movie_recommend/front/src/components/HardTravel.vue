<template>
  <div>
    <div>
      <div class="container d-flex justify-content-center ">

        <div class="d-flex flex-column justify-content-center" >
          <div class="d-flex justify-content-center">
            <div>
              <h3>여행가기 쉽지않은 나라로의 여행</h3>
            </div>
            <br>

          </div>
          <br>
          <br>
          <div class="swiper" style="display:flex; width: 1720px; white-space:nowrap; overflow-x:scroll;">
            <div
              v-for="movie in hardTravel"
              :key="movie['id']"
            > 
              <div class="card mx-3" style="width: 20rem;">
                <img :src="movie['poster_path']" class="card-img-top " alt="..."
                  height="475"
                  @click="getMovieDetail(movie.id)" type="button" data-toggle="modal" data-target="#exampleModal"
                >
              </div>
            </div>
          </div>
        </div>
        <br>
        <br>
        <br>
      </div>
    </div>
        <div class="modal fade" id="exampleModal" tabindex="-1"  aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered modal-xl" >
        <div class="modal-content">
          <div class="modal-body row">
            <div :style="{backgroundImage: 'linear-gradient(to right bottom, rgba(232, 232, 232, 0.3), rgba(191, 191, 191, 0.3)),url(' + movie.backdrop_path + ')', overflow: 'hidden', backgroundSize: 'cover', backgroundRepeat: 'no-repeat', backgroundPostion:'center', height:'100%'}"  class="col-12">
              <div class="row">
                <div class="col-6 col-md-12">
                  <h5 class="card-title">{{movie.title}}</h5>
                  <p>release_date: {{movie.release_date}}</p>
                  <p>vote_average: {{movie.vote_average}}</p>
                  <p>popularity: {{movie.popularity}}</p>
                  <p>runtime: {{movie.runtime}}</p>
                  <div>genres:
                    <span
                      v-for="genre in movie.genres"
                      :key=genre.id
                    >{{genre.name}} </span>
                  </div>
                </div>
                <div class="d-none d-sm-none d-md-block  col-md-12 col-lg-8">
                  <p>{{movie.overview}}</p>
                </div>
              </div>
            </div>
            <div class="col-12">
              <div class="row">
                <div class="swiper" style="display:flex; white-space:nowrap; overflow-x:scroll;">
                  <div v-for="actor in movie.actors" v-show="actor.profile_path" :key="actor.id" class="col-3 col-md-2 col-lg-1">
                      <div>
                        <img class="img-fluid" :src="'https://image.tmdb.org/t/p/w500'+actor.profile_path" alt="">
                      </div>
                      <div style="white-space:wrap;">
                        <p>{{actor.name.slice(0, 10)}}</p>
                      </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-6">
              <div>
                <form @submit.prevent="onSubmit">
                  <v-rating
                    v-model="rating"
                    color="yellow darken-3"
                    background-color="grey darken-1"
                    empty-icon="$ratingFull"
                    hover
                    size="20"
                  ></v-rating>
                  <input type="text" v-model="content" required class="form-control">
                </form>
              </div>
              <hr>
              <div
                v-for="review in movie.moviereview_set"
                :key=review.pk
                v-show="review.user.id === $store.state.accounts.currentUser.pk"
              >
                <v-rating
                    :value=review.grade 
                    color="yellow darken-3"
                    background-color="grey darken-1"
                    empty-icon="$ratingFull"
                    size="20"
                    readonly
                ></v-rating>
                <div class="d-flex">
                  <p id="b"> 내  용 : {{ review.content }}</p>
                </div>
                <p>{{ review.updated_at| yyyyMMdd }}</p>
                <button @click="deleteReview({'movie_pk': movie.id, 'review_pk': review.id})"> 삭제 </button>
              </div>
            </div>

            <div class="col-6">
              <div class="swiper" style="overflow-y:scroll; height: 100%">
                <div
                  v-for="review in movie.moviereview_set"
                  :key=review.pk
                  v-show="review.user.id !== $store.state.accounts.currentUser.pk"
                >
                  <v-rating
                    :value=review.grade 
                    color="yellow darken-3"
                    background-color="grey darken-1"
                    empty-icon="$ratingFull"
                    size="20"
                    readonly
                  ></v-rating>
                  <span>작성자 : 
                    <router-link :to="{ name: 'profile', params: { username: review.user.username } }" data-dismiss="modal" >
                      <span class="text-decoration-none color-black">
                        {{ review.user.username }}
                      </span>
                    </router-link>
                  </span>
                  <div class="d-flex">
                    <p id="b"> 내  용 : {{ review.content }}</p>
                  </div>
                  <p>{{ review.updated_at| yyyyMMdd }}</p>
                </div>
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import storetmp from '@/store/modules/main.js'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'HardTravel',

  computed: {
    ...mapGetters(['movie']),

    hardTravel: function() {
      return this.$store.state.main.hardTravel
    },
  },

  methods: {
    ...mapActions([
      'fetchMovies',
      'updateSortingLevel',
      'updateSorting',
      'updateGenrefilter',
      'updateRuntime',
      'updateVoteNum',
      'searchMovie',
      'searchActor',
      'getMovieDetail',
      'gradingMovie',
      'deleteReview',
    ]),

    getHardTravel: function() {
      storetmp.dispatch("getHardTravel") 

    },
    onSubmit(){
      this.gradingMovie({pk: this.movie.id, content: this.content, grade: this.rating,})
      this.content = ''
      this.rating= null
    },
  },
  created() {
    this.getHardTravel();
  }

}

</script>

<style>

</style>