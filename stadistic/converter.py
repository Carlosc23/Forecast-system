# -*- coding: utf-8 -*-
import pandas as pd
import os
def conversion():
    pre = os.path.dirname(os.path.realpath(__file__))
    fname = 'Base_de_datos1_-_proyecto_No._1.xlsx'
    path = os.path.join(pre, fname)
    data_xls = pd.read_excel(path, 'Hoja1', index_col=None)
    path = os.path.join(pre, 'csvfile.csv')
    data_xls.to_csv(path, encoding='utf-8', index=False)