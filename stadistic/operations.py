import base64
import io
from pandas import read_csv, DataFrame
import matplotlib.pyplot as plt
from mpltools import style
from mpltools import layout
import os
import csv
style.use('ggplot')
def smoothing():
    pass
def averageM():
    fecha = []
    dinero = []
    with open("stadistic/csvfile.csv") as csvDataFile:
        csvReader = csv.reader(csvDataFile, delimiter=",")
        for row in csvReader:
            fecha.append(row[0])
            dinero.append(row[1])
        print dinero[3]
        print fecha[3]
def generate_graphs():
    pre = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(pre, 'csvfile.csv')
    series = read_csv(path, header=0, parse_dates=[0], index_col=0, squeeze=True)
    a = series['2015-01':'2015-03']
    #ax1.plot(series['2015-01'], color=plt.rcParams['axes.color_cycle'][1], linewidth=1.5, linestyle="-")
    a.plot(color=plt.rcParams['axes.color_cycle'][1], linewidth=1.5, linestyle="-")
    #ax1.plot(series['2015-02'], color=plt.rcParams['axes.color_cycle'][2], linewidth=1.5, linestyle="-")
    #ax1.plot(series['2015-03'], color=plt.rcParams['axes.color_cycle'][2], linewidth=1.5, linestyle="-")
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return plot_url

