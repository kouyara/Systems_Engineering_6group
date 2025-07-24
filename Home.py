import streamlit as st

st.title("アンケートへようこそ！")

st.markdown("""
このアンケートは◯◯に関する調査です。  
目的や概要は以下のとおりです：
- 例：ナビアプリの利用実態の調査
- 回答所要時間：3分程度
""")

col1, col2 = st.columns(2)
with col1:
    if st.button("アンケートに回答する"):
        st.switch_page("./pages/app.py")  # 遷移

with col2:
    if st.button("管理者ログイン"):
        st.switch_page("./pages/login.py")  # 遷移
