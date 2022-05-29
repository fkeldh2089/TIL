------

# Git init 후 브랜치이름 출력하도록 하기

## 1. 터미널 열기

![image-20220529132301319](C:\Users\dheld\AppData\Roaming\Typora\typora-user-images\image-20220529132301319.png)

## 2. **터미널에 명령어 입력하기**

![image-20220529132308249](C:\Users\dheld\AppData\Roaming\Typora\typora-user-images\image-20220529132308249.png)

- 터미널에 아래 명령어를 입력합니다.

```bash
$ code ~/.zshrc
```

- 그러면 vscode가 켜지고, .zshrc 파일이 열림

<aside> ❗ 혹시 `code ~/.zshrc`라고 입력하면 `code: command not found` 라고 나오나요? 그렇다면 아래 블로그를 참고해서 조치를 취해봅시다!

</aside>

[맥 터미널에서 code 명령어가 실행이 안되는 경우 해결 방법](https://smilehugo.tistory.com/entry/code-command-is-not-working-on-mac-how-to-solve)

## 3. vscode에 아래의 내용 복사-붙여넣기 하기

```bash
# Find and set branch name var if in git repository.

function git_branch_name()
{
  branch=$(git symbolic-ref HEAD 2> /dev/null | awk 'BEGIN{FS="/"} {print $NF}')
  if [[ $branch == "" ]];
  then
    :
  else
    echo '- ('$branch')'
  fi
}

# Enable substitution in the prompt.
setopt prompt_subst

# Config for prompt. PS1 synonym.
prompt='%2/ $(git_branch_name) > '
```

- 화면예시

  ![image-20220529132319887](C:\Users\dheld\AppData\Roaming\Typora\typora-user-images\image-20220529132319887.png)

## 4. 터미널 종료 후 재시작

- **열려있는 모든 터미널 (vscode 포함)을 종료하고 다시 시작**

## 5. 결과 확인

- `$ git init`을 해보면 master 표시가 잘 나타나는 것을 확인

  ![image-20220529132325910](C:\Users\dheld\AppData\Roaming\Typora\typora-user-images\image-20220529132325910.png)