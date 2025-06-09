def generate_summary(portfolio_data):
    # Process the portfolio data to create a summary
    total_value = sum(asset['value'] for asset in portfolio_data)
    asset_summary = {asset['name']: asset['value'] for asset in portfolio_data}
    
    summary = {
        'total_value': total_value,
        'asset_summary': asset_summary
    }
    
    return summary

def generate_recommendations(summary):
    # Generate recommendations based on the summary
    recommendations = []
    
    if summary['total_value'] < 100000:
        recommendations.append("Consider increasing your investment to diversify your portfolio.")
    
    if len(summary['asset_summary']) < 5:
        recommendations.append("Try to include more asset classes for better diversification.")
    
    return recommendations

def create_analysis_summary(portfolio_data):
    summary = generate_summary(portfolio_data)
    recommendations = generate_recommendations(summary)
    
    return {
        'summary': summary,
        'recommendations': recommendations
    }