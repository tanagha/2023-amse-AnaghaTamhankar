# import libraries
from urllib.request import urlretrieve
import pandas as pd
import os
import zipfile
import sqlite3

# Fetch the data
url = ' https://gtfs.rhoenenergie-bus.de/GTFS.zip'
filename = 'GTFS.zip'
urlretrieve(url, filename)

with zipfile.ZipFile("GTFS.zip") as zip:
    zip.extract("stops.txt")

# Read the data
col_type = { 'stop_id': int, 'stop_name': str, 'stop_lat': float, 'stop_lon': float, 'zone_id': int }
data = pd.read_csv('stops.txt', sep=',', header=0, encoding='UTF-8', dtype= col_type, usecols = col_type.keys())

# Filter and Validate data 
data = data[(data['zone_id'] == 2001) & (data['stop_lat'] >= -90) & (data['stop_lat'] <= 90) & (data['stop_lon'] >= -90) & (data['stop_lon'] <= 90)].dropna()

# Write data to SQLite database
database_path = "gtfs.sqlite"
table_name = "stops"

with sqlite3.connect(database_path) as conn:
    data.to_sql(table_name, conn, if_exists="replace", index=False)

# Remove the downloaded files
os.remove('GTFS.zip')
os.remove('stops.txt')