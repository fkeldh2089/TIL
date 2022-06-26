```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>

</head>

<body>
  <script>
    // 주어진 문자열이 회문인지 판별하는 isPalindrome 함수를 완성하시오.
    function isPalindrome(str) {
      const str3 = str.split('') // 배열로 만들고
      const str2 = str3.filter((num, index) => {
        return num != ' '
      })  // 띄어쓰기 제거
      let str4 = []
      for (let ss of str2){
        str4.unshift(ss)
      }  // 역순 배열 생성
      result1 = str2.join()  // 다시 string으로 합치고
      result2 = str4.join()

      return result2 === result1  // 비교
    }

    // 출력
    console.log(
      isPalindrome('a santa at nasa'),  // true
      isPalindrome('google')  // false
    )
  </script>
</body>

</html>
```

