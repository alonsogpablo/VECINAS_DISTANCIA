__author__ = 'palonso0'
import pandas as pd
import json
from collections import defaultdict


cell = pd.read_csv('C:\\Desarrollo_Pablo\\Estad\\E3G_UTRANRELATION.csv',sep=';',decimal='.')

cell_vecina_eri3g = open("C:\\Desarrollo_Pablo\\Estad\\vecinas_eri3g.json","w")


celda=cell['PRC6_UN_UTRANCELL'].tolist()
vecina=cell['PRC7_UN_UTRANRELATION'].tolist()

data_dict = defaultdict(list)
for a in range(len(celda)):
    data_dict[celda[a]].append(vecina[a])




json.dump(data_dict,cell_vecina_eri3g, indent=4)


cell_vecina_eri3g.close()
