from summary import create_analysis_summary
from export.pdf_export import export_to_pdf
from export.csv_export import export_to_csv

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
export_to_pdf(result, "analysis_summary.pdf")
print("PDF export completed: analysis_summary.pdf")

# Export to CSV
export_to_csv(result, "analysis_summary.csv")
print("CSV export completed: analysis_summary.csv")