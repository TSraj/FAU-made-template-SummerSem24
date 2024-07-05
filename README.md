# Exercise Badges

![](https://byob.yarr.is/TSraj/FAU-made-template-SummerSem24/score_ex1) ![](https://byob.yarr.is/TSraj/FAU-made-template-SummerSem24/score_ex2) ![](https://byob.yarr.is/TSraj/FAU-made-template-SummerSem24/score_ex3) ![](https://byob.yarr.is/TSraj/FAU-made-template-SummerSem24/score_ex4) ![](https://byob.yarr.is/TSraj/FAU-made-template-SummerSem24/score_ex5)

# Methods of Advanced Data Engineering Project

# Impact of Weather and Climate Conditions on Average Daily Traffic Counts in Chicago (2006)

## Project Overview

This project investigates the major impact of weather and climate conditions on average daily traffic counts in the city of Chicago for the year 2006. The analysis aims to uncover how different weather parameters such as temperature, precipitation, snowfall, and wind speed influence traffic volume on a monthly basis. The findings can have significant implications for emergency travelers, public health, and environmental awareness.

<!-- # Impact-of-Weather-on-Traffic/
│
├── data/
│   ├── raw/
│   │   ├── traffic_data.csv
│   │   └── weather_data.csv
│   ├── processed/
│   │   ├── processed_traffic_data.csv
│   │   └── processed_weather_data.csv
│   └── database/
│       └── MADE.sqlite
│
├── notebooks/
│   ├── data_exploration.ipynb
│   ├── data_visualization.ipynb
│   └── final_analysis.ipynb
│
├── scripts/
│   ├── pipeline.py
│   └── visualizations.py
│
├── output/
│   ├── traffic_vs_weather.png
│   ├── correlation_matrix.png
│   ├── seasonal_analysis.png
│   └── scatter_plots.png
│
├── .gitignore
├── README.md
├── requirements.txt
└── LICENSE -->


## Table of Contents

- [Introduction](#introduction)
- [Data Source](#data-source)
- [Data Pipeline](#data-pipeline)
- [Analysis](#analysis)
- [Results](#results)
- [Conclusion](#conclusion)
- [Usage](#usage)
- [Contact](#contact)

## Introduction

The primary question addressed in this project is: What is the major impact of weather and climate conditions on average daily traffic counts?

Understanding this relationship is crucial for:
- **Emergency Travelers:** Helping them make informed decisions to avoid heavily impacted routes.
- **Public Health Awareness:** Highlighting the health risks associated with prolonged exposure to heavy traffic.
- **Environmental Impact:** Demonstrating the contribution of traffic to air pollution and raising awareness for necessary actions.

## Data Source

The data for this analysis was collected from two sources:
1. **Traffic Data:** City of Chicago traffic data for the year 2006, obtained from [data.cityofchicago.org](https://data.cityofchicago.org).
2. **Weather Data:** Weather data for Chicago in 2006, sourced from [Meteostat](https://bulk.meteostat.net).

The traffic data includes the total passing vehicle volume on a monthly basis, while the weather data includes monthly averages of temperature, precipitation, snowfall, and wind speed.

## Data Pipeline

The data pipeline involves the following steps:
1. **Retrieve Data:** Download traffic and weather data from their respective sources.
2. **Process Data:** Clean and preprocess the data to extract relevant information.
3. **Store Data:** Save the processed data into a SQLite database for easy access and analysis.
4. **Merge Data:** Combine the traffic and weather data into a single dataset for comprehensive analysis.

The detailed pipeline can be found in the `pipeline.py` file in this repository.

## Analysis

The analysis involves examining the relationship between traffic volume and weather conditions through various visualizations:
- **Traffic Counts Over Time:** Line graph showing monthly traffic counts.
- **Weather Conditions Over Time:** Line graphs for average temperature, precipitation, and snowfall.
- **Traffic vs. Weather Conditions:** Bar graphs showing the relationship between traffic counts and each weather variable.
- **Correlation Analysis:** Scatter plots with trend lines to show the correlation between traffic counts and individual weather variables.
- **Correlation Matrix:** Heatmap displaying the correlation coefficients between all pairs of variables.
- **Seasonal Analysis:** Violin plots showing traffic volume distribution across different seasons.

## Results

The results of the analysis provide insights into how weather conditions affect traffic volume. Key findings include:
- Significant decrease in traffic volume during months with high snowfall and precipitation.
- Strong correlation between average temperature and traffic volume, with higher traffic observed in warmer months.
- Seasonal patterns indicating higher traffic in summer months compared to winter months.

## Conclusion

The analysis concludes that weather and climate conditions have a substantial impact on average daily traffic counts in Chicago. Emergency travelers can benefit from this information to avoid critical routes, and public health awareness can be raised regarding the effects of heavy traffic. Additionally, understanding the impact of traffic on air pollution can drive efforts to mitigate environmental issues.

## Usage

To replicate this analysis, follow these steps:
1. Clone this repository: `git clone https://github.com/yourusername/impact-of-weather-on-traffic.git`
2. Navigate to the project directory: `cd impact-of-weather-on-traffic`
3. Install the required packages: `pip install -r requirements.txt`
4. Run the data pipeline: `python scripts/pipeline.py`
5. Generate the visualizations: `python scripts/visualizations.py`

The visualizations will be saved in the `output` directory.

## Contact

For any questions or feedback, please contact:
- **Name:** MD TANVER SADIK RAJ
- **Email:** [tanvirraj475@gmail.com](mailto:tanvirraj475@gmail.com)
- **GitHub:** [TSraj](https://github.com/TSraj)

## License

This project is licensed under the EPL-2.0 License.
