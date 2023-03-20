from Arbol import Arbol
from Nodos import NodoCamino
from Nodos import NodoCaja
import matplotlib.pyplot as plt

class Aestrella:

    # Creamos el constructor de la clase

    def __init__(self, nodoInicial, nodoFinal, arbol):

        self.nodoInicial = nodoInicial
        self.nodoFinal = nodoFinal
        self.arbol = arbol
        self.camino = []
        self.distanciaRecorrida = 0
        # En un principio el nodo actual sera el nodo inicial
        self.nodoActual = None
        self.vecinoFmin = None

        # Creamos una lista donde cargaremos la hoja de ruta
        self.instrucciones = []
        #Creamos una lista donde cargaremos las coordenadas en X del camino
        self.coordenadasX = []
        #Creamos una lista donde cargaremos las coordenadas en Y del camino
        self.coordenadasY = []
    
    
    # Ahora, una vez teniendo los parametros que necesitamos, creamos un metodo para implementar el algoritmo A*

    def buscador(self):
        #Establecemos al nodo actual como el nodo inicial
        self.nodoActual=self.nodoInicial
        '''
        Tenemos que hayar la forma de recorrer el arbol que creamos mediante el objeto arbol, calcular el g,h y f de cada nodo 
        y luego ir comparando los valores de f para ir eligiendo el nodo con menor f
        '''
        # Para ello primero debemos establecer la condicion de satisfaccion, es decir, cuando nuestro encuentra el test objeto, o nodo final
        while (self.nodoActual != self.nodoFinal):

            # Calculamos la funcion F de los vecinos del nodo actual
            # Colocamos un valor muy alto para que el primer vecino que se encuentre tenga menor F
            valorFmin = 100000
            for vecino in self.nodoActual.vecinos:

                # Si el vecino no fue visitado, proseguimos, si ya fue visitado lo ignoramos
                #Ademas establecemos la condicion de que lo ignore si es un nodo obstaculo (caja)
                #Para ello verificamos si el vecino es una instancia de la clase NodoCamino, ya que si es una instancia de la clase NodoCaja, no es un nodo camino
                if (vecino.estado == False) and (type(vecino) is NodoCamino):
                    # Calculamos funcion F
                    vecino.funcionF = self.calculaF(vecino)
                    # Elegimos al nodo con menor F
                    if (vecino.funcionF <= valorFmin):
                        valorFmin = vecino.funcionF
                        self.vecinoFmin = vecino
                    # Establecemos al vecino analizado como visado
                    vecino.estado = True

                else:
                    None

            # Le pasamos al metodo ruta las coordenadas del vecino que elegimos y el nodo actual, para que determine la direccion
            self.ruta(self.nodoActual.coordenadaX, self.nodoActual.coordenadaY,self.vecinoFmin.coordenadaX, self.vecinoFmin.coordenadaY)
            # Actualizamos nodo actual al vecino con menor F y lo agregamos al camino
            self.camino.append(self.vecinoFmin)
            self.nodoActual = self.vecinoFmin

        #Asignamos la distancia recorrida al atributo
        self.distanciaRecorrida = len(self.camino)

        #Una vez terminado el while le volvemos a pasar el self.ruta para que cargue el ultimo nodo actual
        self.ruta(self.nodoActual.coordenadaX, self.nodoActual.coordenadaY,self.vecinoFmin.coordenadaX, self.vecinoFmin.coordenadaY)

        return f"El camino es: {self.instrucciones} y la distancia es {self.distanciaRecorrida} casillas"
    
    #Definimos metodo de reseteo de valores para poder iniciar una nueva busqueda sin problema
    def reset(self):
        #Reseteo de valores del objeto Aestrella
        self.nodoInicial = None
        self.nodoFinal = None
        self.camino = []
        self.distanciaRecorrida = 0
        self.nodoActual = None
        self.vecinoFmin = None
        self.instrucciones = []
        self.coordenadasX = []
        self.coordenadasY = []
        #Reseteo de valores de los nodos
        for nodo in self.arbol.nodos:
            nodo.estado = False
            nodo.funcionF = 0

    def calculaG(self):

        return len(self.camino)+1

    def calculaF(self, nodo):

        return self.calculaG() + self.calculaH(nodo)

    def calculaH(self, nodo):

        # Elijo como heuristica la distancia de Manhattan
        return abs(nodo.coordenadaX - self.nodoFinal.coordenadaX) + abs(nodo.coordenadaY - self.nodoFinal.coordenadaY)
    
    

    # Creamos un metodo que me indique en que direccion se desplazo el algoritmo y lo coloque en la hoja de ruta

    def ruta(self, coordenadaXActual, coordenadaYActual, coordenadaXVecino, coordenadaYVecino):

        variacionX = coordenadaXVecino-coordenadaXActual
        variacionY = coordenadaYVecino-coordenadaYActual

        if ((variacionX) > 0):
            instruccion = "Derecha"

        elif ((variacionX) < 0):
            instruccion = "Izquierda"

        elif ((variacionY) < 0):
            instruccion = "Arriba"

        elif ((variacionY) > 0):
            instruccion = "Abajo"

        else:
            instruccion = "Llego a destino"
        self.instrucciones.append(instruccion)
    
        #Ademas vamos a agregar las coordenadas en X a una lista y las coordenadas en Y a otra lista para luego plotear el camino
        self.coordenadasX.append(coordenadaXActual)
        self.coordenadasY.append(coordenadaYActual)

    
    #Creamos un metodo para plotear el camino realizado por el algoritmo
    def plotear(self):
        
        plt.figure("Roadmap",figsize=(15,7.5))
        plt.xlabel("Coordenada X")
        plt.ylabel("Coordenada Y")
        plt.plot(self.coordenadasX, self.coordenadasY,linewidth=10.0,color='magenta')
        #Tambien vamos a plotear los nodos prohibidos en color negro con un grosor grande y rectangulos
        for nodo in self.arbol.nodos:
            if type(nodo) is NodoCaja:
                plt.plot(nodo.coordenadaX, nodo.coordenadaY, marker='s', markersize=25, markerfacecolor='gray', markeredgecolor='black')
                #Asignacion del numero de nodo a cada caja
                plt.text(nodo.coordenadaX, nodo.coordenadaY, str(nodo.id), color='white', fontsize=15, ha='center', va='center')
        
