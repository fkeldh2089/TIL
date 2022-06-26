console.log("수정")
const myNum = 1
const myString = "string"
const myArr = [1, 2, 3]
const myObj = { a: 1 }

const greeting = function (name = 'hoho') {
  return `HI ${name}`
}
console.log(greeting())


const spreader = function (arg1, arg2, arg3, arg4) {
  return arg1 + arg2 + arg3 + arg4
}

const nums = [1, 2, 3]

console.log(spreader(1, ...nums))

const arrow = function(name){
  return 'hello'
}

// 1. function 생략 
const arrow1 = (name) => {return 'hello'}

// 2. 매개변수 1개일 경우 ()생략
const arrow2 = name => {return 'hello'}

// 3. return한 줄일 경우,,
const arrow3 = name => 'hello'


const numbers = [1, 2, 3, 4, 5]
for (let number of numbers){
    console.log(number)
}

const newNums = []
console.log(newNums)
for(let number of numbers){
    newNums.push(number+10)
}
console.log(newNums)

const oddNums = []
for(let number of numbers){
    if(number%2===1){
        oddNums.push(number)
    }
}
console.log(oddNums)

let numsSum = 0
for (let number of numbers){
    numsSum += number
}
console.log(numsSum)

let firstName
console.log(firstName)
firstName = '싸피 '
console.log(firstName)
firstName = 'ssafy'
console.log(firstName)

for (let i = 1; i <= 9; i = i+2){  // 별의 최대 개수 9개; 별의 개수는 1-3-5-7-9로 2개씩 증가
  console.log(" ".repeat((9-i)/2) + "*".repeat(i))
}