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

if "lang" not in st.session_state:
    st.session_state.lang = "ja"
lang_map = {"日本語": "ja", "English": "en"}
choice = st.selectbox("言語 / Language", list(lang_map.keys()))
st.session_state.lang = lang_map[choice]

t = {
    "ja": {
        "admin_only_warning": "このページは管理者専用です。ログインしてください。",
        "font_size_title": "文字の大きさ",
        "small": "小",
        "medium": "中",
        "large": "大",
        "admin_page_title": "管理者ページ",
        "logged_in_as": "ログイン中：",
        "csv_not_found_error": "CSVファイルが見つかりません：",
        "empty_data_info": "まだ十分な回答がありません。",
        "csv_unexpected_error": "CSV読み込み時に予期せぬエラーが発生しました:\n",
        "individual_view_title": "個別回答ビュー",
        "prev_button": "⏴ 前の回答",
        "next_button": "次の回答 ⏵",
        "responder_label": "回答者 {idx} / {total}",
        "table_field": "項目",
        "table_response": "回答",
        "logout_button": "ログアウト",
        "logout_success": "ログアウトしました",
    },
    "en": {
        "admin_only_warning": "This page is for administrators only. Please log in.",
        "font_size_title": "Font Size",
        "small": "Small",
        "medium": "Medium",
        "large": "Large",
        "admin_page_title": "Administrator Page",
        "logged_in_as": "Logged in as: ",
        "csv_not_found_error": "CSV file not found: ",
        "empty_data_info": "Not enough responses yet.",
        "csv_unexpected_error": "Unexpected error while loading CSV:\n",
        "individual_view_title": "Individual Response View",
        "prev_button": "⏴ Previous",
        "next_button": "Next ⏵",
        "responder_label": "Respondent {idx} / {total}",
        "table_field": "Field",
        "table_response": "Response",
        "logout_button": "Logout",
        "logout_success": "You have been logged out",
    }
}
current = t[st.session_state.lang]

if "admin_user" not in st.session_state or st.session_state.admin_user is None:
    st.warning(current["admin_only_warning"])
    st.stop()

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
    f"<style>html, body, [class*='css']{{font-size: {font_map[st.session_state.font_size]} !important;}}</style>",
    unsafe_allow_html=True
)

st.title(current["admin_page_title"])
st.write(f"{current['logged_in_as']}{st.session_state.admin_user}")

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
    st.error(f"{current['csv_not_found_error']}{DATA_FILE}")
    st.stop()
except pd.errors.EmptyDataError:
    st.info(current["empty_data_info"])
    st.stop()
except Exception as e:
    st.error(f"{current['csv_unexpected_error']}{e}")
    st.stop()

df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["experience_years"] = pd.to_numeric(df["experience_years"], errors="coerce")
df["skill_rating"] = pd.to_numeric(df["skill_rating"], errors="coerce")

st.title(current["individual_view_title"])
if df.empty or df.get("name", pd.Series()).isna().all():
    st.info(current["empty_data_info"])
else:
    if "individual_idx" not in st.session_state:
        st.session_state.individual_idx = 0
    col_prev, col_next = st.columns([1, 1])
    with col_prev:
        if st.button(current["prev_button"]):
            st.session_state.individual_idx = max(st.session_state.individual_idx - 1, 0)
    with col_next:
        if st.button(current["next_button"]):
            st.session_state.individual_idx = min(st.session_state.individual_idx + 1, len(df) - 1)
    idx = st.session_state.individual_idx
    row = df.iloc[idx]
    st.markdown(f"### {current['responder_label'].format(idx=idx+1, total=len(df))}")
    display_df = pd.DataFrame({
        current["table_field"]: row.index,
        current["table_response"]: row.values
    })
    st.table(display_df)

    col1, col2 = st.columns(2)
    with col1:
        show_gender_pie(df)
    with col2:
        show_age_bar(df)

    col3, col4 = st.columns(2)
    with col3:
        show_interest_bar(df)
    with col4:
        show_experience_skill_line(df)

    col5, col6 = st.columns(2)
    with col5:
        show_skill_rating_bar(df)
    with col6:
        show_occupation_bar(df)

    st.markdown("---")

    col7, col8 = st.columns(2)
    with col7:
        show_dance_genre_bar(df)
    with col8:
        show_practice_problems_bar(df)

    col9, col10 = st.columns(2)
    with col9:
        show_practice_tools_bar(df)
    with col10:
        show_tech_experience_pie(df)

    col11, col12 = st.columns(2)
    with col11:
        show_preferred_devices_bar(df)
    with col12:
        show_pay_willingness_bar(df)

    show_system_usefulness_bar(df)

if st.button(current["logout_button"]):
    st.session_state.admin_user = None
    st.success(current["logout_success"])
    st.switch_page("Home.py")
