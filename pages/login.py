import streamlit as st
import firebase_admin
from firebase_admin import auth, credentials
from datetime import datetime, timedelta

SESSION_DURATION = timedelta(hours=1)

if "login_expires_at" in st.session_state:
    if datetime.now() > st.session_state.login_expires_at:
        st.session_state.pop("admin_user", None)
        st.session_state.pop("login_expires_at", None)
        st.warning("セッションの有効期限が切れました。再度ログインしてください。")

if (
    st.session_state.get("admin_user")
    and st.session_state.get("login_expires_at")
    and datetime.now() <= st.session_state["login_expires_at"]
):
    st.switch_page("./pages/admin.py")

if not firebase_admin._apps:
    cred = credentials.Certificate(dict(st.secrets["FIREBASE"]))
    firebase_admin.initialize_app(cred)

st.title("ログインページ")

with st.form("login_form"):
    email = st.text_input("メールアドレス")
    password = st.text_input("パスワード", type="password")
    submitted = st.form_submit_button("ログイン")

if submitted:
    if not email.strip():
        st.error("メールアドレスを入力してください。")
    elif not password:
        st.error("パスワードを入力してください。")
    else:
        try:
            user = auth.get_user_by_email(email)
            st.session_state.admin_user = user.email
            st.session_state.login_expires_at = datetime.now() + SESSION_DURATION
            st.success("ログイン成功！管理者ページに移動します")
            st.switch_page("./pages/admin.py")
        except Exception as e:
            st.error("ログイン失敗！ページ管理人に問い合わせしてください")
            st.error(f"エラー詳細: {e}")
            print(e)
