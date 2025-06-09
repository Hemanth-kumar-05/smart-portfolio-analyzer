# src/analytics/risk_analyzer.py

def compute_risk_score(portfolio, risk_tolerance):
    """
    Compute the risk score for a given portfolio and risk tolerance.
    
    Args:
        portfolio (dict): Dictionary containing asset allocations
        risk_tolerance (str): User's risk tolerance level
    
    Returns:
        float: Risk score between 0 and 1
    """
    # Define risk weights for different assets
    risk_weights = {
        'stocks': 0.7,
        'bonds': 0.3,
        'crypto': 0.9,
        'real_estate': 0.6,
        'cash': 0.1,
        'other': 0.5
    }
    
    # Calculate weighted risk score
    total_risk = sum(portfolio[asset] * risk_weights[asset] for asset in portfolio) / 100
    
    # Adjust based on risk tolerance
    risk_tolerance_multiplier = {
        'Very Conservative': 0.5,
        'Conservative': 0.7,
        'Moderate': 1.0,
        'Aggressive': 1.3,
        'Very Aggressive': 1.5
    }.get(risk_tolerance, 1.0)
    
    return min(max(total_risk * risk_tolerance_multiplier, 0), 1)

def diversification_check(portfolio):
    """
    Check portfolio diversification and return recommendations.
    
    Args:
        portfolio (dict): Dictionary containing asset allocations
    
    Returns:
        dict: Dictionary containing diversification metrics and recommendations
    """
    # Define asset classes
    equity_assets = ['stocks']
    fixed_income = ['bonds']
    alternative = ['crypto', 'real_estate']
    cash_equivalents = ['cash']
    
    # Calculate class allocations
    equity_allocation = sum(portfolio[asset] for asset in equity_assets)
    fixed_income_allocation = sum(portfolio[asset] for asset in fixed_income)
    alternative_allocation = sum(portfolio[asset] for asset in alternative)
    cash_allocation = sum(portfolio[asset] for asset in cash_equivalents)
    
    # Check for concentration
    max_allocation = max(portfolio.values())
    concentrated_assets = [asset for asset, allocation in portfolio.items() if allocation > 30]
    
    # Generate recommendations
    recommendations = []
    
    if max_allocation > 40:
        recommendations.append(f"High concentration in {', '.join(concentrated_assets)}. Consider diversifying.")
    
    if equity_allocation > 60:
        recommendations.append("High equity exposure. Consider increasing fixed income allocation.")
    
    if fixed_income_allocation > 50:
        recommendations.append("High fixed income exposure. Consider adding growth assets.")
    
    if alternative_allocation > 30:
        recommendations.append("High alternative investment exposure. Consider reducing for more traditional assets.")
    
    if cash_allocation > 20:
        recommendations.append("High cash allocation. Consider investing excess cash.")
    
    return {
        'equity_allocation': equity_allocation,
        'fixed_income_allocation': fixed_income_allocation,
        'alternative_allocation': alternative_allocation,
        'cash_allocation': cash_allocation,
        'max_allocation': max_allocation,
        'concentrated_assets': concentrated_assets,
        'recommendations': recommendations
    }
