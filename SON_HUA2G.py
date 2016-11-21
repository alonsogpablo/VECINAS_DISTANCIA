__author__ = 'palonso0'

import pandas as pd
import json
import csv
from collections import defaultdict
from geopy.distance import vincenty
import operator
from Compass_Bearing import calculate_initial_compass_bearing
import simplekml
import os

cell_lat_file = open("C:\\Desarrollo_Pablo\\Estad\\cell_lat.json", "r")
cell_lat_dict = json.load(cell_lat_file)
cell_lon_file = open("C:\\Desarrollo_Pablo\\Estad\\cell_lon.json", "r")
cell_lon_dict = json.load(cell_lon_file)




def genera_vecinas(celda_origen):
    lat_origen=float(cell_lat_dict[celda_origen])
    lon_origen=cell_lon_dict[celda_origen]
    coord_origen=(lat_origen,lon_origen)

    gsm_azimuth=pd.read_csv("C:\\Desarrollo_Pablo\\VECINAS\\CELDAS_GSM_NAVARRA.csv",sep=';',decimal='.')
    celdas_gsm=gsm_azimuth['CELL_NAME'].tolist()
    azimuth_celdas=gsm_azimuth['AZIMUTH'].tolist()


    vecinas_gsm=pd.read_csv("C:\\Desarrollo_Pablo\\VECINAS\\VECINAS_GSM_NAVARRA.csv",sep=';',decimal='.')
    origen=vecinas_gsm['CELLNAME'].tolist()
    vecina=vecinas_gsm['2GNCELL'].tolist()

    dict_vecinas = defaultdict(list)
    for a in range(len(origen)):
        dict_vecinas[origen[a]].append(vecina[a])

    dict_azimuth_gsm={}
    for i in range(len(celdas_gsm)):
        dict_azimuth_gsm[celdas_gsm[i]]=azimuth_celdas[i]

#CALCULO DISTANCIA DE CELDA ORIGEN A TODA LA RED
    dict_distancia_marcacion_celdas={}

    kml=simplekml.Kml(open=1)
    f_candidatas = open('C:\\Desarrollo_Pablo\\VECINAS\\CANDIDATAS\\%scandidatas.csv' % celda_origen, 'wb')
    f_candidatas_writer = csv.writer(f_candidatas)
    f_candidatas_writer.writerow(['CANDIDATA', 'DISTANCIA', 'MARCACION', 'ARCO RESPECTO AZIMUTH ORIGEN'])

    for celda in celdas_gsm:

        try:
            coord_destino = (float(cell_lat_dict[celda]), cell_lon_dict[celda])
            dict_distancia_marcacion_celdas[celda]=[vincenty(coord_origen,coord_destino).kilometers,calculate_initial_compass_bearing(coord_origen,coord_destino),coord_destino]

        except:
            pass

    falta_vecinas=0
    faltan_cosite=0
    for celda in dict_distancia_marcacion_celdas:
        if (dict_distancia_marcacion_celdas[celda][0]<1 and abs((dict_distancia_marcacion_celdas[celda][1]-dict_azimuth_gsm[celda_origen]))<60 and celda not in dict_vecinas[celda_origen] and celda<>celda_origen):
            f_candidatas_writer.writerow([celda, dict_distancia_marcacion_celdas[celda][0],dict_distancia_marcacion_celdas[celda][1],dict_distancia_marcacion_celdas[celda][1]-dict_azimuth_gsm[celda_origen]])
            falta_vecinas=falta_vecinas+1
            try:
                pnt=kml.newpoint()
                pnt.name=celda
                pnt.coords=[(dict_distancia_marcacion_celdas[celda][2][1],dict_distancia_marcacion_celdas[celda][2][0])]
            except:pass
        if dict_distancia_marcacion_celdas[celda][0]==0:
            faltan_cosite=1
    print falta_vecinas
    f_candidatas.close()
    if falta_vecinas<=1:
        print 'No le faltan vecinas'
        os.remove('C:\\Desarrollo_Pablo\\VECINAS\\CANDIDATAS\\%scandidatas.csv' % celda_origen)
    else:
        kml.save('C:\\Desarrollo_Pablo\\VECINAS\\CANDIDATAS\\%svecinasgsm$s.kml'%(celda_origen, faltan_cosite))


celdas_gsm_provincia=pd.read_csv("C:\\Desarrollo_Pablo\\VECINAS\\CELDAS_GSM_NAVARRA.csv", sep=';',decimal='.')
celdas = celdas_gsm_provincia['CELL_NAME'].tolist()

for celda in celdas:
    genera_vecinas(celda)



