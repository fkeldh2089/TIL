------

## Windows

### 다운로드

- https://www.python.org/downloads/release/python-399/로 이동 후 페이지 최하단 이동

### 설치

- 설치 전 본인의 CPU 구조(32bit/64bit) 확인하기

- 순서대로 진행

  ![image-20220529131528575](C:\Users\dheld\AppData\Roaming\Typora\typora-user-images\image-20220529131528575.png)

  ![img](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2b471011-b4ff-4385-aa29-4109993cf7c1/4.png)

  `git bash가 있다면 git bash에서도 확인 가능`

  설치 확인

------

## macOS

- Homebrew 사전 설치 필수 [macOS 초기 설정](https://www.notion.so/macOS-52abdd7d62604f90b99b970abd3054bb)

### 다운로드 및 설치

<aside> ❗ **m1 칩셋 사용자인 경우 `For m1` 부분에서 진행**

</aside>

- `For m1`

  <aside> ❗ Apple Silicon Native은 `3.9.1` 이상부터 지원합니다.

  </aside>

  [List of Homebrew Formulae that work on Apple Silicon?](https://doesitarm.com/kind/homebrew/)

  - Command Line Tools 설치

    ```bash
    $ xcode-select --install
    ```

  - Homebrew를 이용하여 pyenv 설치

    ```bash
    $ brew install pyenv
    ```

  - `3.9.1` 버전부터 Apple Silicon Native 지원

    ```bash
    $ echo 'eval "$(pyenv init --path)"' >> ~/.zprofile
    $ echo 'eval "$(pyenv init -)"' >> ~/.zshrc
    $ exec "$SHELL"
    
    $ pyenv install 3.9.9
    $ pyenv global 3.9.9
    ```

    ```bash
    $ python -V
    Python 3.9.9
    ```

**pyenv 설치**

```bash
$ brew install pyenv
$ echo 'eval "$(pyenv init --path)"' >> ~/.zprofile
$ echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

- 터미널 종료 후 재시작

  ```python
  $ pyenv -v
  ```

**Python 설치 및 적용**

```bash
$ pyenv install 3.9.9
$ pyenv global 3.9.9
```

**설치 확인**

```bash
$ python -V
Python 3.9.9
```

- **설치 후에도 python 버전이 2.x.x가 출력되는 경우**

  ```bash
  $ code ~/.zprofile
  ```

  ```bash
  eval "$(pyenv init --path)"
  ```

  ```bash
  $ source ~/.zprofile 
  ```

  ```bash
  $ code ~/.zshrc
  ```

  ```bash
  eval "$(pyenv init -)"
  ```

  ```bash
  $ source ~/.zshrc
  ```

  ```bash
  $ python -V
  Python 3.9.9
  ```