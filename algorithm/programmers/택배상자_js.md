택배상자

```js
function solution(order) {
    let answer = 0;
    const orderLen = order.length
    let waitQ = []
    let idx = 0
    order.push(-1)
    for(let i=1;i<=orderLen+1;i++){
        while(idx<orderLen && waitQ.at(-1)===order[idx]){
            idx++;
            waitQ.pop()
            answer ++;
        }
        if (order[idx] === i){
            answer ++;
            idx ++
        }else{
            waitQ.push(i)
        }

        // console.log(waitQ, order[idx], i, answer)
    }
    return answer;
}
```

