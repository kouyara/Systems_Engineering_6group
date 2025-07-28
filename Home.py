import streamlit as st
from pathlib import Path

def load_css(file_name: str):
    with open(file_name, encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css(Path(__file__).with_name("style.css"))

st.markdown(
    '<h1 class="custom-title">琉球舞踊習得支援に関する<br>アンケートへようこそ</h1>',
    unsafe_allow_html=True
)

overview_html = """
<div class="overview">
    <h3>アンケート概要</h3>
    <p>このアンケートは <strong>姿勢推定による琉球舞踊動作の補助に関する調査</strong> です。<br>
        目的や概要は以下のとおりです。</p>
    <hr>
    <h4>研究背景</h4>
    <p>琉球舞踊は沖縄を代表する伝統文化の一つです。<br>
        未経験者がこの動作を練習する際、動画などの資料から独学で琉球舞踊を習得するのはハードルが高いです。<br>
        本研究は初心者が気軽に舞踊を始められるよう、<strong>練習の補助システムの開発</strong>を目指しています。</p>
    <hr>
    <h4>アンケート・研究目的</h4>
    <ul>
        <li>本アンケートは研究の社会的価値を明らかにすることを目的としています。</li>
        <li>開発するシステムが実際に初心者の補助になるかを再検討します。</li>
        <li>本研究をその他のダンス等の表現芸術の習得に応用できるかも考察します。</li>
    </ul>
    <hr>
    <h4>研究概要</h4>
    <ol>
        <li>ダンスの動画から人物の動きを抽出し、3Dモデルを動かします。</li>
        <li>手本の動画と初心者の動画から、それぞれの動作を再現した3Dモデルを作成します。</li>
        <li>それらを重ねることで、手本の動きと異なる部分を可視化します。</li>
    </ol>
    <p><strong>回答所要時間： 約5分</strong></p>
</div>
"""
st.markdown(overview_html, unsafe_allow_html=True)

video_path = Path(__file__).with_name("for_surveys.mp4")
if video_path.exists():
    st.video(str(video_path))
else:
    st.warning("動画ファイル(for_surveys.mp4)が見つかりません。")

col1, col2 = st.columns(2)
with col1:
    if st.button("アンケートに回答する"):
        st.switch_page("./pages/app.py")

with col2:
    if st.button("管理者ログイン"):
        st.switch_page("./pages/login.py")
