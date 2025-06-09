import streamlit as st

def user_profile_form():
    with st.form("profile_form"):
        age = st.number_input("Age", min_value=18, max_value=100, value=30)
        risk_tolerance = st.selectbox(
            "Risk Tolerance",
            ["Conservative", "Balanced", "Aggressive"]
        )
        investment_goal = st.selectbox("Investment Goal", ["Wealth Growth", "Income", "Preservation"])
        submitted_profile = st.form_submit_button("Save Profile")
        if submitted_profile:
            st.session_state['profile'] = {
                "age": age,
                "risk_tolerance": risk_tolerance,
                "investment_goal": investment_goal
            }
            st.success("Profile saved!")

def portfolio_form():
    st.write("Enter your total portfolio value and the amount for each asset class.")
    with st.form("portfolio_form"):
        total_value = st.number_input("Total Portfolio Value", min_value=0.0, value=None, step=1000.0, format="%.2f", placeholder="Enter total value")
        stocks_value = st.number_input("Stocks Amount", min_value=0.0, value=None, step=100.0, format="%.2f", placeholder="Enter amount")
        bonds_value = st.number_input("Bonds Amount", min_value=0.0, value=None, step=100.0, format="%.2f", placeholder="Enter amount")
        mutual_funds_value = st.number_input("Mutual Funds Amount", min_value=0.0, value=None, step=100.0, format="%.2f", placeholder="Enter amount")
        crypto_value = st.number_input("Crypto Amount", min_value=0.0, value=None, step=100.0, format="%.2f", placeholder="Enter amount")
        gold_value = st.number_input("Gold Amount", min_value=0.0, value=None, step=100.0, format="%.2f", placeholder="Enter amount")
        submitted_portfolio = st.form_submit_button("Save Portfolio")
        
        asset_values = {
            "Stocks": stocks_value,
            "Bonds": bonds_value,
            "Mutual Funds": mutual_funds_value,
            "Crypto": crypto_value,
            "Gold": gold_value
        }
        clean_asset_values = {k: (v if v is not None else 0.0) for k, v in asset_values.items()}
        sum_assets = sum(clean_asset_values.values())
        if total_value and total_value > 0:
            st.write("### Calculated Percentages")
            for asset, value in clean_asset_values.items():
                percent = (value / total_value) * 100 if total_value else 0
                st.write(f"{asset}: {percent:.2f}%")
        if submitted_portfolio:
            if abs(sum_assets - (total_value if total_value else 0.0)) > 1e-2:
                st.error(f"Sum of asset values ({sum_assets}) does not match total portfolio value ({total_value}).")
            else:
                allocations = {asset: (value / total_value) * 100 if total_value else 0 for asset, value in clean_asset_values.items()}
                st.session_state['portfolio'] = allocations
                st.success("Portfolio saved!")