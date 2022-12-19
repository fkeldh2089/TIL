javascript_array.reduce



```js
let value = arr.reduce(function(accumulator, currentValue, currentIndex, array) {
   // ... 
}, [initialValue]);
```

위의 함수를 활용하여 array의 전체 합을 구할 수 있음

```js
const result = arr.reduce(function add(sum, currValue) {
  return sum + currValue;
}, 0);
```

