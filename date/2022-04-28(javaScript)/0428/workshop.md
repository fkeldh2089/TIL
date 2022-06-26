1. 

```js
<!DOCTYPE html>
<html lang="en">

<head>
  <title>Document</title>
  <link rel="stylesheet" href="./workshop01.css">
</head>

<body>
  <ul class="switcher">
    <li id="grayButton"></li>
    <li id="whiteButton"></li>
    <li id="navyButton"></li>
  </ul>

  <h1>Theme Switcher</h1>

  <p>테마를 바꿔봅시다.</p>

  <script>
    /*
      아래 이미지를 참조하여 li를 클릭하면, 아래와 같이 컬러 테마를 바꾸는 기능을 구현하시오.
      body의 background color 와 color 를 직접 조작하여 테마를 바꾸도록 코드를 작성하시오.
      (CSS는 변경할 필요 없음)
      1. li#grayButton 클릭시 background-color는 gray, color는 white로 변경
      2. li#whiteButton 클릭시 background-color는 white, color는 black으로 변경
      3. li#navyButton 클릭시 background-color는 navy, color는 white로 변경
    */
   // 1.
   const obj = document.querySelector('body')
   const gray = document.querySelector('#grayButton')
   gray.addEventListener('click', function(event){
     obj.style.color = 'white'
     obj.style.background = 'gray'
   })
   const white = document.querySelector('#whiteButton')
   white.addEventListener('click', function(event){
     obj.style.color = 'black'
     obj.style.background = 'white'
   })
   const navy = document.querySelector('#navyButton')
   navy.addEventListener('click', function(event){
     obj.style.color = 'white'
     obj.style.background = 'navy'
   })


  </script>
</body>

</html>
```

2.

```js
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>

<body>
  <div>
    Input: <input id="userInput" type="text" autofocus>
  </div>
  <div>
    Output: <span id="output"></span>
  </div>

  <script>
    /* 
      현재 코드에서는 input#userInput에 입력한 내용이 그대로 span#output에 출력된다.
      아래 이미지를 참고하여 badWords에 포함된 단어가 사용자 입력에 포함되어 있을 경우,
      span#output에서 해당 단어를 '**' 로 바꿔 출력하도록 filterMessage 함수를 완성하시오.
    */
    const badWords = ['바보', '멍청', '메롱',]
    const userInput = document.querySelector('#userInput')
    const output = document.querySelector('#output')

    function filterMessage(event) {
      // badWords에 포함된 단어가 입력될 경우, '**'으로 변환하여 output에 출력
      const A = /바보/g;
      const B = /멍청/g;
      const C = /메롱/g;
      filteredInput = event.target.value.replace(A, '**').replace(B, '**').replace(C, '**')
      // filteredInput = event.target.value
      // let i = 1
      // while(i = 1){
      //   let i = 0
      //   for(word of badWords){
      //     if(word.indexOf(filteredInput)){
      //       filteredInput.replace(word, '**')
      //       let i = 1
      //     }
      //   }
      // }
      output.innerText = filteredInput
    }

    userInput.addEventListener('input', filterMessage)   
  </script>
</body>
```

3.

