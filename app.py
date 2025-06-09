import streamlit as st
from src.frontend.forms import user_profile_form, portfolio_form
from src.frontend.layout import results_and_downloads
from src.frontend.session_manager import reset_session

st.set_page_config(page_title="Smart Portfolio Analyzer", layout="centered")
st.title("Smart Portfolio Analyzer")

user_profile_form()
portfolio_form()

col1, col2 = st.columns(2)
with col1:
    if st.button("Analyze"):
        st.session_state['analyze'] = True
with col2:
    if st.button("Reset"):
        reset_session()

results_and_downloads()