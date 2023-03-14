from Arbol import Arbol
from Nodos import Nodo
import matplotlib.pyplot as plt

class Aestrella:

    # Creamos el constructor de la clase

    def __init__(self, nodoInicial, nodoFinal, arbol):

        self.nodoInicial = nodoInicial
        self.nodoFinal = nodoFinal
        self.arbol = arbol
        self.camino = []
        # En un principio el nodo actual sera el nodo inicial
        self.nodoActual = self.nodoInicial
        self.vecinoFmin = None

        # Creamos una lista donde cargaremos la hoja de ruta
        self.instrucciones = []
        #Creamos una lista donde cargaremos las coordenadas en X del camino
        self.coordenadasX = []
        #Creamos una lista donde cargaremos las coordenadas en Y del camino
        self.coordenadasY = []

    # Ahora, una vez teniendo los parametros que necesitamos, creamos un metodo para implementar el algoritmo A*

    def buscador(self):
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
                #Ademas tambien lo ignoramos si su condicion es prohibida por ser un obstaculo
                if ((vecino.estado == False) and (vecino.nodoProhibido == False)):
                    # Calculamos funcion F
                    vecino.funcionF = self.calculaF(vecino)
                    # Elegimos al nodo con menor F
                    if (vecino.funcionF < valorFmin):
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
        
        #Una vez terminado el while le volvemos a pasar el self.ruta para que cargue el ultimo nodo actual
        self.ruta(self.nodoActual.coordenadaX, self.nodoActual.coordenadaY,self.vecinoFmin.coordenadaX, self.vecinoFmin.coordenadaY)

        return f"El camino es: {self.instrucciones} y la distancia es {len(self.camino)} casillas"

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
            instruccion = "Abajo"

        elif ((variacionY) > 0):
            instruccion = "Arriba"

        else:
            instruccion = "Llego a destino"
        self.instrucciones.append(instruccion)
    
        #Ademas vamos a agregar las coordenadas en X a una lista y las coordenadas en Y a otra lista para luego plotear el camino
        self.coordenadasX.append(coordenadaXActual)
        self.coordenadasY.append(coordenadaYActual)

    
    #Creamos un metodo para plotear el camino realizado por el algoritmo
    def plotear(self):
        
        plt.plot(self.coordenadasX, self.coordenadasY,linewidth=8.0,color='magenta')
        #Tambien vamos a plotear los nodos prohibidos en color negro con un grosor grande y rectangulos
        for nodo in self.arbol.nodos:
            if nodo.nodoProhibido == True:
                plt.plot(nodo.coordenadaX, nodo.coordenadaY, marker='s', markersize=25, markerfacecolor='gray', markeredgecolor='black')
        ax = plt.gca()
        ax.set_facecolor('gray')
        plt.show()
