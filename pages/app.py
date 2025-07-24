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
    "name", "email", "age", "gender", "occupation",
    "interest_ryukyu",
    "dance_genres",
    "experience_years",
    "skill_rating",
    "satisfaction_rating",
    "self_learning_difficulty",
    "practice_problems",
    "practice_tools",
    "preservation_opinion",
    "tech_resistance",
    "education_opinion",
    "used_tech_before",
    "want_compare_3d",
    "preferred_devices",
    "pay_willingness",
    "system_usefulness",
    "usefulness_points",
    "usage_frequency",
    "motivate_to_start",
    "start_trigger_feature",
    "concerns",
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
    interest_ryukyu = st.radio(
        "琉球舞踊に興味はありますか？",
        ["機会があれば習いたい", "見てみたい", "いいえ"],
    )
    dance_genres = st.multiselect(
        "これまでに経験したことのある舞踊・ダンスジャンル（複数選択可）",
        [
            "琉球舞踊", "その他の伝統舞踊", "バレエ", "ジャズ",
            "コンテンポラリー", "社交", "ヒップホップ", "その他", "未経験",
        ],
    )
    experience_years = st.number_input("ダンス歴 (年数)", min_value=0, max_value=100, step=1)
    skill_rating = st.slider("舞踊の技術力を1〜5で評価してください", 1, 5, 3)
    satisfaction_rating = st.slider("舞踊の満足度を1〜5で評価してください", 1, 5, 3)

    st.subheader("■ 学習・練習について")
    self_learning_difficulty = st.slider(
        "独学で舞踊を学ぶことの困難度を1〜5で評価してください", 1, 5, 3
    )
    practice_problems = st.multiselect(
        "練習で困っていること（複数選択可）",
        [
            "正しい動きがわからない", "自分の動作が正しいかわからない",
            "習得時間がかかる", "手本が少ない", "教わる機会・教室がない",
            "練習環境がない", "時間が取れない", "モチベーションがない", "その他記述",
        ],
    )
    practice_tools = st.multiselect(
        "舞踊・ダンスの練習で利用しているツール（複数選択可）",
        ["実際のレッスン", "レッスン動画", "自撮り確認", "鏡", "AR/VR", "練習アプリ", "その他"],
    )

    st.subheader("■ IT 技術活用への意識")
    preservation_opinion = st.slider(
        "伝統芸能を現代技術で継承・普及する取り組みについてどう思いますか？", 1, 5, 3
    )
    tech_resistance = st.slider(
        "伝統舞踊の保存や教育に IT 技術を使うことへの抵抗感はありますか？", 1, 5, 3
    )
    education_opinion = st.slider(
        "このシステムが教育機関で利用されることについてどう思いますか？", 1, 5, 3
    )
    used_tech_before = st.radio(
        "AR/VR・モーションキャプチャなどの技術を使用したことはありますか？", ["はい", "いいえ"]
    )
    want_compare_3d = st.radio(
        "3Dモデルや比較映像で自分の動きを確認したいですか？", ["はい", "いいえ"]
    )

    st.subheader("■ 利用シーンと料金")
    preferred_devices = st.multiselect(
        "どのようなデバイスで使いたいですか？（複数選択可）",
        ["PC", "スマートフォン", "タブレット", "その他"],
    )
    pay_willingness = st.selectbox(
        "費用がかかっても使用したいと思いますか？",
        [
            "無料でなければ使わない",
            "月100円",
            "月300円",
            "月500円〜1,000円",
            "内容次第でそれ以上払える",
            "わからない",
        ],
    )
    system_usefulness = st.slider(
        "このシステムは舞踊・ダンスの練習に役立つと思いますか？", 1, 5, 3
    )
    usefulness_points = st.multiselect(
        "役立つと思う点（複数選択可）",
        [
            "正しい動作を習得しやすい", "時間短縮になる", "独学がしやすい",
            "客観的に動作を見れる", "映像ではわからない部分が見れる",
        ],
    )
    usage_frequency = st.selectbox(
        "どれくらいの頻度で利用したいですか？",
        ["月1", "週1", "それ以上"],
    )

    st.subheader("■ 動機・懸念点")
    motivate_to_start = st.radio(
        "このシステムは琉球舞踊を始めるきっかけになると思いますか？", ["はい", "いいえ"]
    )
    start_trigger_feature = st.text_area("「この機能があれば始めるきっかけになる」と思うもの")
    concerns = st.text_area("不安・懸念点")

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
        "dance_genres": ";".join(dance_genres),
        "experience_years": experience_years,
        "skill_rating": skill_rating,
        "satisfaction_rating": satisfaction_rating,
        "self_learning_difficulty": self_learning_difficulty,
        "practice_problems": ";".join(practice_problems),
        "practice_tools": ";".join(practice_tools),
        "preservation_opinion": preservation_opinion,
        "tech_resistance": tech_resistance,
        "education_opinion": education_opinion,
        "used_tech_before": used_tech_before,
        "want_compare_3d": want_compare_3d,
        "preferred_devices": ";".join(preferred_devices),
        "pay_willingness": pay_willingness,
        "system_usefulness": system_usefulness,
        "usefulness_points": ";".join(usefulness_points),
        "usage_frequency": usage_frequency,
        "motivate_to_start": motivate_to_start,
        "start_trigger_feature": start_trigger_feature,
        "concerns": concerns,
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
