import streamlit as st
import pandas as pd
import os
import japanize_matplotlib
import matplotlib.pyplot as plt

plt.ion()

DATA_FILE = "survey_results.csv"

if not os.path.exists(DATA_FILE):
    df_init = pd.DataFrame(columns=["name", "age", "gender", "rating"])
    df_init.to_csv(DATA_FILE, index=False)

st.title("アンケートフォーム")

with st.form(key="survey_form"):
    name = st.text_input("お名前")
    age = st.number_input("年齢", min_value=0, max_value=120, step=1)
    gender = st.selectbox("性別", ["選択してください", "男性", "女性", "その他"])
    rating = st.slider("満足度を1～5で評価してください", 1, 5, 3)
    submit = st.form_submit_button("送信")

if submit:
    new_data = {"name": name, "age": age, "gender": gender, "rating": rating}
    df = pd.read_csv(DATA_FILE)
    df.loc[len(df)] = new_data
    df.to_csv(DATA_FILE, index=False)
    st.success("回答ありがとうございました！")

st.header("集計結果: 満足度の分布")
df = pd.read_csv(DATA_FILE)

rating_counts = df["rating"].value_counts().sort_index()

fig, ax = plt.subplots()
ax.bar(rating_counts.index, rating_counts.values)
ax.set_xlabel("満足度")
ax.set_ylabel("人数")
ax.set_title("満足度の分布")

st.pyplot(fig)
