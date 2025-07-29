import streamlit as st
import pandas as pd
import os

if "lang" not in st.session_state:
    st.session_state.lang = "ja"
lang_map = {"日本語": "ja", "English": "en"}
st.session_state.lang = lang_map[st.selectbox("言語 / Language", list(lang_map.keys()))]

t = {
    "ja": {
        "font_size_title": "文字の大きさ",
        "small": "小",
        "medium": "中",
        "large": "大",
        "form_title": "アンケートフォーム (琉球舞踊)",
        "required_note": "※ <span style='color:red'>*</span> は必須項目です。",
        "section_basic": "■ 基本情報",
        "label_email": "メールアドレス <span style='color:red'>*</span>",
        "label_age": "年齢 <span style='color:red'>*</span>",
        "label_gender": "性別 <span style='color:red'>*</span>",
        "gender_options": ["選択してください", "男性", "女性", "その他"],
        "label_occupation": "職業 (例: 学生・会社員 など) <span style='color:red'>*</span>",
        "section_about": "■ 琉球舞踊について",
        "label_interest": "琉球舞踊に興味はありますか？ <span style='color:red'>*</span>",
        "interest_options": ["機会があれば習いたい", "見てみたい", "いいえ"],
        "label_genres": "経験のある舞踊・ダンスジャンル（複数選択可） <span style='color:red'>*</span>",
        "genres_options": ["琉球舞踊", "その他の伝統舞踊", "バレエ", "ジャズ", "コンテンポラリー", "社交", "ヒップホップ", "その他", "未経験"],
        "label_experience": "ダンス歴 (年数)",
        "section_ratings": "■ 評価（1〜5）",
        "label_skill": "舞踊の技術力を1〜5で評価してください",
        "label_satisfaction": "舞踊の満足度を1〜5で評価してください",
        "label_difficulty": "独学で舞踊を学ぶことの困難度を1〜5で評価してください",
        "label_preservation_opinion": "伝統芸能を現代技術で継承・普及する取り組みについてどう思いますか？ <span style='color:red'>*</span>",
        "label_tech_resistance": "伝統舞踊の保存や教育にIT技術を使うことへの抵抗感はありますか？ <span style='color:red'>*</span>",
        "label_education_opinion": "このシステムが教育機関で利用されることについてどう思いますか？ <span style='color:red'>*</span>",
        "label_system_usefulness": "このシステムは舞踊・ダンスの練習に役立つと思いますか？ <span style='color:red'>*</span>",
        "section_practice": "■ 学習・練習について",
        "label_practice_problems": "練習で困っていること（複数選択可）",
        "practice_problems_options": ["正しい動きがわからない", "自分の動作が正しいかわからない", "習得時間がかかる", "手本が少ない", "教わる機会・教室がない", "練習環境がない", "時間が取れない", "モチベーションがない", "その他記述"],
        "label_practice_tools": "舞踊・ダンスの練習で利用しているツール（複数選択可）",
        "practice_tools_options": ["実際のレッスン", "レッスン動画", "自撮り確認", "鏡", "AR/VR", "練習アプリ", "その他"],
        "section_it": "■ IT 技術活用への意識",
        "label_used_tech_before": "AR/VR・モーションキャプチャなどの技術を使用したことはありますか？ <span style='color:red'>*</span>",
        "used_tech_before_options": ["はい", "いいえ"],
        "label_want_compare_3d": "3Dモデルや比較映像で自分の動きを確認したいですか？ <span style='color:red'>*</span>",
        "want_compare_3d_options": ["はい", "いいえ"],
        "section_fee": "■ 利用シーンと料金",
        "label_devices": "どのようなデバイスで使いたいですか？（複数選択可）",
        "devices_options": ["PC", "スマートフォン", "タブレット", "その他"],
        "label_pay": "費用がかかっても使用したいと思いますか？ <span style='color:red'>*</span>",
        "pay_options": ["無料でなければ使わない", "月100円", "月300円", "月500円〜1,000円", "内容次第でそれ以上払える", "わからない"],
        "label_usefulness_points": "役立つと思う点（複数選択可）",
        "usefulness_points_options": ["正しい動作を習得しやすい", "時間短縮になる", "独学がしやすい", "客観的に動作を見れる", "映像ではわからない部分が見れる"],
        "label_frequency": "どれくらいの頻度で利用したいですか？",
        "frequency_options": ["未回答", "月1", "週1", "それ以上"],
        "section_motivation": "■ 動機・懸念点",
        "label_motivate_to_start": "このシステムは琉球舞踊を始めるきっかけになると思いますか？ <span style='color:red'>*</span>",
        "motivate_to_start_options": ["はい", "いいえ"],
        "label_start_trigger": "「この機能があれば始めるきっかけになる」と思うもの",
        "label_concerns": "不安・懸念点",
        "submit_button": "送信",
        "error_required": "必須項目（* 印）をすべて入力・選択してください。",
        "error_missing_intro": "**未入力 / 未選択項目:**",
        "success_message": "ご回答ありがとうございました！",
        "unanswered": "未回答"
    },
    "en": {
        "font_size_title": "Font Size",
        "small": "Small",
        "medium": "Medium",
        "large": "Large",
        "form_title": "Survey Form (Ryukyu Dance)",
        "required_note": "* indicates required fields.",
        "section_basic": "■ Basic Information",
        "label_email": "Email Address <span style='color:red'>*</span>",
        "label_age": "Age <span style='color:red'>*</span>",
        "label_gender": "Gender <span style='color:red'>*</span>",
        "gender_options": ["Please select", "Male", "Female", "Other"],
        "label_occupation": "Occupation (e.g., Student, Company Employee) <span style='color:red'>*</span>",
        "section_about": "■ About Ryukyu Dance",
        "label_interest": "Are you interested in Ryukyu Dance? <span style='color:red'>*</span>",
        "interest_options": ["Would like to learn if opportunity arises", "Would like to watch", "No"],
        "label_genres": "Dance genres experienced (multiple selections) <span style='color:red'>*</span>",
        "genres_options": ["Ryukyu Dance", "Other Traditional Dance", "Ballet", "Jazz", "Contemporary", "Social Dance", "Hip-hop", "Other", "No Experience"],
        "label_experience": "Dance Experience (Years)",
        "section_ratings": "■ Ratings (1-5)",
        "label_skill": "Please rate your dance skills from 1 to 5",
        "label_satisfaction": "Please rate your satisfaction with dance from 1 to 5",
        "label_difficulty": "Please rate the difficulty of self-learning dance from 1 to 5",
        "label_preservation_opinion": "What do you think about preserving and promoting traditional performing arts through modern technology? <span style='color:red'>*</span>",
        "label_tech_resistance": "Do you have any resistance to using IT for preservation and education of traditional dance? <span style='color:red'>*</span>",
        "label_education_opinion": "What do you think about using this system in educational institutions? <span style='color:red'>*</span>",
        "label_system_usefulness": "Do you think this system would help with dance practice? <span style='color:red'>*</span>",
        "section_practice": "■ About Learning & Practice",
        "label_practice_problems": "Problems faced during practice (multiple selections)",
        "practice_problems_options": ["Not sure of correct movements", "Not sure if my movements are correct", "Takes time to master", "Few examples available", "No opportunity or classes", "No practice environment", "Cannot find time", "Lack of motivation", "Other (please specify)"],
        "label_practice_tools": "Tools used for dance practice (multiple selections)",
        "practice_tools_options": ["In-person lessons", "Lesson videos", "Self-recording", "Mirror", "AR/VR", "Practice apps", "Other"],
        "section_it": "■ Attitudes Toward IT",
        "label_used_tech_before": "Have you used AR/VR or motion capture technologies? <span style='color:red'>*</span>",
        "used_tech_before_options": ["Yes", "No"],
        "label_want_compare_3d": "Would you like to check your movements with 3D models or comparison videos? <span style='color:red'>*</span>",
        "want_compare_3d_options": ["Yes", "No"],
        "section_fee": "■ Usage & Fees",
        "label_devices": "Which devices would you like to use? (multiple selections)",
        "devices_options": ["PC", "Smartphone", "Tablet", "Other"],
        "label_pay": "Would you be willing to pay for this system? <span style='color:red'>*</span>",
        "pay_options": ["Won't use unless free", "100 JPY/month", "300 JPY/month", "500–1000 JPY/month", "Willing to pay more depending on content", "Not sure"],
        "label_usefulness_points": "Points you think would be helpful (multiple selections)",
        "usefulness_points_options": ["Easier to learn correct movements", "Saves time", "Facilitates self-learning", "Can view movements objectively", "See details not visible in videos"],
        "label_frequency": "How often would you like to use it?",
        "frequency_options": ["Unanswered", "Once a month", "Once a week", "More often"],
        "section_motivation": "■ Motivation & Concerns",
        "label_motivate_to_start": "Do you think this system would motivate you to start Ryukyu dance? <span style='color:red'>*</span>",
        "motivate_to_start_options": ["Yes", "No"],
        "label_start_trigger": "Features that would motivate you to start",
        "label_concerns": "Anxieties / Concerns",
        "submit_button": "Submit",
        "error_required": "Please complete all required fields (*) .",
        "error_missing_intro": "**Missing items:**",
        "success_message": "Thank you for your response!",
        "unanswered": "Unanswered"
    }
}

