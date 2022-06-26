<template>
  <div>
    <br>
    <v-carousel
      cycle
      height="1050"
      hide-delimiter-background
      show-arrows-on-hover
      interval="10000"
    >
    <v-app id="inspire">
      <v-carousel-item>
        <v-item-group class="d-flex justify-space-around">
          <span v-for="i in 3" :key="i"> <!--i = 1, 2, 3-->
            <v-item v-slot="{ active, toggle }" class="mx-15" style="transition: all 0.2s linear; overflow: hidden;">
              <v-card class="mx-auto" max-width="400" :color="active ? 'primary' : ''" @click="toggle">
                <v-img
                  :src="finalMovies[i-1].poster_path"
                  height="600px"
                  @click="getMovieDetail(finalMovies[i-1].id)" type="button" data-toggle="modal" data-target="#exampleModal"
                ></v-img>
                <v-card-title><h4 class="font-weight-bold">{{ finalMovies[i-1].title }} </h4></v-card-title>
                <v-card-subtitle>
                  <h5>
                    <pre>
개봉일 {{ finalMovies[i-1].release_date }} 
평점 {{ finalMovies[i-1].vote_average }}
러닝타임 {{ finalMovies[i-1].runtime}} 분
                    </pre>
                  </h5>
                </v-card-subtitle>
              </v-card>
            </v-item>
          </span>
        </v-item-group>
      </v-carousel-item>

      <v-carousel-item>
        <v-item-group class="d-flex justify-space-around">
          <span v-for="i in 3" :key="i"> <!--i = 1, 2, 3-->
            <v-item v-slot="{ active, toggle }">
              <v-card class="mx-auto" max-width="400" :color="active ? 'primary' : ''" @click="toggle">
                <v-img
                  :src="finalMovies[i+2].poster_path"
                  height="600px"
                  @click="getMovieDetail(finalMovies[i+2].id)" type="button" data-toggle="modal" data-target="#exampleModal"
                  class="img-fluid"
                ></v-img>
                <v-card-title><h4 class="font-weight-bold">{{ finalMovies[i+2].title }} </h4></v-card-title>
                <v-card-subtitle>
                  <h5>
                    <pre>
개봉일 {{ finalMovies[i+2].release_date }} 
평점 {{ finalMovies[i+2].vote_average }}
러닝타임 {{ finalMovies[i+2].runtime}} 분
                    </pre>
                  </h5>
                </v-card-subtitle>
              </v-card>
            </v-item>
          </span>
        </v-item-group>
      </v-carousel-item>
      </v-app>
    </v-carousel>
    
    <div class="d-flex justify-content-center">
      <v-btn @click="getCompletedRate"
      x-large depressed color="primary">영화불러오기</v-btn>
    </div>

    <!-- Modal -->
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
import { mapActions, mapGetters } from 'vuex'
import storetmp from '@/store/modules/main.js'

export default {
  name: 'MovieCarousel',

  computed: {
    ...mapGetters(['movie']),

    finalMovies: function() {
      return this.$store.state.main.finalMovies
    },
    covidPassCountries: function() {
      return this.$store.state.main.covidPassCountries
    },
    yearRates: function() {
      return this.$store.state.main.yearRates
    },
    todayRates: function() {
      return this.$store.state.main.todayRates
    },
    weatherIndexes: function() {
      return this.$store.state.main.weatherIndexes
    },
    selectedIndex: function() {
      return this.$store.state.main.selectedIndex
    },
    selectedIndexSorted: function() {
      return this.$store.state.main.selectedIndexSorted
    },
    completedRates: function() {
      return this.$store.state.main.completedRates
    },
    finalCountry: function() {
      return this.$store.state.main.finalCountry
    },
  },

  data() {
      return{
        moviequery: '',
        content: '',
        rating: null,
        selectedCountry: null,
      } 
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

    getFinalMovie: function() {
      const finalCountry = this.$store.state.main.finalCountry
      storetmp.dispatch('getFinalMovie', finalCountry[0])
    },

    onSubmit(){
      this.gradingMovie({pk: this.movie.id, content: this.content, grade: this.rating,})
      this.content = ''
      this.rating= null
    },

    getCompletedRate: function() {
      const completedRates = []
      for(let i = 0; i < 9; i++) {
        completedRates.push((this.$store.state.main.todayRates[i]-this.$store.state.main.yearRates[i])*100/this.$store.state.main.yearRates[i])
      }
      // 미국은 나머지 국가의 평균으로 계산
      const result = completedRates.reduce(function add(sum, currValue){
        return sum + currValue;
      }, 0);
      const average = result / completedRates.length;
      completedRates.push(average)
      storetmp.dispatch('getCompletedRateData', completedRates)
      this.selectCountryFirst()
    },
    
    selectCountryFirst: function() {
      const selectedIndex = []
      const countries = ['Australia', 'Canada', 'China', 'France', 'Germany', 'Japan', 'Mexico', 'Spain', 'Uk', 'USA']

      for(let i = 0; i < 10; i++) {
        selectedIndex.push({'country': countries[i], 'index': this.$store.state.main.completedRates[i]/this.$store.state.main.weatherIndexes[i]})
      }      
      storetmp.dispatch('getSelectedIndex', selectedIndex)
      this.selectCountrySecond()
    },

    selectCountrySecond: function() {
      const selectedIndex = this.$store.state.main.selectedIndex
      let selectedIndexSorted;
      selectedIndexSorted = selectedIndex.sort(function (b, a){
        return a.index - b.index;
      });
      storetmp.dispatch('getSelectedIndexSorted', selectedIndexSorted)
      this.selectCountryThird()
    },

    selectCountryThird: function() {
      for(let i = 0; i < 10; i++) {
        if (this.$store.state.main.covidPassCountries.includes(this.$store.state.main.selectedIndexSorted[i].country)) {
          storetmp.dispatch('getFinalCountry', this.$store.state.main.selectedIndexSorted[i].country)
          break
        }
      }
      this.getFinalMovie()
    },
  }

}
</script>

<style>
#movie-poster:hover {
  transform: scale(1.2);
  z-index : 3;

}
#b {
  word-break: break-all;
  word-wrap: break-word;
}
</style>

