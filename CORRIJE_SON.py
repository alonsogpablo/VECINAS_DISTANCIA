__author__ = 'palonso0'
import pandas as pd
import json
from collections import defaultdict


cell = pd.read_csv('C:\\Users\\palonso0\\Downloads\\Enginparam_UMTS_20161114_171836_CYL70R01.csv',sep=',',decimal='.')
cell_oss = pd.read_csv('C:\\Users\\palonso0\\Downloads\\CYL70R01.csv',sep=';',decimal='.')

celda_son=cell['Cell Name'].tolist()
lac_son=cell['LAC'].tolist()
rnc_son=cell['RNC Name'].tolist()
sac_son=cell['SAC'].tolist()
rac_son=cell['RAC'].tolist()

celda_oss=cell_oss['Cell Name'].tolist()
lac_oss=cell_oss['LAC_OSS'].tolist()
rnc_oss=cell_oss['RNC_OSS'].tolist()
sac_oss=cell_oss['SAC_OSS'].tolist()
rac_oss=cell_oss['RAC_OSS'].tolist()



for celda in celda_oss:
    cell.set_value(cell.loc[cell['Cell Name'] == celda]['LAC'].index,'LAC',lac_oss[celda_oss.index(celda)])
    cell.set_value(cell.loc[cell['Cell Name'] == celda]['RNC Name'].index, 'RNC Name', rnc_oss[celda_oss.index(celda)])
    cell.set_value(cell.loc[cell['Cell Name'] == celda]['* RNC ID'].index, '* RNC ID', rnc_oss[celda_oss.index(celda)][-3:])
    cell.set_value(cell.loc[cell['Cell Name'] == celda]['SAC'].index, 'SAC', sac_oss[celda_oss.index(celda)])
    cell.set_value(cell.loc[cell['Cell Name'] == celda]['RAC'].index, 'RAC', rac_oss[celda_oss.index(celda)])

    #print celda,lac_oss[celda_oss.index(celda)]


#print cell.loc[cell['Cell Name'] == 'NA65AU3']['RNC Name']


cell.to_csv('C:\\Users\\palonso0\\Downloads\\Enginparam_UMTS_20161114_171836_CYL70R01_nuevo.csv',sep=',',decimal='.',quoting=1,quotechar='"',index = False)



