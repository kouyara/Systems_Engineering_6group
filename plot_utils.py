import japanize_matplotlib
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

plt.ion()

translations = {
    "ja": {
        "gender_pie_title": "① 性別の割合",
        "gender_pie_no": "※ 性別の回答がまだありません",
        "age_bar_title": "② 年齢階層",
        "age_bar_no": "※ 年齢に関する回答がまだありません",
        "age_bar_ylabel": "人数",
        "interest_bar_title": "② 琉球舞踊への興味",
        "interest_bar_no": "※ 興味に関する回答がまだありません",
        "ratings_ylabel": "人数",
        "experience_skill_line_title": "③ 舞踊歴と自己評価 (平均)",
        "experience_skill_line_no": "※ 舞踊歴または技術力の回答がまだありません",
        "experience_skill_line_xlabel": "舞踊歴 (年)",
        "experience_skill_line_ylabel": "平均 技術力・満足度 (1〜5)",
        "skill_rating_bar_title": "④ 技術力・満足度の分布",
        "skill_rating_bar_no": "※ 技術力・満足度に関する回答がまだありません",
        "skill_rating_bar_xlabel": "評価 (1=低〜5=高)",
        "occupation_bar_title": "⑥ 職業の分布",
        "occupation_bar_no": "※ 職業に関する回答がまだありません",
        "occupation_bar_ylabel": "人数",
        "dance_genre_bar_title": "⑦ 経験したダンスジャンル",
        "dance_genre_bar_no": "※ ジャンルに関する回答がまだありません",
        "dance_genre_bar_ylabel": "人数",
        "practice_problems_title": "⑧ 練習時の困りごと",
        "practice_problems_no": "※ 練習の困りごとに関する回答がまだありません",
        "practice_problems_ylabel": "人数",
        "practice_tools_title": "⑨ 利用している練習ツール",
        "practice_tools_no": "※ 練習ツールに関する回答がまだありません",
        "practice_tools_ylabel": "人数",
        "tech_experience_pie_title": "⑩ AR/VRなどの技術使用経験",
        "tech_experience_pie_no": "※ 技術使用経験の回答がまだありません",
        "preferred_devices_title": "⑪ 使用したいデバイス",
        "preferred_devices_no": "※ デバイスに関する回答がまだありません",
        "preferred_devices_ylabel": "人数",
        "pay_willingness_title": "⑫ 支払い意欲",
        "pay_willingness_no": "※ 支払い意欲に関する回答がまだありません",
        "pay_willingness_ylabel": "人数",
        "system_usefulness_title": "⑬ システムの有用性評価",
        "system_usefulness_no": "※ 有用性に関する回答がまだありません",
        "system_usefulness_xlabel": "評価 (1〜5)",
        "system_usefulness_ylabel": "人数",
    },
    "en": {
        "gender_pie_title": "① Gender Distribution",
        "gender_pie_no": "No gender responses yet",
        "age_bar_title": "② Age Groups",
        "age_bar_no": "No age responses yet",
        "age_bar_ylabel": "Count",
        "interest_bar_title": "② Interest in Ryukyu Dance",
        "interest_bar_no": "No interest responses yet",
        "ratings_ylabel": "Count",
        "experience_skill_line_title": "③ Dance Experience vs. Skill (Average)",
        "experience_skill_line_no": "No dance experience or skill responses yet",
        "experience_skill_line_xlabel": "Dance Experience (Years)",
        "experience_skill_line_ylabel": "Average Skill & Satisfaction (1–5)",
        "skill_rating_bar_title": "④ Skill & Satisfaction Distribution",
        "skill_rating_bar_no": "No skill or satisfaction responses yet",
        "skill_rating_bar_xlabel": "Rating (1=Low–5=High)",
        "occupation_bar_title": "⑥ Occupation Distribution",
        "occupation_bar_no": "No occupation responses yet",
        "occupation_bar_ylabel": "Count",
        "dance_genre_bar_title": "⑦ Experienced Dance Genres",
        "dance_genre_bar_no": "No dance genre responses yet",
        "dance_genre_bar_ylabel": "Count",
        "practice_problems_title": "⑧ Practice Challenges",
        "practice_problems_no": "No practice challenge responses yet",
        "practice_problems_ylabel": "Count",
        "practice_tools_title": "⑨ Practice Tools Used",
        "practice_tools_no": "No practice tools responses yet",
        "practice_tools_ylabel": "Count",
        "tech_experience_pie_title": "⑩ AR/VR & Motion Tech Experience",
        "tech_experience_pie_no": "No tech experience responses yet",
        "preferred_devices_title": "⑪ Preferred Devices",
        "preferred_devices_no": "No preferred devices responses yet",
        "preferred_devices_ylabel": "Count",
        "pay_willingness_title": "⑫ Willingness to Pay",
        "pay_willingness_no": "No payment willingness responses yet",
        "pay_willingness_ylabel": "Count",
        "system_usefulness_title": "⑬ System Usefulness Rating",
        "system_usefulness_no": "No system usefulness responses yet",
        "system_usefulness_xlabel": "Rating (1–5)",
        "system_usefulness_ylabel": "Count",
    }
}

