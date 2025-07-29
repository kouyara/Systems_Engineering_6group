import streamlit as st
import time

if "lang" not in st.session_state:
    st.session_state.lang = "ja"
lang_map = {"日本語": "ja", "English": "en"}

t = {
    "ja" : {
        "font_size_title": "文字の大きさ",
        "small": "小",
        "medium": "中",
        "large": "大",
        "title": "アンケートの送信が完了しました",
        "contents": "ご協力ありがとうございました。数秒後にトップページに戻ります。"
    },
    "en" : {
        "font_size_title": "Font Size",
        "small": "Small",
        "medium": "Medium",
        "large": "Large",
        "title": "Your Survey Has Been Submitted",
        "contents": "Thank you for your cooperation. You will be redirected to the homepage in a few seconds."
    }
}

current = t[st.session_state.lang]

if "font_size" not in st.session_state:
    st.session_state.font_size = "medium"

font_map = {"small": "14px", "medium": "18px", "large": "24px"}
st.markdown(
    f"<style>html, body, [class*=\"css\"] {{font-size: {font_map[st.session_state.font_size]} !important;}}</style>",
    unsafe_allow_html=True
)
st.markdown(
    "<style>.st-emotion-cache-1s2v671 { display: contents; }</style>",
    unsafe_allow_html=True
)
st.balloons()
st.subheader(current["title"])

st.success(current["contents"])
time.sleep(5)
st.switch_page('./Home.py')