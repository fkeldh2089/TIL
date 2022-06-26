1.  Semantic Tag

​		- header, h1, section, footer, a, form

```html

```

2. input Tag

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
  <div>
    <label for="username">USERNAME : </label>
    <input type="text" name="username" id="username" autofocus>
  </div>
  <div>
    <label for="pass">PWD : </label>
    <input type="password" name="pass" id="pass" autofocus>
    <input type="submit" value="제출">
  </div>
</body>
</html>

```

3. 크기 단위

​		- rem

```html
```

4. 선택자

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    div p{
      color:crimson;
    }

    /* div > p{
      color:crimson;
    } */
  </style>

</head>
<body>
<div> 
  <h1>
    <p>야야야</p>
  </h1>
  
  <p>야야야야</p>
<div>
<div>
  <div>
    <p>야야야야야</p>
  </div>
</div>

  
  
</body>
</html>
```

위와 같이 예제 코드를 짠다면, 자손 결합자의 경우 모든 텍스트가 crimson으로 출력되는 것을 알 수 있다.

하지만 자식 결합자의 경우,`야야야`는 crimson으로 변하지 않는 것을 확인할 수 있다. 여기서 자손 결합자의 경우 div 밑의 p는 모두 영향을 받고, 자식 결합자의 경우 div 바로 밑의 p가 아닌 경우는 영향을 받지 않음을 알 수 있다.
