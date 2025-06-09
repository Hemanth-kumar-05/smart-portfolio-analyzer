import streamlit as st

def reset_session():
    """Clears all session state and reruns the app."""
    st.session_state.clear()
    st.experimental_rerun()