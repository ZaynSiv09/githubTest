<template>
  <div class="centerContent">
    <div class="title">NDI推流画面</div>
    <div class="btns">
      <button class="findSource" @click="findDevice()">查找可用源</button>
    </div>
    <div class="textureView">
      <div class="msg" v-if="msg">{{msg}}</div>
    </div>
  </div>
  <!-- <div class="wrapper">
    <nav>
      <RouterLink to="/">Home</RouterLink> -->
  <!-- <RouterLink to="/about">About</RouterLink>
    </nav>
  </div> -->
  <!-- <RouterView /> -->
</template>
<script>
// import { RouterLink, RouterView } from 'vue-router'
// import Ndi_view from './components/Ndi_view.vue'
// import  "require.js"

export default {
  data(){
    return {
      msg: '',
    }
  },
  methods: {
    findDevice() {
      console.log("1111111");
      const findSource = require('./build/Release/grandiose');
      console.log(findSource.find());
      console.log("1111111");
    }
  }
}
</script>
<style lang="scss" scoped>
.centerContent {
  display: flex;
  /* 转换主轴 */
  flex-direction: column;
  /* 次轴居中 */
  align-items: center;
  /* 主轴两侧分布 */
  justify-content: space-between;

  .title {
    margin-bottom: 5px;
    font-size: 30px;
  }

  .btns {
    margin-bottom: 5px;
    left: -550px;
  }

  .textureView{
    width: 1220px;
    height: 707px;
    border: 1px solid #ffff;
}
}
</style>
