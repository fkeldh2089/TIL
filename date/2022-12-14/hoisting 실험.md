# hoisting 실험

#### 기본 설명

1. JavaScript에서 **호이스팅**(hoisting)이란, 인터프리터가 변수와 함수의 메모리 공간을 선언 전에 미리 할당하는 것을 의미합니다. `var`로 선언한 변수의 경우 호이스팅 시 `undefined`로 변수를 초기화
2. js 인터프리터가 두 단계로 나눈다고 할 때, 먼저 코드를 훑어서 필요한 것들은 먼저 할당하고 실행하기 떄문에 발생
   - var 변수 선언과 함수 선언문에서 발생한다.
3. 나는 function 과 arrow function 에서의 차이점이 궁금하여 공부하기 시작하였다.
   - .env 파일에서 키값을 임포트해서 function에서 활용하였는데, 호이스팅 문제가 발생한 듯하다.



#### 실험

1. 간단하게 하나의 js 내부에서 실험

   - 기본적인 var로 인한 hoisting

   ```js
   console.log(ar) // hoisting 문제
   
   var ar = 3;
   console.log(ar)
   
   /*
   undefined
   */
   ```

   - 만약 const와 같은 경우

   ```js
   console.log(ar) // hoisting 문제
   
   var ar = 3;
   console.log(ar)
   
   /*
   err
   */
   ```

   hoisting 문제가 발생한 경우 undefined가 출력되는 것을 볼 수 있다. undefined를 보면 hoisting을 의심해 보는 것이 좋을 것 같다.

   

2. import를 이용하여 실험

   - `npm install live-server` 를 통하여 서버 설치 후 실험

     ```html
     <div>
       <p>hi</p>
       <script type="module" src="./hoist.js">ab</script>
     </div>
     ```

     간단하게 html을 구성

     ```js
     // hoist.js
     import {NAME} from "./key.js"
     
     // function a(){
       //   console.log(NAME)
       // }
     let st
     const a = () =>{
       st = NAME
     }
     console.log("1", st)
     a()
     console.log("2", st)
     
     
     // key.js
     export const NAME = 'mike';
     ```

     아래 파일을 다음과 같이 구성

     하지만 결과 바라던 현상(import보다 function이 먼저 호출 되는)은 나타나지 않았다.

3. import 되는 파일을 하나 더 추가

   - script.js를 추가하여 hoist에서 함수를 받아왔다.

   ```js
   // script.js
   import a from "./hoist.js"
   
   console.log(a())
   
   // hoist.js
   import {NAME} from "./key.js"
   
   export default function a(){
       const tmps = {name:NAME}
     }
   ```

   ​	여전히 너무나도 잘 동작한다.

4. React Native를 활용하여 재현
   - 왜 안되지?, 단순 function, arrow function 뿐만 아니라 복합적인 요소가 있었던 듯 하다.