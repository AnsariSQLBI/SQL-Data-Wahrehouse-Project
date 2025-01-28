from pathlib import Path
import pandas as pd

df = pd.read_csv('Datasets/source_crm/cust_info.csv')

df['cst_firstname'] = df['cst_firstname'].str.strip()
df['cst_lastname'] = df['cst_lastname'].str.strip()
df['cst_marital_status'] = df['cst_marital_status'].str.strip().str.upper().replace(
    {'S': 'Single', 'M': 'Married', 'NULL': 'n/a'})
df['cst_gndr'] = df['cst_gndr'].str.strip().str.upper().replace(
    {'M': 'Male', 'F': 'Female', 'NULL': 'n/a'})
print(df['cst_id'].value_counts())

filepath = Path('Datasets/source_crm/silver_cust_info.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(filepath)

