"""
Test module for the Portfolio Analyzer AI engine.
"""

import os
import asyncio
import pytest
from dotenv import load_dotenv
from src.ai_engine import PortfolioAnalyzer

# Load environment variables
load_dotenv()

# Test data
test_profile = {
    "age": 28,
    "risk_tolerance": "Moderate",
    "investment_goal": "Wealth Growth"
}

test_portfolio = {
    "Stocks": 40.0,
    "Bonds": 20.0,
    "Crypto": 20.0,
    "Gold": 20.0
}

@pytest.mark.asyncio
async def test_portfolio_analysis():
    """Test the main portfolio analysis functionality."""
    analyzer = PortfolioAnalyzer()
    result = await analyzer.analyze_portfolio(test_profile, test_portfolio)
    
    # Basic validation of response structure
    assert isinstance(result, dict), "Result should be a dictionary"
    assert "risk_score" in result, "Result should contain risk_score"
    assert "recommendations" in result, "Result should contain recommendations"
    assert "recommended_allocation" in result, "Result should contain recommended_allocation"
    
    # Validate risk score range
    assert 1 <= result["risk_score"] <= 100, "Risk score should be between 1 and 100"
    
    # Validate portfolio allocations
    assert isinstance(result["recommended_allocation"], dict), "Recommended allocation should be a dictionary"
    total_allocation = sum(result["recommended_allocation"].values())
    assert abs(total_allocation - 100.0) < 0.01, "Recommended allocations should sum to 100%"

@pytest.mark.asyncio
async def test_invalid_portfolio():
    """Test handling of invalid portfolio data."""
    analyzer = PortfolioAnalyzer()
    invalid_portfolio = {
        "Stocks": 50.0,
        "Bonds": 60.0  # Total > 100%
    }
    
    with pytest.raises(ValueError):
        await analyzer.analyze_portfolio(test_profile, invalid_portfolio)

@pytest.mark.asyncio
async def test_rebalancing_suggestions():
    """Test the portfolio rebalancing suggestions."""
    analyzer = PortfolioAnalyzer()
    result = await analyzer.get_rebalancing_suggestions(
        test_portfolio,
        risk_score=65,
        profile=test_profile
    )
    
    assert isinstance(result, dict), "Result should be a dictionary"
    assert "suggestions" in result, "Result should contain suggestions"
    assert "target_allocation" in result, "Result should contain target allocation"
    
    # Validate target allocation totals
    total_target = sum(result["target_allocation"].values())
    assert abs(total_target - 100.0) < 0.01, "Target allocations should sum to 100%"

if __name__ == "__main__":
    # For manual testing without pytest
    async def run_tests():
        await test_portfolio_analysis()
        await test_invalid_portfolio()
        await test_rebalancing_suggestions()
        print("All manual tests completed successfully!")

    asyncio.run(run_tests())
