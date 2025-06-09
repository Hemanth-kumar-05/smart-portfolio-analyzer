def generate_recommendations(analysis_summary):
    recommendations = []

    # Example logic for generating recommendations based on analysis summary
    if analysis_summary['risk_score'] > 7:
        recommendations.append("Consider reducing high-risk assets in your portfolio.")
    
    if analysis_summary['diversification'] < 0.5:
        recommendations.append("Increase diversification by adding more asset classes.")
    
    if analysis_summary['performance'] < benchmark_performance:
        recommendations.append("Review underperforming assets and consider reallocating funds.")

    return recommendations

def format_recommendations(recommendations):
    formatted_recommendations = "\n".join(f"- {rec}" for rec in recommendations)
    return formatted_recommendations

def get_recommendations_summary(analysis_summary):
    recommendations = generate_recommendations(analysis_summary)
    return format_recommendations(recommendations)