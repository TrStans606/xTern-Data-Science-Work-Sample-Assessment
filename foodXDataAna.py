#Import pandas to use dataframes
import pandas as pd
import geopandas as gpd
from geopy.geocoders import Nominatim
import matplotlib.pyplot as plt
#this creates a data frame from the given .csv
foodTrucks = pd.read_csv('foodTrucks.csv')

#this shows off the data frame
print(foodTrucks)

#this gives a mean of the ratings

print(foodTrucks['Rating'].mean())

#this will find all of the closed locations and drop them from the frame
#I write all of the spaces to drop in a list
#As dropping them in the loop changes the indexing
dropList =[]
for x in range(0,len(foodTrucks)):
    if foodTrucks.iloc[x,4] =='closed':
        dropList.append(x)
        print("check")

foodTrucks = foodTrucks.drop(dropList,axis=0)
#This will show the data frame with the dropped data
print(foodTrucks)

#Next is to get the cordinates of each adress via Nominatim
addresses = []
for x in range(0,len(foodTrucks)):
    addresses.append(foodTrucks.iloc[x,1])
locator = Nominatim(timeout=10, user_agent = "TrStans")
latitude =[]
longitude = []
for place in addresses:
    location = locator.geocode(place)
    latitude.append(location.latitude)
    longitude.append(location.longitude)
#Now its time to add those cordinates to a data frame
locations = pd.DataFrame(
    {"Address": addresses,
     "Latitude": latitude,
     "Longitude": longitude})
#the dataframe will be converted to a geo dataframe
geoLocations = gpd.GeoDataFrame(locations, 
                                geometry=gpd.points_from_xy(locations.Longitude, locations.Latitude))

indyShape = gpd.read_file('indy_shape_files/tl_2017_18_cousub.shp')

fig, ax = plt.subplots(figsize=(7,7))

#This generates a plot of each food truck on a map of Indy
indyShape.plot(ax=ax)

geoLocations.plot(ax=ax, color='red')
