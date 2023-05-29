<script lang="js" setup>

import loading from '@/assets/image/loading.gif'
import { ref,h,render,onMounted} from 'vue'
import axios  from "axios"
import Card from './Card.vue'

import {
  Search,
} from '@element-plus/icons-vue'

axios.defaults.baseURL="/api"
axios.defaults.headers.post['Content-Type'] = 'application/json';

const activeName = ref('first')


const handleClick = (tab, event) => {
  switch(activeName._value){
    case "first": //清除所有标签
    removecard();
      break
  }
  // console.log(tab, event)
}
var getmes="getMes"
//提交数据到服务器
const submit=()=>{
  console.log(checkedmodels._rawValue[0])
  addcard("user",textarea.value)
  axios.get(getmes, {
    params: {
      msg:textarea.value,
      model:checkedmodels._rawValue[0]
    }
}) .then(response=> { 
    console.log(response)
    var str
    if(response.data.ans.content!=undefined){
    str=response.data.ans.content
    str=str.replace(/\n/g,"<br>");
    // console.log(str)
    addcard("ChatAI",str)
    }
    else{
    str=response.data.ans
    str=str.replace(/\\n/g,"<br>");
    addcard("ChatAI",str)
    }
}) .catch(error=> { 
    console.log(error)
});
  textarea.value=""
}
let cardnum=0;
//插入对话
function addcard(title,msg) {
  //创建一个容器用于存放需要动态渲染的组件
  let son = document.createElement('div')
  //把容器插入到指定的位置
  document
			.querySelector('#chats')
			.insertBefore(son,document.querySelector('#chats').firstChild)
  render(h(Card,{title:title,msg:msg}),son)
  cardnum++;
}
//删除卡片
function removecard() {
  //删除卡片
  let chats =document.querySelector('#chats')
  for(let i=0;i<cardnum;i++)
  chats.children[0].remove();

}
defineProps({
})

const textarea = ref('')

//设置选项
const checkedmodels = ref(['gpt-3.5-turbo'])
const models = ['text-davinci-003', 'text-davinci-002', 'text-davinci-001', '	text-curie-001','text-babbage-001','gpt-3.5-turbo']
//AI绘画
const input3 = ref('')
const select = ref('')
// const image=ref('')
// const AIimage = ref('')
const src =
  ref('https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg')
var getImage="getImage"
// var getImage="getImage"
function getImg(){
  var image=document.querySelector('#image1')
  image.src=loading
  console.log(input3,select)
  axios.get(getImage, {
    params: {
      prompt:input3.value,
      model:select.label
    }
}) .then(response=> { 
    console.log(response.data)
    image.src=response.data
    console.log(image)
}) .catch(error=> { 
    console.log(error)
});
}

//头像url
const circleUrl =ref('https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png')

</script >

<template>

    <el-row style="padding: 0;margin-bottom: 150px;">
    <el-tabs style="height: 100%;width:100%;" v-model="activeName" tab-position="left"  class="demo-tabs" @tab-click="handleClick">
    <el-col :span="24">
    <el-tab-pane  label="New chat" id="chats" name="first">
      <!-- <Gpt></Gpt> -->
      <el-card class="box-card">
    <!-- <template #header> -->
      <div class="card-header">
        <span style="font-family:Georgia;color:#B7E8BD;">
          <el-avatar :size="30" :src="circleUrl" />
          ChatAI
        </span>
        <el-button class="button" text>复制</el-button>
      </div>
    <!-- </template> -->
      <div class="scrolltext">  
        Hello ,我是chatgpt，您可以向我提问
      </div>
    </el-card>
    </el-tab-pane>
  </el-col>
    <el-tab-pane label="AI chat" name="second">
      <!-- 输入框 -->
    <div class="mt-4">
    <el-input
      v-model="input3"
      placeholder="mountain"
      class="input-with-select"
      style="width:80%"
    >
      <template #prepend>
        <el-button :icon="Search" @click="getImg"/>
      </template>
      <template #append>
        <el-select v-model="select" placeholder="size" style="width: 115px">
          <el-option label="1024x1024" value="1" />
          <el-option label="512x512" value="2" />
          <el-option label="256x256" value="3" />
        </el-select>
      </template>
    </el-input>
    </div>

    <!-- 绘画 -->
    <div class="demo-image__placeholder">
    <div class="block">
      <span class="demonstration">AI绘画</span>
      <el-image id="image1" style="width:100%;" :src="src"/>
    </div>
  </div>
    <!-- <img :v-model="AIimage" src="" alt="" style="height:500px;width: 500px;"> -->
    </el-tab-pane>
    <el-tab-pane label="config" name="third">
      <el-text class="mx-1" type="info">model(default in gpt-3.5-turbo)</el-text>
      <el-row>
      <el-checkbox-group v-model="checkedmodels" :min="0" :max="1">
    <el-checkbox v-for="model in models" :key="model" :label="model">{{
      model
    }}</el-checkbox>
  </el-checkbox-group>
      </el-row>
    </el-tab-pane>
    <el-tab-pane label="about" name="fourth" style="height: 100%;width:100%;">
      <el-descriptions title="About me">
    <el-descriptions-item label="Author">MXL</el-descriptions-item>
    <el-descriptions-item label="Email">1192698984@qq.com</el-descriptions-item>
    <el-descriptions-item label="github"><a href="https://github.com/asd1192698984">git主页</a></el-descriptions-item>
    <!-- <el-descriptions-item label="code"
      >这里获得</el-descriptions-item
    > -->
    <el-descriptions-item label="school">
      <el-tag size="small">WHT</el-tag>
    </el-descriptions-item>
    </el-descriptions>
    </el-tab-pane>
    </el-tabs>
  </el-row>
    <el-input  
    class="input"
    v-model="textarea"
    :rows="4"
    type="textarea"
    placeholder="Please input"
    @keyup.enter="submit"
    />
    <el-button class="submit" :icon="Search" circle @click="submit"/>
    <!-- <el-button  class="submit" type="success" :icon="Check" circle /> -->
</template>


<style scoped>
*{
    padding: 0;
    margin: 0;
}
.demo-tabs > .el-tabs__content {
  padding: 32px;
  color: #6b778c;
  font-size: 32px;
  font-weight: 600;
}
.input{
  position: fixed;
  bottom: 20px;
  /* margin-left: auto;
  margin-right: auto;
  margin-bottom: 10px; */
}
.submit{
  position: fixed;
  bottom: 20px;
  right: 20px;
}
.card-header {
  padding: 0;
  margin: 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 30px;
}

.text {
  font-size: 14px;
}

.item {
  margin-bottom: 1px;
}

.box-card {
  margin-top: 10px;
   /* height: 250px; */
   max-height: 25%;
  /* width: 780px; */
  width: 80%;
  overflow:auto
}
.demo-image__placeholder .block {
  padding: 30px 0;
  text-align: center;
  border-right: solid 1px var(--el-border-color);
  display: inline-block;
  width: 65%;
  box-sizing: border-box;
  vertical-align: top;
}
.demo-image__placeholder .demonstration {
  display: block;
  color: var(--el-text-color-secondary);
  font-size: 14px;
  margin-bottom: 20px;
}
.demo-image__placeholder .el-image {
  padding: 0 5px;
  max-width: 500px;
  max-height: 500px;
}

.demo-image__placeholder.image-slot {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
  background: var(--el-fill-color-light);
  color: var(--el-text-color-secondary);
  font-size: 14px;
}
.demo-image__placeholder .dot {
  animation: dot 2s infinite steps(3, start);
  overflow: hidden;
}
/* .scrolltext{
  overflow:auto
} */
</style>
