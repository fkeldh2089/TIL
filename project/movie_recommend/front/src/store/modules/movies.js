import axios from 'axios'
import drf from '@/api/drf'

export default {

  state: {
    movies: [],
    movie: {},
    filteringWords: {
      checking: 'to-recently',
      sort_level: 'to-up',
      drama_check: 'to-on',
      action_check: 'to-on',
      adventure_check: 'to-on',
      animation_check: 'to-on',
      comedy_check: 'to-on',
      crime_check: 'to-on',
      documentary_check: 'to-on',
      family_check: 'to-on',
      fantasy_check: 'to-on',
      hitory_check: 'to-on',
      horror_check: 'to-on',
      music_check: 'to-on',
      mystery_check: 'to-on',
      romance_check: 'to-on',
      sf_check: 'to-on',
      tv_check: 'to-on',
      thriller_check: 'to-on',
      war_check: 'to-on',
      western_check: 'to-on',
      runtime: 1,
      vote_num: 5,
      moviequery: '',
      actorquery:'',

    },
  },

  getters: {
    movies: state => state.movies,
    movie: state => state.movie,
  },

  mutations: {
    GET_MOIVES: (state, movies) => state.movies = movies,
    GET_MOIVES_DETAIL: (state, movie) => state.movie = movie,
    UPDATESORTINGLEVEL(state){
      if (state.filteringWords['sort_level']==='to-up'){
        state.filteringWords['sort_level']='to-down'
      }
      else{
        state.filteringWords['sort_level']='to-up'
      }
    },
    UPDATESORTING(state){
      if(state.filteringWords['checking']==='to-recently'){
        state.filteringWords['checking']='to-vote'
      }
      else if(state.filteringWords['checking']==='to-vote'){
        state.filteringWords['checking']='to-popu'
      }
      else if(state.filteringWords['checking']==='to-popu'){
        state.filteringWords['checking']='to-reviewnum'
      }
      else if(state.filteringWords['checking']==='to-reviewnum'){
        state.filteringWords['checking']='to-reviewgrade'
      }
      else{
        state.filteringWords['checking']='to-recently'
      }
    },
    UPDATEGENREFILTER(state, input){
      if (state.filteringWords[input]==='to-on'){
        state.filteringWords[input]='to-off'
      }
      else{
        state.filteringWords[input]='to-on'
      }
    },
    UPDATERUNTIME(state){
      if(state.filteringWords['runtime']===1){
        state.filteringWords['runtime']=120
      }
      else if(state.filteringWords['runtime']===120){
        state.filteringWords['runtime']=180
      }
      else{
        state.filteringWords['runtime']=1
      }   
    },
    UPDATEVOTENUM(state){
      if(state.filteringWords['vote_num']===5){
        state.filteringWords['vote_num']=6
      }
      else if(state.filteringWords['vote_num']===6){
        state.filteringWords['vote_num']=7
      }
      else if(state.filteringWords['vote_num']===7){
        state.filteringWords['vote_num']=8
      }
      else{
        state.filteringWords['vote_num']=5
      }   
    },
    SEARCHMOVIE(state, input){
      state.filteringWords['moviequery'] = input
    },
    SEARCHACTOR(state, input){
      state.filteringWords['actorquery'] = input
    },
    MAKE_NULL(state){
      state.filteringWords['moviequery'] = ''
      state.filteringWords['actorquery'] = ''

    }
  },

  actions: {
    fetchMovies({ commit, getters }) {
      const filteringWords = this.state.movies.filteringWords
      axios({
        url: drf.movies.movies(),
        method: 'post',
        headers: getters.authHeader,
        data: filteringWords

      })
        .then(res => commit('GET_MOIVES', res.data))
        .then(commit('MAKE_NULL'))
        .catch(err => console.error(err.response))
    },
    updateSortingLevel({ commit }){
      commit('UPDATESORTINGLEVEL')
    },
    updateSorting({ commit }){
      commit('UPDATESORTING')
    },
    updateGenrefilter({ commit }, input){
      commit('UPDATEGENREFILTER', input)
    },
    updateRuntime({ commit }){
      commit('UPDATERUNTIME')
    },
    updateVoteNum({ commit }){
      commit('UPDATEVOTENUM')
    },
    searchMovie({ commit }, input){
      commit('SEARCHMOVIE', input)
    },
    searchActor({ commit }, input){
      commit('SEARCHACTOR', input)
    },
    getMovieDetail({ commit, getters }, input){
      axios({
        url: drf.movies.movieDetail(input),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('GET_MOIVES_DETAIL', res.data))
        .catch(err => console.error(err.response))
    },
    gradingMovie({commit, getters}, data){
      axios({
        url: drf.movies.movieReview(data['pk']),
        method: 'post',
        headers: getters.authHeader,
        data: data
      })
        .then(res => commit('GET_MOIVES_DETAIL', res.data))
        .catch(err => console.error(err.response))
    },
    deleteReview({commit, getters}, data){
      axios({
        url: drf.movies.movieReview(data['movie_pk']),
        method: 'delete',
        headers: getters.authHeader,
        data: data
      })
        .then(res => commit('GET_MOIVES_DETAIL', res.data))
        .catch(err => console.error(err.response))
    }

  },
}