current = t[st.session_state.lang]
unanswered = current["unanswered"]

if "font_size" not in st.session_state:
    st.session_state.font_size = "medium"
st.markdown(
    f"<h5 style='font-weight:600; margin-bottom:0.5rem;'>{current['font_size_title']}</h5>",
    unsafe_allow_html=True
)
col_small, col_medium, col_large = st.columns(3, gap="small")
with col_small:
    if st.button(current["small"]):
        st.session_state.font_size = "small"
with col_medium:
    if st.button(current["medium"]):
        st.session_state.font_size = "medium"
with col_large:
    if st.button(current["large"]):
        st.session_state.font_size = "large"
font_map = {"small": "14px", "medium": "18px", "large": "24px"}
st.markdown(
    f"<style>html, body, [class*=\"css\"] {{font-size: {font_map[st.session_state.font_size]} !important;}}</style>",
    unsafe_allow_html=True
)
st.markdown(
    "<style>.st-emotion-cache-1s2v671 { display: contents; }</style>",
    unsafe_allow_html=True
)

def radio_rating(key: str, max_value: int = 5):
    opts = [None] + list(range(1, max_value + 1))
    return st.radio(
        "", opts, key=key,
        index=opts.index(st.session_state.form_data[key]) if st.session_state.form_data[key] in opts else 0,
        format_func=lambda x: unanswered if x is None else str(x),
        horizontal=True,
    )

