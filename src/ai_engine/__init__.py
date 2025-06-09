"""
AI Engine module for Smart Portfolio Analyzer
Uses Google's Gemini API for portfolio analysis and recommendations
"""

from typing import Dict, Any
import os
import google.generativeai as genai
from .portfolio_analyzer import PortfolioAnalyzer
from .prompts import PortfolioPrompts

from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# Configure Gemini API
if 'GEMINI_API_KEY' in os.environ:
    genai.configure(api_key=os.environ['GEMINI_API_KEY'])
else:
    raise EnvironmentError("GEMINI_API_KEY not found in environment variables")

# Set default model configuration
DEFAULT_MODEL = genai.GenerativeModel('gemini-pro')
DEFAULT_GENERATION_CONFIG = {
    'temperature': 0.7,
    'top_p': 0.8,
    'top_k': 40,
    'max_output_tokens': 2048,
}

# Version info
__version__ = '0.1.0'
__author__ = 'Your Name'

# Export main classes
__all__ = ['PortfolioAnalyzer', 'PortfolioPrompts']