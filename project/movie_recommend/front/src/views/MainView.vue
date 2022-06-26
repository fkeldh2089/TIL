<template>
  <div  class="container ">
    <h1>여행가기 좋은 나라는?</h1>
    <movie-carousel></movie-carousel>

    <br>
    <br>
    <br>
    <release-date></release-date>
    
    <br>
    <br>
    <br>
    <east-asia></east-asia>

    <br>
    <br>
    <br>
    <hard-travel></hard-travel>

    <br>
    <br>
    <br>
    <asia-oceania></asia-oceania>
        
    <br>
    <br>
    <br>
    <many-genre></many-genre>

    <br>
    <br>
    <br>
    <vote-genre></vote-genre>
    <br>
    <br>
    <br>
  </div>
</template>

<script>
import MovieCarousel from '@/components/MovieCarousel'
import ReleaseDate from '@/components/ReleaseDate'
import ManyGenre from '@/components/ManyGenre'
import VoteGenre from '@/components/VoteGenre'
import EastAsia from '@/components/EastAsia.vue'
import HardTravel from '@/components/HardTravel.vue'
import AsiaOceania from '@/components/AsiaOceania.vue'

import axios from 'axios'
import storetmp from '@/store/modules/main.js'

const moment = require('moment')
const API_KEY = ''
const API_URL = 'https://api.themoviedb.org/3/movie/popular'
const countries = ['Australia', 'Canada', 'China', 'France', 'Germany', 'Japan', 'Mexico', 'Spain', 'Uk', 'USA']
const currencies = ['AUD', 'CAD', 'CNY', 'EUR', 'EUR', 'JPY', 'MXN', 'EUR', 'GBP', 'USD']
const capitals = ['Canberra', 'Ottawa', 'Beijing', 'Paris', 'Munich', 'Tokyo', 'Mexico City', 'Madrid', 'London', 'Washington D.C.']

export default {
  name: 'MainView',

  components: {
    MovieCarousel,
    ReleaseDate,
    ManyGenre,
    VoteGenre,
    EastAsia,
    HardTravel,
    AsiaOceania,
  },

  methods:{
    getMovie: function() {
        axios({
          method: 'get',
          url: API_URL,
          params: {
            api_key: API_KEY,
            page: 1
          }
        })
        .then(response => {
          storetmp.dispatch('getMovieData', response.data.results)
        })
      },

    getCovid: function() {
      countries.forEach((country, index) => {
        const options = {
          method: 'GET',
          url: 'https://covid-193.p.rapidapi.com/statistics',
          params: {country: country},
          headers: {
            'X-RapidAPI-Host': 'covid-193.p.rapidapi.com',
            'X-RapidAPI-Key': ''
          }
        };
        axios.request(options)
          .then(response => {
            const active = response.data.response[0].cases.active
            const today = response.data.response[0].cases.new
            if (today === 'null') {
              today === 0
            } else {
              today === Number(today)
            }
            const population = response.data.response[0].population
            const key = (active + today * 10) *100 / population

            if (key <= 1) {
              storetmp.dispatch('getCovidPassCountryData', country)
              console.log({[country]: index})
            }
          })
            .catch(error => {
              console.error(error);
            });
        })
      },

    getYearRate: function() {
      const ago = moment().subtract(1, 'year').format('YYYY-MM-DD')
      const options = {
        method: 'GET',
        url: 'https://currencyscoop.p.rapidapi.com/historical',
        params: {date: ago},
        headers: {
          'X-RapidAPI-Host': 'currencyscoop.p.rapidapi.com',
          'X-RapidAPI-Key': ''
        }
      };
      axios.request(options)
        .then(response => {
          const rates = response.data.response.rates
          for(let i = 0; i < 10; i++) {
            storetmp.dispatch('getYearRateData', rates[currencies[i]])
          }
        })
        .catch(error => {
          console.error(error);
        });
    },

    getTodayRate: function() {
        const options = {
          method: 'GET',
          url: 'https://currencyscoop.p.rapidapi.com/latest',
          headers: {
            'X-RapidAPI-Host': 'currencyscoop.p.rapidapi.com',
            'X-RapidAPI-Key': ''
          }
        };
        axios.request(options)
          .then(response => {
            const rates = response.data.response.rates
            for(let i = 0; i < 10; i++) {
              storetmp.dispatch('getTodayRateData', rates[currencies[i]])
            }
          })
          .catch(function (error) {
            console.error(error);
          });
    },

    getWeather: function() {
      for(let i = 0; i < 10; i++) {
        let capital = capitals[i]
        
        axios({
          method: 'GET',
          url: 'http://api.openweathermap.org/data/2.5/forecast',
          params: {
            q: capital ,
            appid: ''
          }
        })
          .then(response => {
            const index = capitals.indexOf(capital)
            const country = countries[index]
            console.log(index, country)
            const humidity = response.data.list[39].main.humidity // 습도
            const kelvin = response.data.list[39].main.temp       // 온도(켈빈)
            const degree = kelvin - 273.15                          // 온도(섭씨)
            const discomfort = degree*9/5 - 0.55*(1-humidity/100)*(degree*9/5-26) + 32
            const weatherStatus = response.data.list[39].weather[0].id
            let weatherIndex = 0 // 불쾌지수에 날씨를 보완한, 날씨지수
            switch(weatherStatus) {
              case 500:
                weatherIndex = discomfort + 10
                break;
              case 501:
                weatherIndex = discomfort + 20
                break;
              case 502:
                weatherIndex = discomfort + 30
                break;
              case 600:
                weatherIndex = discomfort + 20
                break;
              case 804:
                weatherIndex = discomfort + 5
                break;
              default:
                weatherIndex = discomfort
            }
            storetmp.dispatch('getWeatherIndexData', weatherIndex)
          })
          .catch(function (error) {
            console.error(error)
          });
      }
    },
    getYearAgoMovie: function() {
      storetmp.dispatch("getYearAgoMovie")
    },


    
  },

  computed: {

    movies: function() {
      return this.$store.state.main.movies
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
    completedRates: function() {
      return this.$store.state.main.completedRates
    },
  },
  
  created() {
    this.getCovid();        // 방문가능국가
    this.getMovie();     
    this.getYearRate()      // 1년전 환율
    this.getTodayRate()     // 오늘 환율
    this.getWeather()       // 날씨지수(5일뒤)
    this.getYearAgoMovie();
  },


}
</script>

<style>

</style>