```js
<!DOCTYPE html>
<html lang="en">

<head>
  <title>Document</title>
  <!-- CSS only -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>

<body>

  <div class="container">

    <form id="form" class="my-3">
      <div class="mb-3">
        <input type="text" class="form-control" id="title">
      </div>
      <div class="mb-3">
        <textarea class="form-control" id="content" rows="3"></textarea>
      </div>
      <div class="d-grid gap-2">
        <button class="btn btn-primary">add</button>
      </div>
    </form>

    <section id="cardsSection" class="row">



    </section>

  </div>

  <script>
    /*
      이전 workshop을 참조하여
      사용자가 form 에 title과 content를 입력하고 submit하면, 예시와 같은 카드를 생성하여 div#cardSection에 추가하는 코드를 작성하시오.
      카드가 생성되면 기존에 입력된 input과 textarea의 내용은 삭제되어야 합니다.
      (완성 이후 카드 예시는 삭제)
    */
    const form = document.querySelector('#form')
    const titleInput = document.querySelector('#title')
    const contentInput = document.querySelector('#content')

    form.addEventListener('submit', function(event){
      event.preventDefault()
      const article = document.createElement('article')
      article.classList.add('col-4')

      const card = document.createElement('div')
      card.classList.add('card', 'm-1')

      const cardBody = document.createElement('div')
      cardBody.classList.add('card-title')

      const h5Tag = document.createElement('h5')
      h5Tag.classList.add('card-title')
      h5Tag.innerText = titleInput.value

      const pTag = document.createElement('p')
      pTag.classList.add('card-text')
      pTag.innerText = contentInput.value

      cardBody.append(h5Tag, pTag)
      card.appendChild(cardBody)
      article.appendChild(card)

      const cardsSection = document.querySelector('#cardsSection')
      cardsSection.appendChild(article)

      event.target.reset()


    })

  </script>
</body>

</html>
```

4.

```js
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>

<body>
  <form action="/todos/">
    <input type="text">
    <button>Add</button>
  </form>
  <ul></ul>

  <script>
    /*
    [필수사항]	
      form에서 submit 이벤트가 발생되었을 때 input에 작성된 값이 todo로 추가된다.
      todo는 ul 태그의 li 태그로 추가된다.
      todo가 추가된 후 input value의 값은 초기화 된다.
      
      (선택) 빈 값인 데이터는 입력을 방지한다.
      빈 값이면 알림창을 띄워 값을 입력하도록 안내한다.
    */
    const form = document.querySelector('form')
    const todoInput = document.querySelector('input')
    const todos = document.querySelector('ul')

    form.addEventListener('submit', function(event){
      event.preventDefault()
      const li = document.createElement('li')
      if(todoInput.value){
        li.innerText = todoInput.value
        todos.appendChild(li)
      }
      else{
        alert("입력 하세요!")
      }

      event.target.reset()
    })

  </script>
</body>

</html>
```

5.

```js
<!DOCTYPE html>
<html lang="ko">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <!-- CSS only -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
  <title>Document</title>
  <style>
    html,
    body {
      width: 100%;
      height: 100%;
      margin: 0;
      background-size: cover;
      background-position: center;
    }

    .parent {
      height: 100%;
    }

    #time {
      font-size: 5rem;
      padding: 0 2rem;
      background-color: rgba(0, 0, 0, 0.2);
      border-radius: 10px;
    }

    .row {
      margin: 0;
    }
  </style>
</head>

<body>
  <div class="parent row justify-content-center align-items-center">
    <div id="time" class="font-weight-bold text-light text-center"></div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
  <script>
    /* 
      loadash를 활용하여 body의 배경이미지를 랜덤하게 선택하고,
      div#time의 내부 content가 매 초마다 갱신되어 화면에 출력될 수 있도록 displayTime 함수를 완성하시오.
    */


    // 1. lodash 를 활용하여 1.jpg ~ 6.jpg 중 랜덤한 이미지의 경로로 body의 backgroundImage url을 설정
    const back = document.querySelector('body')
    const IMAGES = ['./images/1.jpg', 'images/2.jpg', './images/3.jpg', './images/4.jpg', 'images/5.jpg', 'images/6.jpg']
    const nums = _.random(0, 5)
    const urls = './images/' + String(nums)
    console.log(IMAGES[nums])
    console.log("url('"+ IMAGES[nums] + "')")
    back.style.backgroundImage = "url('"+ IMAGES[nums] + "')"


    const timeDiv = document.querySelector('#time')
    const displayTime = function () {
      // 2. 아래 now를 활용하여 timeDiv의 innerText를 적절하게 re-format
      const now = new Date()
      timeDiv.innerText = now.toLocaleString('ko-KR').slice(-10)
    }

    // 1초에 한번 displayTime 함수 실행
    setInterval(displayTime, 1000)
  </script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p"
    crossorigin="anonymous"></script>
</body>

</html>
```

