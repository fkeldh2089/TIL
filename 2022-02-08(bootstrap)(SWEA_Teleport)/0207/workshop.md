```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="style.css">
  <title>Document</title>
</head>
<body>
  <!-- 1. Nav -->
  <nav class="navbar navbar-dark bg-dark fixed-top mx-0 justify-content-between">
    <a href="#">
      <img src="images/logo.png" alt="Logo Image">
    </a>

    
    <ul class="nav justify-content-end gap-3 list-unstyled mb-0">
      <li class="nav-item ">
        <a class="nav-link text-light text-decoration-none" href="#">Home</a>
      </li>
      <li class="nav-item ">
        <a class="nav-link text-light text-decoration-none" href="#">Community</a>
      </li>
      <li class="nav-item ">
        <a class="nav-link text-light text-decoration-none" href="#">Login</a>
      </li>
    </ul>

  </nav>

  <!-- 2. Header -->
  <header class="text-center d-flex flex-column justify-content-center">
      <strong class="display-2 text-light">Cinema</strong>
      <strong class="display-2 text-light">Community</strong>

      <div class="col-12 my-5">
        <button type="submit" class="btn btn-lg  btn-primary">Let's Go</button>
      </div>
  </header>

  <!-- 3. Section -->
  <section>
    <h2 class="text-center my-5">Used Skills</h2>
    <article class="text-center d-flex flex-row justify-content-around">
      <div>
        <img src="images/web.png" alt="Web Image">
        <p>Web</p>
      </div>
      <div>
        <img src="images/html5.png" alt="HTML5 Image">
        <p>HTML5</p>
      </div>
      <div>
        <img src="images/css3.png" alt="CSS3 Image">
        <p>CSS3</p>
      </div>
    </article>
  </section>

  <!-- 4. Footer -->
  <footer class="fixed-bottom text-center text-align-center text-light bg-primary" style="height:30px;">
    <p class="mb-0">HTML & CSS project. Created by Hong</p>
  </footer>
</body>
</html>

```

CCS를 위주로 아래의 코드를 완성 시키고, DOC을 보면서 위의 코드로 변환하였다.





```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="style.css">
  <title>Document</title>
  <style>
    .fontwhite{
      color : white;
    }
    .fontcenter{
      text-align: center;
    }
    .headerfont{
      font-weight: bold;
    }
    .headerposition{
      display: flex;
      text-align: center;
      flex-direction: column;
      justify-content: center;
      
    }
    .usedskill{
      display: flex;
      text-align: center;
      flex-direction: row;
      justify-content: center;
    }
    .navigationb{
      justify-content: right;
    }
    .navigationa{
      justify-content: left;
    }
    .footerpo{
      position: fixed;
      width: 100%;
      height: 30px;
      line-height: 30px;
      text-align: center;
      bottom:0;
      background-color: blue;
    }
    .hea{
      position: fixed;
      top:0;
      width:100%;

    }
    .wid{
      justify-content: space-between;
    }

  </style>
</head>
<body>
  <!-- 1. Nav -->
  <nav class="navbar navbar-dark bg-dark hea mx-0 wid">
    <a href="#">
      <img src="images/logo.png" alt="Logo Image">
    </a>

    
    <ul class="nav justify-content-end gap-3">
      <li class="nav-item ">
        <a class="nav-link fontwhite" href="#">Home</a>
      </li>
      <li class="nav-item ">
        <a class="nav-link fontwhite" href="#">Community</a>
      </li>
      <li class="nav-item ">
        <a class="nav-link fontwhite" href="#">Login</a>
      </li>
    </ul>

  </nav>

  <!-- 2. Header -->
  <header class="headerposition">
      <h1 class="display-2 fontwhite headerfont">Cinema</h1>
      <h1 class="display-2 fontwhite headerfont">Community</h1>

      <div class="col-12 my-5">
        <button type="submit" class="btn btn-primary">Let's Go</button>
      </div>
  </header>

  <!-- 3. Section -->
  <section>
    <h2 class="fontcenter">Used Skills</h2>
    <article class="usedskill">
      <div>
        <img src="images/web.png" alt="Web Image">
        <p>Web</p>
      </div>
      <div>
        <img src="images/html5.png" alt="HTML5 Image">
        <p>HTML5</p>
      </div>
      <div>
        <img src="images/css3.png" alt="CSS3 Image">
        <p>CSS3</p>
      </div>
    </article>
  </section>

  <!-- 4. Footer -->
  <footer class="footerpo fontcenter fontwhite bg-primary">
    <p>HTML & CSS project. Created by Hong</p>
  </footer>
</body>
</html>

```

