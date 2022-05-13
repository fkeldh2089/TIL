<template>
  <div>
    <h1>로또 번호 추천</h1>
    <h2>{{$route.params.lottoNum}}</h2>
    <button @click="getLuckyNums">로또</button>
    <p>{{ resultNums}}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'LottoView',
  data: function(){
    return{
      resultNums: [],
    }
  },
  methods: {
    getLuckyNums: function(){
      const numbers = _.range(1, 46)
      this.resultNums = _.sampleSize(numbers, this.$route.params.lottoNum)
    }
  }
}
</script>

<style>

</style>