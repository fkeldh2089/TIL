#### javascript

```js
let myFirstPromise = new Promise((resolve, reject) => {
  // 우리가 수행한 비동기 작업이 성공한 경우 resolve(...)를 호출하고, 실패한 경우 reject(...)를 호출합니다.
  // 이 예제에서는 setTimeout()을 사용해 비동기 코드를 흉내냅니다.
  // 실제로는 여기서 XHR이나 HTML5 API를 사용할 것입니다.
  setTimeout( function() {
    resolve("성공!")  // 와! 문제 없음!
  }, 250)
})

function mySecondPromise(){
  return new Promise(function(resolve, reject) {
    resolve("good")
  })
}

console.log(1, myFirstPromise)
myFirstPromise.then((successMessage) => {
  // successMessage는 위에서 resolve(...) 호출에 제공한 값입니다.
  // 문자열이어야 하는 법은 없지만, 위에서 문자열을 줬으니 아마 문자열일 것입니다.
  console.log(2, "와! " + successMessage)
});

let result
mySecondPromise().then(function(re){
  result = re
  console.log(3, "함수 내부에서는 제대로 불러지고", result)
})
console.log(4, "외부에서는 순서에 의해 불러지지 않는다", result)
```

다음과 같이 promise 객체를 생성, 사용할 수 있다

순서에도 주의하자