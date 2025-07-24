import japanize_matplotlib
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

plt.ion()

# -------- ① 性別の割合（円グラフ） --------
def show_gender_pie(df: pd.DataFrame):
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
        return

    fig, ax = plt.subplots(figsize=(3, 3))
    ax.pie(
        gender_counts.values,
        labels=gender_counts.index,
        autopct="%1.0f%%",
        startangle=90,
        colors=["#ffb3c6", "#bde0fe", "#caffbf"][: len(gender_counts)],
        wedgeprops={"linewidth": 1, "edgecolor": "white"},
    )
    ax.axis("equal")
    st.pyplot(fig)

# -------- ② 興味（棒グラフ） --------
def show_interest_bar(df: pd.DataFrame):
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
        return

    fig, ax = plt.subplots(figsize=(6, 4), facecolor="#f7f7f7")
    bars = ax.bar(
        interest_counts.index,
        interest_counts.values,
        color="#ff4b4b",
        edgecolor="white",
        linewidth=0.8,
    )
    ax.set_ylabel("人数")
    ax.set_ylim(0, interest_counts.values.max() + 1)
    ax.bar_label(bars, padding=3)
    ax.yaxis.grid(True, linestyle="--", alpha=0.3)
    ax.set_axisbelow(True)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    st.pyplot(fig)

# -------- ③ 舞踊歴と自己評価（折れ線） --------
def show_experience_skill_line(df: pd.DataFrame):
    st.subheader("③ 舞踊歴と自己評価 (平均)")
    xpiv = (
        df.dropna(subset=["experience_years", "skill_rating"])
        .groupby("experience_years")["skill_rating"]
        .mean()
        .sort_index()
    )
    if xpiv.empty:
        st.write("※ 舞踊歴または技術力の回答がまだありません")
        return

    fig, ax = plt.subplots(figsize=(6, 4), facecolor="#f7f7f7")
    ax.plot(xpiv.index, xpiv.values, marker="o", linewidth=2)
    ax.set_xlabel("舞踊歴 (年)")
    ax.set_ylabel("平均 技術力・満足度 (1〜5)")
    ax.set_xticks(xpiv.index.astype(int))
    ax.set_ylim(1, 5)
    ax.yaxis.grid(True, linestyle="--", alpha=0.3)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    st.pyplot(fig)

# -------- ④ 技術力・満足度（棒グラフ） --------
def show_skill_rating_bar(df: pd.DataFrame):
    st.subheader("④ 技術力・満足度の分布")
    rating_counts = df["skill_rating"].dropna().value_counts().sort_index()
    if rating_counts.empty:
        st.write("※ 技術力・満足度に関する回答がまだありません")
        return

    fig, ax = plt.subplots(figsize=(6, 4), facecolor="#f7f7f7")
    bars = ax.bar(
        rating_counts.index,
        rating_counts.values,
        color="#ff4b4b",
        edgecolor="white",
        linewidth=0.8,
    )
    ax.set_xlabel("評価 (1=低〜5=高)")
    ax.set_ylabel("人数")
    ax.set_ylim(0, rating_counts.values.max() + 1)
    ax.bar_label(bars, labels=[f"{v}人" for v in rating_counts.values], padding=3)
    ax.yaxis.grid(True, linestyle="--", alpha=0.3)
    ax.set_axisbelow(True)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    st.pyplot(fig)
