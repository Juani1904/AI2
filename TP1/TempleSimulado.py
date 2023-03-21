#En este modulo implementaremos la clase del algoritmo temple simulado, para encontrar el optimo deoperacion de picking

import itertools
from Aestrella import Aestrella
import random
import math
import matplotlib.pyplot as plt

class TempleSimulado:

    #Definimos el constructor. Al constructor le pasaremos como parametro la lista con las distintos parametros del almacen a despachar
    #Tambien le pasamos como dato el nodo donde se estaciona el camion, que puede ser cualquiera de las esquinas, y ese sera el nodo inicial y final
    #Este puede ser cualquiera de las esquinas del almacen
    def __init__(self,arbol,nodoEstacionamiento,listaProductos,tempInicial,numIteraciones):

        self.arbol=arbol
        self.nodoInicial=nodoEstacionamiento
        self.nodoFinal=nodoEstacionamiento
        self.tempInicial=tempInicial
        self.numIteraciones=numIteraciones
        self.temperaturas=[]
        self.estadoActual=listaProductos
        self.estadosVecinos=[]
        self.estadosPosibles=[]
        self.aEstrella=Aestrella(None,None,self.arbol)
        #Ejecutamos el algoritmo
        self.ejecutaAlgortimo()


    #Definimos el metodo que ejecuta el algortimo de TempleSimulado
    def ejecutaAlgortimo(self):
        
        #Calculamos la agenda o schedule de enfriamiento mediante nuestro metodo
        self.tempSchedule()
        
        #Establecemos la condicion de corte del algoritmo
        for temperatura in self.temperaturas:

            #Calculamos los vecinos
            self.calculaVecinos()

            #Calculamos costo del estado actual
            costoActual=self.calculaCosto(self.estadoActual)

            #Elegimos al azar un estado vecino del estado actual y tomamos su costo

            estadoVecino=self.estadosVecinos[random.randint(0,len(self.estadosVecinos)-1)]
            costoVecino=self.calculaCosto(estadoVecino)

            #Calculamos la diferencia de costo entre el estado actual y el vecino
            deltaCosto=costoVecino-costoActual
            
            #Analizamos el valor de delta Costo
            if deltaCosto<0: #Estado vecino mejor que el actual
                self.estadoActual=estadoVecino #Actualizamos el estado actual
            else: #Estado vecino peor que el actual
                #Calculamos la probabilidad de aceptar el estado vecino
                probabilidadAceptacion=math.exp(-deltaCosto/temperatura)
                #Ahora vemos si la probabilidad de aceptacion es mayor que un numero aleatorio entre 0 y 1 generado por random
                if random.random() < probabilidadAceptacion:
                    self.estadoActual=estadoVecino #Actualizamos el estado actual
        
        #Imprimimos el estado final
        print("El orden optimo es: ")
        print("1° Camion")
        contador=1
        for i,elemento in enumerate(self.estadoActual):
            print(f"{i+2}° Articulo ID {self.arbol.coordenadaAId(elemento)}")
            contador+=1
        print (f"{contador+1}° Camion")
        #Ploteamos los caminos recorridos por el estado optimo (actual en este caso)
        self.plotEstadoActual()
                


    #Definimos metodo para obtener el orden de los estados vecinos
    #Para ello haremos uso de la libreria iter tools
    def calculaVecinos(self):

        self.estadosPosibles=list(itertools.permutations(self.estadoActual))

        #Ahora vamos a determinar cuales de las permutaciones son vecinas del estado actual
        for estado in self.estadosPosibles: #Iteramos sobre cada estado posible
            contador=0 #Contador para saber cuantos elementos dentro de un estado son iguales
            for i,item in enumerate(estado): #Iteramos sobre cada elemento del estado
                if self.estadoActual[i]!=item: #Si el elemento del estado actual es distinto al elemento del estado posible aumentamos el contador en 1
                    contador+=1
            if contador==2: #Si el contador es igual a 2 significa que hubieron 2 cambios en el estado, por ende 1 permutacion
                self.estadosVecinos.append(estado)
    

    #Definimos el metodo para calcular la agenda o esquema de enfriamiento
    #En este caso para mi implementacion me decidi por una temperatura con decrecimiento LINEAL
    def tempSchedule(self):

        for iteracion in range(self.numIteraciones+1):
            temperatura=self.tempInicial+((1-self.tempInicial)/self.numIteraciones)*iteracion
            self.temperaturas.append(temperatura)

    
    #Definimos metodo para calcular los costos
    def calculaCosto(self,estado):
        
        costo=0
        for i,elemento in enumerate(estado): 
            if i==0:
                self.aEstrella.nodoInicial=self.nodoInicial
                self.aEstrella.nodoFinal=elemento
                self.aEstrella.buscador()
                costo+=self.aEstrella.distanciaRecorrida
                self.aEstrella.reset() #Reseteamos el algoritmo para que no se acumulen los costos y estados de los nodos, ni los parametros de busqueda

            elif i==len(estado)-1:
                self.aEstrella.nodoInicial=elemento
                self.aEstrella.nodoFinal=self.nodoFinal
                self.aEstrella.buscador()
                costo+=self.aEstrella.distanciaRecorrida
                self.aEstrella.reset()

            else:
                elementoAnterior=estado[i-1]
                self.aEstrella.nodoInicial=elementoAnterior
                self.aEstrella.nodoFinal=elemento
                self.aEstrella.buscador()
                costo+=self.aEstrella.distanciaRecorrida
                self.aEstrella.reset()
        
        return costo
    
    #Ahora definimos el metodo para plotear el estado optimo, el cual es el resultado de varios caminos
    def plotEstadoActual(self):
        for i,elemento in enumerate(self.estadoActual): 
            if i==0:
                self.aEstrella.nodoInicial=self.nodoInicial
                self.aEstrella.nodoFinal=elemento
                self.aEstrella.buscador()
                self.aEstrella.plotear()
                self.aEstrella.reset() #Reseteamos el algoritmo para que no se acumulen los costos y estados de los nodos, ni los parametros de busqueda

            elif i==len(self.estadoActual)-1:
                self.aEstrella.nodoInicial=elemento
                self.aEstrella.nodoFinal=self.nodoFinal
                self.aEstrella.buscador()
                self.aEstrella.plotear()
                self.aEstrella.reset()

            else:
                elementoAnterior=self.estadoActual[i-1]
                self.aEstrella.nodoInicial=elementoAnterior
                self.aEstrella.nodoFinal=elemento
                self.aEstrella.buscador()
                self.aEstrella.plotear()
                self.aEstrella.reset()
        
        #Finalmente mostramos todo
        ax = plt.gca()
        ax.set_facecolor('gray')
        ax.invert_yaxis()
        plt.axis('equal')
        plt.show()


        



    
    
       
        
        