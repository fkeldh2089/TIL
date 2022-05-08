```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lunch & Lotto</title>
</head>

<body>
  <div id="app">
    <h2>점심메뉴</h2>
    <button @click="ChoiceMenu">Pick One</button>
    <p>{{menu}}</p>
    <hr>

    <h2>로또</h2>
    <button @click="ChoiceNums">Get Lucky Numbers</button>
    <p>{{nums}}</p>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.20/lodash.min.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        menu : '뭐먹을까?',
        menus:['국밥', '찜닭', '제육'],
        nums: ['오늘의 로또?']
      },
      methods:{
        ChoiceMenu: function(){
          //console.log('왜 안돼')
          //console.log(`${this.menus}`)
          num = _.random(0, this.menus.length-1);
          this.menu = this.menus[num]
        },
        ChoiceNums: function(){
          nums = []
          for(let i=1; i<=50; i++){
            nums.push(i)
          }
          lucky_nums = _.sampleSize(nums, 6)
          this.nums = lucky_nums
        }
      }
    })
  </script>
</body>

</html>
```

