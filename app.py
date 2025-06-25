import streamlit as st
import pandas as pd
import os
import japanize_matplotlib
import matplotlib.pyplot as plt

# matplotlib のインタラクティブモードを有効化
plt.ion()

# CSV ファイルのパス
DATA_FILE = "survey_results.csv"

# データファイルが存在しない場合はヘッダーだけの空ファイルを作成
if not os.path.exists(DATA_FILE):
    df_init = pd.DataFrame(columns=["name", "age", "gender", "rating"])
    df_init.to_csv(DATA_FILE, index=False)

# アプリタイトル
st.title("アンケートフォーム")

# フォームの作成
with st.form(key="survey_form"):
    name = st.text_input("お名前")
    age = st.number_input("年齢", min_value=0, max_value=120, step=1)
    gender = st.selectbox("性別", ["選択してください", "男性", "女性", "その他"])
    rating = st.slider("満足度を1～5で評価してください", 1, 5, 3)
    submit = st.form_submit_button("送信")

# フォーム送信時の処理
if submit:
    # CSV に追記
    new_data = {"name": name, "age": age, "gender": gender, "rating": rating}
    df = pd.read_csv(DATA_FILE)
    df.loc[len(df)] = new_data
    df.to_csv(DATA_FILE, index=False)
    st.success("回答ありがとうございました！")

# 集計結果の表示
st.header("集計結果: 満足度の分布")
# CSV を読み込み
df = pd.read_csv(DATA_FILE)

# 集計: 満足度ごとの人数
rating_counts = df["rating"].value_counts().sort_index()

# グラフ描画
fig, ax = plt.subplots()
ax.bar(rating_counts.index, rating_counts.values)
ax.set_xlabel("満足度")
ax.set_ylabel("人数")
ax.set_title("満足度の分布")

# Streamlit へ表示
st.pyplot(fig)
