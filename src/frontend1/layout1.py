import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import io

def create_portfolio_pie_chart(portfolio):
    """Create a pie chart for portfolio allocation."""
    labels = list(portfolio.keys())
    values = list(portfolio.values())
    
    fig = px.pie(
        values=values,
        names=labels,
        title="Portfolio Allocation",
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig

def create_risk_analysis(portfolio, risk_tolerance):
    """Create risk analysis visualization."""
    # Define risk scores for different assets
    risk_scores = {
        'stocks': 0.7,
        'bonds': 0.3,
        'crypto': 0.9,
        'real_estate': 0.6,
        'cash': 0.1,
        'other': 0.5
    }
    
    # Calculate weighted risk score
    total_risk = sum(portfolio[asset] * risk_scores[asset] for asset in portfolio) / 100
    
    # Create gauge chart
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=total_risk * 100,
        title={'text': "Portfolio Risk Score"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 30], 'color': "lightgreen"},
                {'range': [30, 70], 'color': "yellow"},
                {'range': [70, 100], 'color': "red"}
            ],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': 50
            }
        }
    ))
    return fig

def results_and_downloads():
    """Display analysis results and download options."""
    analyze_clicked = st.session_state.get('analyze', False)
    if not analyze_clicked:
        return

    st.markdown("### Portfolio Analysis Results")
    
    # Get data from session state
    portfolio = st.session_state.get('portfolio', {})
    user_profile = st.session_state.get('user_profile', {})
    
    if not portfolio or not user_profile:
        st.warning("Please complete both profile and portfolio forms first.")
        return

    # Create tabs for different sections
    tab1, tab2, tab3 = st.tabs(["Portfolio Overview", "Risk Analysis", "Recommendations"])
    
    with tab1:
        st.plotly_chart(create_portfolio_pie_chart(portfolio), use_container_width=True)
        
        # Display portfolio summary
        st.markdown("#### Portfolio Summary")
        df_portfolio = pd.DataFrame({
            'Asset': list(portfolio.keys()),
            'Allocation (%)': list(portfolio.values())
        })
        st.dataframe(df_portfolio, use_container_width=True)
    
    with tab2:
        st.plotly_chart(create_risk_analysis(portfolio, user_profile.get('risk_tolerance')), use_container_width=True)
        
        # Risk analysis text
        st.markdown("#### Risk Analysis")
        risk_tolerance = user_profile.get('risk_tolerance', 'Moderate')
        st.write(f"Your risk tolerance: {risk_tolerance}")
        
        # Add risk assessment text
        total_risk = sum(portfolio.values()) / 100
        if total_risk > 0.7:
            st.warning("Your portfolio appears to be high risk. Consider rebalancing towards more conservative assets.")
        elif total_risk < 0.3:
            st.info("Your portfolio is very conservative. You might want to consider adding some growth assets.")
        else:
            st.success("Your portfolio risk level appears to be well-balanced.")
    
    with tab3:
        st.markdown("#### AI-Powered Recommendations")
        # Placeholder for AI recommendations
        st.write("Based on your profile and portfolio, here are some recommendations:")
        
        recommendations = [
            "Consider diversifying your portfolio across different asset classes",
            "Review your risk tolerance alignment with current allocation",
            "Regularly rebalance your portfolio to maintain target allocations",
            "Consider tax-efficient investment strategies"
        ]
        
        for rec in recommendations:
            st.write(f"- {rec}")
    
    # Download section
    st.markdown("---")
    st.markdown("### Download Report")
    
    # Prepare data for download
    report_data = {
        "User Profile": {
            "Age": user_profile.get('age', ''),
            "Investment Horizon": user_profile.get('investment_horizon', ''),
            "Risk Tolerance": user_profile.get('risk_tolerance', ''),
            "Investment Goals": ', '.join(user_profile.get('investment_goals', [])),
            "Monthly Investment": f"${user_profile.get('monthly_investment', 0):,.2f}",
            "Existing Investments": f"${user_profile.get('existing_investments', 0):,.2f}"
        },
        "Portfolio Allocation": portfolio
    }
    
    # Convert to DataFrame for CSV export
    df_report = pd.DataFrame([
        ["User Profile", "Value"],
        ["Age", user_profile.get('age', '')],
        ["Investment Horizon", user_profile.get('investment_horizon', '')],
        ["Risk Tolerance", user_profile.get('risk_tolerance', '')],
        ["Investment Goals", ', '.join(user_profile.get('investment_goals', []))],
        ["Monthly Investment", f"${user_profile.get('monthly_investment', 0):,.2f}"],
        ["Existing Investments", f"${user_profile.get('existing_investments', 0):,.2f}"],
        ["", ""],
        ["Portfolio Allocation", "Percentage"],
    ] + [[asset, f"{value}%"] for asset, value in portfolio.items()])
    
    # Create download buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Download PDF Report"):
            st.info("PDF download feature coming soon!")
    
    with col2:
        csv = df_report.to_csv(index=False)
        st.download_button(
            label="Download CSV Report",
            data=csv,
            file_name="portfolio_analysis.csv",
            mime="text/csv"
        )