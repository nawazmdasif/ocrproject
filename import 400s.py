import camelot
import pandas as pd
# Define file paths
pdf_file_path = r"G:\Downloaded for linux\bangladesh bureau of statistics data, 2022 (1).pdf"
excel_file_path = r"C:\Users\Admin\Downloads\CV\4000s.xlsx"
# Extract tables using Camelot
tables = camelot.read_pdf(pdf_file_path, flavor='stream', pages="400")  # Handle complex layouts
# Process tables and export to Excel
for i, table in enumerate(tables):
    df = table.df  # Convert table to DataFrame
    # Export to Excel
    df.to_excel(excel_file_path, sheet_name=f"Sheet{i+1}", index=False)
print(f"Data successfully converted from {pdf_file_path}to {excel_file_path}")