<template>
  <li @click="selectVideo">
    <img :src="youtubeImageSrc" alt="akak">
    {{video.snippet.title|stringUnescaped}}
  </li>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoListItem',
  props: {
    video: Object
  },
  computed: {
    youtubeImageSrc: function() {
      return this.video.snippet.thumbnails.default.url
    }
  },
  filters: {
    stringUnescaped: function (rawText){
      return _.unescape(rawText)
    }
  },
  methods: {
    selectVideo: function () {
      this.$emit('select-video', this.video)
      console.log('why')
      console.log(this.video)
    }
  }
}
</script>

<style>

</style>