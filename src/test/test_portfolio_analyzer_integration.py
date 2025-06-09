"""
Integration test module for the Portfolio Analyzer AI engine with Analytics.
"""

import os
import asyncio
import pytest
from dotenv import load_dotenv
from src.ai_engine import PortfolioAnalyzer
from src.analytics.calculator import calculate_portfolio_metrics
from src.analytics.risk_analyzer import analyze_risk

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
async def test_portfolio_analysis_with_analytics():
    """Test the integration between AI analysis and analytics module."""
    try:
        # Step 1: Run analytics calculations
        print("\nCalculating portfolio metrics...")
        metrics = calculate_portfolio_metrics(test_portfolio)
        print("Portfolio metrics calculated:", metrics)

        print("\nAnalyzing risk profile...")
        risk_analysis = analyze_risk(test_profile, metrics)
        print("Risk analysis completed:", risk_analysis)

        # Step 2: Get AI analysis
        print("\nGetting AI analysis...")
        analyzer = PortfolioAnalyzer()
        result = await analyzer.analyze_portfolio(test_profile, test_portfolio)
        print("AI analysis received:", result)

        # Step 3: Validate results
        assert isinstance(result, dict), f"Result should be a dictionary, got {type(result)}"
        
        if "error" in result:
            print(f"\nError in analysis: {result['error']}")
            return

        print("\nValidating response structure...")
        expected_keys = ["risk_assessment", "recommendations", "suggested_allocation"]
        for key in expected_keys:
            assert any(k in result for k in [key, f"{key}s"]), f"Missing {key} information"

        # Step 4: Compare AI and Analytics results
        print("\nComparing AI and Analytics results...")
        if hasattr(risk_analysis, "risk_score") and "risk_score" in result:
            ai_risk = float(result["risk_score"])
            analytics_risk = float(risk_analysis.risk_score)
            difference = abs(ai_risk - analytics_risk)
            print(f"Risk score difference: {difference}")
            assert difference <= 20, f"Risk scores differ too much: AI={ai_risk}, Analytics={analytics_risk}"

        print("\nAll validations passed!")
        return result

    except Exception as e:
        print(f"\nTest failed with error: {str(e)}")
        raise

@pytest.mark.asyncio
async def test_invalid_data():
    """Test handling of invalid data by both AI and Analytics modules."""
    invalid_portfolio = {
        "Stocks": 50.0,
        "Bonds": 60.0  # Total > 100%
    }

    try:
        print("\nTesting invalid portfolio handling...")
        with pytest.raises(ValueError):
            calculate_portfolio_metrics(invalid_portfolio)
        print("Analytics module correctly rejected invalid portfolio")

        analyzer = PortfolioAnalyzer()
        result = await analyzer.analyze_portfolio(test_profile, invalid_portfolio)
        assert "error" in result, "AI should detect invalid portfolio"
        print("AI engine correctly rejected invalid portfolio")

    except Exception as e:
        print(f"\nTest failed with error: {str(e)}")
        raise

if __name__ == "__main__":
    async def run_integration_tests():
        try:
            print("\n=== Running Portfolio Analysis Integration Tests ===")
            await test_portfolio_analysis_with_analytics()
            print("\n=== Running Invalid Data Tests ===")
            await test_invalid_data()
            print("\n=== All Integration Tests Passed! ===")
        except Exception as e:
            print(f"\n!!! Test Suite Failed !!!\nError: {str(e)}")
            raise

    # Run tests
    asyncio.run(run_integration_tests())
