import streamlit as st
import pandas as pd
import os

st.markdown(
    """
    <style>
    .st-emotion-cache-1s2v671 { display: contents; }
    </style>
    """,
    unsafe_allow_html=True,
)

def radio_rating(key: str, max_value: int = 5):
    """1〜5 評価（未回答を含む）"""
    opts = [None] + list(range(1, max_value + 1))
    return st.radio(
        "", opts, index=0, key=key,
        format_func=lambda x: "未回答" if x is None else str(x),
        horizontal=True,
    )

def radio_unanswered(key: str, choices: list[str]):
    """はい／いいえなど（未回答を含む）"""
    return st.radio(
        "", ["未回答"] + choices, index=0, key=key, horizontal=True,
    )

DATA_FILE = "survey_results.csv"
COLS = [
    "email","age","gender","occupation",
    "interest_ryukyu","dance_genres","experience_years",
    "skill_rating","satisfaction_rating",
    "self_learning_difficulty","practice_problems",
    "practice_tools","preservation_opinion",
    "tech_resistance","education_opinion",
    "used_tech_before","want_compare_3d",
    "preferred_devices","pay_willingness",
    "system_usefulness","usefulness_points",
    "usage_frequency","motivate_to_start",
    "start_trigger_feature","concerns",
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

with st.form("survey_form"):
    st.subheader("■ 基本情報")
    st.markdown("メールアドレス <span style='color:red'>*</span>", unsafe_allow_html=True)
    email = st.text_input("", key="email")

    st.markdown("年齢 <span style='color:red'>*</span>", unsafe_allow_html=True)
    age = st.number_input("", 0, 120, step=1, key="age")

    st.markdown("性別 <span style='color:red'>*</span>", unsafe_allow_html=True)
    gender = st.selectbox("", ["選択してください", "男性", "女性", "その他"], key="gender")

    st.markdown("職業 (例: 学生・会社員 など) <span style='color:red'>*</span>", unsafe_allow_html=True)
    occupation = st.text_input("", key="occupation")

    st.subheader("■ 琉球舞踊について")
    st.markdown("琉球舞踊に興味はありますか？ <span style='color:red'>*</span>", unsafe_allow_html=True)
    interest_ryukyu = radio_unanswered("interest_ryukyu", ["機会があれば習いたい","見てみたい","いいえ"])

    st.markdown("経験のある舞踊・ダンスジャンル（複数選択可） <span style='color:red'>*</span>", unsafe_allow_html=True)
    dance_genres = st.multiselect(
        "", ["琉球舞踊","その他の伝統舞踊","バレエ","ジャズ",
                "コンテンポラリー","社交","ヒップホップ","その他","未経験"],
        key="dance_genres",
    )

    st.markdown("ダンス歴 (年数)", unsafe_allow_html=True)
    experience_years = st.number_input("", 0, 100, step=1, key="experience_years")

    st.subheader("■ 評価（1〜5）")
    st.markdown("舞踊の技術力を1〜5で評価してください", unsafe_allow_html=True)
    skill_rating = radio_rating("skill_rating")

    st.markdown("舞踊の満足度を1〜5で評価してください", unsafe_allow_html=True)
    satisfaction_rating = radio_rating("satisfaction_rating")

    st.markdown("独学で舞踊を学ぶことの困難度を1〜5で評価してください", unsafe_allow_html=True)
    self_learning_difficulty = radio_rating("self_learning_difficulty")

    st.markdown("伝統芸能を現代技術で継承・普及する取り組みについてどう思いますか？ <span style='color:red'>*</span>", unsafe_allow_html=True)
    preservation_opinion = radio_rating("preservation_opinion")

    st.markdown("伝統舞踊の保存や教育にIT技術を使うことへの抵抗感はありますか？ <span style='color:red'>*</span>", unsafe_allow_html=True)
    tech_resistance = radio_rating("tech_resistance")

    st.markdown("このシステムが教育機関で利用されることについてどう思いますか？ <span style='color:red'>*</span>", unsafe_allow_html=True)
    education_opinion = radio_rating("education_opinion")

    st.markdown("このシステムは舞踊・ダンスの練習に役立つと思いますか？ <span style='color:red'>*</span>", unsafe_allow_html=True)
    system_usefulness = radio_rating("system_usefulness")

    st.subheader("■ 学習・練習について")
    st.markdown("練習で困っていること（複数選択可）", unsafe_allow_html=True)
    practice_problems = st.multiselect(
        "", ["正しい動きがわからない","自分の動作が正しいかわからない",
            "習得時間がかかる","手本が少ない","教わる機会・教室がない",
            "練習環境がない","時間が取れない","モチベーションがない","その他記述"],
        key="practice_problems",
    )

    st.markdown("舞踊・ダンスの練習で利用しているツール（複数選択可）", unsafe_allow_html=True)
    practice_tools = st.multiselect(
        "", ["実際のレッスン","レッスン動画","自撮り確認","鏡","AR/VR","練習アプリ","その他"],
        key="practice_tools",
    )

    st.subheader("■ IT 技術活用への意識")
    st.markdown("AR/VR・モーションキャプチャなどの技術を使用したことはありますか？ <span style='color:red'>*</span>", unsafe_allow_html=True)
    used_tech_before = radio_unanswered("used_tech_before", ["はい","いいえ"])

    st.markdown("3Dモデルや比較映像で自分の動きを確認したいですか？ <span style='color:red'>*</span>", unsafe_allow_html=True)
    want_compare_3d = radio_unanswered("want_compare_3d", ["はい","いいえ"])

    st.subheader("■ 利用シーンと料金")
    st.markdown("どのようなデバイスで使いたいですか？（複数選択可）", unsafe_allow_html=True)
    preferred_devices = st.multiselect("", ["PC","スマートフォン","タブレット","その他"], key="preferred_devices")

    st.markdown("費用がかかっても使用したいと思いますか？ <span style='color:red'>*</span>", unsafe_allow_html=True)
    pay_willingness = st.selectbox(
        "", ["無料でなければ使わない","月100円","月300円","月500円〜1,000円","内容次第でそれ以上払える","わからない"],
        key="pay_willingness",
    )

    st.markdown("役立つと思う点（複数選択可）", unsafe_allow_html=True)
    usefulness_points = st.multiselect(
        "", ["正しい動作を習得しやすい","時間短縮になる","独学がしやすい",
                "客観的に動作を見れる","映像ではわからない部分が見れる"],
        key="usefulness_points",
    )

    st.markdown("どれくらいの頻度で利用したいですか？", unsafe_allow_html=True)
    usage_frequency = st.selectbox("", ["未回答","月1","週1","それ以上"], key="usage_frequency")

    st.subheader("■ 動機・懸念点")
    st.markdown("このシステムは琉球舞踊を始めるきっかけになると思いますか？ <span style='color:red'>*</span>", unsafe_allow_html=True)
    motivate_to_start = radio_unanswered("motivate_to_start", ["はい","いいえ"])

    st.markdown("「この機能があれば始めるきっかけになる」と思うもの", unsafe_allow_html=True)
    start_trigger_feature = st.text_area("", key="start_trigger_feature")

    st.markdown("不安・懸念点", unsafe_allow_html=True)
    concerns = st.text_area("", key="concerns")

    submitted = st.form_submit_button("送信")

if submitted:
    checks = {
        "メールアドレス": email.strip() != "",
        "年齢": age > 0,
        "性別": gender != "選択してください",
        "職業": occupation.strip() != "",
        "琉球舞踊への興味": interest_ryukyu in ["機会があれば習いたい","見てみたい","いいえ"],
        "経験ジャンル": len(dance_genres) > 0,
        "現代技術での継承評価": preservation_opinion in range(1,6),
        "IT 活用への抵抗感": tech_resistance in range(1,6),
        "教育機関での利用評価": education_opinion in range(1,6),
        "システム有用性評価": system_usefulness in range(1,6),
        "AR/VR 使用経験": used_tech_before in ["はい","いいえ"],
        "3D 比較ニーズ": want_compare_3d in ["はい","いいえ"],
        "支払意欲": bool(pay_willingness),
        "始めるきっかけになるか": motivate_to_start in ["はい","いいえ"],
    }
    missing = [label for label, ok in checks.items() if not ok]
    all_ok = len(missing) == 0

    if not all_ok:
        st.error(
            "必須項目（* 印）をすべて入力・選択してください。"
            + "\n\n**未入力 / 未選択項目:**\n- "
            + "\n- ".join(missing)
        )
    else:
        df = pd.read_csv(DATA_FILE)
        df.loc[len(df)] = {
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
        df.to_csv(DATA_FILE, index=False)
        st.success("ご回答ありがとうございました！")
        st.balloons()
