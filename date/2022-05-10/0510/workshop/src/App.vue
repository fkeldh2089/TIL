<template>
  <div id="app">
    <h1>My First Youtube</h1>
    <the-search-bar
      @input-change="onInputChange"
    ></the-search-bar>
    <video-detail :selected-video="selectedVideo"></video-detail>

    <video-list
      :videos="videos"
      @select-video="selectVideo"
    ></video-list>
    
  </div>
</template>

<script>
import axios from 'axios'
import TheSearchBar from '@/components/TheSearchBar'
import VideoList from '@/components/VideoList'
import VideoDetail from '@/components/VideoDetail'

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  data: function () {
    return{
      inputData: null,
      videos: [],
      selectedVideo: null,

    }
  },
  components: {
    TheSearchBar,
    VideoList,
    VideoDetail,

  },
  methods: {
    selectVideo: function(video) {
      this.selectedVideo = video
      console.log('why3')
      console.log(video)
    },

    onInputChange: function (inputData) {
      this.inputData = inputData

      // API 요청
      axios({
        method: 'get',
        url: API_URL,
        params: {
          key: API_KEY,
          part: 'snippet',
          type: 'video',
          q: inputData
        }
      })
      .then(res => {
        console.log(res)
        console.log(res.data.items)
        this.videos = res.data.items
      })
      .catch(err=> {
        console.log(err)
      })
    },
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
