<script lang="js" setup>
import { ElButton, ElCard,ElAvatar} from 'element-plus'
import {onMounted, ref} from 'vue'
const props=defineProps({
  title: {
    type: String,
    required: true
  },
  msg: {
    type: String,
    required: true
  }
})
onMounted(()=>{
  document.getElementById("scrolltext").innerHTML=props.msg
})
//头像url
const circleUrl =ref('https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png')
</script>
<template>
<el-card class="box-card">
    <!-- <template #header> -->
      <div class="card-header">
        <span style="font-family:Georgia;color:#B7E8BD;">
          <el-avatar :size="30" :src="circleUrl" />
          {{title}}
        </span>
        <el-button class="button" text>复制</el-button>
      </div>
    <!-- </template> -->
      <div id="scrolltext" :v-html="msg" :v-model="scrolltext"   class="scrolltext"> 
      </div>
</el-card>
</template>
<style scoped>
.card-header {
  padding: 0;
  margin: 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 30px;
}
.box-card {
  margin-top: 10px;
   /* height: 250px; */
   max-height: 25%;
  /* width: 780px; */
  width: 80%;
  overflow:auto
}
/* .scrolltext{
} */
</style>