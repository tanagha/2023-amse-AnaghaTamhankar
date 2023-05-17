# Project Plan

## Summary
<!-- Describe your data science project in max. 5 sentences. -->
To increase traffic efficiency and safety, this data science project will examine Cologne's traffic violations and light positions. We can pinpoint regions with a high number of violations and look into possible changes in traffic signal layout by merging reported fines data from the year 2021(past datasets are also available from 2015 but for now we are only using 2021) with the dataset of traffic lights in Cologne. Data integration, exploratory data analysis, and the creation of conclusions and suggestions are all parts of the project.

## Rationale
<!-- Outline the impact of the analysis, e.g. which pains it solves. -->
The following concerns are addressed in this analysis:
1. Determine high-traffic locations so that you can concentrate your enforcement efforts there and increase road safety.
2. To evaluate the effectiveness of traffic signal placement, look at the relationship between the occurrence of infractions and the presence of traffic lights.
3. Find potential locations for the installation of extra traffic lights to improve traffic flow and decrease infractions.
The project intends to deliver practical insights that may be utilized to make data-driven decisions for enhancing traffic management and safety in Cologne by merging the information and doing a thorough analysis.

## Datasources
<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource5645705113511462355: Ampelanlagen Koeln (Traffic lights in Cologne)
* Metadata URL: https://mobilithek.info/offers/-5645705113511462355
* Data URL: https://offenedaten-koeln.de/sites/default/files/2023_LSA_Koeln.csv
            https://offenedaten-koeln.de/sites/default/files/20181116_LSA_Ko%25CC%2588ln.csv
            https://offenedaten-koeln.de/sites/default/files/20131118_lsa_koordinaten_wgs84.csv
* Data Type: CSV

Short description:
Traffic lights (traffic lights) in Cologne (location, LSA number, building authority and district).

Additional information: These are the locations of traffic lights. The localization reflects the relevant crossing point of traffic flows, the location controlled by a control device of a traffic light system. The scope of control of an installation can cover a larger area up to 75 m away from this point.

The source of the data is the inventory of traffic signals at the Office for Traffic Management. The data is updated at the beginning of each year. 


### Datasource6868803491867755462: Bußgelddaten Koeln (Fine data Cologne)
* Metadata URL: https://mobilithek.info/offers/-6868803491867755462
* Data URL: https://offenedaten-koeln.de/sites/default/files/Bussgeld_2021.csv
* Data Type: CSV

Short description:
Recorded fines from 2021, including by date, street, vehicle type and offense.

## Work Packages
<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->
    [Issue #1] Obtain and preprocess the dataset on fines with the dataset of traffic lights in Cologne.
    [Issue #2] Handle inconsistent or missing data to ensure data quality and suitability for additional analysis.
    [Issue #3] Conduct descriptive statistics and visualizations.
    [Issue #4] Examine the connection between the frequency of crimes and the presence of traffic signals.
    [Issue #5] Find out where there are a lot of infractions happening, then evaluate how well the traffic lights that are already there are working there.
    [Issue #6] Make suggestions for concentrated enforcement measures, possible changes to traffic signal locations, and locations where more traffic lights could be useful.

[i1]: https://github.com/jvalue/2023-amse-template/issues/1