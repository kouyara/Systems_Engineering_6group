# システムエンジニアリング演習6班

## 概要
本アプリは、システムエンジニアリング演習6班が開発したWebアプリケーションです。  
アンケートフォームの作成および送信、集計結果のグラフ表示が可能です。

- **Pythonバージョン**：3.9.x
- **フレームワーク**：Streamlit
- **コンテナ環境**：Docker

## インストール & セットアップ手順
### 1. リポジトリをクローン
   ```bash
   git clone git@github.com:kouyara/Systems_Engineering_6group.git
   cd Systems_Engineering_6group
   ```
### 2. Docker Desktop のインストール
   以下のリンクからDocker Desktopをインストールしてください:
   https://www.docker.com/ja-jp/products/docker-desktop/
### 3. Docker Composeをビルド:
   ```bash
   docker compose up --build
   ```

## アプリの起動
Docker Composeを起動:
```bash
docker compose up
```
起動後、以下のURLにアクセスしてください：
http://0.0.0.0:8501/

ローカル環境でStreamlitを起動する場合:
```bash
streamlit run app.py
```

docker run -it --rm \
  -v $(pwd):/app \
  -w /app \
  -p 8080:8080 \
  app