1. 기본 그리드 레이아웃

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="style.css">
  <title>practice1</title>
</head>
<body>
  <div class="container">
    <div class="row">
      <div class="col">
        <h1>Bootstrap Grid System 1</h1>
      </div>
    </div>

    <!-- 1. -->
    <div class="row">
      <div class="item col-4 ">
        <p>1</p>
      </div>
      <div class="item col-4 ">
        <p>2</p>
      </div>
      <div class="item col-4 ">
        <p>3</p>
      </div>
    </div>

    <!-- 2. -->
    <div class="row">
      <div class="item col-6">
        <p>1</p>
      </div>
      <div class="item col-6">
        <p>2</p>
      </div>   
    </div>

    <!-- 3. -->
    <div class="row">
      <div class="item col-3">
        <p>3</p>
      </div>  
      <div class="item col-6">
        <p>6</p>
      </div>
      <div class="item col-3">
        <p>3</p>
      </div>
    </div> 
    
    <!-- 4. -->
    <div class="row">
      <div class="item col-2">
        <p>1</p>
      </div>
      <div class="item col-7">
        <p>2</p>
      </div>
      <div class="item col-3">
        <p>3</p>
      </div> 
    </div>
  </div>
  
</body>
</html>

```



2. 반응형 그리드

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="style.css">
  <title>practice2</title>
</head>
<body>
  <div class="container">
    <div class="row">
      <div class="col">
        <h1>Bootstrap Grid System 2</h1>
      </div>
    </div>

    
    <!-- 1. -->
    <div class="row">
      <div class="item col-4 col-sm-2">
        <p>576px 미만 4 <br> 576px 이상 2</p>
      </div>
      <div class="item col-4 col-sm-5">
        <p>576px 미만 4 <br> 576px 이상 5</p>
      </div>
      <div class="item col-4 col-sm-5">
        <p>576px 미만 4 <br> 576px 이상 5</p>
      </div>
    </div>


    <!-- 2. -->
    <div class="row">
      <div class="item col-1 col-md-2">
        <p>768px 미만 1 <br> 768px 이상 2</p>
      </div>
      <div class="item col-3 col-md-3">
        <p>768px 미만 3 <br> 768px 이상 3</p>
      </div>
      <div class="item col-4 col-md-3">
        <p>768px 미만 4 <br> 768px 이상 3</p>
      </div>
      <div class="item col-1 col-md-2">
        <p>768px 미만 1 <br> 768px 이상 2</p>
      </div>
      <div class="item col-3 col-md-2">
        <p>768px 미만 3 <br> 768px 이상 2</p>
      </div>
    </div>


    <!-- 3. -->
    <div class="row">
      <div class="item col-4 col-sm-3 col-md-6">
        <p>576px 미만 4 <br> 768px 미만 3 <br> 768px 이상 6</p>
      </div>
      <div class="item col-6 col-sm-3 col-md-6">
        <p>576px 미만 6 <br> 768px 미만 3 <br> 768px 이상 6</p>
      </div>
      <div class="item col-2 col-sm-6 col-md-12">
        <p>576px 미만 2 <br> 768px 미만 6 <br> 768px 이상 12</p>
      </div>
    </div>


    <!-- 4. -->
    <div class="row">
      <div class="item col-12 col-md-4 col-xl-2">
        <p>768px 미만 12 <br> 768px 이상 4 <br> 1200px 이상 2</p>
      </div>
      <div class="item col-12 col-md-4 col-xl-2">
        <p>768px 미만 12 <br> 768px 이상 4 <br> 1200px 이상 2</p>
      </div>
      <div class="item col-12 col-md-4 col-xl-12">
        <p>768px 미만 12 <br> 768px 이상 4 <br> 1200px 이상 12</p>
      </div>
    </div>
  </div>
  
</body>
</html>
```



3. 그리드 심화

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="style.css">
  <title>practice3</title>
</head>
<body>
  <div class="container">
    <div class="row">
      <div class="">
        <h1>Bootstrap Grid System 3</h1>
      </div>
    </div>

    <!-- 1. -->
    <div class="row">
      <div class="item col-4 col-md-4">
        <p>item1</p>
      </div>
      <div class="item col-8 offset-md-4 col-md-4">
        <p>item2</p>
      </div>
    </div>


    <!-- 2. -->
    <div class="row">
      <div class="item col-4 offset-md-4 col-md-4 offset-lg-7 col-lg-5">
        <p>item1</p>
      </div>
      <div class="item offset-4 col-4  offset-md-0 col-md-4 offset-lg-2 col-lg-8">
        <p>item2</p>
      </div>
    </div>
    

    <!-- 3. -->
    <div class="row">
      <div class="item col-12 col-md-3 col-lg-3">
        item1
      </div>
      <div class="item col-12 col-md-9 col-lg-9">
        <div class="row">
          <div class="item col-6 col-md-6 col-lg-3">item2</div>
          <div class="item col-6 col-md-6 col-lg-3">item3</div>
          <div class="item col-6 col-md-6 col-lg-3">item4</div>
          <div class="item col-6 col-md-6 col-lg-3">item5</div>
        </div>
      </div>
    </div>
  </div>
  
</body>
</html>
```

