import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

# Define the seasons
def categorize_season(month):
    if month in ['JUN', 'JUL', 'AUG']:
        return 'Summer'
    elif month in ['DEC', 'JAN', 'FEB']:
        return 'Winter'
    elif month in ['MAR', 'APR', 'MAY']:
        return 'Spring'
    else:
        return 'Fall'

# Load data from SQLite database
def load_data_from_sqlite(database_path, table_name):
    conn = sqlite3.connect(database_path)
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    conn.close()
    return df

# Plot: Temperature vs Traffic Volume
def plot_temperature_vs_traffic(merged_df):
    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=merged_df, x='avg_temp', y='traffic', hue='season', palette='coolwarm', s=100)
    plt.title('Average Temperature vs Traffic Volume')
    plt.xlabel('Average Temperature (°C)')
    plt.ylabel('Traffic Volume')
    plt.show()

# Plot: Average Snowfall vs Traffic Volume
def plot_snowfall_vs_traffic(merged_df):
    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=merged_df, x='snowfall', y='traffic', hue='season', palette='coolwarm', s=100)
    plt.title('Average Snowfall vs Traffic Volume')
    plt.xlabel('Average Snowfall (mm)')
    plt.ylabel('Traffic Volume')
    plt.show()

# Plot: Precipitation vs Traffic Volume
def plot_precipitation_vs_traffic(merged_df):
    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=merged_df, x='precipitation', y='traffic', hue='season', palette='coolwarm', s=100)
    plt.title('Precipitation vs Traffic Volume')
    plt.xlabel('Precipitation (mm)')
    plt.ylabel('Traffic Volume')
    plt.show()

# Plot: Wind Speed vs Traffic Volume
def plot_wind_speed_vs_traffic(merged_df):
    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=merged_df, x='wind_speed', y='traffic', hue='season', palette='coolwarm', s=100)
    plt.title('Wind Speed vs Traffic Volume')
    plt.xlabel('Wind Speed (km/h)')
    plt.ylabel('Traffic Volume')
    plt.show()

# Plot: Season vs Traffic Volume
def plot_season_vs_traffic(merged_df):
    season_traffic = merged_df.groupby('season')['traffic'].mean().reset_index()
    plt.figure(figsize=(12, 6))
    sns.barplot(data=season_traffic, x='season', y='traffic', palette='viridis')
    plt.title('Season vs Traffic Volume')
    plt.xlabel('Season')
    plt.ylabel('Average Traffic Volume')
    plt.show()

# Plot: Multiple Weather Factors vs Traffic Volume
def plot_multiple_factors_vs_traffic(merged_df):
    fig, axs = plt.subplots(2, 2, figsize=(14, 12))

    sns.scatterplot(data=merged_df, x='avg_temp', y='traffic', hue='season', palette='coolwarm', s=100, ax=axs[0, 0])
    axs[0, 0].set_title('Average Temperature vs Traffic Volume')
    axs[0, 0].set_xlabel('Average Temperature (°C)')
    axs[0, 0].set_ylabel('Traffic Volume')

    sns.scatterplot(data=merged_df, x='snowfall', y='traffic', hue='season', palette='coolwarm', s=100, ax=axs[0, 1])
    axs[0, 1].set_title('Average Snowfall vs Traffic Volume')
    axs[0, 1].set_xlabel('Average Snowfall (mm)')
    axs[0, 1].set_ylabel('Traffic Volume')

    sns.scatterplot(data=merged_df, x='precipitation', y='traffic', hue='season', palette='coolwarm', s=100, ax=axs[1, 0])
    axs[1, 0].set_title('Precipitation vs Traffic Volume')
    axs[1, 0].set_xlabel('Precipitation (mm)')
    axs[1, 0].set_ylabel('Traffic Volume')

    sns.scatterplot(data=merged_df, x='wind_speed', y='traffic', hue='season', palette='coolwarm', s=100, ax=axs[1, 1])
    axs[1, 1].set_title('Wind Speed vs Traffic Volume')
    axs[1, 1].set_xlabel('Wind Speed (km/h)')
    axs[1, 1].set_ylabel('Traffic Volume')

    plt.tight_layout()
    plt.show()

# Main function
def main():
    database_path = '../data/MADE.sqlite'
    traffic_df = load_data_from_sqlite(database_path, 'traffic_data')
    weather_df = load_data_from_sqlite(database_path, 'weather_data')

    # Merge dataframes on 'month' column
    merged_df = pd.merge(weather_df, traffic_df, on='month')

    # Add season column
    merged_df['season'] = merged_df['month'].apply(categorize_season)

    # Plot different graphs
    plot_temperature_vs_traffic(merged_df)
    plot_snowfall_vs_traffic(merged_df)
    plot_precipitation_vs_traffic(merged_df)
    plot_wind_speed_vs_traffic(merged_df)
    plot_season_vs_traffic(merged_df)
    plot_multiple_factors_vs_traffic(merged_df)

if __name__ == "__main__":
    main()