def radio_unanswered(key: str, choices: list[str]):
    answerlist = [unanswered] + choices
    return st.radio(
        "", answerlist,
        index=answerlist.index(st.session_state.form_data[key]) if st.session_state.form_data[key] in answerlist else 0,
        key=key, horizontal=True,
    )

DATA_FILE = "survey_results.csv"
COLS = [
    "email","age","gender","occupation",
    "interest_ryukyu","dance_genres","experience_years",
    "skill_rating","satisfaction_rating","self_learning_difficulty",
    "practice_problems","practice_tools","preservation_opinion",
    "tech_resistance","education_opinion","used_tech_before",
    "want_compare_3d","preferred_devices","pay_willingness",
    "system_usefulness","usefulness_points","usage_frequency",
    "motivate_to_start","start_trigger_feature","concerns"
]

if "form_data" not in st.session_state:
    st.session_state.form_data = {k: "" for k in COLS}

if not os.path.exists(DATA_FILE):
    pd.DataFrame(columns=COLS).to_csv(DATA_FILE, index=False)
else:
    df_tmp = pd.read_csv(DATA_FILE)
    for c in COLS:
        if c not in df_tmp.columns:
            df_tmp[c] = pd.NA
    df_tmp.to_csv(DATA_FILE, index=False)

def update_column(col):
    st.session_state.form_data[f"{col}"] = eval(col)

