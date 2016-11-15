__author__ = 'palonso0'

import pandas as pd
import json
import csv
from geopy.distance import vincenty
import operator
from Compass_Bearing import calculate_initial_compass_bearing

def vecina_minima_distancia(x):
    cell_vecinas_eri3g = open("C:\\Desarrollo_Pablo\\Estad\\vecinas_eri3g.json", "r")
    cell_vecinas_eri3g_dict = json.load(cell_vecinas_eri3g)
    cell_azimuth_eri3g = open("C:\\Desarrollo_Pablo\\Estad\\azimuth_eri3g.json", "r")
    cell_azimuth_eri3g_dict = json.load(cell_azimuth_eri3g)
    cell_lat_file = open("C:\\Desarrollo_Pablo\\Estad\\cell_lat.json","r")
    cell_lat_dict = json.load(cell_lat_file)
    cell_lon_file = open("C:\\Desarrollo_Pablo\\Estad\\cell_lon.json","r")
    cell_lon_dict = json.load(cell_lon_file)
    azimuth_celda_origen=cell_azimuth_eri3g_dict[x][0]
    distancia_vecina={}
    lat_origen=float(cell_lat_dict[x])
    lon_origen=cell_lon_dict[x]
    coord_origen=(lat_origen,lon_origen)
    for celda in cell_vecinas_eri3g_dict[x]:
        coord_destino=(float(cell_lat_dict[celda]),cell_lon_dict[celda])
        bearing=calculate_initial_compass_bearing(coord_origen,coord_destino)
        if vincenty(coord_origen,coord_destino).kilometers >0 and abs(azimuth_celda_origen-bearing)<30:
            distancia_vecina[celda]=vincenty(coord_origen,coord_destino).kilometers

    celda_final=min(distancia_vecina.iteritems(),key=operator.itemgetter(1))[0]
    coord_destino_final=(float(cell_lat_dict[celda_final]),cell_lon_dict[celda_final])

    return min(distancia_vecina.iteritems(),key=operator.itemgetter(1))[0], min(distancia_vecina.iteritems(),key=operator.itemgetter(1))[1],calculate_initial_compass_bearing(coord_origen,coord_destino_final),azimuth_celda_origen




celdas_largo_alcance_file=pd.read_csv("C:\\Desarrollo_Pablo\\Estad\\LARGO_ALCANCE_ERI.csv",sep=',',decimal='.')
celdas_largo_alcance_list=celdas_largo_alcance_file['celda'].tolist()
alcance_list=celdas_largo_alcance_file['3G_ERI_Alcance'].tolist()
minutos_list=celdas_largo_alcance_file['3G_Minutes_Voice'].tolist()

dict_alcance={}

csv_file=open('C:\\Desarrollo_Pablo\\Estad\\eri_largo_alcance_vecina.csv','wb')
csv_writer=csv.writer(csv_file,delimiter=',')
csv_writer.writerow(['CELDA','ALCANCE','MINUTOS','VECINA_CERCANA','DISTANCIA','BEARING','AZIMUTH_CELDA_ORIGEN'])
for a in range(len(celdas_largo_alcance_list)):
    try:

        csv_writer.writerow([celdas_largo_alcance_list[a]]+[alcance_list[a]]+[minutos_list[a]]+[vecina_minima_distancia(celdas_largo_alcance_list[a])[0]]+[vecina_minima_distancia(celdas_largo_alcance_list[a])[1]]+[vecina_minima_distancia(celdas_largo_alcance_list[a])[2]]+[vecina_minima_distancia(celdas_largo_alcance_list[a])[3]])

    except:pass

csv_file.close()




