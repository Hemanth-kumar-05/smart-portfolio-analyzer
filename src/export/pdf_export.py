from fpdf import FPDF

def create_pdf_report(analysis_summary, recommendations, output_path):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, 'Portfolio Analysis Report', ln=True, align='C')

    # Summary Section
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, 'Analysis Summary', ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, analysis_summary)

    # Recommendations Section
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, 'Recommendations', ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, recommendations)

    # Save the PDF to the specified path
    pdf.output(output_path)

def generate_pdf(analysis_summary, recommendations):
    output_path = "portfolio_analysis_report.pdf"
    create_pdf_report(analysis_summary, recommendations, output_path)
    return output_path

def export_to_pdf(data, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Portfolio Analysis Summary", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Total Value: {data['summary']['total_value']}", ln=True)
    
    pdf.cell(200, 10, txt="Asset Summary:", ln=True)
    for asset, value in data['summary']['asset_summary'].items():
        pdf.cell(200, 10, txt=f"{asset}: {value}", ln=True)
    
    pdf.cell(200, 10, txt="Recommendations:", ln=True)
    for recommendation in data['recommendations']:
        pdf.cell(200, 10, txt=recommendation, ln=True)
    
    pdf.output(filename)