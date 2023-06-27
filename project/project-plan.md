# Project Plan

## Summary
<!-- Describe your data science project in max. 5 sentences. -->
The relationship between the traffic lights and trafic volations can be understood by merging reported fines data from the year 2021(past datasets are also available from 2015 but for now we are only using first 3 months of 2021) with the dataset of traffic lights in Cologne.
## Rationale
<!-- Outline the impact of the analysis, e.g. which pains it solves. -->
To evaluate the effectiveness of traffic signal placement, look at the relationship between the occurrence of violations and the presence of traffic lights.
The project intends to deliver practical insights that may be utilized to make data-driven decisions for enhancing traffic management and safety in Cologne by merging the information and doing a thorough analysis.

## Datasources
<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource5645705113511462355: Ampelanlagen Koeln (Traffic lights in Cologne)
* Metadata URL: https://mobilithek.info/offers/-5645705113511462355
* Data URL: https://offenedaten-koeln.de/sites/default/files/2023_LSA_Koeln.csv
            https://offenedaten-koeln.de/sites/default/files/20181116_LSA_Ko%CC%88ln.csv
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
    [Issue #3] Merge both the datasets for further use. 
    [Issue #4] Perform exploratory data analysis on the final dataset.
    [Issue #5] Perform hypothesis testing.
    [Issue #6] Write report on the findings. 

[i1]: https://github.com/jvalue/2023-amse-template/issues/1