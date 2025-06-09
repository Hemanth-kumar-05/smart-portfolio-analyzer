# src/analytics/risk_analyzer.py

def diversification_check(df):
    alerts = []
    for _, row in df.iterrows():
        if row['Percentage'] > 50:
            alerts.append(f"⚠️ Overconcentration in {row['Asset']} ({row['Percentage']:.1f}%)")
    return alerts
