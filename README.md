# surfs_up
Module 9
Overview of the Analysis
Following a much-needed vacation to Hawaii, my theoretical self decided to start the process of opening a "Surf n' Shake" shop in Oahu which will provide customers with surfing gear and also ice cream. With some money in the bank to invest into this business idea, I contacted W. Avy - an investor willing to support the business plan. W. Avy requests an analysis of the weather in Oahu to ensure that this business would be sustainable despite fluctations in temperature and precipitation.

An in-depth analysis of the precipitation levels, min and max temperatures, and an average temperature in Oahu was completed initially. This information was made available on a web browser (using Flask). W. Avy now would like to gather more information about temperature trends for the months of June and December in Oahu.

Results
Determine the Summary Statistics for June
Utilizing a SQLite file with all of the weather data for Oahu and after setting up a session to allow for the querying of the database, a list of all of the temperatures in June (june_temps). Then converted into a Pandas DataFrame.  The summary statistics for June can be calculated and viewed using the describe() function.

On average, the temperature in June is around 74.9°F. The June temperatures do not tend to deviate far from the mean (standard deviation of 3.357417).

Also, to better visualize the distribution of all of the reported June temperatures a simple histogram was created.

It's clear from the histogram that most of the time the temperature is somewhere between 70-79°F (most notably 74-75°F which is consistent with the summary statistics). NOTE: "Frequency" in the y-axis represents the number of times a datapoint in a specific temperature range appears in the dataset.

Determine the Summary Statistics for December
The same process was repeated for the temperatures in the months of December in Oahu. A list of all of the temperatures in December (december_temps). Simialrly it is also converted into a Pandas DataFrame. The summary statistics for December can be calculated and viewed using the describe() function.

On average, the temperature in December is around 71.0°F. The December temperatures do not tend to deviate far from the mean (standard deviation of 3.745920). To better visualize the distribution of all of the reported December temperatures a simple histogram was created.

It's clear from this histogram that most of the time the temperature is somewhere between 70-75°F (most notably 70-71°F which is consistent with the summary statistics).

Summary
June Temperature Trends in Oahu
On average, the temperature in June is around 74.9°F. The June temperatures do not tend to deviate far from the mean (standard deviation of 3.357417).
Despite a large range of 65-85°F, the dataset shows that the upper quartile is between 75-77°F and the lower quartile is between 73-75°F meaning the temperature rarely gets as low as 65°F or as high as 85°F.
Most of the time the temperature is somewhere between 70-79°F (most notably 74-75°F as seen in the histogram above).
December Temperature Trends in Oahu
On average, the temperature in December is around 71.0°F. The December temperatures do not tend to deviate far from the mean (standard deviation of 3.745920).
Despite a large range of 69-83°F, the dataset shows that the upper quartile is between 71-74°F and the lower quartile is between 69-71°F meaning the temperature does tend to be closer to the lower range and rarely ever gets as hot as 83°F.
Most of the time the temperature is somewhere between 70-75°F.
Additional Queries
It would be worthwhile to view the precipitation data for these months to correlate how precipitation might affect customer traffic. The measurement table of the hawaii.sqlite file can be filtered for June precipitation data and December precipitation data.
In the previous analysis (from the Module) the weather station which collected the highest number of temperature observations (USC00519281) was filtered in the measurement table and used to plot a histogram of temperatures. The stations table in the hawaii.sqlite file has columns for latitude and longitude for each station. Using the latitude and longitude of Oahu (21.4389° N, 158.0001° W) the station with the most relevant temperature/precipitation data could be determined and the analysis could be redone for June and December of this data subset. This could potentially provide an even more accurate summary of the weather in Oahu.