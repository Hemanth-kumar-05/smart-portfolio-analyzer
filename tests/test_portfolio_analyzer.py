import unittest
from src.analytics.portfolio_analyzer import analyze_portfolio
from src.analytics.risk_analyzer import compute_risk_score, diversification_check

class TestPortfolioAnalyzer(unittest.TestCase):
    def setUp(self):
        # Sample portfolio data
        self.sample_portfolio = {
            'stocks': 40,
            'bonds': 30,
            'crypto': 10,
            'real_estate': 15,
            'cash': 5
        }
        
        # Sample user profile
        self.sample_user_profile = {
            'risk_tolerance': 'Moderate',
            'investment_horizon': 'Long Term (7+ years)',
            'existing_investments': 100000,
            'monthly_investment': 1000
        }

    def test_compute_risk_score(self):
        # Test risk score calculation
        risk_score = compute_risk_score(self.sample_portfolio, 'Moderate')
        self.assertIsInstance(risk_score, float)
        self.assertTrue(0 <= risk_score <= 1)

        # Test different risk tolerances
        conservative_score = compute_risk_score(self.sample_portfolio, 'Conservative')
        aggressive_score = compute_risk_score(self.sample_portfolio, 'Aggressive')
        self.assertLess(conservative_score, aggressive_score)

    def test_diversification_check(self):
        # Test diversification analysis
        diversification = diversification_check(self.sample_portfolio)
        
        # Check if all required keys are present
        required_keys = [
            'equity_allocation',
            'fixed_income_allocation',
            'alternative_allocation',
            'cash_allocation',
            'max_allocation',
            'concentrated_assets',
            'recommendations'
        ]
        for key in required_keys:
            self.assertIn(key, diversification)

        # Test allocations sum to 100%
        total_allocation = (
            diversification['equity_allocation'] +
            diversification['fixed_income_allocation'] +
            diversification['alternative_allocation'] +
            diversification['cash_allocation']
        )
        self.assertEqual(total_allocation, 100)

    def test_analyze_portfolio(self):
        # Test complete portfolio analysis
        analysis = analyze_portfolio(self.sample_portfolio, self.sample_user_profile)
        
        # Check if all required keys are present
        required_keys = [
            'risk_score',
            'diversification',
            'asset_values',
            'total_investment',
            'monthly_contribution',
            'risk_assessment',
            'horizon_assessment',
            'recommendations'
        ]
        for key in required_keys:
            self.assertIn(key, analysis)

        # Test asset values calculation
        self.assertEqual(
            analysis['asset_values']['stocks'],
            (self.sample_portfolio['stocks'] / 100) * self.sample_user_profile['existing_investments']
        )

    def test_edge_cases(self):
        # Test with empty portfolio
        empty_portfolio = {
            'stocks': 0,
            'bonds': 0,
            'crypto': 0,
            'real_estate': 0,
            'cash': 0
        }
        risk_score = compute_risk_score(empty_portfolio, 'Moderate')
        self.assertEqual(risk_score, 0)

        # Test with concentrated portfolio
        concentrated_portfolio = {
            'stocks': 90,
            'bonds': 5,
            'crypto': 0,
            'real_estate': 0,
            'cash': 5
        }
        diversification = diversification_check(concentrated_portfolio)
        self.assertIn('stocks', diversification['concentrated_assets'])

    def test_invalid_inputs(self):
        # Test with invalid risk tolerance
        risk_score = compute_risk_score(self.sample_portfolio, 'Invalid')
        self.assertIsInstance(risk_score, float)
        self.assertTrue(0 <= risk_score <= 1)

        # Test with missing asset class
        incomplete_portfolio = {
            'stocks': 50,
            'bonds': 50
        }
        risk_score = compute_risk_score(incomplete_portfolio, 'Moderate')
        self.assertIsInstance(risk_score, float)
        self.assertTrue(0 <= risk_score <= 1)

if __name__ == '__main__':
    unittest.main() 