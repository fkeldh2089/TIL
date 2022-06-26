<template>
  <div class="container">
    <div v-if="!this.search_m" class="d-flex justify-content-center">
      <h1>Search</h1><i @click="converSearchActor()" class="fa-solid btn fa-magnifying-glass fa-lg"></i>
    </div>
    <div v-if="this.search_m" class="d-flex justify-content-center">
      <h1>Search</h1><i @click="converSearchTitle()" class="fa-solid btn fa-person fa-lg"></i>
    </div>
    
    <div v-if="!this.search_m" class="input-group input-group-sm mb-3">
      <input type="text"
        class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-sm"
        style="ime-mode:active"
        v-model="moviequery"
        @keyup.enter="searchMovie(moviequery), fetchMovies()"
      >
    </div>
    <div v-if="this.search_m" class="input-group input-group-sm mb-3">
      <input type="text"
        class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-sm"
        style="ime-mode:active"
        v-model="actorquery"
        @keyup.enter="searchActor(actorquery), fetchMovies()"
      >
    </div>
    

    <button class="btn btn-primary" type="button" data-toggle="collapse" data-target="#filters_sp" aria-expanded="false" aria-controls="filters_sp">
      filter
    </button><br>
    <div class="collapse ml-3 mt-3" id="filters_sp">
      <div class="row">
        <div class="col col-1" style="white-space:nowrap;">
          <p class="text-center">장  르:</p>
        </div>
        <div class="col col-11">
          <v-btn
            class="white black--text"
            v-if="filteringWords['drama_check'] === 'to-on'"
            @click="updateGenrefilter(data='drama_check'), fetchMovies()"
          >드라마 </v-btn>
          <v-btn
            class="yellow black--text"
            v-else
            @click="updateGenrefilter(data='drama_check'), fetchMovies()"
            style="font-weight: bold"
          >드라마 </v-btn>
          <v-btn
            class="white black--text"
            v-if="filteringWords['action_check'] === 'to-on'"
            @click="updateGenrefilter(data='action_check'), fetchMovies()"
          >액션 </v-btn>
          <v-btn
            class="yellow black--text"
            v-else
            @click="updateGenrefilter(data='action_check'), fetchMovies()"
            style="font-weight: bold"
          >액션 </v-btn>
          <v-btn
            class="white black--text"
            v-if="filteringWords['adventure_check'] === 'to-on'"
            @click="updateGenrefilter(data='adventure_check'), fetchMovies()"
          >모험 </v-btn>
          <v-btn
            class="yellow black--text"
            v-else
            @click="updateGenrefilter(data='adventure_check'), fetchMovies()"
            style="font-weight: bold"
          >모험 </v-btn>
          <v-btn
            class="white black--text"
            v-if="filteringWords['animation_check'] === 'to-on'"
            @click="updateGenrefilter(data='animation_check'), fetchMovies()"
          >애니메이션 </v-btn>
          <v-btn
            class="yellow black--text"
            v-else
            @click="updateGenrefilter(data='animation_check'), fetchMovies()"
            style="font-weight: bold"
          >애니메이션 </v-btn>
          <v-btn
            class="white black--text"
            v-if="filteringWords['comedy_check'] === 'to-on'"
            @click="updateGenrefilter(data='comedy_check'), fetchMovies()"
          >코미디 </v-btn>
          <v-btn
            class="yellow black--text"
            v-else
            @click="updateGenrefilter(data='comedy_check'), fetchMovies()"
            style="font-weight: bold"
          >코미디 </v-btn>
          <v-btn
            class="white black--text"
            v-if="filteringWords['crime_check'] === 'to-on'"
            @click="updateGenrefilter(data='crime_check'), fetchMovies()"
          >범죄 </v-btn>
          <v-btn
            class="yellow black--text"
            v-else
            @click="updateGenrefilter(data='crime_check'), fetchMovies()"
            style="font-weight: bold"
          >범죄 </v-btn>
          <v-btn
            class="white black--text"
            v-if="filteringWords['documentary_check'] === 'to-on'"
            @click="updateGenrefilter(data='documentary_check'), fetchMovies()"
          >다큐 </v-btn>
          <v-btn
            class="yellow black--text"
            v-else
            @click="updateGenrefilter(data='documentary_check'), fetchMovies()"
            style="font-weight: bold"
          >다큐 </v-btn>
          <v-btn
            class="white black--text"
            v-if="filteringWords['family_check'] === 'to-on'"
            @click="updateGenrefilter(data='family_check'), fetchMovies()"
          >가족 </v-btn>
          <v-btn
            class="yellow black--text"
            v-else
            @click="updateGenrefilter(data='family_check'), fetchMovies()"
            style="font-weight: bold"
          >가족 </v-btn>

          <v-btn
            class="white black--text"
            v-if="filteringWords['fantasy_check'] === 'to-on'"
            @click="updateGenrefilter(data='fantasy_check'), fetchMovies()"
          >판타지 </v-btn>
          <v-btn
            class="yellow black--text"
            v-else
            @click="updateGenrefilter(data='fantasy_check'), fetchMovies()"
            style="font-weight: bold"
          >판타지 </v-btn>
          <v-btn
            class="white black--text"
            v-if="filteringWords['hitory_check'] === 'to-on'"
            @click="updateGenrefilter(data='hitory_check'), fetchMovies()"
          >역사 </v-btn>
          <v-btn
            class="yellow black--text"
            v-else
            @click="updateGenrefilter(data='hitory_check'), fetchMovies()"
            style="font-weight: bold"
          >역사 </v-btn>
          <v-btn
            class="white black--text"
            v-if="filteringWords['horror_check'] === 'to-on'"
            @click="updateGenrefilter(data='horror_check'), fetchMovies()"
          >호러 </v-btn>
          <v-btn
            class="yellow black--text"
            v-else
            @click="updateGenrefilter(data='horror_check'), fetchMovies()"
            style="font-weight: bold"
          >호러 </v-btn>
          <v-btn
            class="white black--text"
            v-if="filteringWords['music_check'] === 'to-on'"
            @click="updateGenrefilter(data='music_check'), fetchMovies()"
          >음악 </v-btn>
          <v-btn
            class="yellow black--text"
            v-else
            @click="updateGenrefilter(data='music_check'), fetchMovies()"
            style="font-weight: bold"
          >음악 </v-btn>
          <v-btn
            class="white black--text"
            v-if="filteringWords['mystery_check'] === 'to-on'"
            @click="updateGenrefilter(data='mystery_check'), fetchMovies()"
          >미스터리 </v-btn>
          <v-btn
            class="yellow black--text"
            v-else
            @click="updateGenrefilter(data='mystery_check'), fetchMovies()"
            style="font-weight: bold"
          >미스터리 </v-btn>
          <v-btn
            class="white black--text"
            v-if="filteringWords['romance_check'] === 'to-on'"
            @click="updateGenrefilter(data='romance_check'), fetchMovies()"
          >로맨스 </v-btn>
          <v-btn
            class="yellow black--text"
            v-else
            @click="updateGenrefilter(data='romance_check'), fetchMovies()"
            style="font-weight: bold"
          >로맨스 </v-btn>
          <v-btn
            class="white black--text"
            v-if="filteringWords['sf_check'] === 'to-on'"
            @click="updateGenrefilter(data='sf_check'), fetchMovies()"
          >SF </v-btn>
          <v-btn
            class="yellow black--text"
            v-else
            @click="updateGenrefilter(data='sf_check'), fetchMovies()"
            style="font-weight: bold"
          >SF </v-btn>
          <v-btn
            class="white black--text"
            v-if="filteringWords['tv_check'] === 'to-on'"
            @click="updateGenrefilter(data='tv_check'), fetchMovies()"
          >티비 </v-btn>
          <v-btn
            class="yellow black--text"
            v-else
            @click="updateGenrefilter(data='tv_check'), fetchMovies()"
            style="font-weight: bold"
          >티비 </v-btn>
          <v-btn
            class="white black--text"
            v-if="filteringWords['thriller_check'] === 'to-on'"
            @click="updateGenrefilter(data='thriller_check'), fetchMovies()"
          >스릴러 </v-btn>
          <v-btn
            class="yellow black--text"
            v-else
            @click="updateGenrefilter(data='thriller_check'), fetchMovies()"
            style="font-weight: bold"
          >스릴러 </v-btn>
          <v-btn
            class="white black--text"
            v-if="filteringWords['war_check'] === 'to-on'"
            @click="updateGenrefilter(data='war_check'), fetchMovies()"
          >전쟁 </v-btn>
          <v-btn
            class="yellow black--text"
            v-else
            @click="updateGenrefilter(data='war_check'), fetchMovies()"
            style="font-weight: bold"
          >전쟁 </v-btn>
          <v-btn
            class="white black--text"
            v-if="filteringWords['western_check'] === 'to-on'"
            @click="updateGenrefilter(data='western_check'), fetchMovies()"
          >서부 </v-btn>
          <v-btn
            class="yellow black--text"
            v-else
            @click="updateGenrefilter(data='western_check'), fetchMovies()"
            style="font-weight: bold"
          >서부 </v-btn>
        </div>

        <div class="col col-1" style="white-space:nowrap;">
          <p>시 간:</p>
        </div>  
        <div class="col col-11">
          <v-btn
            class="white black--text"
            v-if="filteringWords['runtime'] === 1"
            @click="updateRuntime(), fetchMovies()"
          >0 </v-btn>
          <v-btn
            class="blue black--text"
            v-else-if="filteringWords['runtime'] === 90"
            @click="updateRuntime(), fetchMovies()"
          >90 </v-btn>
          <v-btn
            class="yellow black--text"
            v-else-if="filteringWords['runtime'] === 120"
            @click="updateRuntime(), fetchMovies()"
          >120 </v-btn>
          <v-btn
            class="pink black--text"
            v-else-if="filteringWords['runtime'] === 150"
            @click="updateRuntime(), fetchMovies()"
          >150 </v-btn>
          <v-btn
            class="red black--text"
            v-else
            @click="updateRuntime(), fetchMovies()"
          >180 </v-btn>
        </div>

        <div class="col col-1" style="white-space:nowrap;">
          <p>평 점:</p>
        </div>  
        <div class="col col-11">
          <v-btn
            class="white black--text"
            v-if="filteringWords['vote_num'] === 5"
            @click="updateVoteNum(), fetchMovies()"
          >5 </v-btn>
          <v-btn
            class="blue black--text"
            v-else-if="filteringWords['vote_num'] === 6"
            @click="updateVoteNum(), fetchMovies()"
          >6 </v-btn>
          <v-btn
            class="yellow black--text"
            v-else-if="filteringWords['vote_num'] === 7"
            @click="updateVoteNum(), fetchMovies()"
          >7 </v-btn>
          <v-btn
            class="pink black--text"
            v-else
            @click="updateVoteNum(), fetchMovies()"
          >8 </v-btn>
        </div>
      </div>
    </div>


    <div class="d-flex justify-content-end mr-4" style="height:1rem;" >
      <a
        class="mr-1 text-decoration-none"
        style="color: black; cursor: pointer;"
        v-if="filteringWords['checking'] === 'to-recently'"
        @click="updateSorting(), fetchMovies()"
      >날짜순 </a>
      <a
        class="mr-1 text-decoration-none"
        style="color: black; cursor: pointer;"
        v-else-if="filteringWords['checking'] === 'to-vote'"
        @click="updateSorting(), fetchMovies()"
      >점수순 </a>
      <a
        class="mr-1 text-decoration-none"
        style="color: black; cursor: pointer;"
        v-else-if="filteringWords['checking'] === 'to-popu'"
        @click="updateSorting(), fetchMovies()"
      >대중성순 </a>
      <a
        class="mr-1 text-decoration-none"
        style="color: black; cursor: pointer;"
        v-else-if="filteringWords['checking'] === 'to-reviewnum'"
        @click="updateSorting(), fetchMovies()"
      >리뷰수 순 </a>
      <a
        class="mr-1 text-decoration-none"
        style="color: black; cursor: pointer;"
        v-else
        @click="updateSorting(), fetchMovies()"
      >별점 순 </a>
      <p>|</p>
      <a
        class="ml-1 text-decoration-none"
        style="color: black; cursor: pointer;"
        v-if="filteringWords['sort_level'] === 'to-up'"
        @click="updateSortingLevel(), fetchMovies()"
      >오름 </a>
      <a
        v-else
        class="ml-1 text-decoration-none"
        style="color: black; cursor: pointer;"
        @click="updateSortingLevel(), fetchMovies()"
      >내림 </a>
    </div>
    <hr>

    <div>
      <div class="d-flex row m-1 p-0">
        <div id="movie-poster" v-for="movie in movies" :key="movie.pk" class="col col-6 col-md-3 col-lg-2"
          style="transition: all 0.2s linear; overflow: hidden;"
        >
            <img 
              :src="movie.poster_path" 
              id="movie-poster-each"
              
              alt="..."
              @click="getMovieDetail(movie.id)" type="button" data-toggle="modal" data-target="#movieListModal"
            >
        </div>
      </div>
    </div>

    <!-- Modal -->
    <div class="modal fade" id="movieListModal" tabindex="-1"  aria-labelledby="movieListModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered modal-xl" >
        <div class="modal-content">
          <div class="modal-body row" style="height:100%">
            <div :style="{backgroundImage: 'linear-gradient(to left, rgba(232, 232, 232, 0.3), white),url(' + movie.backdrop_path + ')', overflow: 'hidden', backgroundSize: 'cover', backgroundRepeat: 'no-repeat', backgroundPostion:'center', width:'100%'}"  class="col-12">
              <div class="row">
                <div class="col-6 col-md-12">
                  <h5 class="card-title">{{movie.title}}</h5>
                  <p>release_date: {{movie.release_date}}</p>
                  <p>vote_average: {{movie.vote_average}}</p>
                  <p>popularity: {{movie.popularity}}</p>
                  <p>runtime: {{movie.runtime}}</p>
                  <p>grade: {{movie.moviereview_grade}}</p>
                  <p>reviews: {{movie.moviereview_num}}</p>
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
              <div style="height:8rem">
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

  export default {
    name: 'MovieList',
    data() {
      return{
        filteringWords: this.$store.state.movies.filteringWords,
        moviequery: '',
        actorquery:'',
        content: '',
        rating: null,
        search_m: 0,
      } 
    },

    filters : {
      yyyyMMdd : function(value){ 
        // 들어오는 value 값이 공백이면 그냥 공백으로 돌려줌
        if(value == '') return '';

        // 현재 Date 혹은 DateTime 데이터를 javaScript date 타입화
        var js_date = new Date(value);

        // 연도, 월, 일 추출
        var year = js_date.getFullYear();
        var month = js_date.getMonth() + 1;
        var day = js_date.getDate();

        // 월, 일의 경우 한자리 수 값이 있기 때문에 공백에 0 처리
        if(month < 10){
          month = '0' + month;
        }

        if(day < 10){
          day = '0' + day;
        }

        // 최종 포맷 (ex - '2021-10-08')
        return year + '-' + month + '-' + day;
      },
    },

    computed: {
      ...mapGetters(['movies', 'movie'])
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
      onSubmit(){
        this.gradingMovie({pk: this.movie.id, content: this.content, grade: this.rating,})
        this.content = ''
        this.rating= null
      },
      converSearchActor(){
        this.search_m = 1
        this.moviequery= ''
      },
      converSearchTitle(){
        this.search_m = 0
        this.actorquery= ''
      },
    },
    created() {
      this.fetchMovies()
    },
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

@media only screen and (min-width: 0px){
  #movie-poster-each{
    width:100%;
    max-width:100%;
    max-height:267px;
  }
}
@media only screen and (min-width: 768px){
  #movie-poster-each{
    width:100%;
    max-width:100%;
    max-height:420px;
  }
}
@media only screen and (min-width: 992px){
  #movie-poster-each{
    width:100%;
    max-width:100%;
    max-height:255px;
  }
}
@media only screen and (min-width: 1200px){
  #movie-poster-each{
    width:100%;
    max-width:100%;
    max-height:235px;
  }
}

</style>
