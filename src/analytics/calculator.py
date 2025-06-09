# src/analytics/calculator.py

import pandas as pd

# Risk mapping per asset type
risk_map = {
    'Stocks': 0.7,
    'Bonds': 0.3,
    'Crypto': 0.9,
    'Gold': 0.4,
    'Mutual Funds': 0.5
}

def compute_allocation(assets, allocations):
    total = sum(allocations)
    df = pd.DataFrame({'Asset': assets, 'Allocation': allocations})
    df['Percentage'] = df['Allocation'] / total * 100
    return df

def compute_risk_score(df):
    df['RiskWeight'] = df['Asset'].map(risk_map).fillna(0.5)
    portfolio_risk_score = (df['RiskWeight'] * df['Percentage']).sum() / 100
    if portfolio_risk_score < 0.4:
        label = "Low Risk"
    elif portfolio_risk_score < 0.7:
        label = "Moderate Risk"
    else:
        label = "High Risk"
    return round(portfolio_risk_score, 2), label