def _t(key: str) -> str:
    lang = st.session_state.get("lang", "ja")
    return translations.get(lang, translations["ja"])[key]

def show_gender_pie(df: pd.DataFrame):
    st.subheader(_t("gender_pie_title"))
    gender_counts = df["gender"].replace("選択してください", pd.NA).dropna().value_counts().sort_index()
    if gender_counts.empty:
        st.write(_t("gender_pie_no"))
        return
    fig, ax = plt.subplots(figsize=(3, 3))
    ax.pie(gender_counts.values, labels=gender_counts.index, autopct="%1.0f%%", startangle=90, wedgeprops={"linewidth":1,"edgecolor":"white"})
    ax.axis("equal")
    st.pyplot(fig)

def show_age_bar(df: pd.DataFrame):
    st.subheader(_t("age_bar_title"))
    age_bins = [10,20,30,40,50,60,70,80]
    df2 = df.copy()
    df2["age_group"] = pd.cut(df2["age"], bins=age_bins, right=False)
    age_counts = df2["age_group"].value_counts().sort_index()
    if age_counts.sum() == 0:
        st.write(_t("age_bar_no"))
        return
    fig, ax = plt.subplots(figsize=(6,4))
    bars = ax.bar(age_counts.index.astype(str), age_counts.values)
    ax.set_ylabel(_t("age_bar_ylabel"))
    ax.set_ylim(0, age_counts.values.max()+1)
    ax.bar_label(bars, padding=3)
    buf = ax.yaxis
    buf.grid(True, linestyle="--", alpha=0.3)
    ax.set_axisbelow(True)
    st.pyplot(fig)

def show_interest_bar(df: pd.DataFrame):
    st.subheader(_t("interest_bar_title"))
    interest_counts = df["interest_ryukyu"].dropna().value_counts()
    if interest_counts.sum() == 0:
        st.write(_t("interest_bar_no"))
        return
    fig, ax = plt.subplots(figsize=(6,4))
    bars = ax.bar(interest_counts.index, interest_counts.values)
    ax.set_ylabel(_t("ratings_ylabel"))
    ax.set_ylim(0, interest_counts.values.max()+1)
    ax.bar_label(bars, padding=3)
    ax.grid(axis="y", linestyle="--", alpha=0.3)
    ax.set_axisbelow(True)
    st.pyplot(fig)

def show_experience_skill_line(df: pd.DataFrame):
    st.subheader(_t("experience_skill_line_title"))
    xpiv = df.dropna(subset=["experience_years","skill_rating"]).groupby("experience_years")["skill_rating"].mean().sort_index()
    if xpiv.empty:
        st.write(_t("experience_skill_line_no"))
        return
    fig, ax = plt.subplots(figsize=(6,4))
    ax.plot(xpiv.index, xpiv.values, marker="o", linewidth=2)
    ax.set_xlabel(_t("experience_skill_line_xlabel"))
    ax.set_ylabel(_t("experience_skill_line_ylabel"))
    ax.set_xticks(xpiv.index.astype(int))
    ax.set_ylim(1,5)
    ax.grid(axis="y", linestyle="--", alpha=0.3)
    ax.set_axisbelow(True)
    st.pyplot(fig)

def show_skill_rating_bar(df: pd.DataFrame):
    st.subheader(_t("skill_rating_bar_title"))
    rating_counts = df["skill_rating"].dropna().value_counts().sort_index()
    if rating_counts.empty:
        st.write(_t("skill_rating_bar_no"))
        return
    fig, ax = plt.subplots(figsize=(6,4))
    bars = ax.bar(rating_counts.index, rating_counts.values)
    ax.set_xlabel(_t("skill_rating_bar_xlabel"))
    ax.set_ylabel(_t("ratings_ylabel"))
    ax.set_ylim(0, rating_counts.values.max()+1)
    ax.bar_label(bars, padding=3)
    st.pyplot(fig)

def show_occupation_bar(df: pd.DataFrame):
    st.subheader(_t("occupation_bar_title"))
    occ_counts = df["occupation"].dropna().value_counts()
    if occ_counts.empty:
        st.write(_t("occupation_bar_no"))
        return
    fig, ax = plt.subplots(figsize=(6,4))
    bars = ax.bar(occ_counts.index, occ_counts.values)
    ax.set_ylabel(_t("occupation_bar_ylabel"))
    ax.set_xticklabels(occ_counts.index, rotation=45, ha="right")
    ax.bar_label(bars, padding=3)
    st.pyplot(fig)

