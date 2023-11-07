import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel('TablaCapitales.xlsx', header=None)

datos=df.to_numpy()
coordenadas = pd.read_csv('coordenadas.csv')

class Cromosoma:
    def __init__(self, recorrido=0, distancia=0):
        self.recorrido=recorrido
        self.totalDist=distancia
        self.fitness=0
    
    def getRecorrido(self):
        return self.recorrido

    def setRecorrido(self, recorrido):
        self.recorrido = recorrido
    
    def getDistancia(self):
        return self.totalDist

    def setDistancia(self, dist):
        self.totalDist=dist
    
    def generarRecorrido(self, startingCity):
        recorrido=np.array([], dtype=int)
        for i in range(24):
            recorrido=np.append(recorrido, i+1)
        
        recorrido=np.random.permutation(recorrido)
        recorrido=np.delete(recorrido, np.where(recorrido==startingCity))
        recorrido=np.insert(recorrido, 0, startingCity)
        recorrido=np.append(recorrido, startingCity)

        return recorrido

    def calcularDistancia(self):
        sum=0
        for i in range(len(self.recorrido)-1):
            sum += int(datos[self.recorrido[i], self.recorrido[i+1]])
        return sum
    
    def setFitness(self, fitness):
        self.fitness=fitness

    def getFitness(self):
        return self.fitness

    def imprimirRecorrido(self):
        print('El recorrido es: ')
        for i in self.recorrido:
            print(datos[0, i])
        
        print('Distancia total: ', self.totalDist)

    def print_map(self):
        coordenadas = pd.read_csv('coordenadas.csv')
        x = []
        y = []
        for i in self.recorrido:
            x.append(coordenadas.iloc[i-1]['x'])
            y.append(coordenadas.iloc[i-1]['y'])

        plt.rcParams["figure.figsize"] = [7.50, 3.50]
        plt.rcParams["figure.autolayout"] = True

        background = plt.imread(r'mapa.jpg')
        plt.imshow(background, extent=[0, 117, 0, 160])
        plt.plot(x, y, 'bo', linestyle="--")
        ax = plt.gca()
        bbox_props = dict(boxstyle="circle,pad=0.1", fc='red', ec="black", lw=0.1)
        for i in range(len(self.recorrido)-1):
            ax.text(x[i], y[i], str(i), ha="center", va="center",
                size=8,
                bbox=bbox_props)
        ax.text(x[0], y[0], 'O', ha="center", va="center",
                size=8,
                bbox=dict(boxstyle="circle,pad=0.1", fc='green', ec="black", lw=0.1))
        plt.show()

