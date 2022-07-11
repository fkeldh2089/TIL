##### 문제

backend-java를 파일명을 변경하지 않을 경우

`src/main.../dist`를 찾지못한다는 오류가 발생하는데,,



##### 원인

1.  webpack에서 gradle task를 진행할 경우 새로 backend라는 경로가 생기고 그 안에 위의 문제의 경로의 파일이 생기는 것을 확인할 수 있다.

2. 해당 파일이 적당한 경로에 생기지 않아 발생하는 문제로 보입니다.



##### 해결 

1. 간단하게 해당 파일을 복사해서 backend-java의 옳바른 경로로 복사해주면 됩니다.
1. 그냥 파일 이름을 backend로 바꾸는 것이 더 편해보이긴 합니다.





##### 문제 2

backend를 먼저 설정할 경우



##### 원인

`Syntax Error: Error: PostCSS received undefined instead of`의 문구가 뜬다.

##### 해결

`npm install`후 서버를 실행하기 전에

```js

npm rebuild node-sass
```

정확한 원인은 모르겠고, 일단 돌아가긴 한다.