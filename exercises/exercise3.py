import pandas as pd
import sqlite3


# Download the CSV file
url = "https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv"
cols_toUse = [0, 1, 2, 12, 22,  32, 42, 52, 62, 72] 
col_names = ['date', 'CIN', 'name', 'petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']

# Read the data
data = pd.read_csv(url, encoding="latin1", skiprows=7, skipfooter=4, engine="python", sep = ';', usecols= cols_toUse, header=None)
data.columns = col_names

# Validate the name and CIN column
data['date'] = data['date'].astype(str)
data['CIN'] = data['CIN'].astype(str).str.zfill(5)
data['name'] = data['name'].astype(str)

# Get all the numeric values 
data[['petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']]  = data[['petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']].apply(pd.to_numeric, errors='coerce')
data.dropna(axis=0,inplace=True)


# Write data to SQLite database
database_path = "cars.sqlite"
table_name = "cars"

with sqlite3.connect(database_path) as conn:
    data.to_sql(table_name, conn, if_exists="replace", index=False)
