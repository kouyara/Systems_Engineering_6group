import streamlit as st
import pandas as pd
import os

t = {
    "ja": {
        "font_size_title": "文字の大きさ",
        "small": "小",
        "medium": "中",
        "large": "大",
        "form_title": "アンケートフォーム (琉球舞踊)",
        "required_note": "※   は必須項目です。",
        "section_basic": "■ 基本情報",
        "label_email": "メールアドレス",
        "label_age": "年齢 ",
        "label_gender": "性別  ",
        "gender_options": ["選択してください", "男性", "女性", "その他"],
        "label_occupation": "職業 (例: 学生・会社員 など)  ",
        "section_about": "■ 琉球舞踊について",
        "label_interest": "琉球舞踊に興味はありますか？  ",
        "interest_options": ["機会があれば習いたい", "見てみたい", "いいえ"],
        "label_genres": "経験のある舞踊・ダンスジャンル（複数選択可）  ",
        "genres_options": ["琉球舞踊", "その他の伝統舞踊", "バレエ", "ジャズ", "コンテンポラリー", "社交", "ヒップホップ", "その他", "未経験"],
        "label_experience": "ダンス歴 (年数)",
        "section_ratings": "■ 評価（1〜5）",
        "label_skill": "舞踊の技術力を1〜5で評価してください",
        "label_satisfaction": "舞踊の満足度を1〜5で評価してください",
        "label_difficulty": "独学で舞踊を学ぶことの困難度を1〜5で評価してください",
        "label_preservation_opinion": "伝統芸能を現代技術で継承・普及する取り組みについてどう思いますか？  ",
        "label_tech_resistance": "伝統舞踊の保存や教育にIT技術を使うことへの抵抗感はありますか？  ",
        "label_education_opinion": "このシステムが教育機関で利用されることについてどう思いますか？  ",
        "label_system_usefulness": "このシステムは舞踊・ダンスの練習に役立つと思いますか？  ",
        "section_practice": "■ 学習・練習について",
        "label_practice_problems": "練習で困っていること（複数選択可）",
        "practice_problems_options": ["正しい動きがわからない", "自分の動作が正しいかわからない", "習得時間がかかる", "手本が少ない", "教わる機会・教室がない", "練習環境がない", "時間が取れない", "モチベーションがない", "その他記述"],
        "label_practice_tools": "舞踊・ダンスの練習で利用しているツール（複数選択可）",
        "practice_tools_options": ["実際のレッスン", "レッスン動画", "自撮り確認", "鏡", "AR/VR", "練習アプリ", "その他"],
        "section_it": "■ IT 技術活用への意識",
        "label_used_tech_before": "AR/VR・モーションキャプチャなどの技術を使用したことはありますか？  ",
        "used_tech_before_options": ["はい", "いいえ"],
        "label_want_compare_3d": "3Dモデルや比較映像で自分の動きを確認したいですか？  ",
        "want_compare_3d_options": ["はい", "いいえ"],
        "section_fee": "■ 利用シーンと料金",
        "label_devices": "どのようなデバイスで使いたいですか？（複数選択可）",
        "devices_options": ["PC", "スマートフォン", "タブレット", "その他"],
        "label_pay": "費用がかかっても使用したいと思いますか？  ",
        "pay_options": ["無料でなければ使わない", "月100円", "月300円", "月500円〜1,000円", "内容次第でそれ以上払える", "わからない"],
        "label_usefulness_points": "役立つと思う点（複数選択可）",
        "usefulness_points_options": ["正しい動作を習得しやすい", "時間短縮になる", "独学がしやすい", "客観的に動作を見れる", "映像ではわからない部分が見れる"],
        "label_frequency": "どれくらいの頻度で利用したいですか？",
        "frequency_options": ["未回答", "月1", "週1", "それ以上"],
        "section_motivation": "■ 動機・懸念点",
        "label_motivate_to_start": "このシステムは琉球舞踊を始めるきっかけになると思いますか？  ",
        "motivate_to_start_options": ["はい", "いいえ"],
        "label_start_trigger": "「この機能があれば始めるきっかけになる」と思うもの",
        "label_concerns": "不安・懸念点",
        "submit_button": "送信",
        "error_required": "必須項目（* 印）をすべて入力・選択してください。",
        "error_missing_intro": "**未入力 / 未選択項目:**",
        "success_message": "ご回答ありがとうございました！",
        "unanswered": "未回答",
        "confirm_title": "アンケート確認画面",
        "no_list": "回答なし",
        "fix_button": "内容を修正する",
        "confirm_button": "この内容で送信",
    },
    "en": {
        "font_size_title": "Font Size",
        "small": "Small",
        "medium": "Medium",
        "large": "Large",
        "form_title": "Survey Form (Ryukyu Dance)",
        "required_note": "* indicates required fields.",
        "section_basic": "■ Basic Information",
        "label_email": "Email Address  ",
        "label_age": "Age  ",
        "label_gender": "Gender  ",
        "gender_options": ["Please select", "Male", "Female", "Other"],
        "label_occupation": "Occupation (e.g., Student, Company Employee)  ",
        "section_about": "■ About Ryukyu Dance",
        "label_interest": "Are you interested in Ryukyu Dance?  ",
        "interest_options": ["Would like to learn if opportunity arises", "Would like to watch", "No"],
        "label_genres": "Dance genres experienced (multiple selections)  ",
        "genres_options": ["Ryukyu Dance", "Other Traditional Dance", "Ballet", "Jazz", "Contemporary", "Social Dance", "Hip-hop", "Other", "No Experience"],
        "label_experience": "Dance Experience (Years)",
        "section_ratings": "■ Ratings (1-5)",
        "label_skill": "Please rate your dance skills from 1 to 5",
        "label_satisfaction": "Please rate your satisfaction with dance from 1 to 5",
        "label_difficulty": "Please rate the difficulty of self-learning dance from 1 to 5",
        "label_preservation_opinion": "What do you think about preserving and promoting traditional performing arts through modern technology?  ",
        "label_tech_resistance": "Do you have any resistance to using IT for preservation and education of traditional dance?  ",
        "label_education_opinion": "What do you think about using this system in educational institutions?  ",
        "label_system_usefulness": "Do you think this system would help with dance practice?  ",
        "section_practice": "■ About Learning & Practice",
        "label_practice_problems": "Problems faced during practice (multiple selections)",
        "practice_problems_options": ["Not sure of correct movements", "Not sure if my movements are correct", "Takes time to master", "Few examples available", "No opportunity or classes", "No practice environment", "Cannot find time", "Lack of motivation", "Other (please specify)"],
        "label_practice_tools": "Tools used for dance practice (multiple selections)",
        "practice_tools_options": ["In-person lessons", "Lesson videos", "Self-recording", "Mirror", "AR/VR", "Practice apps", "Other"],
        "section_it": "■ Attitudes Toward IT",
        "label_used_tech_before": "Have you used AR/VR or motion capture technologies?  ",
        "used_tech_before_options": ["Yes", "No"],
        "label_want_compare_3d": "Would you like to check your movements with 3D models or comparison videos?  ",
        "want_compare_3d_options": ["Yes", "No"],
        "section_fee": "■ Usage & Fees",
        "label_devices": "Which devices would you like to use? (multiple selections)",
        "devices_options": ["PC", "Smartphone", "Tablet", "Other"],
        "label_pay": "Would you be willing to pay for this system?  ",
        "pay_options": ["Won't use unless free", "100 JPY/month", "300 JPY/month", "500–1000 JPY/month", "Willing to pay more depending on content", "Not sure"],
        "label_usefulness_points": "Points you think would be helpful (multiple selections)",
        "usefulness_points_options": ["Easier to learn correct movements", "Saves time", "Facilitates self-learning", "Can view movements objectively", "See details not visible in videos"],
        "label_frequency": "How often would you like to use it?",
        "frequency_options": ["Unanswered", "Once a month", "Once a week", "More often"],
        "section_motivation": "■ Motivation & Concerns",
        "label_motivate_to_start": "Do you think this system would motivate you to start Ryukyu dance?  ",
        "motivate_to_start_options": ["Yes", "No"],
        "label_start_trigger": "Features that would motivate you to start",
        "label_concerns": "Anxieties / Concerns",
        "submit_button": "Submit",
        "error_required": "Please complete all required fields (*) .",
        "error_missing_intro": "**Missing items:**",
        "success_message": "Thank you for your response!",
        "unanswered": "Unanswered",
        "confirm_title": "Survey Review",
        "no_list": "No answer",
        "fix_button": "Go Back and Edit",
        "confirm_button": "Confirm and Submit",
    }
}

