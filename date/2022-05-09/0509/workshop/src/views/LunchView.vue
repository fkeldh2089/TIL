<template>
  <div class="about">
    <h1>점심 메뉴</h1>
    <button @click='pickLunch'>점심메뉴</button>
    <p>{{ menu }}</p>
    <h1>로또를 뽑아보자</h1>
    <button @click="moveToLotto">Pick Lotto</button>
    <!-- <h1>ㅠㅠ</h1>
    <input type="text" v-model="lottoNum">
    <button @click="moveToLotto2">로또 뽑</button> -->
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'LunchView',
  data: function() {
    return {
      lunchMenus: ['국밥', '밥', '국'],
      menu: null,
      lottoNum: null,
    }
  },
  methods:{
    moveToLotto: function(){
      this.$router.push({ name: 'Lotto' , params: { lottoNum: 6} })
    },
    pickLunch: function() {
      this.menu = _.sample(this.lunchMenus)
    },
    moveToLotto2: function() {
      this.$router.push({ name: 'Lotto' , params: { lottoNum: this.lottoNum} })
    }
  }
}
</script>
