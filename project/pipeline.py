import pandas as pd
import sqlite3
import requests
import io
import gzip
from io import BytesIO
import os

def retrieve_data(url, compressed=False):
    print(f"Retrieving data from {url}...")
    response = requests.get(url)
    if compressed:
        print("Decompressing data...")
        return gzip.decompress(response.content)
    else:
        return response.content.decode('utf-8')

def store_in_sqlite(df, database_path, table_name):
    print(f"Storing data in {table_name} table in {database_path}...")
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    
    if table_name == 'traffic_data':
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY,
            month TEXT,
            traffic INTEGER
        );
        """)
    elif table_name == 'weather_data':
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY,
            month TEXT,
            avg_temp REAL,
            snowfall REAL,
            precipitation REAL,
            wind_speed REAL
        );
        """)
    
    for row in df.itertuples(index=False):
        if table_name == 'traffic_data':
            cursor.execute(f"""
            INSERT INTO {table_name} (month, traffic) VALUES (?, ?)
            """, (row.month, row.traffic))
        elif table_name == 'weather_data':
            cursor.execute(f"""
            INSERT INTO {table_name} (month, avg_temp, snowfall, precipitation, wind_speed) VALUES (?, ?, ?, ?, ?)
            """, (row.month, row.avg_temp, row.snowfall, row.precipitation, row.wind_speed))
    
    conn.commit()
    conn.close()

def process_traffic_data(data):
    print("Processing traffic data...")
    df = pd.read_csv(io.StringIO(data))
    
    df['Date of Count'] = pd.to_datetime(df['Date of Count'])
    df['month'] = df['Date of Count'].dt.strftime('%b').str.upper()
    
    monthly_totals = df.groupby('month')['Total Passing Vehicle Volume'].sum().reset_index()
    
    all_months_df = pd.DataFrame({
        'month': ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 
                  'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    })
    
    monthly_totals = all_months_df.merge(monthly_totals, on='month', how='left')
    monthly_totals['Total Passing Vehicle Volume'].fillna(0, inplace=True)
    monthly_totals.columns = ['month', 'traffic']
    
    return monthly_totals

def process_weather_data(data):
    print("Processing weather data...")
    selected_columns = [0, 3, 4, 5, 8]
    df = pd.read_csv(BytesIO(data), header=None, usecols=selected_columns)
    df.columns = ['date', 'avg_temp', 'snowfall', 'precipitation', 'wind_speed']
    df['date'] = pd.to_datetime(df['date'])
    df_2006 = df[df['date'].dt.year == 2006]
    df_2006 = df_2006.dropna()
    df_2006['month'] = df_2006['date'].dt.strftime('%b').str.upper()
    
    monthly_avg = df_2006.groupby('month').mean().reset_index()
    months_order = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    monthly_avg['month'] = pd.Categorical(monthly_avg['month'], categories=months_order, ordered=True)
    monthly_avg = monthly_avg.sort_values('month')
    monthly_avg = monthly_avg.drop(columns=['date'], errors='ignore')
    monthly_avg[['avg_temp', 'snowfall', 'precipitation', 'wind_speed']] = monthly_avg[['avg_temp', 'snowfall', 'precipitation', 'wind_speed']].round(2)
    
    return monthly_avg

def main():
    os.makedirs('../data', exist_ok=True)
    
    database_path = '../data/MADE.sqlite'
    
    traffic_url = "http://data.cityofchicago.org/api/views/pfsx-4n4m/rows.csv"
    traffic_data = retrieve_data(traffic_url)
    traffic_df = process_traffic_data(traffic_data)
    store_in_sqlite(traffic_df, database_path, 'traffic_data')
    print("Monthly traffic data for the year 2006 has been saved to the SQLite database.")
    
    weather_url = "https://bulk.meteostat.net/v2/hourly/72534.csv.gz"
    weather_data = retrieve_data(weather_url, compressed=True)
    weather_df = process_weather_data(weather_data)
    store_in_sqlite(weather_df, database_path, 'weather_data')
    print("Monthly averaged weather data for the year 2006 has been saved to the SQLite database.")
    
if __name__ == "__main__":
    main()
