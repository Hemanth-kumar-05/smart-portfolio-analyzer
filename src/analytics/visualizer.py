# src/analytics/visualizer.py

import plotly.express as px
import streamlit as st

def plot_allocation_pie(df):
    fig = px.pie(df, names='Asset', values='Percentage', title="Current Portfolio Allocation")
    st.plotly_chart(fig, use_container_width=True)
