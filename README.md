# xTern-Data-Science-Work-Sample-Assessment
## My Solution to the xTern Data Science Work Sample Assessment

## Assumptions
I am assuming everyone is going to get food on saturday 10/14/2023.

## Launages and packages used
Python 3.11
Pandas
OSMPythonTools
GeoPandas

## API Usage

I attempted to use the open street map overpass API in order to collect data on food trucks in Indianapolis. I am unfamilar with collecting data from APIs as I come from a biology research background so I had to teach myself this process during the WSA. I was able to collect the number of fast food restaurants and then the number of of fast food places which were also street vendors. According to the API there were no street vendors in Indianapolis which told me the OpenStreetMap data on food trucks in Indy was lacking. I wanted to use OpenStreetMap data as it was free and easily acessible and I could not get the GoogleMaps API or the AWS API to work.

The API data is contained in the program "foodXOpenMapApi.py". Which can simply be run like:
```
python3 foodXOpenMapApi.py
```

## Data anayalsis 

Since I was unable to get the API to work I wanted to show off my python data anayslsis skills so I premade a CSV of food trucks in Indy called "foodTrucks.csv" to read into pandas. Some basic anaylsis of the data shows that most of the food trucks serve either taco or Mexican cuisine, and two of the food trucks will be closed on 10/14/2023.

