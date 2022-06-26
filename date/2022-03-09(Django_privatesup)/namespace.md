# 개인 보충

### templates namespace

발단 : 저번 수업 도중, 앱 하단에 templates 경로를 만들 때, ㄱ.`template/index.html`이 아니라, ㄴ.`template/apps/index.html`이라고 만들길래, 이유가 있나~ 했었다. 시간이 있을 때 찾아보기로함,



결과 :  ㄱ과 같이 경로를 설정할 경우, 앱이 여러 개를 만들 경우에 namespace가 겹칠 확률이 높아진다. 개인적인 생각으로는, Django가 templates를 찾을 때 해당 앱의 하단에서 찾을 줄 알았는데, setting에 등록되어있는 순서대로 찾아 간다고 한다. 

url mapping 할 때에도 `app_name`을 설정하지 않으면, namespace가 겹칠 가능성이 있다.





### HTML form

발단 : `name`,  `id` 등 이 수업을 들을 때에는 이해가 간다고 생각했는데, 혼자해보면서 헷갈리는 점이 있었다.



결과 : 

- action : 입력 데이터가 전송될 URL 지정
- method : 입력 데이터 전달 방식 지정(GET)
- name: HTML의 input element로, GET/POST 방식으로 서버에 전달하는 패러미터(dictionary 형태)를 가져올 수 있다.