def show_dance_genre_bar(df: pd.DataFrame):
    st.subheader(_t("dance_genre_bar_title"))
    series = df["dance_genres"].dropna().astype(str).str.strip()
    series = series[series!=""]
    all_genres = series.str.split(";").explode().value_counts()
    if all_genres.empty:
        st.write(_t("dance_genre_bar_no"))
        return
    fig, ax = plt.subplots(figsize=(6,4))
    bars = ax.bar(all_genres.index, all_genres.values)
    ax.set_ylabel(_t("dance_genre_bar_ylabel"))
    ax.set_xticklabels(all_genres.index, rotation=45, ha="right")
    ax.bar_label(bars, padding=3)
    st.pyplot(fig)

def show_practice_problems_bar(df: pd.DataFrame):
    st.subheader(_t("practice_problems_title"))
    series = df["practice_problems"].dropna().astype(str).str.strip()
    series = series[series!=""]
    problems = series.str.split(";").explode().value_counts()
    if problems.empty:
        st.write(_t("practice_problems_no"))
        return
    fig, ax = plt.subplots(figsize=(6,4))
    bars = ax.bar(problems.index, problems.values)
    ax.set_ylabel(_t("practice_problems_ylabel"))
    ax.set_xticklabels(problems.index, rotation=45, ha="right")
    ax.bar_label(bars, padding=3)
    st.pyplot(fig)

def show_practice_tools_bar(df: pd.DataFrame):
    st.subheader(_t("practice_tools_title"))
    tools = df["practice_tools"].dropna().str.split(";").explode().value_counts()
    if tools.empty:
        st.write(_t("practice_tools_no"))
        return
    fig, ax = plt.subplots(figsize=(6,4))
    bars = ax.bar(tools.index, tools.values)
    ax.set_ylabel(_t("practice_tools_ylabel"))
    ax.set_xticklabels(tools.index, rotation=45, ha="right")
    ax.bar_label(bars, padding=3)
    st.pyplot(fig)

def show_tech_experience_pie(df: pd.DataFrame):
    st.subheader(_t("tech_experience_pie_title"))
    exp_counts = df["used_tech_before"].dropna().value_counts()
    if exp_counts.empty:
        st.write(_t("tech_experience_pie_no"))
        return
    fig, ax = plt.subplots(figsize=(3,3))
    ax.pie(exp_counts.values, labels=exp_counts.index, autopct="%1.0f%%", startangle=90, wedgeprops={"linewidth":1,"edgecolor":"white"})
    ax.axis("equal")
    st.pyplot(fig)

def show_preferred_devices_bar(df: pd.DataFrame):
    st.subheader(_t("preferred_devices_title"))
    series = df["preferred_devices"].dropna().astype(str).str.strip()
    series = series[series!=""]
    devices = series.str.split(";").explode().value_counts()
    if devices.empty:
        st.write(_t("preferred_devices_no"))
        return
    fig, ax = plt.subplots(figsize=(6,4))
    bars = ax.bar(devices.index, devices.values)
    ax.set_ylabel(_t("preferred_devices_ylabel"))
    ax.set_xticklabels(devices.index, rotation=45, ha="right")
    ax.bar_label(bars, padding=3)
    st.pyplot(fig)

def show_pay_willingness_bar(df: pd.DataFrame):
    st.subheader(_t("pay_willingness_title"))
    pay_counts = df["pay_willingness"].dropna().value_counts().sort_index()
    if pay_counts.empty:
        st.write(_t("pay_willingness_no"))
        return
    fig, ax = plt.subplots(figsize=(6,4))
    bars = ax.bar(pay_counts.index, pay_counts.values)
    ax.set_ylabel(_t("pay_willingness_ylabel"))
    ax.set_xticklabels(pay_counts.index, rotation=45, ha="right")
    ax.bar_label(bars, padding=3)
    st.pyplot(fig)

def show_system_usefulness_bar(df: pd.DataFrame):
    st.subheader(_t("system_usefulness_title"))
    values = df["system_usefulness"].dropna().value_counts().sort_index()
    if values.empty:
        st.write(_t("system_usefulness_no"))
        return
    fig, ax = plt.subplots(figsize=(6,4))
    bars = ax.bar(values.index.astype(str), values.values)
    ax.set_xlabel(_t("system_usefulness_xlabel"))
    ax.set_ylabel(_t("system_usefulness_ylabel"))
    ax.set_ylim(0, values.values.max()+1)
    ax.bar_label(bars, padding=3)
    st.pyplot(fig)
