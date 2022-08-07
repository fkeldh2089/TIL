# Open Vidu

### 실행

1) 깃 클론,

```bash
git clone https://github.com/OpenVidu/openvidu-tutorials.git -b v2.22.0
```

2) 원하는 튜토리얼(vue, 등등) 파일에 npm 설치

```bash
cd openvidu-tutorials/openvidu-insecure-vue
npm install
npm run serve
```
   - 이 때 아래와 같은 에러가 발생한다면,

      ![image-20220804080517141](../../../../AppData/Roaming/Typora/typora-user-images/image-20220804080517141.png)

     `npm install --save --legacy-peer-deps`으로 해결

3. docker 다운로드 및 실행, 아래 코드를 cmd창에 실행

   - window의 경우 docker 다운로드 후 lts(?) 2버전 까지 기본 설정 완료해야 함

   ```bash
   docker run -p 4443:4443 --rm -e OPENVIDU_SECRET=MY_SECRET openvidu/openvidu-server-kms:2.22.0
   ```

4. localhost로 이동하여 화면 확인
   
   - 만약 화면이 뜨지 않는 다면, docker 서버인 4443포트를 확인할 것, https:라서 보안 문제가 있을 수 있다고 경고창이 뜨는데, 한 번 접속해 두면 정상적으로 동작합니다.

### 사용방법

: 새로운 환경

1. 비디오 토글, 오디오 토글
   
   - 아래의 코드를 method에 추가한 후 사용

```javascript
toggleVideo(){
            this.publishVideo = !this.publishVideo;
            if(this.publishVideo){
                this.publisher.publishVideo(true)
            }
            else{
                this.publisher.publishVideo(false)
            }
        },
        toggleAudio(){
            this.publishaudio = !this.publishaudio;
            if(this.publishaudio){
                this.publisher.publishAudio(true)
            }
            else{
                this.publisher.publishAudio(false)
            }
        },
```

2. 유저가 비디오나 오디오를 끄고 있는지 확인하는 방법
   
   ```javascript
           connectionData () {
               const { connection } = this.streamManager.stream;
               console.log(connection.stream.videoActive)
               return JSON.parse(connection.stream.videoActive);
           },
   ```
   
   - 위에서 볼 수 있 듯이 `streamManager.stream.stream.videoActive`
   
   - 오디오는 `streamManager.stream.stream.audioActive`

3. 해당 유저가 떠들고 있는가?

```javascript
        isSpeech: function(){
            this.streamManager.on('publisherStartSpeaking', (event) => {
            console.log('User in data ' + event.connection.connectionId + ' start speaking');
            this.sp = true
        });

            this.streamManager.on('publisherStopSpeaking', (event) => {
            console.log('User ' + event.connection.connectionId + ' stop speaking');
            this.sp=false
        });
            return this.sp
        }
```

- 이거 한 사람의 비디오를 중복해서 띄워둘 경우 recursive error 발생, option API 의 경우 해결 가능





### 과제

1. watched 를 이용한 함수들이 recursive하게 동작한다.

2.  메세지를 보낼때마다 등차수열로 많이 보낸다.

   - 둘 모두 watched를 computed로 바꾸면 해결될 듯 보인다. - 안된다 

   - 메세지는 computed로 해결이 되지만, 오디오의 활성화 여부를 알려주는 함수는 여전히 recursive 오류 존재

게임 진행 자체는 소켓을 쓰지 않고도 사용 가능 할 듯, 채팅 또한 그럴듯

여기서 문제가 소켓을 사용할 경우에는 직접 변수들을 쪼개서 세션별로 만들어줘야하고, 초기화도 신경 써줘야 할듯 이거에 대해서는 월욜에 물어보고 진행 하면 될듯 합니다. 대강 로직만 짜면 게임은 돌릴 수 있을 정도가 됐기는 했는데,,,



1. 방 입장 버튼을 누른 후 router를 통하여 다른 페이지로 연결 될것 같은데 그것에 대한 구현이 부족할 듯 싶다.
2. 소켓 소켓 소켓 안쓰다가 쓰려니 조금 어렵다.
3. 게임 도중에 난입하거나 탈주하거나 하는 경우 간단하게 숫자만 동기화 시키면 될지 알았는데, 생각보다 그냥 구현하는게 복잡하더라. 예외 상황 생길 경우는 모두 게임 자체를 종료하는 것이 마음이 편할 듯 싶다.
4. 세션별로 변수 쪼개고 초기화 등등을 오픈비두는 무려 그냥 해준다.
