import pandas as pd

df = pd.read_parquet("SRO_Project/files/df.parquet.gzip")

def data_cleaner():
    df['CPF_Cliente'] = df['CPF_Cliente'].fillna("CPF Não informado")
    df['Valor_Premio_R$'] = df['Valor_Premio_R$'].replace()
    df.dropna(subset='ID_Apolice')

def dtype_changer():
    df['ID_Apolice'] = df['ID_Apolice'].astype('string')
    df['Ramo_Seguro'] = df['Ramo_Seguro'].astype('category')
    pd.to_datetime(df['Data_Inicio_Vigencia'], format="mixed", dayfirst=True)
    pd.to_datetime(df['Data_Fim_Vigencia'], format="mixed", dayfirst=True)
    df['CPF_Cliente'] = df['CPF_Cliente'].astype('string')
    df['Status_Regulador'] = df['Status_Regulador'].astype('category')

def column_rename():
    df.rename(columns={"ID_Apolice":"police_id","Ramo_Seguro":"insurance_type","Data_Inicio_Vigencia":"start_date",
                            "Data_Fim_Vigencia":"end_date","Valor_Premio_R$":"premium_account",
                            "Valor_Segurado_R$":"coverage_amount","CPF_Cliente":"client_cpf","Status_Regulador":"claim_status"}, inplace=True)
def missing_apolice_df():
    missing_apolices = df.loc[df['ID_Apolice'] == '',['Ramo_Seguro','CPF_Cliente','Data_Inicio_Vigencia',
                                                      'Data_Fim_Vigencia','Valor_Premio_R$',
                                                      'Valor_Segurado_R$','Status_Regulador']]
    missing_apolices.to_csv("missing_apolices.csv",index=False,encoding="utf-8")

dtype_changer()
data_cleaner()
column_rename()