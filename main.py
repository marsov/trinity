__author__ = 'marsov'

import yaml
import datetime
import ee
from ee import mapclient

# read auth config
config = open('conf.yaml', 'r')
eeAuthConfig = yaml.load(config)

SERVICE_ACCOUNT = eeAuthConfig['SERVICE_ACCOUNT']
KEY_FILE = eeAuthConfig['KEY_FILE']
EEAPI_URL = eeAuthConfig['EEAPI_URL']

# auth
ee.Initialize(ee.ServiceAccountCredentials(SERVICE_ACCOUNT, KEY_FILE), EEAPI_URL)



countries = ee.FeatureCollection('ft:1tdSwUL7MVpOauSgRzqVTOwdfy17KDbw-1d9omPw')
macedonia = countries.filter(ee.Filter().eq('Country', 'Macedonia'))

#var fc = ee.FeatureCollection(3513341);
#fc = fc.filter(ee.Filter().eq("Country", "Mexico"));

# Create a Landsat 7 composite for Summer of 2002, bounded to Mexico.
collection = ee.ImageCollection("L7_L1T")

startDate = datetime.datetime(1999, 7, 1)
endDate = datetime.datetime(2000, 1, 30)
collection = collection.filterDate(startDate, endDate)
collection = collection.filterBounds(macedonia)

# Map the normalizedDifference algorithm over the collection, and
# display the median.
ndvi = collection.map_normalizedDifference(["40", "30"])
#addToMap(ndvi.median(), {min:-1, max:1}, "Median NDVI");

#collection = ee.ImageCollection('L7_L1T')
#collection.filterBounds(macedonia.geometry())
#collection.filterDate('1999-07-01', '2000-01-31')

image = ndvi.median()

#image = image1.clip(countries.geometry())

#print collection.median().getInfo()

map = ee.mapclient.MapClient()
map.CenterMap(22.467041, 41.666757, 8)
map.addOverlay(mapclient.MakeOverlay(image.getMapId()))
