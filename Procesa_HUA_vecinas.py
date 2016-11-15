__author__ = 'palonso0'
import pandas as pd
import json
from collections import defaultdict


cell = pd.read_csv('C:\\Desarrollo_Pablo\\Estad\\H3G_UINTRAFREQNCELL.csv',sep=';',decimal='.')

cell_vecina_hua3g = open("C:\\Desarrollo_Pablo\\Estad\\vecinas_hua3g.json","w")


celda=cell['CELLNAME'].tolist()
vecina=cell['NEIGHBOUR3G'].tolist()

data_dict = defaultdict(list)
for a in range(len(celda)):
    data_dict[celda[a]].append(vecina[a])




json.dump(data_dict,cell_vecina_hua3g, indent=4)


cell_vecina_hua3g.close()