st.title(current["form_title"])
st.markdown(current["required_note"], unsafe_allow_html=True)

with st.form("survey_form"):
    # 基本情報
    st.subheader(current["section_basic"])

    st.markdown(current["label_email"], unsafe_allow_html=True)
    email = st.text_input("", key="email", value=st.session_state.form_data["email"])

    st.markdown(current["label_age"], unsafe_allow_html=True)
    age = st.number_input(
        "", 0, 120, step=1, key="age",
        value=0 if type(st.session_state.form_data["age"]) == str else int(st.session_state.form_data["age"])
    )

    st.markdown(current["label_gender"], unsafe_allow_html=True)
    gender = st.selectbox(
        "", current["gender_options"], key="gender",
        index= current["gender_options"].index(st.session_state.form_data["gender"]) if st.session_state.form_data["gender"] in current["gender_options"] else 0
    )

    st.markdown(current["label_occupation"], unsafe_allow_html=True)
    occupation = st.text_input("", key="occupation", value=st.session_state.form_data["occupation"])

    # 琉球舞踊について
    st.subheader(current["section_about"])
    st.markdown(current["label_interest"], unsafe_allow_html=True)
    interest_ryukyu = radio_unanswered("interest_ryukyu", current["interest_options"])

    st.markdown(current["label_genres"], unsafe_allow_html=True)
    dance_genres = st.multiselect(
        "", current["genres_options"], key="dance_genres",
        default=[] if type(st.session_state.form_data["dance_genres"]) == str else st.session_state.form_data["dance_genres"]
    )

    st.markdown(current["label_experience"], unsafe_allow_html=True)
    experience_years = st.number_input(
        "", 0, 100, step=1, key="experience_years",
        value=0 if type(st.session_state.form_data["experience_years"]) == str else int(st.session_state.form_data["experience_years"])
    )

    # 評価
    st.subheader(current["section_ratings"])
    st.markdown(current["label_skill"], unsafe_allow_html=True)
    skill_rating = radio_rating("skill_rating")

    st.markdown(current["label_satisfaction"], unsafe_allow_html=True)
    satisfaction_rating = radio_rating("satisfaction_rating")

    st.markdown(current["label_difficulty"], unsafe_allow_html=True)
    self_learning_difficulty = radio_rating("self_learning_difficulty")

    st.markdown(current["label_preservation_opinion"], unsafe_allow_html=True)
    preservation_opinion = radio_rating("preservation_opinion")

    st.markdown(current["label_tech_resistance"], unsafe_allow_html=True)
    tech_resistance = radio_rating("tech_resistance")

    st.markdown(current["label_education_opinion"], unsafe_allow_html=True)
    education_opinion = radio_rating("education_opinion")

    st.markdown(current["label_system_usefulness"], unsafe_allow_html=True)
    system_usefulness = radio_rating("system_usefulness")

    # 学習・練習について
    st.subheader(current["section_practice"])
    st.markdown(current["label_practice_problems"], unsafe_allow_html=True)
    practice_problems = st.multiselect(
        "", current["practice_problems_options"], key="practice_problems",
        default=[] if type(st.session_state.form_data["practice_problems"]) == str else st.session_state.form_data["practice_problems"]
    )

    st.markdown(current["label_practice_tools"], unsafe_allow_html=True)
    practice_tools = st.multiselect(
        "", current["practice_tools_options"], key="practice_tools",
        default=[] if type(st.session_state.form_data["practice_tools"]) == str else st.session_state.form_data["practice_tools"]
    )

    # IT技術活用への意識
    st.subheader(current["section_it"])
    st.markdown(current["label_used_tech_before"], unsafe_allow_html=True)
    used_tech_before = radio_unanswered("used_tech_before", current["used_tech_before_options"])

    st.markdown(current["label_want_compare_3d"], unsafe_allow_html=True)
    want_compare_3d = radio_unanswered("want_compare_3d", current["want_compare_3d_options"])

    # 利用シーンと料金
    st.subheader(current["section_fee"])
    st.markdown(current["label_devices"], unsafe_allow_html=True)
    preferred_devices = st.multiselect(
        "", current["devices_options"], key="preferred_devices",
        default=[] if type(st.session_state.form_data["preferred_devices"]) == str else st.session_state.form_data["preferred_devices"]
    )

    st.markdown(current["label_pay"], unsafe_allow_html=True)
    pay_willingness = st.selectbox(
        "", current["pay_options"], key="pay_willingness",
        index= current["pay_options"].index(st.session_state.form_data["pay_willingness"]) if st.session_state.form_data["pay_willingness"] in current["pay_options"] else 0
    )

    st.markdown(current["label_usefulness_points"], unsafe_allow_html=True)
    usefulness_points = st.multiselect(
        "", current["usefulness_points_options"], key="usefulness_points",
        default=[] if type(st.session_state.form_data["usefulness_points"]) == str else st.session_state.form_data["usefulness_points"]
    )
    st.markdown(current["label_frequency"], unsafe_allow_html=True)
    usage_frequency = st.selectbox(
        "", current["frequency_options"], key="usage_frequency",
        index= current["frequency_options"].index(st.session_state.form_data["usage_frequency"]) if st.session_state.form_data["usage_frequency"] in current["frequency_options"] else 0
    )

    # 動機・懸念点
    st.subheader(current["section_motivation"])
    st.markdown(current["label_motivate_to_start"], unsafe_allow_html=True)
    motivate_to_start = radio_unanswered("motivate_to_start", current["motivate_to_start_options"])

    st.markdown(current["label_start_trigger"], unsafe_allow_html=True)
    start_trigger_feature = st.text_area("", key="start_trigger_feature", value=st.session_state.form_data["start_trigger_feature"])

    st.markdown(current["label_concerns"], unsafe_allow_html=True)
    concerns = st.text_area("", key="concerns", value=st.session_state.form_data["concerns"])

    submitted = st.form_submit_button(current["submit_button"])

