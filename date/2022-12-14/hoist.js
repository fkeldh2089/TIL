import {NAME} from "./key.js"
import axios from 'https://cdn.skypack.dev/axios';

axios.get("http://127.0.0.1:8090").then(res => console.log(22, res)).catch((err)=>{console.log(22,err)})
export default function a(){
    const tmps = {name:NAME}
    return tmps
  }
