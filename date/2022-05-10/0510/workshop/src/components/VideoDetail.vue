<template>
<div>
  <iframe :src="videoUrl" frameborder="0"></iframe>
</div>
</template>

<script>
export default {
  name: 'VideoDetail',
  props: {
    selectedVideo: Object
  },
  computed: {
    videoUrl: function () {
      const videoId = this.selectedVideo.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    }
  }
}
</script>

<style>

</style>