# Project Plan

# Project Title
Impact of Weather & Climate condition on Average Daily Traffic Counts

## Summary

<!-- Describe your data science project in max. 5 sentences. -->
This Methods of Advanced Data Engineering project aims to analyze **the weather and climate conditions of Chicago and its Average Daily Traffic Counts** generated from several automatic counting stations throughout the city Average Daily Traffic(ADT) Counts of vehicles on city street passing through a given location on an average weekday for the city of Chicago. The project will use two open data sources: [DATA.GOV](https://catalog.data.gov/), which contains information on Average Daily Traffic Counts fot the city of Chicago, and [visualcrossing](https://www.visualcrossing.com/), which shares weather and climate data of Chicago for the year 2006. This comprehensive analysis will focus on identifying patterns and trends in Average Daily Traffic in Chicago throughout the year 2006 to assess the Daily Traffic condition in the city. Additionally, this analysis will examine the weather and climate data to find out if Chicago's weather and climate conditions are affecting the daily Traffic counts.

## Rationale

<!-- Outline the impact of the analysis, e.g. which pains it solves. -->
This comprehensive analysis of weather and climate conditions, along with Average Daily Traffic in Chicago, can have several significant impacts on the targeted audience, including:
1. **Emergency Travellers:** This analysis can help the emergency travellers make a proper decision about which are the strret of Chicago will be highly affected. Due to the urgency of there needs an informed decision can make a huge difference in there life. It can help them to avoid any kinds of critical conditions make an easy route plan according to there needs.
2. **Extreme Health Issues:** This analysis can help to spread an awareness of extreme health issues which are being caused due to extreme traffic. Trvellers and general people who needs to travel via any transport media if they are consumed to heavy traffic for a long period of time it can affect there health. So by raising awareness it can help a huge number of peoples.
3. **Heavy Air Pollution:** This analysis can provide a clear understanding how traffic is impacting our air. Air pollution has become a major issues in our current era. A huge portion of it's being contributed by the increasing traffics in our roads. By gaining a proper view and understanding we can raise a drastic awareness which can help us to deteriorate the air pollution.

Overall, the analysis can help alleviate the pains of uncertainty about the emergency travellers about there critical movement decisions, provide a extensive overview of average daily traffic effects a person health condition alongside raise awareness against heavy air pollution.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Average Daily Traffic Counts Data in Chicago
* Metadata URL: [https://catalog.data.gov/dataset/average-daily-traffic-counts/resource/fa81c305-4308-40ab-8f95-f7063fdcf769](https://catalog.data.gov/dataset/average-daily-traffic-counts/resource/fa81c305-4308-40ab-8f95-f7063fdcf769)
* Sample Data URL: [https://data.cityofchicago.org/api/views/pfsx-4n4m/rows.csv](https://data.cityofchicago.org/api/views/pfsx-4n4m/rows.csv)
* Data Type: CSV

This data source contains Chicago's Average Daily Traffic Counts for the year 2006. This data set contains Traffic Volume Count Location Address, Date of Count, Total Passing Vehicle Volume etc.

### Datasource2: Weather and Climate Data of Chicago, Year 2006
* Metadata URL: [https://www.visualcrossing.com/weather/weather-data-services](https://www.visualcrossing.com/weather/weather-data-services)
* Sample Data URL: [https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/retrievebulkdataset?&key=QRR4QHM7YBZYBLZ68WD8PRFTN&taskId=0fb86a43c6c0bb66baf69a2ce6911efd&zip=false](https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/retrievebulkdataset?&key=QRR4QHM7YBZYBLZ68WD8PRFTN&taskId=0fb86a43c6c0bb66baf69a2ce6911efd&zip=false)
* Data Type: CSV

This data source will provide weather and climate data in Chicago for the year 2006. This data set is generated from [visualcrossing](https://www.visualcrossing.com/). This data set includes datetime,tempmax, tempmin, humidity, snow, windspeeed, visibility, cloud cover etc.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Extract Data from Multiple Sources [#1][i1]
2. Implement Data Transformation Step in ETL Pipeline [#2][i2]
3. Implement Data Loading Step in ETL Data Pipeline [#3][i3]
4. Automated Tests for the Project [#4][i4]
5. Continuous Integration Pipeline for the Project [#5][i5]
6. Final Report and Presentation Submission [#6][i6]

[i1]: https://github.com/TSraj/FAU-made-template-SummerSem24/issues/1
[i2]: https://github.com/TSraj/FAU-made-template-SummerSem24/issues/2
[i3]: https://github.com/TSraj/FAU-made-template-SummerSem24/issues/3
[i4]: https://github.com/TSraj/FAU-made-template-SummerSem24/issues/4
[i5]: https://github.com/TSraj/FAU-made-template-SummerSem24/issues/5
[i6]: https://github.com/TSraj/FAU-made-template-SummerSem24/issues/6