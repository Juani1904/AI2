#En este modulo implementaremos la clase del algoritmo temple simulado, para encontrar el optimo deoperacion de picking

import itertools
from Aestrella import Aestrella

class TempleSimulado:

    #Definimos el constructor. Al constructor le pasaremos como parametro la lista con las distintos parametros del almacen a despachar
    #Tambien le pasamos como dato el nodo donde se estaciona el camion, que puede ser cualquiera de las esquinas, y ese sera el nodo inicial y final
    #Este puede ser cualquiera de las esquinas del almacen
    def __init__(self,nodoEstacionamiento,listaProductos):

        self.listaProductos=listaProductos
        self.nodoInicial=nodoEstacionamiento
        self.nodoFinal=nodoEstacionamiento
        self.nodoActual=self.nodoInicial
        self.estadoActual=listaProductos
        self.estadosVecinos=[]
        self.estadosPosibles=[]
        
        #Ejecutamos el algoritmo
        self.ejecutaAlgortimo()


    #Definimos metodo para obtener el orden de los estados vecinos
    #Para ello haremos uso de la libreria iter tools
    def calculaVecinos(self):

        self.estadosPosibles=itertools.permutations(self.listaProductos)

        #Ahora vamos a determinar cuales de las permutaciones son vecinas del estado actual
        for estado in self.estadosPosibles: #Iteramos sobre cada estado posible
            contador=0 #Contador para saber cuantos elementos dentro de un estado son iguales
            for item in estado: #Iteramos sobre cada elemento del estado
                if self.estadoActual[int(estado.index(item))]==item: #Si el elemento del estado actual es igual al elemento del estado posible aumentamos el contador en 1
                    contador+=1
            if contador==2: #Si el contador es igual a 2 significa que hubo 1 sola permutacion, dado que solo cambiaron 2 valores de posicion en el estado
                self.estadosVecinos.append(estado)



    
    #Definimos el metodo que ejecuta el algortimo de TempleSimulado
    def ejecutaAlgortimo(self):

        #Calculamos los vecinos
        self.calculaVecinos()
       
        
        