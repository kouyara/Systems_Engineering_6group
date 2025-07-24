import streamlit as st
import firebase_admin
from firebase_admin import auth, credentials

# Firebase初期化（初回のみ）
if not firebase_admin._apps:
    cred = credentials.Certificate(dict(st.secrets["FIREBASE"]))
    firebase_admin.initialize_app(cred)



st.title("ログインページ")

email = st.text_input("メールアドレス")
password = st.text_input("パスワード", type="password")

if "user" not in st.session_state:
    st.session_state.user = None

if st.button("ログイン"):
    try:
        user = auth.get_user_by_email(email)
        st.session_state.user = user.email  # セッションに保存
        st.success("ログイン成功。左側の『app』ページへ移動してください。")
    except:
        st.error("ログイン失敗。登録されていません。")