# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hNuFT5BvNhZA6-FmmDZcT-l1rGKKwI-7
"""

!pip install geemap

"""To install the google earth engine maps , use the extension PIP

installing all the plugins of geemaps
"""

pip install geemap[all]

pip install geemap[lidar]

"""Lidar is a 3d data. to visualise lidar data on top of the gee interactive map"""

pip install geemap[raster]

pip install geemap[sql]

pip install geemap[streamlit]

"""to publish our results as interactive webmap we need streamlit https://streamlit.io/"""

pip install geemap[vector]

import geemap.geemap as map

"""importing the library and naming as map"""

import ee

ee.Authenticate()

ee.Initialize(project = 'ee-dnyandagawathe24')

m = map.Map()
m

m

"""installation
authentication
initiation
webmap
vector data visualisation
"""

India = ee.FeatureCollection('projects/ee-dnyandagawathe24/assets/India_state')
m.addLayer(India,{},'India')
m

"""for raster its imagecollections for vector its feature (where only one attribute is there) featurecollections"""

Kerala = India.filter(ee.Filter.eq('STATE','KERALA'))
m.addLayer(Kerala,{},'Kerala')
m

Kerala_District = ee.FeatureCollection('projects/ee-dnyandagawathe24/assets/Indian_district')
m.addLayer(Kerala_District,{},'Kerala_District')
m

Thiruvananthapuram = Kerala_District.filter(ee.Filter.eq('District','THIRUVANANTHAPURAM'))
m.addLayer(Thiruvananthapuram,{},'Thiruvananthapuram')
m

NDVI = ee.ImageCollection("LANDSAT/COMPOSITES/C02/T1_L2_8DAY_NDVI").select('NDVI').filterDate('2024-1-1','2024-12-15')
Kerala_ndvi = NDVI.mean().clip(Kerala)
NDVI_CC = {'min': 0,'max': 0.9, 'palette': ['ffffff', 'ce7e45', 'df923d', 'f1b555', 'fcd163', '99b718', '74a901','66a000', '529400', '3e8601', '207401', '056201', '004c00', '023b01','012e01', '011d01', '011301']}
m.addLayer(Kerala_ndvi, NDVI_CC, 'NDVI')
m

FCC = ee.ImageCollection("LANDSAT/LC09/C02/T1_L2").select('SR_B2', 'SR_B4', 'SR_B3').filterDate('2024-01-01','2024-12-15')
Kerala_FCC = FCC.mean().clip(Kerala)
m.addLayer(Kerala_FCC,{},'FCC')
m

FCC_sen = ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED").select('B2', 'B8', 'B4', 'B3').filterDate('2024-03-03','2024-06-15')
Kerala_FCCsen = FCC_sen.mean().clip(Kerala)
m.addLayer(Kerala_FCCsen,{},'FCC_sen')
m

export_task = ee.batch.Export.image.toDrive(
    image=Kerala_FCCsen,
    description='Kerala_FCCsen',
    folder='EarthEngine',
    fileNamePrefix='Kerala_FCC_sen',
    region=Kerala.geometry().bounds().getInfo()['coordinates'],
    scale=30,  # Adjust the scale as needed
    maxPixels=1e13
)
export_task.start()

FCC_lan = ee.ImageCollection("LANDSAT/LC09/C02/T1_L2").select('SR_B3', 'SR_B4', 'SR_B5', 'SR_B6').filterDate('2024-03-03','2024-06-15')
Kerala_FCClan = FCC_lan.mean().clip(Kerala)
m.addLayer(Kerala_FCClan,{},'FCC_lan')
m

export_task = ee.batch.Export.image.toDrive(
    image=Kerala_FCClan,
    description='Kerala_FCClan',
    folder='EarthEngine',
    fileNamePrefix='Kerala_FCC_lan',
    region=Kerala.geometry().bounds().getInfo()['coordinates'],
    scale=30,  # Adjust the scale as needed
    maxPixels=1e13
)
export_task.start()

Kerala_dem = ee.Image("NASA/NASADEM_HGT/001").select('elevation').clip(Kerala)
m.addLayer(Kerala_dem,{},'Kerala_dem')
m

export_task = ee.batch.Export.image.toDrive(
    image=Kerala_dem,
    description='Kerala_dem',
    folder='EarthEngine',
    fileNamePrefix='Kerala_dem',
    region=Kerala.geometry().bounds().getInfo()['coordinates'],
    scale=30,  # Adjust the scale as needed
    maxPixels=1e13
)
export_task.start()

import geemap,geemap as import_map

import ee

ee.Authenticate()

ee.Initialize(project='ee-dnyandagawathe24')

vis_map=import_map.Map()

Guwahati = ee.FeatureCollection('projects/ee-dnyandagawathe24/assets/GUWAHATI')
m.addLayer(Guwahati,{},'Guwahati')
m

FCC_sent14 = ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED").select('B2', 'B8', 'B4', 'B3').filterDate('2014-03-03','2024-06-15')
Guwahati_sent_FCC = FCC_sent14.mean().clip(Guwahati)
m.addLayer(Guwahati_sent_FCC,{},'FCC_sent14')
m

TCC_sent16 = ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED").select('B2', 'B8', 'B4', 'B3').filterDate('2016-03-03','2024-06-15')
Guwahati_sent_TCC = TCC_sent16.mean().clip(Guwahati)
m.addLayer(Guwahati_sent_TCC,{},'TCC_sent16')
m

vector_layer = ee.FeatureCollection("projects/ee-dnyandagawathe24/assets/streams")

Map = geemap.Map()

Map.addLayer(vector_layer, {}, 'bulidings')

VectorLayer = ee.Image("streams").clip(Guwahati)
m.addLayer(vector_layer, {}, 'Guwahati_streams')
m

FCC_lan9 = ee.ImageCollection("LANDSAT/LC09/C02/T1_L2").select('SR_B3', 'SR_B4', 'SR_B5', 'SR_B6').filterDate('2016-03-03','2024-06-15')
Guwahati_FCClan9 = FCC_lan.mean().clip(Guwahati)
m.addLayer(Guwahati_FCClan9,{},'FCC_lan9')
m