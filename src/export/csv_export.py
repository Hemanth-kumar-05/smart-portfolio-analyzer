from pathlib import Path
import pandas as pd
import csv

def export_to_csv(data, filename='portfolio_analysis.csv'):
    """
    Exports the given data to a CSV file.

    Parameters:
    - data: A dictionary or DataFrame containing the analysis results.
    - filename: The name of the file to save the CSV as.
    """
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow(["Portfolio Analysis Summary"])
        writer.writerow(["Total Value", data['summary']['total_value']])
        
        writer.writerow(["Asset Summary"])
        for asset, value in data['summary']['asset_summary'].items():
            writer.writerow([asset, value])
        
        writer.writerow(["Recommendations"])
        for recommendation in data['recommendations']:
            writer.writerow([recommendation])