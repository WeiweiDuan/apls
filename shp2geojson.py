from osgeo import ogr
import geojson
import gdal
from gdalconst import *


def convert_to_image_coood(x,y,path): # convert geocoord to image coordinate
    dataset = gdal.Open( path, GA_ReadOnly )
    adfGeoTransform = dataset.GetGeoTransform()

    dfGeoX=float(x)
    dfGeoY =float(y)
    det = adfGeoTransform[1] * adfGeoTransform[5] - adfGeoTransform[2] *adfGeoTransform[4]

    X = ((dfGeoX - adfGeoTransform[0]) * adfGeoTransform[5] - (dfGeoY -
    adfGeoTransform[3]) * adfGeoTransform[2]) / det

    Y = ((dfGeoY - adfGeoTransform[3]) * adfGeoTransform[1] - (dfGeoX -
    adfGeoTransform[0]) * adfGeoTransform[4]) / det
    return [int(Y),int(X)]

# ds = ogr.Open('C:\Users\weiweiduan\Documents\Map_proj_data\CA\CA_Bray_100414_2001_24000_bag\\recognition_results\\bray_waterlines_2001_align_ijgis.shp')
# ds = ogr.Open('C:\Users\weiweiduan\Documents\Map_proj_data\CA\CA_Bray_100414_2001_24000_bag\data\Perfect_shp\CA_Bray_waterlines_2001_perfect_espg4267.shp')
# ds = ogr.Open('C:\Users\weiweiduan\Documents\Map_proj_data\CO\CO_Louisville_450543_1965_24000_bag\data\Perfect_shp\Louisville_railroads_perfect_1965_espg4267.shp')
ds = ogr.Open('C:\Users\weiweiduan\Documents\Map_proj_data\CO\CO_Louisville_450543_1965_24000_bag\data\\recognition_results\louisville_railroads_1965_ncut_align_ijgis.shp')
layer = ds.GetLayer(0)
f = layer.GetNextFeature()

geojosn = {"type": "FeatureCollection",\
"crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },\
"features": []}

count = 0
while f:
    geom = f.GetGeometryRef()
    if geom != None:
    # points = geom.GetPoints()
        points = geom.ExportToJson()
        points = eval(points)
        pointsList = points.values()[1]
        # print pointsList
        if len(pointsList) >= 2:
            coordinates = []
            for p in pointsList:
                if p == None:
                    print(p)
                # print [p[0], p[1], 0.0]
                coordinates.append([p[0], p[1], 0.0])
            geojosn["features"].append({'type':'Feature','properties':[],\
                                        'geometry':{'type':'LineString','coordinates':coordinates}})
    count += 1
    f = layer.GetNextFeature()
print count

with open('ca_bray_2001_railroads.geojson', 'w') as outfile:
    geojson.dump(geojosn, outfile)
