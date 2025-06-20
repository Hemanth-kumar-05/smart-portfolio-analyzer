"""Module containing prompt templates for Gemini API interactions."""

from typing import Dict, Any

class PortfolioPrompts:
    @staticmethod
    def get_analysis_prompt(profile: Dict[str, Any], portfolio: Dict[str, float]) -> str:
        """
        Generate a structured prompt for portfolio analysis.
        
        Args:
            profile: User profile containing age, risk_tolerance, and investment_goal
            portfolio: Current portfolio allocation as percentages
            
        Returns:
            Formatted prompt string for Gemini API
        """
        allocations = '\n'.join([f'- {asset}: {percentage}%' for asset, percentage in portfolio.items()])
        return f"""You are an expert financial advisor analyzing an investment portfolio.

Client Profile:
- Age: {profile['age']} years old
- Risk Tolerance: {profile['risk_tolerance']}
- Investment Goal: {profile['investment_goal']}

Current Portfolio Allocation:
{allocations}

Provide a structured analysis in JSON format with the following sections:
{{
    "risk_score": "<number between 1-100>",
    "risk_assessment": "<brief evaluation of portfolio risk level>",
    "diversification_analysis": "<analysis of portfolio diversification>",
    "goal_alignment": "<how well portfolio matches client goals>",
    "recommendations": [
        "<list of specific rebalancing recommendations>"
    ],
    "suggested_allocation": {{
        "<asset_name>": "<percentage>"
    }},
    "summary": "<one-line summary of key findings>"
}}"""

    @staticmethod
    def get_risk_assessment_prompt(profile: Dict[str, Any]) -> str:
        """Generate a prompt for risk tolerance assessment."""
        return f"""Based on the following investor profile:
- Age: {profile['age']}
- Risk Tolerance: {profile['risk_tolerance']}
- Investment Goal: {profile['investment_goal']}

Provide a risk assessment score and explanation in JSON format:
{
    "base_risk_score": "<number between 1-100>",
    "explanation": "<brief explanation of the score>",
    "recommended_asset_mix": {
        "<asset_class>": "<percentage_range>"
    }
}"""

    @staticmethod
    def get_rebalancing_prompt(current_allocation: Dict[str, float], 
                             risk_score: float, 
                             profile: Dict[str, Any]) -> str:
        """Generate a prompt for portfolio rebalancing suggestions."""
        allocation_items = [f'{asset}: {percentage}%' for asset, percentage in current_allocation.items()]
        if not allocation_items:
            allocation_items = ["No assets in portfolio"]
        return f"""For an investor with:
- Risk Score: {risk_score}/100
- Age: {profile['age']}
- Goal: {profile['investment_goal']}

Current Portfolio:
{', '.join(allocation_items)}

Provide rebalancing recommendations in JSON format:
{
    "suggestions": [
        "<specific action to take>"
    ],
    "target_allocation": {
        "<asset_name>": "<target_percentage>"
    },
    "rationale": "<brief explanation of recommendations>"
}"""
