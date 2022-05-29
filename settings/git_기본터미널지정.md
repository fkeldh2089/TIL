------

## 기본 터미널 지정

<aside> 📌 Git bash 사전 설치 필수 [Git 설치](https://www.notion.so/Git-960d56ca6e8f404bba8a16e43898ebb2)

</aside>

- vscode 화면에서 터미널 보기

  - `vscode 화면 상단 → View → Terminal`

    ![image-20220529132138007](C:\Users\dheld\AppData\Roaming\Typora\typora-user-images\image-20220529132138007.png)

### Windows

- 기본 터미널을 

  ```
  powershell → Git Bash
  ```

   로 바꾸기

  - 현재 Windows는 vscode에서 터미널을 열 vs때, 기본적으로 Powershell이 설정 되어 있음

  - 아래 사진에 쓰인 숫자 순서대로 클릭 (`아래 화살표 → 기본 프로필 선택`)

    ![image-20220529132156208](C:\Users\dheld\AppData\Roaming\Typora\typora-user-images\image-20220529132156208.png)

<aside> 💡 **터미널을 닫을 때 X(닫기)와 휴지통의 차이**

`X(닫기)` 버튼은 터미널의 내용은 유지하고 잠시 숨겨두는 것입니다. (Close panel) `휴지통` 버튼은 터미널을 아예 삭제하는 것입니다. (Kill terminal)

따라서 가독성을 위해 잠시 닫아 놓을 때는 `X(닫기)` 버튼을, 터미널을 삭제하고 싶을 때는 `휴지통` 버튼을 사용해야 하는 점 잊지 말기!

</aside>

- [선택] 위 방법으로 기본 터미널 설정이 되지 않는다면

  1. `ctrl(command) + shift + p` → `default` 검색 → `Terminal: Select Default Profile` 선택 → `Git bash` 선택

     ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/031f922f-f4ee-48d6-b6c1-5e988be73a78/(7).png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/031f922f-f4ee-48d6-b6c1-5e988be73a78/(7).png)

  2. `ctrl(command) + shift + p` → `json` 검색 → `Preferences: Open Settings (JSON)` 선택

     ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7a2fbf97-5942-4302-a448-00c60b84bd9a/1123.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7a2fbf97-5942-4302-a448-00c60b84bd9a/1123.png)

  ### Windows

  - 하단 코드 작성

    ```json
    // settings.json
    
    {
        ... 생략 ...,
    
        **"terminal.integrated.profiles.windows": {
            "PowerShell": null,
            "Windows PowerShell": null,
            "Command Prompt": null,
            "Git Bash": {
                "source": "Git Bash",
                "path": "C:\\\\Program Files\\\\Git\\\\bin\\\\bash.exe",
            }
        },
        "terminal.integrated.defaultProfile.windows": "Git Bash"**
    }
    ```

  ### macOS

  - 하단 코드 작성

    ```json
    // settings.json
    
    {
        ... 생략 ...,
    
        **"terminal.integrated.profiles.osx": {
            "zsh": {
                "path": "/bin/zsh",
            }
        },
        "terminal.integrated.defaultProfile.osx": "zsh"**
    }
    ```

------

### macOS

- Windows 진행순서와 동일하며 다른 점은 bash가 아닌 `**zsh`을 기본 터미널로 선택**

  ![image-20220529132210997](C:\Users\dheld\AppData\Roaming\Typora\typora-user-images\image-20220529132210997.png)

------