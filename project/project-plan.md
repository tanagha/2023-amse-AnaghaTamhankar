# Project Plan

## Summary
<!-- Describe your data science project in max. 5 sentences. -->
The dataset on bicycle streets in each district, together with other pertinent data, will be used in the project to examine the bicycle infrastructure in Cologne. The goal of the project is to shed light on the efficiency and use of bicycle infrastructure, point out potential areas for improvement, and comprehend the relationship between bicycle streets, motor vehicle traffic, and the predominance of bicycle traffic.

## Rationale
<!-- Outline the impact of the analysis, e.g. which pains it solves. -->
For the purpose of increasing eco-friendly transportation and enhancing the overall cycling experience, a review of the city of Cologne's bicycle infrastructure is important. The project can pinpoint regions where infrastructure improvements may be necessary by assessing the existing state of bicycle roadways in various districts and their impact on motor vehicle traffic and bicycle traffic preponderance. This analysis can aid in making well-informed choices for improving bicycle infrastructure, focusing investments, and promoting active transportation options by municipal planners, lawmakers, and transportation authorities.

## Datasources
<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource4167135070585053422: Cycle streets in Cologne
* Metadata URL: https://mobilithek.info/offers/-4167135070585053422
* Data URL: https://offenedaten-koeln.de/sites/default/files/Fahrradstra%25C3%259Fen_Koeln.csv
* Data Type: CSV

Short description:
Bicycle streets in Cologne by district.
Attributes:
- City district 
- Street from/to 
- Motor vehicle traffic permitted 
- Set up since 
- Bicycle traffic predominates 
- Other remarks 
- Length


### Datasource7728616938658132563: Traffic volume in the city of Cologne
* Metadata URL: https://mobilithek.info/offers/-7728616938658132563
* Data URL: https://offenedaten-koeln.de/dataset/resource/90e5fad9-fd9f-4e7d-8e3d-934eb7dc1d34
* Data Type: JSON

Short description:
The data in the traffic calendar gives you various options for getting an overview of the traffic situation in Cologne.
Here you can get information about how traffic works on Cologne's main streets.
[identifier] => ID Bsp.: ST035
[name] => name - eg: belt - A 57 - exit Ehrenfeld to Aachener Straße
[utilization] => utilization - example (0,1 or 2) 0 = free 1 = slow-moving 2 = traffic jam 16 = no display, probably due to defective sensors 32 = additional information in the link field (e.g. for major events)
[link] => link - e.g. link to further information
[geometryType] => esriGeometryPolyline [spatialReference] => stdClass Object
The update times are around 5 to 10 minutes.


## Work Packages
<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. [Issue #1]: Obtain and preprocess the dataset on bicycle streets in Cologne by district.
2. [Issue #2]: Gather traffic volume, traffic density, and traffic load data for the corresponding streets.
3. [Issue #3]: Conduct descriptive statistics and visualizations to understand the distribution of bicycle streets, motor vehicle traffic, and bicycle traffic predominance.
4. [Issue #4]: Perform correlation analysis between bicycle streets, motor vehicle traffic, and bicycle traffic predominance.
5. [Issue #5]: Identify districts or streets with high motor vehicle traffic but inadequate bicycle infrastructure.
6. [Issue #6]: Determine areas where bicycle traffic predominance can be improved through infrastructure enhancements.
7. [Issue #7]: Summarize the analysis results and key findings.
8. [Issue #8]: Provide recommendations for improving bicycle infrastructure in different districts.
9. [Issue #9]: Prepare a detailed report outlining the analysis methodology, results, and recommendations.

[i1]: https://github.com/jvalue/2023-amse-template/issues/1