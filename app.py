import streamlit as st
import pandas as pd
import os
import japanize_matplotlib
import matplotlib.pyplot as plt

plt.ion()

DATA_FILE = "survey_results.csv"
COLS = [
    "name", "email",
    "age", "gender", "occupation",
    "interest_ryukyu",
    "experience_years",
    "skill_rating",
    "other_dance_exp",
    "practice_tools"
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
        ["YouTube", "鏡", "VR/AR", "スタジオ講座", "その他"]
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
        "practice_tools": ";".join(practice_tools)
    }
    df_save.to_csv(DATA_FILE, index=False)
    st.success("ご回答ありがとうございました！")

df = pd.read_csv(DATA_FILE)

if df.empty or df["name"].isna().all():
    st.info("まだ十分な回答がないため、可視化は表示されません🐾")
else:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("① 性別の割合")
        gender_counts = (
            df["gender"]
            .replace("選択してください", pd.NA)
            .dropna()
            .value_counts()
            .sort_index()
        )
        if gender_counts.empty:
            st.write("※ 性別の回答がまだありません")
        else:
            fig1, ax1 = plt.subplots(figsize=(3, 3))   # ★円グラフを小さめ
            ax1.pie(
                gender_counts.values,
                labels=gender_counts.index,
                autopct="%1.0f%%",
                startangle=90,
                colors=["#ffb3c6", "#bde0fe", "#caffbf"][: len(gender_counts)],
                wedgeprops={"linewidth": 1, "edgecolor": "white"}
            )
            ax1.axis("equal")
            st.pyplot(fig1)

    with col2:
        st.subheader("② 琉球舞踊への興味")
        interest_counts = (
            df["interest_ryukyu"]
            .dropna()
            .value_counts()
            .reindex(["はい", "いいえ", "わからない"])
            .fillna(0)
            .astype(int)
        )
        if interest_counts.sum() == 0:
            st.write("※ 興味に関する回答がまだありません")
        else:
            fig2, ax2 = plt.subplots(figsize=(6, 4), facecolor="#f7f7f7")
            bars2 = ax2.bar(
                interest_counts.index, interest_counts.values,
                color="#ff4b4b", edgecolor="white", linewidth=0.8
            )
            ax2.set_ylabel("人数")
            ax2.set_ylim(0, interest_counts.values.max() + 1)
            ax2.bar_label(bars2, padding=3)
            ax2.yaxis.grid(True, linestyle="--", alpha=0.3)
            ax2.set_axisbelow(True)
            for spine in ["top", "right"]:
                ax2.spines[spine].set_visible(False)
            fig2.tight_layout()
            st.pyplot(fig2)

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("③ 舞踊歴と自己評価 (平均)")
        xpiv = (
            df.dropna(subset=["experience_years", "skill_rating"])
            .groupby("experience_years")["skill_rating"]
            .mean()
            .sort_index()
        )
        if xpiv.empty:
            st.write("※ 舞踊歴または技術力の回答がまだありません")
        else:
            fig3, ax3 = plt.subplots(figsize=(6, 4), facecolor="#f7f7f7")
            ax3.plot(
                xpiv.index, xpiv.values,
                marker="o", linewidth=2
            )
            ax3.set_xlabel("舞踊歴 (年)")
            ax3.set_ylabel("平均 技術力・満足度 (1〜5)")
            ax3.set_xticks(xpiv.index.astype(int))
            ax3.set_ylim(1, 5)
            ax3.yaxis.grid(True, linestyle="--", alpha=0.3)
            for spine in ["top", "right"]:
                ax3.spines[spine].set_visible(False)
            fig3.tight_layout()
            st.pyplot(fig3)

    with col4:
        st.subheader("④ 技術力・満足度の分布")
        rating_counts = df["skill_rating"].dropna().value_counts().sort_index()
        if rating_counts.empty:
            st.write("※ 技術力・満足度に関する回答がまだありません")
        else:
            plt.style.use("ggplot")
            fig4, ax4 = plt.subplots(figsize=(6, 4), facecolor="#f7f7f7")
            bars4 = ax4.bar(
                rating_counts.index, rating_counts.values,
                color="#ff4b4b", edgecolor="white", linewidth=0.8
            )
            ax4.set_xlabel("評価 (1=低〜5=高)")
            ax4.set_ylabel("人数")
            ax4.set_ylim(0, rating_counts.values.max() + 1)
            ax4.bar_label(bars4, labels=[f"{v}人" for v in rating_counts.values], padding=3)
            ax4.yaxis.grid(True, linestyle="--", alpha=0.3)
            ax4.set_axisbelow(True)
            for spine in ["top", "right"]:
                ax4.spines[spine].set_visible(False)
            fig4.tight_layout()
            st.pyplot(fig4)