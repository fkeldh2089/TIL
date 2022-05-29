------

## vscode django extension 설치



![image-20220529131347741](C:\Users\dheld\AppData\Roaming\Typora\typora-user-images\image-20220529131347741.png)

------

## django extension 설정

1. `ctrl(command) + shift + p` → `json`검색 → `Preferences: Open Settings (JSON)` 선택

   ![image-20220529131357753](C:\Users\dheld\AppData\Roaming\Typora\typora-user-images\image-20220529131357753.png)

2. 설정 코드 작성

   ```jsx
   // settings.json
   
   {
     ... 생략 ...,
   
     // Django
     **"files.associations": {
       "**/*.html": "html",
   	    "**/templates/**/*.html": "django-html",
       "**/templates/**/*": "django-txt",
       "**/requirements{/**,*}.{txt,in}": "pip-requirements"
     },
     "emmet.includeLanguages": {
       "django-html": "html"
     }**
   }
   ```