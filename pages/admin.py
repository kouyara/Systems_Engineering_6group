import streamlit as st
import streamlit as st
import pandas as pd
from pathlib import Path
import csv

from plot_utils import (
    show_gender_pie,
    show_age_bar,
    show_interest_bar,
    show_experience_skill_line,
    show_skill_rating_bar,
    show_occupation_bar,
    show_dance_genre_bar,
    show_practice_problems_bar,
    show_practice_tools_bar,
    show_tech_experience_pie,
    show_preferred_devices_bar,
    show_pay_willingness_bar,
    show_system_usefulness_bar,
)

if "admin_user" not in st.session_state or st.session_state.admin_user is None:
    st.warning("このページは管理者専用です。ログインしてください。")
    st.stop()

st.title("管理者ページ")
st.write(f"ログイン中：{st.session_state.admin_user}")

DATA_FILE = Path(__file__).parents[1] / "survey_results.csv"

try:
    pd_major, pd_minor = map(int, pd.__version__.split(".")[:2])

    read_csv_kwargs = dict(
        filepath_or_buffer=DATA_FILE,
        sep=",",
        engine="python",
        quoting=csv.QUOTE_MINIMAL,
        encoding="utf-8",
        dtype=str,
    )

    if (pd_major, pd_minor) >= (1, 3):
        read_csv_kwargs["on_bad_lines"] = "skip"
    else:
        read_csv_kwargs["error_bad_lines"] = False
        read_csv_kwargs["warn_bad_lines"] = True

    df = pd.read_csv(**read_csv_kwargs)

except FileNotFoundError:
    st.error(f"CSVファイルが見つかりません：{DATA_FILE}")
    st.stop()

except pd.errors.EmptyDataError:
    st.info("まだ十分な回答がありません。")
    st.stop()
except Exception as e:
    st.error(f"CSV読み込み時に予期せぬエラーが発生しました:\n{e}")
    st.stop()

df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["experience_years"]  = pd.to_numeric(df["experience_years"], errors="coerce")
df["skill_rating"]      = pd.to_numeric(df["skill_rating"], errors="coerce")

st.title("個別回答ビュー")

if df.empty or df["name"].isna().all():
    st.info("まだ十分な回答がありません。")
else:
    if "individual_idx" not in st.session_state:
        st.session_state.individual_idx = 0

    col_prev, col_next = st.columns([1, 1])
    with col_prev:
        if st.button("⏴ 前の回答"):
            st.session_state.individual_idx = max(st.session_state.individual_idx - 1, 0)
    with col_next:
        if st.button("次の回答 ⏵"):
            st.session_state.individual_idx = min(
                st.session_state.individual_idx + 1, len(df) - 1
            )

    idx = st.session_state.individual_idx
    row = df.iloc[idx]

    st.markdown(f"### 回答者 {idx + 1} / {len(df)}")

    display_df = pd.DataFrame({
        "項目": row.index,
        "回答": row.values
    })
    st.table(display_df)

    col1, col2 = st.columns(2)
    with col1:
        show_gender_pie(df)
    with col2:
        show_age_bar(df)

    # ③ 興味 と ④ 舞踊歴×自己評価
    col3, col4 = st.columns(2)
    with col3:
        show_interest_bar(df)
    with col4:
        show_experience_skill_line(df)

    # ⑤ 技術力・満足度 と ⑥ 職業
    col5, col6 = st.columns(2)
    with col5:
        show_skill_rating_bar(df)
    with col6:
        show_occupation_bar(df)

    st.markdown("---")

    # ⑦〜⑧ ジャンル／練習の困りごと
    col7, col8 = st.columns(2)
    with col7:
        show_dance_genre_bar(df)
    with col8:
        show_practice_problems_bar(df)

    # ⑨ 練習ツール と ⑩ 技術使用経験
    col9, col10 = st.columns(2)
    with col9:
        show_practice_tools_bar(df)
    with col10:
        show_tech_experience_pie(df)

    # ⑪ 使用デバイス と ⑫ 支払い意欲
    col11, col12 = st.columns(2)
    with col11:
        show_preferred_devices_bar(df)
    with col12:
        show_pay_willingness_bar(df)

    # ⑬ システムの有用性
    show_system_usefulness_bar(df)


if st.button("ログアウト"):
    st.session_state.admin_user = None
    st.success("ログアウトしました")
    st.switch_page("Home.py")
