from .risk_analyzer import compute_risk_score, diversification_check

def analyze_portfolio(portfolio, user_profile):
    """
    Analyze a portfolio and return comprehensive analysis.
    
    Args:
        portfolio (dict): Dictionary containing asset allocations
        user_profile (dict): Dictionary containing user profile information
    
    Returns:
        dict: Dictionary containing portfolio analysis results
    """
    # Compute risk score
    risk_score = compute_risk_score(portfolio, user_profile['risk_tolerance'])
    
    # Check diversification
    diversification = diversification_check(portfolio)
    
    # Calculate total investment value
    total_investment = user_profile['existing_investments']
    monthly_contribution = user_profile['monthly_investment']
    
    # Calculate asset values
    asset_values = {
        asset: (allocation / 100) * total_investment
        for asset, allocation in portfolio.items()
    }
    
    # Generate risk assessment
    risk_assessment = {
        'Very Conservative': 'Your portfolio is very conservative, suitable for capital preservation.',
        'Conservative': 'Your portfolio is conservative, focusing on stability and income.',
        'Moderate': 'Your portfolio is moderately balanced between growth and stability.',
        'Aggressive': 'Your portfolio is aggressive, focusing on growth potential.',
        'Very Aggressive': 'Your portfolio is very aggressive, maximizing growth potential.'
    }.get(user_profile['risk_tolerance'], 'Risk assessment not available.')
    
    # Generate investment horizon assessment
    horizon_assessment = {
        'Short Term (1-3 years)': 'Your investment horizon is short-term. Consider more liquid and stable investments.',
        'Medium Term (3-7 years)': 'Your investment horizon is medium-term. A balanced approach is appropriate.',
        'Long Term (7+ years)': 'Your investment horizon is long-term. You can consider more growth-oriented investments.'
    }.get(user_profile['investment_horizon'], 'Investment horizon assessment not available.')
    
    return {
        'risk_score': risk_score,
        'diversification': diversification,
        'asset_values': asset_values,
        'total_investment': total_investment,
        'monthly_contribution': monthly_contribution,
        'risk_assessment': risk_assessment,
        'horizon_assessment': horizon_assessment,
        'recommendations': diversification['recommendations']
    } 