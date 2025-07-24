import streamlit as st

if "admin_user" not in st.session_state or st.session_state.admin_user is None:
    st.warning("このページは管理者専用です。ログインしてください。")
    st.stop()

st.title("管理者ページ")
st.write(f"ログイン中：{st.session_state.admin_user}")

# アンケート結果の表示や管理ツールなどを書く
st.markdown("### ここに管理者用機能を追加できます")

if st.button("ログアウト"):
    st.session_state.admin_user = None
    st.success("ログアウトしました")
    st.switch_page("Home.py")
