import streamlit as st

def user_profile_form():
    """Create and handle the user profile form."""
    # Initialize session state for user profile if not exists
    if 'user_profile' not in st.session_state:
        st.session_state.user_profile = {
            'age': 30,
            'investment_horizon': "Medium Term (3-7 years)",
            'risk_tolerance': "Moderate",
            'investment_goals': ["Wealth Growth"],
            'monthly_investment': 1000,
            'existing_investments': 10000
        }

    with st.form(key="user_profile_form"):
        # Personal Information
        st.write("### Personal Information")
        age = st.number_input("Age", min_value=18, max_value=100, value=st.session_state.user_profile['age'])
        
        # Investment Horizon
        investment_horizon = st.selectbox(
            "Investment Horizon",
            ["Short Term (1-3 years)", "Medium Term (3-7 years)", "Long Term (7+ years)"],
            index=["Short Term (1-3 years)", "Medium Term (3-7 years)", "Long Term (7+ years)"].index(st.session_state.user_profile['investment_horizon'])
        )
        
        # Risk Tolerance
        risk_tolerance = st.select_slider(
            "Risk Tolerance",
            options=["Very Conservative", "Conservative", "Moderate", "Aggressive", "Very Aggressive"],
            value=st.session_state.user_profile['risk_tolerance']
        )
        
        # Investment Goals
        investment_goals = st.multiselect(
            "Investment Goals",
            ["Wealth Growth", "Income Generation", "Capital Preservation", "Tax Efficiency", "Retirement Planning"],
            default=st.session_state.user_profile['investment_goals']
        )
        
        # Additional Information
        st.write("### Additional Information")
        monthly_investment = st.number_input("Monthly Investment Amount ($)", min_value=0, value=st.session_state.user_profile['monthly_investment'])
        existing_investments = st.number_input("Existing Investment Amount ($)", min_value=0, value=st.session_state.user_profile['existing_investments'])
        
        submitted = st.form_submit_button("Save Profile")
        if submitted:
            # Update session state
            st.session_state.user_profile.update({
                'age': age,
                'investment_horizon': investment_horizon,
                'risk_tolerance': risk_tolerance,
                'investment_goals': investment_goals,
                'monthly_investment': monthly_investment,
                'existing_investments': existing_investments
            })
            st.success("Profile saved successfully!")

def portfolio_form():
    """Create and handle the portfolio input form."""
    # Initialize portfolio in session state if not exists
    if 'portfolio' not in st.session_state:
        st.session_state.portfolio = {
            'stocks': 0,
            'bonds': 0,
            'crypto': 0,
            'real_estate': 0,
            'cash': 0,
            'other': 0
        }
    
    with st.form(key="portfolio_form"):
        st.write("### Portfolio Allocation")
        
        # Asset Allocation Inputs
        col1, col2 = st.columns(2)
        
        with col1:
            stocks = st.number_input("Stocks (%)", min_value=0, max_value=100, value=st.session_state.portfolio['stocks'])
            bonds = st.number_input("Bonds (%)", min_value=0, max_value=100, value=st.session_state.portfolio['bonds'])
            crypto = st.number_input("Cryptocurrency (%)", min_value=0, max_value=100, value=st.session_state.portfolio['crypto'])
        
        with col2:
            real_estate = st.number_input("Real Estate (%)", min_value=0, max_value=100, value=st.session_state.portfolio['real_estate'])
            cash = st.number_input("Cash (%)", min_value=0, max_value=100, value=st.session_state.portfolio['cash'])
            other = st.number_input("Other (%)", min_value=0, max_value=100, value=st.session_state.portfolio['other'])
        
        # Calculate total allocation
        total_allocation = stocks + bonds + crypto + real_estate + cash + other
        
        # Display total allocation
        st.write(f"Total Allocation: {total_allocation}%")
        
        if total_allocation != 100:
            st.warning("Total allocation must equal 100%")
        
        submitted = st.form_submit_button("Save Portfolio")
        if submitted and total_allocation == 100:
            # Update session state
            st.session_state.portfolio.update({
                'stocks': stocks,
                'bonds': bonds,
                'crypto': crypto,
                'real_estate': real_estate,
                'cash': cash,
                'other': other
            })
            st.success("Portfolio saved successfully!")
        elif submitted:
            st.error("Please ensure total allocation equals 100%")
