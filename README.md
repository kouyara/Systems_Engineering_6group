# システムエンジニアリング演習6班

## 概要
システムエンジニアリング演習6班のwebアプリ。
アンケート等のフォームが動作し、アンケート結果をグラフ描画できる。

python version : 3.9.x

## インストール&セットアップ
### Windowsの場合:
1. リポジトリをクローン:
   ```bash
   git@github.com:kouyara/Systems_Engineering_6group.git
   ```
   ディレクトリに移動する:
   ```bash
   cd Systems_Engineering_6group
   ```
2. pyenv-winを取得:
   ```bash
   git clone https://github.com/pyenv-win/pyenv-win.git $HOME/.pyenv
   ```
   「ユーザー環境変数」の「Path」に次の3つPathを先頭付近に設定:
   ```bash
   %USERPROFILE%\.pyenv\pyenv-win\shims
   %USERPROFILE%\.pyenv\pyenv-win\bin
   %USERPROFILE%\.pyenv
   ```
   インストール済みの Python バージョン一覧を表示:
   ```bash
   pyenv versions
   ```
   Pythonバージョン 3.9.23 をインストール:
   ```bash
   pyenv install 3.9.23
   ```
   Pythonバージョン 3.9.23 を設定:
   ```bash
   pyenv global 3.9.23
   pyenv local 3.9.23
   ```
3. 仮想環境 venv を作成:
   ```bash
   python3 -m venv .venv
   ```
   仮想環境 venv をアクティベート:
   ```bash
   ./.venv/Scripts/activate
   ```
   依存パッケージをインストールする:
   ```bash
   pip install -r requirements.txt
   ```
### Macの場合:
1. リポジトリをクローン:
   ```bash
   git@github.com:kouyara/Systems_Engineering_6group.git
   ```
   ディレクトリに移動する:
   ```bash
   cd Systems_Engineering_6group
   ```
2. pyenv-winを取得:
   ```bash
   git clone https://github.com/pyenv-win/pyenv-win.git $HOME/.pyenv
   ```
   ~/.zshrc に下記のPathを追加:
   ```
   export PYENV_ROOT="$HOME/.pyenv"
   export PATH="$PYENV_ROOT/bin:$PATH"
   eval "$(pyenv init --path)"
   eval "$(pyenv init -)"
   ```
   shellの設定を読み込ませる:
   ```bash
   source ~/.zshrc
   ```
   インストール済みの Python バージョン一覧を表示:
   ```bash
   pyenv versions
   ```
   Pythonバージョン 3.9.23 をインストール:
   ```bash
   pyenv install 3.9.23
   ```
   Pythonバージョン 3.9.23 を設定:
   ```bash
   pyenv global 3.9.23
   pyenv local 3.9.23
   ```
3. 仮想環境 venv を作成:
   ```bash
   python3 -m venv .venv
   ```
   仮想環境 venv をアクティベート:
   ```bash
   source ./.venv/bin/activate
   ```
   依存パッケージをインストールする:
   ```bash
   pip install -r requirements.txt
   ```

## アプリの起動
ローカル環境でアプリを起動するには、以下のコマンドを実行
```bash
streamlit run app.py
```

docker build -t app .
docker run -p 8501:8501 app