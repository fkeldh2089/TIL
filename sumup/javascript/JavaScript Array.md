# JavaScript Array

1. 생성

   - 리터럴 표기법

   ```js	
   let fruits = ['사과', '바나나']
   
   console.log(fruits.length) // 2
   console.log(fruits[0])     // "사과"
   
   ```

   - 매개변수 배열 생성자

   ```js
   let fruits = new Array('사과', '바나나')
   
   console.log(fruits.length) // 2
   console.log(fruits[0])     // "사과"
   
   ```

   - from 활용

   ```js
   ```

   

2. 복사

   - 얕은 복사

   ```js
   let shallowCopySpread = [...fruits]
   // ["Strawberry", "Mango"]
   let shallowCopySlice = fruits.slice()
   // ["Strawberry", "Mango"]
   let shallowCopyFrom = Array.from(fruits)
   // ["Strawberry", "Mango"]
   ```

   - 깊은 복사

     문자열로 변환 후 다시 파싱해야 함.

   ```js
   let deepCopy = JSON.parse(JSON.stringify(fruits));
   // ["Strawberry", "Mango"]
   ```

   

3. 접근

   

4. 기타

   - Array.fill(value, start, end)

   ```js
   const array1 = [1, 2, 3, 4];
   
   // fill with 0 from position 2 until position 4
   console.log(array1.fill(0, 2, 4));
   // expected output: [1, 2, 0, 0]
   
   // fill with 5 from position 1
   console.log(array1.fill(5, 1));
   // expected output: [1, 5, 5, 5]
   
   console.log(array1.fill(6));
   // expected output: [6, 6, 6, 6]
   ```

   - Array.map(callback ( currentValue [, index [, array ]])[, thisArg])

   ```js
   ```

   - Array.from()

     유사 배열 객체, 순환가능 객체를 변환하여 새로운 배열 생성

   ```js
   // 문자열은 이터러블이다.
   const arr1 = Array.from('Hello');
   console.log(arr1); // [ 'H', 'e', 'l', 'l', 'o' ]
   
   // 유사 배열 객체를 새로운 배열을 변환하여 반환한다.
   const arr2 = Array.from({ length: 2, 0: 'a', 1: 'b' });
   console.log(arr2); // [ 'a', 'b' ]
   
   // Array.from의 두번째 매개변수에게 배열의 모든 요소에 대해 호출할 함수를 전달할 수 있다.
   // 이 함수는 첫번째 매개변수에게 전달된 인수로 생성된 배열의 모든 요소를 인수로 전달받아 호출된다.
   const arr3 = Array.from({ length: 5 }, function (v, i) { return i; });
   console.log(arr3); // [ 0, 1, 2, 3, 4 ]
   ```

   