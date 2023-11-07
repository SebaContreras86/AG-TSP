import pandas as pd
import matplotlib.pyplot as plt
import copy

df = pd.read_excel('TablaCapitales.xlsx', header=None)
datos = df.to_numpy()

def init(startingCity):
    path = generarRecorrido(startingCity)
    imprimir(path)
    print_map(path)

def next_city(ciudad, recorrido):
    dist_minima = float('inf')
    nearest_city = float('inf')
    for i in range(1, 25):
        if ((i != ciudad) and (i not in recorrido)):
            dist = int(datos[ciudad, i])
            if (dist < dist_minima):
                nearest_city = i
                dist_minima = int(datos[ciudad, i])
    return nearest_city

#el numero indica de donde empezar, cada numero representa una ciudad en el orden que esta en tabla
def generarRecorrido(startingCity):
    recorrido = []
    recorrido.append(startingCity)
    ciudad_actual = next_city(startingCity, recorrido)
    while (len(recorrido) < 24):
        recorrido.append(ciudad_actual)
        if (len(recorrido) < 24):
            ciudad_actual = next_city(ciudad_actual, recorrido)
    recorrido.append(startingCity)
    return recorrido

def imprimir(recorrido):
    for i in range(len(recorrido)):
        print(i, datos[0, recorrido[i]])
    print ('Distancia: ', calcularDist(recorrido))

def print_map(recorrido):
        coordenadas = pd.read_csv('coordenadas.csv')
        x = []
        y = []
        for i in recorrido:
            x.append(coordenadas.iloc[i-1]['x'])
            y.append(coordenadas.iloc[i-1]['y'])

        plt.rcParams["figure.figsize"] = [7.50, 3.50]
        plt.rcParams["figure.autolayout"] = True

        background = plt.imread(r'mapa.jpg')
        plt.imshow(background, extent=[0, 117, 0, 160])
        plt.plot(x, y, 'bo', linestyle="--")
        ax = plt.gca()
        bbox_props = dict(boxstyle="circle,pad=0.1", fc='red', ec="black", lw=0.1)
        for i in range(len(recorrido)-1):
            ax.text(x[i], y[i], str(i), ha="center", va="center",
                size=8,
                bbox=bbox_props)
        ax.text(x[0], y[0], 'O', ha="center", va="center",
                size=8,
                bbox=dict(boxstyle="circle,pad=0.1", fc='green', ec="black", lw=0.1))
        plt.show()

def calcularDist(recorrido):
    sum = 0
    for i in range (len(recorrido)-1):
        sum += int(datos[recorrido[i], recorrido[i+1]])
    return sum

def find_shortest():
    shortest_distance = float('inf')
    shortest_path = []
    for i in range(1, 25):
        path = generarRecorrido(i)
        if (calcularDist(path) < shortest_distance):
            shortest_distance = calcularDist(path)
            shortest_path = copy.deepcopy(path)
        path.clear()
    imprimir(shortest_path)
    print_map(shortest_path)