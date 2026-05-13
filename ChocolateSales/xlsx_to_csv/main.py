import pandas as pd

file_path = r'C:\Users\Isdras\Documents\My Dashboards\ChocolateSales\Chocolate Sales.xlsx'
all_sheets = pd.read_excel(file_path, sheet_name=None)

for sheet_name, df in all_sheets.items():
    # Check if Date exists 
    if 'purchase_date' in df.columns:
        date_data = df['purchase_date']
        print(f"Found Date column in {sheet_name}")
        df['purchase_date'] = pd.to_datetime(df['purchase_date'])
    
    # Save the CSV as you were doing
    df.to_csv(f'{sheet_name}.csv', index=False)