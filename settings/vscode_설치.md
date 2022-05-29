------

<aside> 📌 이미 설치되어 있어도 설치 단계에서의 설정이 다를 수 있기 때문에 **반드시 재설치**

</aside>

<aside> 💡 **Visual Studio Code 왜 쓰나요?**

- Vscode는 마이크로소프트에서 개발한 코드 에디터의 한 종류
- Windows, Mac, Linux를 모두 지원
- 기존 개발 도구들 보다 가볍고 빠르다는 장점
- 전 세계에서 사랑 받는 굉장한 점유율의 에디터
- Extension을 통해 다양한 기능을 설치할 수 있어서, 무한한 확장성을 가짐
- 무료로 사용 가능

</aside>

**다운로드**

- https://code.visualstudio.com/ 로 이동
  - 화면 중앙 Download 버튼을 통해 다운로드

## Windows

### 설치

- 순서대로 진행

  ![image-20220529131838318](C:\Users\dheld\AppData\Roaming\Typora\typora-user-images\image-20220529131838318.png)

  ![image-20220529131853576](C:\Users\dheld\AppData\Roaming\Typora\typora-user-images\image-20220529131853576.png)

  ![image-20220529131904303](C:\Users\dheld\AppData\Roaming\Typora\typora-user-images\image-20220529131904303.png)

### 설치 확인

1. vscode 실행을 원하는 폴더 내에서 마우스 우클릭을 통해 `Code(으)로 열기` 옵션이 있는 지 확인 **(만약 해당 옵션이 없다면 vscode를 재 설치해야 함)**

   ![image-20220529131918936](C:\Users\dheld\AppData\Roaming\Typora\typora-user-images\image-20220529131918936.png)

2. `Code(으)로 열기` 옵션을 클릭 했을 때 vscode가 정상적으로 실행되는 지 확인합니다.

   

------

## macOS

### 설치

- macOS의 경우는 설치과정에서 Windows와 다르게 라이선스 동의 과정이 없을 수 있음

- 링크의 zip 파일을 열어 생긴 .app 파일을 더블클릭 후 설치

  ![image-20220529131945597](C:\Users\dheld\AppData\Roaming\Typora\typora-user-images\image-20220529131945597.png)

- 설치가 완료 되었다면 하단 바에서 vscode 아이콘을 확인

  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5996c742-5aa8-4311-8187-9600dd33a932/Untitled.png)

### [OpenInTerminal](https://github.com/Ji4n1ng/OpenInTerminal) 설치

- macOS는 Windows와 달리 `Code(으)로 열기` 기능이 설정되지 않음
- `OpenInTerminal`이라는 프로그램을 별도로 설치 후 설정 필요

<aside> ❗ 사전 [macOS 초기 설정](https://www.notion.so/macOS-52abdd7d62604f90b99b970abd3054bb) 필수

</aside>

**설치**

```bash
$ brew install --cask openinterminal
```

**설정**

1. System Preferences

   ![image-20220529132001192](C:\Users\dheld\AppData\Roaming\Typora\typora-user-images\image-20220529132001192.png)

2. Extensions

   ![image-20220529132007192](C:\Users\dheld\AppData\Roaming\Typora\typora-user-images\image-20220529132007192.png)

3. Finder Extensions, 체크박스 체크

   ![image-20220529132014419](C:\Users\dheld\AppData\Roaming\Typora\typora-user-images\image-20220529132014419.png)

**환경설정**

1. openinterminal 실행

   ![image-20220529132022629](C:\Users\dheld\AppData\Roaming\Typora\typora-user-images\image-20220529132022629.png)

2. 기본 terminal 및 text editor 설정

   ![image-20220529132027373](C:\Users\dheld\AppData\Roaming\Typora\typora-user-images\image-20220529132027373.png)

3. 단축키 설정

   - 자유롭게 설정 가능하나 기본 단축키와 중복되지 않도록 주의

   ![image-20220529132036057](C:\Users\dheld\AppData\Roaming\Typora\typora-user-images\image-20220529132036057.png)

   이제 단축키 사용 시 현재 위치경로를 기준으로 터미널 혹은 vscode를 실행 할 수 있음

------

## 확장프로그램

### Python Extention

<aside> ❗ Python 사전 설치 필수

</aside>

- 순서대로 진행

  ![image-20220529132045785](C:\Users\dheld\AppData\Roaming\Typora\typora-user-images\image-20220529132045785.png)

- **python 환경설정 관련 코드 작성 (+ `editor tabsize` 설정)**

  ![image-20220529132056681](C:\Users\dheld\AppData\Roaming\Typora\typora-user-images\image-20220529132056681.png)

  `ctrl(command) + shift + p` → `json` 검색 → `Preferences: Open Settings (JSON)` 선택

  ```jsx
  // settings.json
  
  {
      ... 생략 ...,
  
      **"editor.tabSize": 2,
  
      // python
      "[python]": {
          "editor.insertSpaces": true,
          "editor.tabSize": 4
      },
      "python.languageServer": "Pylance",
      "python.analysis.extraPaths": ["./sources"],**
  }
  ```