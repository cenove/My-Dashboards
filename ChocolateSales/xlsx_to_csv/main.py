import pandas as pd
from sqlalchemy import create_engine
import urllib
import urllib.parse
import os

pasta = os.path.join('.', 'files')

def df_cleaner(df):
        df['purchase_date'] = pd.to_datetime(df['purchase_date'], format='mixed', errors='coerce')
        return df

# If you are going to test the pipeline, dont forget to change the parameters
def to_sql_loader(df, table_name):
    params = urllib.parse.quote_plus(
    'DRIVER={Usually is ODBC Driver 17 for SQL Server};'
    'SERVER=server_name;'
    'DATABASE=database_name;'
    'Trusted_Connection=yes;'
    'TrustServerCertificate=yes;'
)
    engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")
    df.to_sql(table_name, con=engine, if_exists='append', index=False)
    return df

def main():
    for nome_arquivo in os.listdir(pasta):
        if nome_arquivo.endswith('.xlsx'):
            file_path = os.path.join(pasta, nome_arquivo)        
            all_sheets = pd.read_excel(file_path, sheet_name=None)
            for sheet_name, nome_arquivo in all_sheets.items():
                pipeline = (
                    nome_arquivo.pipe(df_cleaner)
                    .pipe(to_sql_loader, sheet_name)
                )

if __name__ == "__main__":
    main()