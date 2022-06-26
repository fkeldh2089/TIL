import drf from '@/api/drf'
import axios from 'axios'
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    countries: ['Australia', 'Canada', 'China', 'France', 'Germany', 'Japan', 'Mexico', 'Spain', 'Uk', 'USA'],

    finalMovies: [],          // 초기 샘플이자, finalMovies
    covidPassCountries: [],   // 여행 가능국가
    yearRates: [],            // 1년전 환율
    todayRates: [],           // 오늘 환율
    completedRates: [],       // 전년동기대비 환율변동률
    weatherIndexes: [],       // 날씨지수

    selectedIndex: [],
    selectedIndexSorted: [],
    finalCountry: [],

    // 서브 알고리즘
    yearAgoMovies: [],
    manyGenre: [],
    voteGenre: [],
    eastAsia: [],
    hardTravel: [],
    asiaOceania: [],
  },


  getters: {

  },


  mutations: {
    GET_MOVIE_DATA: function (state, movieData){
      state.finalMovies=movieData
    },
    GET_COVID_PASS_COUNTRY_DATA: function(state, country){
      state.covidPassCountries.push(country)
    },
    GET_YEAR_RATE_DATA: function(state, yearRates){
      state.yearRates.push(yearRates)
    },
    GET_TODAY_RATE_DATA: function(state, todayRates){
      state.todayRates.push(todayRates)
    },
    GET_WEATHER_INDEX_DATA: function(state, weatherIndexes) {
      state.weatherIndexes.push(weatherIndexes)
    },
    GET_COMPLETED_RATE_DATA: function(state, completedRates) {
      state.completedRates = completedRates
    },
    GET_SELECTED_INDEX: function(state, selectedIndex) {
      state.selectedIndex = selectedIndex
    },
    GET_SELECTED_INDEX_SORTED: function(state, selectedIndexSorted) {
      state.selectedIndexSorted = selectedIndexSorted
    },
    GET_FINAL_COUNTRY: function(state, finalCountry) {
      state.finalCountry.push(finalCountry)
    },
    GET_FINAL_MOVIE: function(state, finalMovies) {
      state.finalMovies = finalMovies
    },
    GET_YEAR_AGO_MOVIE: function(state, yearAgoMovies) {
      state.yearAgoMovies = yearAgoMovies
    },
    GET_MANY_GENRE: function(state, manyGenre){
      state.manyGenre = manyGenre
    },
    GET_VOTE_GENRE: function(state, voteGenre){
      state.voteGenre = voteGenre
    },
    GET_EAST_ASIA: function(state, eastAsia){
      state.eastAsia = eastAsia
    },
    GET_HARD_TRAVEL: function(state, hardTravel){
      state.hardTravel = hardTravel
    },
    GET_ASIA_OCEANIA: function(state, asiaOceania){
      state.asiaOceania = asiaOceania
    },
  },


  actions: {
    getMovieData: function({ commit } ){
      axios({
        url: drf.movies.firstSetting(),
        method: 'post',
      })
        .then(res => {
          console.log(res)
          commit('GET_MOVIE_DATA', res.data)
        })
    },
    getCovidPassCountryData: function({ commit }, country){
      commit('GET_COVID_PASS_COUNTRY_DATA', country)
    },
    getYearRateData: function({ commit }, yearRates){
      commit('GET_YEAR_RATE_DATA', yearRates)
    },
    getTodayRateData: function({ commit }, todayRates){
      commit('GET_TODAY_RATE_DATA', todayRates)
    },
    getWeatherIndexData: function({ commit }, weatherIndexes){
      commit('GET_WEATHER_INDEX_DATA', weatherIndexes)
    },
    getCompletedRateData: function({ commit }, completedRates){
      commit('GET_COMPLETED_RATE_DATA', completedRates)
    },
    getSelectedIndex: function({ commit }, selectedIndex) {
      commit('GET_SELECTED_INDEX', selectedIndex)
    },
    getSelectedIndexSorted: function({ commit }, selectedIndexSorted) {
      commit('GET_SELECTED_INDEX_SORTED', selectedIndexSorted)
    },
    getFinalCountry: function({ commit }, finalCountry) {
      commit('GET_FINAL_COUNTRY', finalCountry)
    },
    getFinalMovie({ commit }, finalCountry) {
      axios({
        url: drf.movies.finalMovie(),
        method: 'post',
        data: {'country': finalCountry}
      })
        .then(res => {
          commit('GET_FINAL_MOVIE', res.data)
        })
        .catch(error => {
          console.log(error)
        })
    },

    getYearAgoMovie({ commit }) {
      const today = new Date();
      const year = today.getFullYear();
      const month = ('0' + (today.getMonth() + 1)).slice(-2);
      const day = ('0' + today.getDate()).slice(-2);
      const dateString = year + '-' + month  + '-' + day;
     
      axios({
        url: drf.movies.yearAgo(),
        method: 'post',
        data: {
          'today': dateString
        }
      })
        .then(res => {
          commit('GET_YEAR_AGO_MOVIE', res.data)
        })


    },

    getManyGenre({ commit }, currentUser) {
      axios({
        url: drf.movies.manyGenre(),
        method: 'post',
        data: {
          'data': currentUser
        }
      })
        .then(res => {
          commit('GET_MANY_GENRE', res.data)
        })
    },

    getVoteGenre({ commit }, currentUser) {
      axios({
        url: drf.movies.voteGenre(),
        method: 'post',
        data: {
          'data': currentUser
        }
      })
        .then(res => {
          commit('GET_VOTE_GENRE', res.data)
        })
    },

    getEastAsia({ commit }) {
      axios({
        url: drf.movies.eastAsia(),
        method: 'post',
      })
        .then(res => {
          commit('GET_EAST_ASIA', res.data)
        })
    },

    getHardTravel({ commit }) {
      axios({
        url: drf.movies.hardTravel(),
        method: 'post',
      })
        .then(res => {
          commit('GET_HARD_TRAVEL', res.data)
        })
    },

    getAsiaOceania({ commit }) {
      axios({
        url: drf.movies.asiaOceania(),
        method: 'post',
      })
        .then(res => {
          commit('GET_ASIA_OCEANIA', res.data)
        })
    },

    





  }

})
