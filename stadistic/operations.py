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
    f2014 = []
    d2014 = []
    f2013 = []
    d2013 = []
    f2015 = []
    d2015 = []
    dinero = []
    with open("stadistic/csvfile.csv") as csvDataFile:
        csvReader = csv.reader(csvDataFile, delimiter=",")
        for row in csvReader:
            fecha.append(row[0])
            dinero.append(row[1])
        for i in range(len(fecha)):
            if "2013" in fecha[i]:
                f2013.append(fecha[i])
                d2013.append(dinero[i])
            elif "2014" in fecha[i]:
                f2014.append(fecha[i])
                d2014.append(dinero[i])
        for j in range(len(f2013) - 3):
            if float(d2014[j + 1]) == 0:
                d2015.append(float(d2013[j + 2]))
            else:
                d2015.append((3 * float(d2013[j + 2]) + 10 * float(d2014[j + 1])) / 13.0)  # linea donde se calcula el promedio/media ponderada
            f2015.append(f2013[j + 1].replace("2013", "2015"))
        d2015.pop(0)
        f2015.pop(len(f2015) - 1)
    with open("stadistic/pronosticoPromedio.csv", "w") as csvDataFile:
        fieldnames = ['fecha', 'cobro']
        writer = csv.DictWriter(csvDataFile, fieldnames=fieldnames)
        writer.writeheader()
        for index in range(len(f2015)):
            writer.writerow({'fecha': str(f2015[index]), 'cobro': str(d2015[index])})


def graficarConPromedio(numMes):
    pre = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(pre, 'pronosticoPromedio.csv')
    series = read_csv(path, header=0, parse_dates=[0], index_col=0, squeeze=True)
    tiempo = "2015-0" + str(numMes)
    print tiempo
    a = series[tiempo]
    a.plot(color=plt.rcParams['axes.color_cycle'][1], linewidth=1.5, linestyle="-")
    plt.savefig('static/images/Graph.png')
    path = 'Graph.png'
    return path


def generate_graphs():
    pre = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(pre, 'csvfile.csv')
    series = read_csv(path, header=0, parse_dates=[0], index_col=0, squeeze=True)
    a = series['2015-01']
    # ax1.plot(series['2015-01'], color=plt.rcParams['axes.color_cycle'][1], linewidth=1.5, linestyle="-")
    a.plot(color=plt.rcParams['axes.color_cycle'][1], linewidth=1.5, linestyle="-")
    # ax1.plot(series['2015-02'], color=plt.rcParams['axes.color_cycle'][2], linewidth=1.5, linestyle="-")
    # ax1.plot(series['2015-03'], color=plt.rcParams['axes.color_cycle'][2], linewidth=1.5, linestyle="-")
    # plt.show()
    plt.savefig('static/images/Graph.png')
    path = 'Graph.png'
    return path
