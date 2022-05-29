------

## 준비사항

### Vue project

- 완성된 프로젝트

## Deploy

### netlify

- 사이트 로그인

  ![image-20220529130305323](vue_배포.assets/image-20220529130305323.png)

- build

```bash
npm run build
```

- dist 폴더 생성 확인
- dist폴더 업로드

### env

<aside> 📌 환경변수 설정시 사용합니다.

</aside>

- `Site settings` > `Build & deploy` > `Environment`

  ![image-20220529130317569](vue_배포.assets/image-20220529130317569.png)

## 도메인 연결

- Site settings > Domain management > Domains >Add custom domain

  !![image-20220529130327590](vue_배포.assets/image-20220529130327590.png)

- check DNS configuration

  ![image-20220529130341090](vue_배포.assets/image-20220529130341090.png)

- IP 주소 확인

  ![image-20220529130348395](vue_배포.assets/image-20220529130348395.png)

- route53 설정

  ![image-20220529130355952](vue_배포.assets/image-20220529130355952.png)

- 새로고침 후 check 확인

  ![image-20220529130404217](vue_배포.assets/image-20220529130404217.png)

- SSL > Verify DNS configuration

  ![image-20220529130411375](vue_배포.assets/image-20220529130411375.png)

- 일정시간 후 인증 완료

  ![image-20220529130418313](vue_배포.assets/image-20220529130418313.png)