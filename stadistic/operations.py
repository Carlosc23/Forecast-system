import base64
import io
from pandas import read_csv, DataFrame
import matplotlib.pyplot as plt
from astropy.table import Table, Column
import astropy.units as astr
import numpy as np
from mpltools import style
from mpltools import layout
import os
import csv

style.use('ggplot')


def smoothing():
    d2015M = []
    d2015M = averageM()[0]
    d2015Suave = []
    f2015 = []
    f2015 = averageM()[1]
    alpha = 0.74
    d2015Suave.append(d2015M[0]) #obtener primer dato para el suavizamiento (es igual al del ponderado)
    for i in range(len(f2015)-1):
        d2015Suave.append(alpha*float(d2015M[i+1])+(1.0-alpha)*float(d2015Suave[i])) #ponderado junto con el del dia anterior
    with open("stadistic/pronosticosSuaves.csv", "w") as csvDataFile:
        fieldnames = ['fecha', 'cobro']
        writer = csv.DictWriter(csvDataFile, fieldnames=fieldnames)
        writer.writeheader()
        for index in range(len(f2015)):
            writer.writerow({'fecha': str(f2015[index]), 'cobro': str(d2015Suave[index])})
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
    return d2015, f2015

def createTable(numMes):
    #print "estoy aqui"
    opcion = numMes
    tEnero = Table(names=("Fecha","Monto"), dtype=('S10','S11'))
    tFebrero = Table(names=("Fecha", "Monto"), dtype=('S10','S11'))
    tMarzo = Table(names=("Fecha", "Monto"), dtype=('S10','S11'))
    tAbril = Table(names=("Fecha", "Monto"), dtype=('S10','S11'))
    tMayo = Table(names=("Fecha", "Monto"), dtype=('S10','S11'))
    tJunio = Table(names=("Fecha", "Monto"), dtype=('S10','S11'))
    tJulio = Table(names=("Fecha", "Monto"), dtype=('S10','S11'))
    tAgosto = Table(names=("Fecha", "Monto"), dtype=('S10','S11'))
    tSeptiembre = Table(names=("Fecha", "Monto"), dtype=('S10','S11'))
    tOctubre = Table(names=("Fecha", "Monto"), dtype=('S10','S11'))
    tNoviembre = Table(names=("Fecha", "Monto"), dtype=('S10','S11'))
    tDiciembre = Table(names=("Fecha", "Monto"), dtype=('S10','S11'))

    with open("stadistic/pronosticosSuaves.csv") as csvDataFile:
        csvReader = csv.reader(csvDataFile, delimiter=",")
        for row in csvReader:
            if "2015-01" in row[0]:
                tEnero.add_row((row[0],str(row[1])))
            elif "2015-02" in row[0]:
                tFebrero.add_row((row[0],row[1]))
            elif "2015-03" in row[0]:
                tMarzo.add_row((row[0],row[1]))
            elif "2015-04" in row[0]:
                tAbril.add_row((str(row[0]),row[1]))
            elif "2015-05" in row[0]:
                tMayo.add_row((row[0],row[1]))
            elif "2015-06" in row[0]:
                tJunio.add_row((row[0],row[1]))
            elif "2015-07" in row[0]:
                tJulio.add_row((row[0],row[1]))
            elif "2015-08" in row[0]:
                tAgosto.add_row((row[0],row[1]))
            elif "2015-09" in row[0]:
                tSeptiembre.add_row((row[0],row[1]))
            elif "2015-10" in row[0]:
                tOctubre.add_row((row[0],row[1]))
            elif "2015-11" in row[0]:
                tNoviembre.add_row((row[0],row[1]))
            elif "2015-12" in row[0]:
                tDiciembre.add_row((row[0],row[1]))
    if opcion == 1:
        return tEnero
    elif opcion == 2:
        return tFebrero
    elif opcion == 3:
        return tMarzo
    elif opcion == 4:
        return tAbril
    elif opcion == 5:
        return tMayo
    elif opcion == 6:
        return tJunio
    elif opcion == 7:
        return tJulio
    elif opcion == 8:
        return tAgosto
    elif opcion == 9:
        return tSeptiembre
    elif opcion == 10:
        return tOctubre
    elif opcion == 11:
        return tNoviembre
    elif opcion == 12:
        return tDiciembre

def graficarConSuavizamiento(numMes):
    pre = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(pre, 'pronosticosSuaves.csv')
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
