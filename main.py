__author__ = 'marsov'

import yaml
import ee
from ee import mapclient

# read auth config
config = open('conf.yaml', 'r')
eeAuthConfig = yaml.load(config)

SERVICE_ACCOUNT = eeAuthConfig['SERVICE_ACCOUNT']
KEY_FILE = eeAuthConfig['KEY_FILE']
EEAPI_URL = eeAuthConfig['EEAPI_URL']

ee.Initialize(ee.ServiceAccountCredentials(SERVICE_ACCOUNT, KEY_FILE), EEAPI_URL)

collection = ee.ImageCollection('L7_L1T')
collection.filterDate('2006-06-01', '2006=07-01')

countries = ee.FeatureCollection('ft:1tdSwUL7MVpOauSgRzqVTOwdfy17KDbw-1d9omPw')

#print collection.median().getInfo()

#map = ee.mapclient.MapClient()
#map.CenterMap(22.467041, 41.666757, 12)
#image = collection.median()

#map.addOverlay(mapclient.MakeOverlay(image.getMapId()))
