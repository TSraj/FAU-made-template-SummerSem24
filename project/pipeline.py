# import libraries
import pandas as pd
import sqlite3
import requests
import io
import gzip
from io import BytesIO
import os

def fetch_data(url, compressed=False):
    print(f"Fetching data from {url}...")
    response = requests.get(url)
    if compressed:
        print("Decompressing data...")
        return gzip.decompress(response.content)
    else:
        return response.content.decode('utf-8')

def save_to_sqlite(df, db_path, table_name):
    print(f"Saving data to {table_name} table in {db_path}...")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create table without auto-incremented primary key
    if table_name == 'traffic':
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY,
            month TEXT,
            traffic INTEGER
        );
        """)
    elif table_name == 'weather':
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY,
            month TEXT,
            tavg REAL,
            snow REAL,
            prcp REAL,
            wspd REAL
        );
        """)
    
    # Insert data into table
    for row in df.itertuples(index=False):
        if table_name == 'traffic':
            cursor.execute(f"""
            INSERT INTO {table_name} (month, traffic) VALUES (?, ?)
            """, (row.month, row.traffic))
        elif table_name == 'weather':
            cursor.execute(f"""
            INSERT INTO {table_name} (month, tavg, snow, prcp, wspd) VALUES (?, ?, ?, ?, ?)
            """, (row.month, row.tavg, row.snow, row.prcp, row.wspd))
    
    conn.commit()
    conn.close()

# Transform Traffic Data
def transform_traffic_data(data):
    print("Transforming traffic data...")
    # Read the CSV data
    df = pd.read_csv(io.StringIO(data))
    
    # Ensure that the 'Date of Count' column is in datetime format
    df['Date of Count'] = pd.to_datetime(df['Date of Count'])
    
    # Extract month from the 'Date of Count' column
    df['month'] = df['Date of Count'].dt.strftime('%b').str.upper()
    
    # Group by month and sum the 'Total Passing Vehicle Volume'
    monthly_data = df.groupby('month')['Total Passing Vehicle Volume'].sum().reset_index()
    
    # Create a DataFrame with all months
    all_months = pd.DataFrame({
        'month': ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 
                  'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    })
    
    # Merge the grouped data with all months to ensure all months are present
    monthly_data = all_months.merge(monthly_data, on='month', how='left')
    
    # Fill NaN values with 0 (for months with no data)
    monthly_data['Total Passing Vehicle Volume'].fillna(0, inplace=True)
    
    # Rename columns to match the desired output
    monthly_data.columns = ['month', 'traffic']
    
    return monthly_data

# Transform Weather Data
def transform_weather_data(data):
    print("Transforming weather data...")
    selected_columns = [0, 3, 4, 5, 8]
    df = pd.read_csv(BytesIO(data), header=None, usecols=selected_columns)
    df.columns = ['date', 'tavg', 'snow', 'prcp', 'wspd']
    df['date'] = pd.to_datetime(df['date'])
    df_2006 = df[df['date'].dt.year == 2006]
    df_2006 = df_2006.dropna()
    df_2006['month'] = df_2006['date'].dt.strftime('%b')
    monthly_avg = df_2006.groupby('month').mean().reset_index()
    months_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    monthly_avg['month'] = pd.Categorical(monthly_avg['month'], categories=months_order, ordered=True)
    monthly_avg = monthly_avg.sort_values('month')
    monthly_avg = monthly_avg.drop(columns=['date'], errors='ignore')
    monthly_avg[['tavg', 'snow', 'prcp', 'wspd']] = monthly_avg[['tavg', 'snow', 'prcp', 'wspd']].round(2)
    return monthly_avg

def main():
    # Ensure the ../data directory exists
    os.makedirs('../data', exist_ok=True)
    
    db_path = '../data/MADE.sqlite'
    
    # Process Traffic data
    traffic_url = "http://data.cityofchicago.org/api/views/pfsx-4n4m/rows.csv"
    traffic_data = fetch_data(traffic_url)
    traffic_df = transform_traffic_data(traffic_data)
    save_to_sqlite(traffic_df, db_path, 'traffic')
    print("Monthly traffic data for the year 2006 has been saved to SQLite database.")
    
    # Process weather data
    weather_url = "https://bulk.meteostat.net/v2/hourly/72534.csv.gz"
    weather_data = fetch_data(weather_url, compressed=True)
    weather_df = transform_weather_data(weather_data)
    save_to_sqlite(weather_df, db_path, 'weather')
    print("Monthly averaged data for the year 2006 has been saved to SQLite database.")

if __name__ == "__main__":
    main()
