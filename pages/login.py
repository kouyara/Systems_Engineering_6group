import streamlit as st
import firebase_admin
from firebase_admin import auth, credentials
from datetime import datetime, timedelta

SESSION_DURATION = timedelta(hours=1)

t = {
    "ja": {
        "title": "ログインページ",
        "home_button": "ホーム画面へ戻る",
        "font_size_title": "文字の大きさ",
        "small": "小",
        "medium": "中",
        "large": "大",
        "email_label": "メールアドレス",
        "password_label": "パスワード",
        "login_button": "ログイン",
        "session_expired": "セッションの有効期限が切れました。再度ログインしてください。",
        "error_email_blank": "メールアドレスを入力してください。",
        "error_password_blank": "パスワードを入力してください。",
        "login_success": "ログイン成功！管理者ページに移動します",
        "login_fail": "ログイン失敗！ページ管理人に問い合わせしてください",
        "error_details_prefix": "エラー詳細: "
    },
    "en": {
        "title": "Login Page",
        "home_button": "Back to Home",
        "font_size_title": "Font Size",
        "small": "Small",
        "medium": "Medium",
        "large": "Large",
        "email_label": "Email Address",
        "password_label": "Password",
        "login_button": "Login",
        "session_expired": "Your session has expired. Please log in again.",
        "error_email_blank": "Please enter your email address.",
        "error_password_blank": "Please enter your password.",
        "login_success": "Login successful! Redirecting to admin page.",
        "login_fail": "Login failed! Please contact the page administrator.",
        "error_details_prefix": "Error details: "
    }
}


if "lang" not in st.session_state:
    st.session_state.lang = "ja"

lang_map = {"日本語": "ja", "English": "en"}
display_langs = list(lang_map.keys())
reverse_map = {v: k for k, v in lang_map.items()}
initial_index = display_langs.index(reverse_map.get(st.session_state.lang, "日本語"))
lang_choice = st.selectbox("言語 / Language", display_langs, index=initial_index)
st.session_state.lang = lang_map[lang_choice]

current = t[st.session_state.lang]
unanswered = current.get("unanswered", "")

if st.button(current["home_button"]):
    st.switch_page("./Home.py")

st.title(current["title"])

if "font_size" not in st.session_state:
    st.session_state.font_size = "medium"
st.markdown(f"<h5 style='font-weight:600; margin-bottom:0.5rem;'>{current['font_size_title']}</h5>", unsafe_allow_html=True)
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
st.markdown(f"<style>html, body, [class*=\"css\"] {{font-size: {font_map[st.session_state.font_size]} !important;}}</style>", unsafe_allow_html=True)
st.markdown("<style>.st-emotion-cache-1s2v671 { display: contents; }</style>", unsafe_allow_html=True)

if "login_expires_at" in st.session_state and datetime.now() > st.session_state.login_expires_at:
    st.session_state.pop("admin_user", None)
    st.session_state.pop("login_expires_at", None)
    st.warning(current["session_expired"])

if (
    st.session_state.get("admin_user")
    and st.session_state.get("login_expires_at")
    and datetime.now() <= st.session_state["login_expires_at"]
):
    st.switch_page("./pages/admin.py")

if not firebase_admin._apps:
    cred = credentials.Certificate(dict(st.secrets["FIREBASE"]))
    firebase_admin.initialize_app(cred)

with st.form("login_form"):
    email = st.text_input(current["email_label"])
    password = st.text_input(current["password_label"], type="password")
    submitted = st.form_submit_button(current["login_button"])

if submitted:
    if not email.strip():
        st.error(current["error_email_blank"])
    elif not password:
        st.error(current["error_password_blank"])
    else:
        try:
            user = auth.get_user_by_email(email)
            st.session_state.admin_user = user.email
            st.session_state.login_expires_at = datetime.now() + SESSION_DURATION
            st.success(current["login_success"])
            st.switch_page("./pages/admin.py")
        except Exception as e:
            st.error(current["login_fail"])
            st.error(f"{current['error_details_prefix']}{e}")
