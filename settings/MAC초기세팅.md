- 초반 커스텀 참고

  https://subicura.com/mac/dev/

  - [주의] CLI 프로그램은 설치한다면 **neovim 플러그인까지만 설치**! (플러그인 너무 무거움)

```bash
$ chsh -s /bin/zsh
```

------

## 패키지 관리자

### Command Line Tools

```bash
$ xcode-select --install

# gcc test

$ gcc
clang: error: no input files
```

### Homebrew

```bash
$ /usr/bin/ruby -e "$(curl -fsSL <https://raw.githubusercontent.com/Homebrew/install/master/install>)"

# brew test
$ brew doctor
Your system is ready to brew.

# mas
$ brew install mas
```

### ZSH

```bash
# iterm2
$ brew install --cask iterm2

# zsh
$ brew install zsh-completions

# oh-my-zsh
$ sh -c "$(curl -fsSL <https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh>)"
$ source ~/.zshrc

# plugin -1
$ brew install zsh-syntax-highlighting
$ echo 'source /usr/local/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh' >> ~/.zshrc

# plugin -2
$ brew install zsh-autosuggestions
$ echo 'source /usr/local/share/zsh-autosuggestions/zsh-autosuggestions.zsh' >> ~/.zshrc

$ source ~/.zshrc
```

### GIT

```bash
$ brew install git git-lfs

# 설정
$ git lfs install
$ echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.zshrc
$ git config --global user.name "Your Name Here"
$ git config --global user.email "your_email@youremail.com"
$ git config --global credential.helper osxkeychain
$ git config --global core.precomposeunicode true
$ git config --global core.quotepath false
```

### 기타

```bash
# optional, but recommended:
$ brew install openssl readline sqlite3 xz zlib
```