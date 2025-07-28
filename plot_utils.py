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

# -------- ① 年齢の割合（棒グラフ） --------
def show_age_bar(df: pd.DataFrame):
    st.subheader("② 年齢階層")
    age_bins = [10, 20, 30, 40, 50, 60, 70, 80]
    df = df.copy()
    df["age_group"] = pd.cut(df["age"], bins=age_bins, right=False)
    age_counts = df["age_group"].value_counts().sort_index()

    if age_counts.sum() == 0:
        st.write("※ 年齢に関する回答がまだありません")
        return

    fig, ax = plt.subplots(figsize=(6, 4), facecolor="#f7f7f7")
    bars = ax.bar(age_counts.index.astype(str), age_counts.values, color="#4b7bec", edgecolor="white", linewidth=0.8)
    ax.set_ylabel("人数")
    ax.set_ylim(0, age_counts.values.max() + 1)
    ax.bar_label(bars, padding=3)
    ax.yaxis.grid(True, linestyle="--", alpha=0.3)
    ax.set_axisbelow(True)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
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

# -------- ⑥ 職業の分布 --------
def show_occupation_bar(df: pd.DataFrame):
    st.subheader("⑥ 職業の分布")
    occ_counts = df["occupation"].dropna().value_counts()
    if occ_counts.empty:
        st.write("※ 職業に関する回答がまだありません")
        return

    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.bar(occ_counts.index, occ_counts.values, color="#a29bfe")
    ax.set_ylabel("人数")

    ax.set_xticks(range(len(occ_counts.index)))
    ax.set_xticklabels(occ_counts.index, rotation=45, ha="right")

    ax.bar_label(bars, padding=3)
    fig.tight_layout()
    st.pyplot(fig)


# -------- ⑦ ダンスジャンルの経験 --------
def show_dance_genre_bar(df: pd.DataFrame):
    st.subheader("⑦ 経験したダンスジャンル")

    series = (
        df["dance_genres"]
        .dropna()
        .astype(str)
        .str.strip()
    )
    series = series[series != ""]

    all_genres = series.str.split(";").explode().value_counts()
    if all_genres.empty:
        st.write("※ ジャンルに関する回答がまだありません")
        return

    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.bar(all_genres.index, all_genres.values, color="#fd9644")
    ax.set_ylabel("人数")

    # xticks を明示的に設定してからラベルを回転
    ax.set_xticks(range(len(all_genres.index)))
    ax.set_xticklabels(all_genres.index, rotation=45, ha="right")

    ax.bar_label(bars, padding=3)
    fig.tight_layout()
    st.pyplot(fig)

# -------- ⑧ 練習時の困りごと --------
def show_practice_problems_bar(df: pd.DataFrame):
    st.subheader("⑧ 練習時の困りごと")

    series = (
        df["practice_problems"]
        .dropna()
        .astype(str)
        .str.strip()
    )
    series = series[series != ""]

    problems = series.str.split(";").explode().value_counts()
    if problems.empty:
        st.write("※ 練習の困りごとに関する回答がまだありません")
        return

    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.bar(problems.index, problems.values, color="#f8c291")
    ax.set_ylabel("人数")

    ax.set_xticks(range(len(problems.index)))
    ax.set_xticklabels(problems.index, rotation=45, ha="right")

    ax.bar_label(bars, padding=3)
    fig.tight_layout()
    st.pyplot(fig)


# -------- ⑨ 利用ツールの分布 --------
def show_practice_tools_bar(df: pd.DataFrame):
    st.subheader("⑨ 利用している練習ツール")
    tools = df["practice_tools"].dropna().str.split(";").explode().value_counts()
    if tools.empty:
        st.write("※ 練習ツールに関する回答がまだありません")
        return
    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.bar(tools.index, tools.values, color="#badc58")
    ax.set_ylabel("人数")
    ax.set_xticklabels(tools.index, rotation=45, ha="right")
    ax.bar_label(bars, padding=3)
    st.pyplot(fig)

# -------- ⑩ AR/VRの使用経験 --------
def show_tech_experience_pie(df: pd.DataFrame):
    st.subheader("⑩ AR/VRなどの技術使用経験")
    exp_counts = df["used_tech_before"].dropna().value_counts()
    if exp_counts.empty:
        st.write("※ 技術使用経験の回答がまだありません")
        return
    fig, ax = plt.subplots(figsize=(3, 3))
    ax.pie(
        exp_counts.values,
        labels=exp_counts.index,
        autopct="%1.0f%%",
        startangle=90,
        colors=["#7ed6df", "#eccc68"],
        wedgeprops={"linewidth": 1, "edgecolor": "white"},
    )
    ax.axis("equal")
    st.pyplot(fig)

def show_preferred_devices_bar(df: pd.DataFrame):
    st.subheader("⑪ 使用したいデバイス")
    series = (
        df["preferred_devices"]
        .dropna()
        .astype(str)
        .str.strip()
    )
    series = series[series != ""]

    devices = series.str.split(";").explode().value_counts()
    if devices.empty:
        st.write("※ デバイスに関する回答がまだありません")
        return

    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.bar(devices.index, devices.values, color="#e17055")
    ax.set_ylabel("人数")

    ax.set_xticks(range(len(devices.index)))
    ax.set_xticklabels(devices.index, rotation=45, ha="right")

    ax.bar_label(bars, padding=3)
    fig.tight_layout()
    st.pyplot(fig)


# -------- ⑫ 支払い意欲 --------
def show_pay_willingness_bar(df: pd.DataFrame):
    st.subheader("⑫ 支払い意欲")
    pay_counts = df["pay_willingness"].dropna().value_counts().sort_index()
    if pay_counts.empty:
        st.write("※ 支払い意欲に関する回答がまだありません")
        return
    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.bar(pay_counts.index, pay_counts.values, color="#fab1a0")
    ax.set_ylabel("人数")
    ax.set_xticklabels(pay_counts.index, rotation=45, ha="right")
    ax.bar_label(bars, padding=3)
    st.pyplot(fig)

# -------- ⑬ システムの有用性 --------
def show_system_usefulness_bar(df: pd.DataFrame):
    st.subheader("⑬ システムの有用性評価")
    values = df["system_usefulness"].dropna().value_counts().sort_index()
    if values.empty:
        st.write("※ 有用性に関する回答がまだありません")
        return
    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.bar(values.index.astype(str), values.values, color="#55efc4")
    ax.set_xlabel("評価 (1〜5)")
    ax.set_ylabel("人数")
    ax.set_ylim(0, values.max() + 1)
    ax.bar_label(bars, padding=3)
    st.pyplot(fig)
