const arr = [0, 1, 2];
const arr2 = arr.map(function(element){ 
  return element * 2;
});
const arr3 = arr.filter(function(el){
  return el-2;
})
console.log(ar) // hoisting 문제
const arr4 = arr.find(el => {
  return el - 1 === 1;
})
var ar = 3;
const str = "Hello my name is Hong"
const str2 = str.split("");
const str3 = str.substr(0,4)
const str4 = str.split("").filter((el,i) => {
  return i % 2
}).join("")

console.log(arr2);
console.log(arr3);
console.log(arr4);
console.log(str2)
console.log(str3)
console.log(str4)

