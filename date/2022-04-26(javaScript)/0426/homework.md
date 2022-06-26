1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

- F
- F
- F
- F



2. 아래 같이 numbers 배열이 주어졌을 때, 아래 요구사항들에 맞도록 코드를 작성하시오

```js
//1 
const numbers = [1, 2, 3, 4, 5]
for (let number of numbers){
    console.log(number)
}

//2
const newNums = []
console.log(newNums)
for(let number of numbers){
    newNums.push(number+10)
}
console.log(newNums)

//3
const oddNums = []
for(let number of numbers){
    if(number%2===1){
        oddNums.push(number)
    }
}
console.log(oddNums)

//4
let numsSum = 0
for (let number of numbers){
    numsSum += number
}
console.log(numsSum)
```

