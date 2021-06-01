"""A Python Function meant for processing NetCDF arrays into a CSV format 
usable for training the correction models."""

import pandas as pd
from pandas import read_csv
import csv



def CSVWriter(Data = 'nothing'):
    counter = 0
    with open('CustomTable.csv', mode='w') as table:
        writer = csv.writer(table, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #Write Headers
        writer.writerow(["Lon","Lat","Time","ReforecastTemp","ReanalysisTemp","ModelError",
                         "Precipitation", "CloudCover", "Landuse",
                        "Water","Ice","Land","Shallow Water", "Desert"])
        MegaTable = pd.read_csv("MegaTable.csv")
        
        
        for time in range(0,407,30):
            counter = counter+1
            for lon in range(359):
                counter = counter+1
                for lat in range(179):
                    counter = counter+1
                    #Create all the CSV Variables
                    CSVReforecastLongitude = lon
                    CSVReforecastLatitude = lat
                    if Data != 'nothing':
                        CSVReforecastTemp = Data[time,lat+1,lon+1]
                        CSVReanalysisTemp = Data[time,lat+1,lon+1]
                        CSVModelError = CSVReanalysisTemp - CSVReforecastTemp
                    else: 
                        CSVReforecastTemp = 0
                        CSVReanalysisTemp = 0
                        CSVModelError = 0
                    if counter < 899650:
                        CSVPrecipitation = MegaTable['Precipitation'][counter]
                        CSVCloudCover = MegaTable['CloudCover'][counter]
                        CSVLanduseType = MegaTable['Landuse'][counter]
                    #OneHotEncoder part:
                    Water = 0
                    Ice = 0
                    Land = 0
                    ShallowWater = 0
                    Desert = 0
                    if CSVLanduseType == 1:
                        Water = 1
                    if CSVLanduseType == 7:
                        Ice = 1
                    if CSVLanduseType == 13:
                        Land = 1
                    if CSVLanduseType == 14:
                        ShallowWater = 1
                    if CSVLanduseType == 19:
                        Desert = 1
                    writer.writerow([CSVReforecastLongitude,CSVReforecastLatitude,time,CSVReforecastTemp,
                                     CSVReanalysisTemp,CSVModelError, CSVPrecipitation, CSVCloudCover, CSVLanduseType,
                                     Water, Ice, Land, ShallowWater, Desert])
