from markdown2pdf import convert
import os

def generate_presentation_pdf():
    # Convert markdown to PDF
    convert('presentation.md', 'Smart_Portfolio_Analyzer_Presentation.pdf')
    print("PDF presentation has been generated successfully!")

if __name__ == "__main__":
    generate_presentation_pdf() 