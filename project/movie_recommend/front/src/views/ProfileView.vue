<template>
  <div class="container">
    <div class="card mb-3" style="width:75%">
      <div class="row no-gutters">
        <div class="col-md-4">
          <img  class="img-fluid" src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F4jYFt%2FbtqIqmfguOM%2FBy54CLe7pbO6R1VQkqDSmK%2Fimg.jpg" alt="...">
        </div>
        <div class="col-md-8">
          <div class="card-body">
            <h5 class="card-title">{{ profile.username }}</h5>
            <p class="card-text">리뷰 수 : {{ profile.movie_count }}</p>
            <p v-if="profile.movie_count>1">많이 본 장르 :
            <span
              v-for="genre in profile.user_many_genre"
              :key=genre.id
            >{{genre[1][2]}}  </span>
             </p>
             <p v-else>
               많이 본 장르 : 정보 없음
             </p>
            <p v-if="profile.movie_count>1">좋게 본 장르 :
            <span
              v-for="genre in profile.user_vote_genre"
              :key=genre.id
            >{{genre[1][2]}}  </span>
             </p>
             <p v-else>
               좋게 본 장르 : 정보 없음
             </p>
             <v-btn :to="{ name: 'logout' }">Logout</v-btn>
          </div>
        </div>
      </div>
    </div>

    <div v-if="profile['5']">
      <div>
        <v-rating
          color="yellow darken-3"
          background-color="grey darken-1"
          empty-icon="$ratingFull"
          size="20"
          readonly
          value=5
        ></v-rating>
        <div class="swiper" style="display:flex; white-space:nowrap; overflow-x:scroll;">
          <div
            v-for="moviereview in profile['5']"
            :key="moviereview[0]"
          >
            <img 
                :src="moviereview[1]" 
                style="height:15rem;"
                alt="..."
                @click="getMovieDetail(moviereview[0])" type="button" data-toggle="modal" data-target="#profileMovieModal"
              >
          </div>
        </div>
      </div>
    </div>

    <div v-if="profile['4']">
      <div>
        <v-rating
          color="yellow darken-3"
          background-color="grey darken-1"
          empty-icon="$ratingFull"
          size="20"
          readonly
          value=4
        ></v-rating>
        <div class="swiper" style="display:flex; white-space:nowrap; overflow-x:scroll;">
          <div
            v-for="moviereview in profile['4']"
            :key="moviereview[0]"
          >
            <img 
                :src="moviereview[1]" 
                style="height:15rem;"
                alt="..."
                @click="getMovieDetail(moviereview[0])" type="button" data-toggle="modal" data-target="#profileMovieModal"
              >
          </div>
        </div>
      </div>
    </div>

    <div v-if="profile['3']">
      <div>
        <v-rating
          color="yellow darken-3"
          background-color="grey darken-1"
          empty-icon="$ratingFull"
          size="20"
          readonly
          value=3
        ></v-rating>
        <div class="swiper" style="display:flex; white-space:nowrap; overflow-x:scroll;">
          <div
            v-for="moviereview in profile['3']"
            :key="moviereview[0]"
          >
            <img 
                :src="moviereview[1]" 
                style="height:15rem;"
                alt="..."
                @click="getMovieDetail(moviereview[0])" type="button" data-toggle="modal" data-target="#profileMovieModal"
              >
          </div>
        </div>
      </div>
    </div>

    <div v-if="profile['2']">
      <div>
        <v-rating
          color="yellow darken-3"
          background-color="grey darken-1"
          empty-icon="$ratingFull"
          size="20"
          readonly
          value=2
        ></v-rating>
        <div class="swiper" style="display:flex; white-space:nowrap; overflow-x:scroll;">
          <div
            v-for="moviereview in profile['2']"
            :key="moviereview[0]"
          >
            <img 
                :src="moviereview[1]" 
                style="height:15rem;"
                alt="..."
                @click="getMovieDetail(moviereview[0])" type="button" data-toggle="modal" data-target="#profileMovieModal"
              >
          </div>
        </div>
      </div>
    </div>

    <div v-if="profile['1']">
      <div>
        <v-rating
          color="yellow darken-3"
          background-color="grey darken-1"
          empty-icon="$ratingFull"
          size="20"
          readonly
          value=1
        ></v-rating>
        <div class="swiper" style="display:flex; white-space:nowrap; overflow-x:scroll;">
          <div
            v-for="moviereview in profile['1']"
            :key="moviereview[0]"
          >
            <img 
                :src="moviereview[1]" 
                style="height:15rem;"
                alt="..."
                @click="getMovieDetail(moviereview[0])" type="button" data-toggle="modal" data-target="#profileMovieModal"
              >
          </div>
        </div>
      </div>
    </div>
    
    <!-- Modal -->
    <div class="modal fade" id="profileMovieModal" tabindex="-1"  aria-labelledby="profileModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered modal-xl" >
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="profileModalLabel">Detail</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body row">
            <div class="col-6">
              <div class="card" >
                <img :src="movie.poster_path" class="card-img-top fluid" alt="...">
                <div class="card-body">
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
                <button @click="onDelete({'movie_pk': movie.id, 'review_pk': review.id})"> 삭제 </button>
              </div>
              <hr>
              <div class="swiper" style="overflow-y:scroll; height: 30%">
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
                  <hr>
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
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ProfileView',
  data() {
      return{
        content: '',
        rating: 0,
      } 

    },
  computed: {
    ...mapGetters(['profile', 'movie']),

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

  methods: {
    ...mapActions([
      'fetchProfile', 
      'getMovieDetail',
      'gradingMovie',
      'deleteReview',
      ]),

      onSubmit(){
        this.gradingMovie({pk: this.movie.id, content: this.content, grade: this.rating,})
        this.content = ''
        this.rating= null
        const payload = { username: this.$route.params.username }
        this.fetchProfile(payload)
      },

      onDelete(data){
        this.deleteReview(data)
        this.$router.go();
      }
  },
  
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  },
}
</script>

<style>

</style>