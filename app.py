import streamlit as st
import plotly.express as px
import pandas as pd
from src.frontend1.forms1 import user_profile_form, portfolio_form
from src.frontend1.layout1 import results_and_downloads
from src.frontend1.session_manager1 import reset_session
from src.analytics.portfolio_analyzer import analyze_portfolio

# Page configuration
st.set_page_config(
    page_title="Smart Portfolio Analyzer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.title("Smart Portfolio Analyzer 📊")
st.markdown("""
    Analyze your investment portfolio and get AI-powered recommendations for optimization.
    Enter your profile and portfolio details below to get started.
""")

# Initialize session state
if 'analyze' not in st.session_state:
    st.session_state['analyze'] = False

# Main content
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Your Profile")
    user_profile_form()

with col2:
    st.subheader("Portfolio Details")
    portfolio_form()

# Analysis button
if st.button("Analyze Portfolio", type="primary"):
    if 'user_profile' in st.session_state and 'portfolio' in st.session_state:
        # Perform portfolio analysis
        analysis_results = analyze_portfolio(
            st.session_state.portfolio,
            st.session_state.user_profile
        )
        st.session_state['analysis_results'] = analysis_results
        st.session_state['analyze'] = True
    else:
        st.error("Please complete both profile and portfolio forms first.")

# Reset button
if st.button("Reset"):
    reset_session()
    st.experimental_rerun()

# Show results if analysis is requested
if st.session_state['analyze']:
    st.markdown("---")
    st.subheader("Analysis Results")
    results_and_downloads()

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit")