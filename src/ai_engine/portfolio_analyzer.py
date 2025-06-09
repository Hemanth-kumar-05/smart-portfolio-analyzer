"""Portfolio analysis module using Google's Gemini API."""

import os
import json
from typing import Dict, Any, List
import google.generativeai as genai
from .prompts import PortfolioPrompts

class PortfolioAnalyzer:
    def __init__(self):
        """Initialize the PortfolioAnalyzer with Gemini API configuration."""
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        self.prompts = PortfolioPrompts()

    async def analyze_portfolio(self, 
                             profile: Dict[str, Any], 
                             portfolio: Dict[str, float]) -> Dict[str, Any]:
        """
        Perform comprehensive portfolio analysis.
        
        Args:
            profile: Dict containing user profile information
            portfolio: Dict containing asset allocations as percentages
            
        Returns:
            Dict containing analysis results and recommendations
        """
        try:
            # Get portfolio analysis
            analysis_prompt = self.prompts.get_analysis_prompt(profile, portfolio)
            analysis_response = await self._get_gemini_response(analysis_prompt)
            analysis_data = json.loads(analysis_response)

            # Validate portfolio total
            if not self._validate_portfolio(portfolio):
                raise ValueError("Portfolio allocations must sum to 100%")

            # Enrich analysis with risk assessment
            risk_prompt = self.prompts.get_risk_assessment_prompt(profile)
            risk_response = await self._get_gemini_response(risk_prompt)
            risk_data = json.loads(risk_response)

            # Combine and structure the response
            return {
                "risk_score": analysis_data["risk_score"],
                "risk_assessment": analysis_data["risk_assessment"],
                "diversification_analysis": analysis_data["diversification_analysis"],
                "goal_alignment": analysis_data["goal_alignment"],
                "current_allocation": portfolio,
                "recommended_allocation": analysis_data["suggested_allocation"],
                "recommendations": analysis_data["recommendations"],
                "summary": analysis_data["summary"],
                "risk_explanation": risk_data["explanation"],
                "timestamp": self._get_timestamp()
            }

        except Exception as e:
            return {
                "error": str(e),
                "status": "failed",
                "timestamp": self._get_timestamp()
            }

    async def get_rebalancing_suggestions(self, 
                                        current_allocation: Dict[str, float],
                                        risk_score: float,
                                        profile: Dict[str, Any]) -> Dict[str, Any]:
        """
        Get specific rebalancing suggestions for the portfolio.
        
        Args:
            current_allocation: Current portfolio allocation
            risk_score: Calculated risk score
            profile: User profile information
            
        Returns:
            Dict containing rebalancing suggestions and target allocation
        """
        try:
            prompt = self.prompts.get_rebalancing_prompt(
                current_allocation, 
                risk_score,
                profile
            )
            response = await self._get_gemini_response(prompt)
            return json.loads(response)
        except Exception as e:
            return {"error": str(e), "status": "failed"}

    async def _get_gemini_response(self, prompt: str) -> str:
        """Get response from Gemini API."""
        response = await self.model.generate_content_async(prompt)
        return response.text

    def _validate_portfolio(self, portfolio: Dict[str, float]) -> bool:
        """Validate that portfolio allocations sum to 100%."""
        return abs(sum(portfolio.values()) - 100.0) < 0.01

    def _get_timestamp(self) -> str:
        """Get current timestamp in ISO format."""
        from datetime import datetime
        return datetime.utcnow().isoformat()
