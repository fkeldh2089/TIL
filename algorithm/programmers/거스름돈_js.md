# 거스름돈

```js
function solution(n, money) {
    let answer = 0;
    const dp = Array.from({length: n+1}, (val, index) => {if(index===0){return 1}else{return 0}})
    const idx = money.length
    for(let p=0;p<idx;p++){
        for(let q=0;q<n+1;q++){
            if(q>=money[p]){
                dp[q] += dp[q-money[p]]
            }
        }
    }
    // console.log(dp)
    return dp[n]%1000000007;
}
/*
테스트 1 〉	통과 (2.86ms, 36.6MB)
테스트 2 〉	통과 (2.71ms, 36.6MB)
테스트 3 〉	통과 (2.76ms, 36.6MB)
테스트 4 〉	통과 (2.69ms, 36.6MB)
테스트 5 〉	통과 (3.53ms, 36.5MB)
테스트 6 〉	통과 (2.40ms, 36.5MB)
테스트 7 〉	통과 (3.03ms, 36.6MB)
테스트 8 〉	통과 (2.80ms, 36.6MB)
테스트 9 〉	통과 (3.62ms, 36.7MB)
테스트 10 〉	통과 (2.47ms, 36.6MB)
테스트 11 〉	통과 (2.73ms, 36.5MB)
테스트 12 〉	통과 (2.60ms, 36.6MB)
테스트 13 〉	통과 (2.66ms, 36.6MB)
테스트 14 〉	통과 (2.89ms, 36.7MB)
효율성  테스트
테스트 1 〉	통과 (20.24ms, 36.1MB)
테스트 2 〉	통과 (24.76ms, 36MB)
테스트 3 〉	통과 (43.62ms, 36.1MB)
테스트 4 〉	통과 (40.70ms, 35.8MB)
테스트 5 〉	통과 (29.42ms, 36.3MB)
테스트 6 〉	통과 (25.91ms, 36.2MB)
```

