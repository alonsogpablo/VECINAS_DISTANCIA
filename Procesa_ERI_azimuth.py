__author__ = 'palonso0'
import pandas as pd
import json
from collections import defaultdict


cell = pd.read_csv('C:\\Desarrollo_Pablo\\Estad\\MV_MAPDBA_CELL_AZIMUTH.csv',sep=';',decimal='.')

cell_azimuth_eri3g = open("C:\\Desarrollo_Pablo\\Estad\\azimuth_eri3g.json","w")


celda=cell['CELL_NAME'].tolist()
azimuth=cell['AZIMUTH'].tolist()

data_dict = defaultdict(list)
for a in range(len(celda)):
    data_dict[celda[a]].append(azimuth[a])




json.dump(data_dict,cell_azimuth_eri3g, indent=4)


cell_azimuth_eri3g.close()
