#En este modulo implementaremos la clase del algoritmo temple simulado, para encontrar el optimo deoperacion de picking

import itertools
from Aestrella import Aestrella
import random
import math
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
        print("El estado final es: ")
        for elemento in self.estadoActual:
            print(elemento.id)
                



            
    #Definimos metodo para obtener el orden de los estados vecinos
    #Para ello haremos uso de la libreria iter tools
    def calculaVecinos(self):

        self.estadosPosibles=itertools.permutations(self.estadoActual)

        #Ahora vamos a determinar cuales de las permutaciones son vecinas del estado actual
        for estado in self.estadosPosibles: #Iteramos sobre cada estado posible
            contador=0 #Contador para saber cuantos elementos dentro de un estado son iguales
            for item in estado: #Iteramos sobre cada elemento del estado
                if self.estadoActual[int(estado.index(item))]==item: #Si el elemento del estado actual es igual al elemento del estado posible aumentamos el contador en 1
                    contador+=1
            if contador==2: #Si el contador es igual a 2 significa que hubo 1 sola permutacion, dado que solo cambiaron 2 valores de posicion en el estado
                self.estadosVecinos.append(estado)
    

    #Definimos el metodo para calcular la agenda o esquema de enfriamiento
    #En este caso para mi implementacion me decidi por una temperatura con decrecimiento LINEAL
    def tempSchedule(self):

        for iteracion in range(self.numIteraciones+1):
            temperatura=self.tempInicial-(self.tempInicial/self.numIteraciones)*iteracion
            self.temperaturas.append(temperatura)

    
    #Definimos metodo para calcular los costos
    def calculaCosto(self,estado):
        
        costo=0
        for i,elemento in enumerate(estado): 
            if i==0:
                aEstrella=Aestrella(self.nodoInicial,elemento,self.arbol)
                aEstrella.buscador()
                costo+=len(aEstrella.camino)
                self.arbol.resetNodos()

            elif i==len(estado)-1:
                aEstrella=Aestrella(elemento,self.nodoFinal,self.arbol)
                aEstrella.buscador()
                costo+=len(aEstrella.camino)
                self.arbol.resetNodos()

            else:
                elementoAnterior=estado[i-1]
                aEstrella=Aestrella(elementoAnterior,elemento,self.arbol)
                aEstrella.buscador()
                costo+=len(aEstrella.camino)
                self.arbol.resetNodos()
        
        return costo

        



    
    
       
        
        