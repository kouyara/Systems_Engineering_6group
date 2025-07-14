import streamlit as st
import pandas as pd
import os

from plot_utils import (
    show_gender_pie,
    show_interest_bar,
    show_experience_skill_line,
    show_skill_rating_bar,
)

DATA_FILE = "survey_results.csv"
COLS = [
    "name", "email",
    "age", "gender", "occupation",
    "interest_ryukyu",
    "experience_years",
    "skill_rating",
    "other_dance_exp",
    "practice_tools",
]

if not os.path.exists(DATA_FILE):
    pd.DataFrame(columns=COLS).to_csv(DATA_FILE, index=False)
else:
    df_tmp = pd.read_csv(DATA_FILE)
    for c in COLS:
        if c not in df_tmp.columns:
            df_tmp[c] = pd.NA
    df_tmp.to_csv(DATA_FILE, index=False)

st.title("アンケートフォーム (琉球舞踊)")

with st.form(key="survey_form"):
    st.subheader("■ 基本情報")
    name = st.text_input("お名前")
    email = st.text_input("メールアドレス")
    age = st.number_input("年齢", min_value=0, max_value=120, step=1)
    gender = st.selectbox("性別", ["選択してください", "男性", "女性", "その他"])
    occupation = st.text_input("職業 (例: 学生・会社員 など)")

    st.subheader("■ 琉球舞踊について")
    interest_ryukyu = st.radio("琉球舞踊に興味はありますか？", ["はい", "いいえ", "わからない"])
    experience_years = st.number_input("舞踊歴 (年数)", min_value=0, max_value=100, step=1)
    skill_rating = st.slider("舞踊の技術力・満足度を1〜5で評価してください", 1, 5, 3)
    other_dance_exp = st.radio("他のダンス経験はありますか？", ["はい", "いいえ"])
    practice_tools = st.multiselect(
        "舞踊の練習で利用しているツールは？ (複数選択可)",
        ["YouTube", "鏡", "VR/AR", "スタジオ講座", "その他"],
    )
    submitted = st.form_submit_button("送信")

if submitted:
    df_save = pd.read_csv(DATA_FILE)
    df_save.loc[len(df_save)] = {
        "name": name,
        "email": email,
        "age": age,
        "gender": gender,
        "occupation": occupation,
        "interest_ryukyu": interest_ryukyu,
        "experience_years": experience_years,
        "skill_rating": skill_rating,
        "other_dance_exp": other_dance_exp,
        "practice_tools": ";".join(practice_tools),
    }
    df_save.to_csv(DATA_FILE, index=False)
    st.success("ご回答ありがとうございました！")

df = pd.read_csv(DATA_FILE)

if df.empty or df["name"].isna().all():
    st.info("まだ十分な回答がないため、可視化は表示されません🐾")
else:
    col1, col2 = st.columns(2)
    with col1:
        show_gender_pie(df)
    with col2:
        show_interest_bar(df)

    col3, col4 = st.columns(2)
    with col3:
        show_experience_skill_line(df)
    with col4:
        show_skill_rating_bar(df)