if submitted:
    checks = {current["label_email"]: email.strip() != "", current["label_age"]: age > 0,
                current["label_gender"]: gender != current["gender_options"][0], current["label_occupation"]: occupation.strip() != "",
                current["label_interest"]: interest_ryukyu in current["interest_options"],
                current["label_genres"]: len(dance_genres) > 0,
                current["label_preservation_opinion"]: preservation_opinion in range(1, 6),
                current["label_tech_resistance"]: tech_resistance in range(1, 6),
                current["label_education_opinion"]: education_opinion in range(1, 6),
                current["label_system_usefulness"]: system_usefulness in range(1, 6),
                current["label_used_tech_before"]: used_tech_before in current["used_tech_before_options"],
                current["label_want_compare_3d"]: want_compare_3d in current["want_compare_3d_options"],
                current["label_pay"]: bool(pay_willingness),
                current["label_motivate_to_start"]: motivate_to_start in current["motivate_to_start_options"]}
    missing = [label for label, ok in checks.items() if not ok]
    if missing:
        st.error(current["error_required"] + "\n\n" + current["error_missing_intro"] + "\n- " + "\n- ".join(missing))
    else:
        st.success(current["success_message"])
        for col in COLS:
            update_column(col)
        st.switch_page('./pages/confirm.py')
