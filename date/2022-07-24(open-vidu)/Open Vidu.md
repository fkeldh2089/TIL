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

3) docker 다운로드 및 실행, 아래 코드를 cmd창에 실행
   - window의 경우 docker 다운로드 후 lts(?) 2버전 까지 기본 설정 완료해야 함
   
   ```bash
   docker run -p 4443:4443 --rm -e OPENVIDU_SECRET=MY_SECRET openvidu/openvidu-server-kms:2.22.0
   ```
4. localhost로 이동하여 화면 확인
   
   - 만약 화면이 뜨지 않는 다면, docker 서버인 4443포트를 확인할 것, https:라서 보안 문제가 있을 수 있다고 경고창이 뜨는데, 한 번 접속해 두면 정상적으로 동작합니다.



### 사용방법

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
   
   
