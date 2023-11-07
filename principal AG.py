import Cromosoma as crom
import Logic as logic
import numpy as np
import pandas as pd
import copy as cp
import heuristica
import os

ciclos=1000
cantPob=50
mutRate=0.05
crossRate=0.30
minimos=[]
maximos=[]
nuevaPoblacion=[]
metodo='ruleta'

def clean():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

def start(startingCity):
    poblacion = cp.deepcopy(logic.generarPoblacion(cantPob, startingCity))
    logic.evaluarPoblacion(poblacion)
    logic.save_data(maximos, minimos, poblacion)
    for _ in range(ciclos):
        nuevaPoblacion.clear()
        while len(nuevaPoblacion) < len(poblacion):
            if (metodo=='torneo'):
                padres=cp.deepcopy(logic.torneo(poblacion))
            else:
                padres=cp.deepcopy(logic.ruleta(poblacion))
            hijos=cp.deepcopy(logic.crossover(padres, crossRate, mutRate))
            for ind in hijos:
                nuevaPoblacion.append(cp.deepcopy(ind))
        logic.evaluarPoblacion(nuevaPoblacion)
        poblacion.clear()
        for ind in nuevaPoblacion:
            poblacion.append(cp.deepcopy(ind))
        logic.save_data(maximos, minimos, poblacion)

    poblacion[0].imprimirRecorrido()
    poblacion[0].print_map()

    logic.graficar(maximos, minimos)

ciudades = pd.read_csv('coordenadas.csv')
rta = 's'
while (rta == 's'):
    print('[1] Algoritmo genético')
    print('[2] Heurística')
    print('[3] Ruta mas corta con heurística')
    alg = input('\n' + "\033[1;34m" + 'Ingrese código de método: ' + '\033[0m')
    clean()

    if (alg == '1' or alg == '2'):
        for i in range(24):
            print(i+1, '-->', ciudades.iloc[i]['ciudad'])
        startingCity = int(input("\033[1;34m" + 'Ingrese el ID de la ciudad de inicio: ' + '\033[0m'))
        clean()

    if (alg == '1'):
        start(startingCity)
    if (alg == '2'):    
        heuristica.init(startingCity)
    if (alg == '3'):
        heuristica.find_shortest()
    
    rta = input("\033[42m" + 'Continuar? s / n:' + '\033[0m' + ' ')
    clean()

