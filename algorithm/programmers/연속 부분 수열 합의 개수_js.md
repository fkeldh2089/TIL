연속 부분 수열 합의 개수

```js
function solution(elements) {
    let answer = 0;
    let sumSet = new Set()
    let l = elements.length
    let numList = elements.concat(elements)
    // console.log(numList)
    for (i1=1;i1<=l;i1++){
        for(i2=0;i2<l;i2++){
            let tmp = numList.slice(i2, i2+i1).reduce(function add(sum, currValue){
                return sum + currValue
            }, 0)
            // console.log(numList.slice(i2, i2+i1),tmp)
            sumSet.add(tmp)
        }
    }
    answer = sumSet.size
    return answer;
}
```

