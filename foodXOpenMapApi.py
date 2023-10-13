#these are the key packages I am installing to generate and anaylze the data
#I am using OpenStreetMap as it is free and doesn't require card verification

from OSMPythonTools.nominatim import Nominatim
from OSMPythonTools.overpass import overpassQueryBuilder, Overpass


#areaIdGrabber takes a string city name as a parameter
#and outputs the OpenStreetMap areaID
#This is used to call more specific api information
def areaIdGrabber(cityName):
    nominatim = Nominatim()
    areaId = nominatim.query(cityName).areaId()
    return areaId

#api = Api()
#way = api.query('relation/1812962')

#print(way.tag('boundary'))

#I made the city varible easily accessible so it could be eaisly changed
city = 'Indianapolis, Indiana'

areaId = areaIdGrabber(city)
print(areaId)
overpass = Overpass()
#this will print out the number of food trucks in indianpolis 
#food trucks should be catagorized as fasst food and street vendor
#OpenStreetMaps does not seem to detect any food trucks
#OpenStreetMaps is built on fixed loactions
#So normally food trucks aren't recorded unless they have a set location and days
query = overpassQueryBuilder(area=areaId, elementType='node', 
                             selector=['"amenity"="fast_food"',
                                       '"street_vendor"="yes"'], 
                             out='count')
result = overpass.query(query)
print(result.countElements())
#this prints just the number of fast food vendors
query = overpassQueryBuilder(area=areaId, elementType='node', 
                             selector='"amenity"="fast_food"', 
                             out='count')
result = overpass.query(query)
print(result.countElements())

