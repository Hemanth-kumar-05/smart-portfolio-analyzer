from .summary import create_analysis_summary
from .recommendations import export_recommendations
from .pdf_export import generate_pdf_report
from .csv_export import export_to_csv

# Sample portfolio data
portfolio_data = [
    {'name': 'Tech Stocks', 'value': 50000},
    {'name': 'Bonds', 'value': 30000},
    {'name': 'Crypto', 'value': 20000},
]

# Run the analysis
result = create_analysis_summary(portfolio_data)

# Print the results
print("Summary:", result['summary'])
print("Recommendations:", result['recommendations'])

# Export to PDF
generate_pdf_report(result, "analysis_summary.pdf")
print("PDF export completed: analysis_summary.pdf")

# Export to CSV
export_to_csv(result, "analysis_summary.csv")
print("CSV export completed: analysis_summary.csv")

__all__ = [
    'create_analysis_summary',
    'export_recommendations',
    'generate_pdf_report',
    'export_to_csv'
]