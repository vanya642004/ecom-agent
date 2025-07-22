import sqlite3
import pandas as pd

def load(csv_path, table):
    df = pd.read_csv(csv_path)
    conn = sqlite3.connect('ecom.db')
    df.to_sql(table, conn, if_exists='replace', index=False)
    conn.close()

if __name__=='__main__':
    load('../data/eligibility.csv','eligibility')
    load('../data/ad_sales.csv','ad_sales')
    load('../data/total_sales.csv','total_sales')
    print("✅ Loaded into ecom.db")
