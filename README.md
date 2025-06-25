# システムエンジニアリング演習6班

## 概要
システムエンジニアリング演習6班のwebアプリ。
アンケート等のフォームが動作し、アンケート結果をグラフ描画できる。

## インストール&セットアップ
1. リポジトリをクローン
   ```bash
   git@github.com:kouyara/Systems_Engineering_6group.git
   ```
2. ディレクトリに移動する
   ```bash
   cd Systems_Engineering_6group
   ```
3. 仮想環境を作成
   ```bash
   python3 -m venv .venv
   ```
4. 仮想環境をアクティベート
   ```bash
   source .venv/bin/activate
   ```
5. 依存パッケージをインストールする
   ```bash
   pip install -r requirements.txt
   ```

## アプリの起動
ローカル環境でアプリを起動するには、以下のコマンドを実行
```bash
streamlit run app.py
```