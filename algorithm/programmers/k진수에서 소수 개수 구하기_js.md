k진수에서 소수 개수 구하기

```js
function solution(n, k) {
    let answer = 0;
    let i = k;
    let dtok = []
    while(n){
        let tmp = n % i
        dtok.unshift((tmp*k)/i)
        n -= tmp
        i *= k
    }
    let num = dtok.join("").split("0")
    num.forEach(el => {
        // console.log(typeof(el), el, el !== "")
        if(!(el === "" || el === "1")){
            // console.log("st",el)
            let tmp = parseInt(el)
            let f =1
            for(let p = 2; p*p<=tmp; p++){
                // console.log(p, el, p%tmp)
                if(tmp%p===0){
                    f = 0
                    break
                }
            }
            if(f || tmp ===2 || tmp === 3 && tmp !== 4){
                answer += 1
            }
        }
    })
    return answer;
}
/*
테스트 1 〉	통과 (11.27ms, 37.2MB)
테스트 2 〉	통과 (0.17ms, 33.5MB)
테스트 3 〉	통과 (0.14ms, 33.6MB)
테스트 4 〉	통과 (0.21ms, 33.4MB)
테스트 5 〉	통과 (0.09ms, 33.5MB)
테스트 6 〉	통과 (0.14ms, 33.4MB)
테스트 7 〉	통과 (0.10ms, 33.4MB)
테스트 8 〉	통과 (0.09ms, 33.6MB)
테스트 9 〉	통과 (0.15ms, 33.6MB)
테스트 10 〉	통과 (0.09ms, 33.4MB)
테스트 11 〉	통과 (0.23ms, 33.5MB)
테스트 12 〉	통과 (0.09ms, 33.5MB)
테스트 13 〉	통과 (0.17ms, 33.6MB)
테스트 14 〉	통과 (0.09ms, 33.4MB)
테스트 15 〉	통과 (0.09ms, 33.5MB)
테스트 16 〉	통과 (0.09ms, 33.5MB)
```