if "lang" not in st.session_state:
    st.session_state.lang = "ja"

current = t[st.session_state.lang]

st.title(current["confirm_title"])

lang_map = {"日本語": "ja", "English": "en"}
st.session_state.lang = lang_map[st.selectbox("言語 / Language", list(lang_map.keys()))]

if "form_data" not in st.session_state:
    st.error("先にアンケートを入力してください。")

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

form_values = {col: st.session_state.form_data.get(col, None) for col in COLS}

if "form_data" not in st.session_state:
    st.error("先にアンケートを入力してください。")
    st.stop()

data = st.session_state.form_data

with st.form("confirm_form"):
    # 基本情報
    st.subheader(current["section_basic"])
    st.write(f"{current['label_email']}: {form_values['email']}")
    st.write(f"{current['label_age']}: {form_values['age']}")
    st.write(f"{current['label_gender']}: {form_values['gender']}")
    st.write(f"{current['label_occupation']}: {form_values['occupation']}")

    # 琉球舞踊について
    st.subheader(current["section_about"])
    st.write(f"{current['label_interest']}: {form_values['interest_ryukyu']}")
    st.write(f"{current['label_genres']}: ")
    if len(form_values["dance_genres"]) > 0:
        for f in form_values["dance_genres"]:
            st.write(f"・{f}")
    else :
        st.write(current["no_list"])

    if form_values["experience_years"] > 0:
        exp_year = f"{form_values['experience_years']}年"
    else:
        exp_year = current["no_list"]
    st.write(f"{current['label_experience']}: {exp_year}")

    # 評価
    st.subheader(current["section_ratings"])
    st.write(
        f"{current['label_skill']}: {form_values['skill_rating'] if type(form_values['skill_rating']) == int else current['no_list']}"
    )
    st.write(f"{current['label_satisfaction']}: {form_values['satisfaction_rating'] if type(form_values['satisfaction_rating']) == int else current['no_list']}")

    st.write(f"{current['label_difficulty']}: {form_values['self_learning_difficulty'] if type(form_values['self_learning_difficulty']) == int else current['no_list']}")

    st.write(f"{current['label_preservation_opinion']}: {form_values['preservation_opinion']}")

    st.write(f"{current['label_tech_resistance']}: {form_values['tech_resistance']}")

    st.write(f"{current['label_education_opinion']}: {form_values['education_opinion']}")

    st.write(f"{current['label_system_usefulness']}: {form_values['system_usefulness']}")

    # 学習・練習について
    st.subheader(current["section_practice"])
    st.write(f"{current['label_practice_problems']}: ")
    if len(form_values["practice_problems"]) > 0:
        for f in form_values["practice_problems"]:
            st.write(f"・{f}")
    else:
        st.write(current["no_list"])

    st.write(f"{current['label_practice_tools']}: ")
    if len(form_values["practice_tools"]) > 0:
        for f in form_values["practice_tools"]:
            st.write(f"・{f}")
    else:
        st.write(current["no_list"])

    # IT技術活用への意識
    st.subheader(current['section_it'])
    st.write(f"{current['label_used_tech_before']}: {form_values['used_tech_before']}")

    st.write(f"{current['label_want_compare_3d']}: {form_values['want_compare_3d']}")

    # 利用シーンと料金
    st.subheader(current["section_fee"])
    st.write(f"{current['label_devices']}: ")
    if len(form_values["preferred_devices"]) > 0:
        for f in form_values["preferred_devices"]:
            st.write(f"・{f}")
    else:
        st.write(current["no_list"])

    st.write(f"{current['label_pay']}: {form_values['pay_willingness']}")

    st.write(f"{current['label_usefulness_points']}:")
    if len(form_values["usefulness_points"]) > 0:
        for f in form_values["usefulness_points"]:
            st.write(f"・{f}")
    else:
        st.write(current["no_list"])
    st.write(f"{current['label_frequency']}: {form_values['usage_frequency']}")

    # 動機・懸念点
    st.subheader(current["section_motivation"])
    st.write(f"{current['label_motivate_to_start']}: {form_values['motivate_to_start']} ")
    st.write(f"{current['label_start_trigger']}:")
    if form_values['start_trigger_feature'] != "":
        st.write(f"{form_values['start_trigger_feature']}")
    else:
        st.write(current["no_list"])

    st.write(f"{current['label_concerns']}:")
    if form_values['concerns'] != "":
        st.write(f"{form_values['concerns']}")
    else:
        st.write(current["no_list"])

    col1, col2 = st.columns(2)
    with col1:
        if st.form_submit_button(current["fix_button"]):
            st.switch_page("./pages/app.py")
    with col2:
        if st.form_submit_button(current["confirm_button"]):
            df = pd.read_csv(DATA_FILE)
            df.loc[len(df)] = {
                "email": form_values["email"],
                "age": form_values["age"],
                "gender": form_values["gender"],
                "occupation": form_values["occupation"],
                "interest_ryukyu": form_values["interest_ryukyu"], 
                "dance_genres": ";".join(form_values["dance_genres"]),
                "experience_years": form_values["experience_years"], 
                "skill_rating": form_values["skill_rating"],
                "satisfaction_rating": form_values["satisfaction_rating"], 
                "self_learning_difficulty": form_values["self_learning_difficulty"],
                "practice_problems": ";".join(form_values["practice_problems"]), 
                "practice_tools": ";".join(form_values["practice_tools"]),
                "preservation_opinion": form_values["preservation_opinion"], 
                "tech_resistance": form_values["tech_resistance"],
                "education_opinion": form_values["education_opinion"], 
                "used_tech_before": form_values["used_tech_before"],
                "want_compare_3d": form_values["want_compare_3d"], 
                "preferred_devices": ";".join(form_values["preferred_devices"]),
                "pay_willingness": form_values["pay_willingness"], 
                "system_usefulness": form_values["system_usefulness"],
                "usefulness_points": ";".join(form_values["usefulness_points"]), 
                "usage_frequency": form_values["usage_frequency"],
                "motivate_to_start": form_values["motivate_to_start"], 
                "start_trigger_feature": form_values["start_trigger_feature"],
                "concerns": form_values["concerns"]
            }
            df.to_csv(DATA_FILE, index=False)
            st.switch_page("./pages/complete.py")