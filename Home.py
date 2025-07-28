import streamlit as st
from pathlib import Path

def load_css(file_name: str):
    with open(file_name, encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css(Path(__file__).with_name("style.css"))

if "lang" not in st.session_state:
    st.session_state.lang = "ja"

lang_map = {"日本語": "ja", "English": "en"}
lang_choice = st.selectbox("言語 / Language", list(lang_map.keys()))
st.session_state.lang = lang_map[lang_choice]

t = {
    "ja": {
        "font_size_title": "文字の大きさ",
        "small": "小",
        "medium": "中",
        "large": "大",
        "welcome_title": '琉球舞踊習得支援に関する<br>アンケートへようこそ',
        "overview_title": "アンケート概要",
        "overview_desc": "このアンケートは <strong>姿勢推定による琉球舞踊動作の補助に関する調査</strong> です。<br>目的や概要は以下のとおりです。",
        "background_title": "研究背景",
        "background_text": "琉球舞踊は沖縄を代表する伝統文化の一つです。<br>未経験者がこの動作を練習する際、動画などの資料から独学で琉球舞踊を習得するのはハードルが高いです。<br>本研究は初心者が気軽に舞踊を始められるよう、<strong>練習の補助システムの開発</strong>を目指しています。",
        "objectives_title": "アンケート・研究目的",
        "objectives_list": [
            "本アンケートは研究の社会的価値を明らかにすることを目的としています。",
            "開発するシステムが実際に初心者の補助になるかを再検討します。",
            "本研究をその他のダンス等の表現芸術の習得に応用できるかも考察します。"
        ],
        "overview_research_title": "研究概要",
        "overview_research_list": [
            "ダンスの動画から人物の動きを抽出し、3Dモデルを動かします。",
            "手本の動画と初心者の動画から、それぞれの動作を再現した3Dモデルを作成します。",
            "それらを重ねることで、手本の動きと異なる部分を可視化します。"
        ],
        "estimated_time": "回答所要時間： 約5分",
        "survey_button": "アンケートに回答する",
        "admin_login": "管理者ログイン",
        "video_warning": "動画ファイル(for_surveys.mp4)が見つかりません。"
    },
    "en": {
        "font_size_title": "Font Size",
        "small": "Small",
        "medium": "Medium",
        "large": "Large",
        "welcome_title": 'Welcome to the survey on supporting Ryukyu dance learning',
        "overview_title": "Survey Overview",
        "overview_desc": "This survey is about <strong>investigating support for Ryukyu dance movements through posture estimation</strong>.<br>The purpose and overview are as follows.",
        "background_title": "Research Background",
        "background_text": "Ryukyu dance is one of Okinawa's representative traditional cultures.<br>It is challenging for beginners to learn the movements independently from videos and materials.<br>This research aims to develop a support system for beginners to start dancing easily.",
        "objectives_title": "Survey & Research Objectives",
        "objectives_list": [
            "This survey aims to clarify the social value of the research.",
            "We will reconsider whether the developed system is actually helpful for beginners.",
            "We will also consider applying this research to learning other performing arts such as dance."
        ],
        "overview_research_title": "Research Overview",
        "overview_research_list": [
            "Extract movements from dance videos and animate a 3D model.",
            "Create 3D models reproducing movements from the reference and beginner videos.",
            "Overlay them to visualize differences from the reference movements."
        ],
        "estimated_time": "Estimated completion time: About 5 minutes",
        "survey_button": "Take the Survey",
        "admin_login": "Administrator Login",
        "video_warning": "Video file (for_surveys.mp4) not found."
    }
}

current = t[st.session_state.lang]

if "font_size" not in st.session_state:
    st.session_state.font_size = "medium"

st.markdown(
    f'<h5 style="font-weight:600; margin-bottom:0.5rem;">{current["font_size_title"]}</h5>',
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
    f"""
    <style>
    html, body, [class*="css"] {{
        font-size: {font_map[st.session_state.font_size]} !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f'<h1 class="custom-title">{current["welcome_title"]}</h1>',
    unsafe_allow_html=True
)

overview_html = f"""
<div class="overview">
    <h3>{current["overview_title"]}</h3>
    <p>{current["overview_desc"]}</p>
    <hr>
    <h4>{current["background_title"]}</h4>
    <p>{current["background_text"]}</p>
    <hr>
    <h4>{current["objectives_title"]}</h4>
    <ul>
        {''.join(f'<li>{item}</li>' for item in current["objectives_list"])}
    </ul>
    <hr>
    <h4>{current["overview_research_title"]}</h4>
    <ol>
        {''.join(f'<li>{item}</li>' for item in current["overview_research_list"])}
    </ol>
    <p><strong>{current["estimated_time"]}</strong></p>
</div>
"""
st.markdown(overview_html, unsafe_allow_html=True)

video_path = Path(__file__).with_name("for_surveys.mp4")
if video_path.exists():
    st.video(str(video_path))
else:
    st.warning(current["video_warning"])

col1, col2 = st.columns(2)
with col1:
    if st.button(current["survey_button"]):
        st.switch_page("./pages/app.py")
with col2:
    if st.button(current["admin_login"]):
        st.switch_page("./pages/login.py")
