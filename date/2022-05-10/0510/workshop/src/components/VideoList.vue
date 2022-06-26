<template>
  <div>
    <ul>
      <!-- <li >
        {{ video.snippet.title }}
      </li> -->
      <video-list-item
        v-for="video in videos" 
        :key="video.id.videoId"
        :video="video"
        @select-video="selectVideo"
      >
      </video-list-item>
    </ul>
  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'


export default {
  name: 'VideoList',
  components: {
    VideoListItem,

  },
  props: {
    videos: Array,

  },
  methods: {
    selectVideo: function (video) {
      this.$emit('select-video', video)
      console.log('why2')
      console.log(video)
    }
  }
}
</script>

<style>

</style>