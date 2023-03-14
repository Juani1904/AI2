from Nodos import Nodo


class Arbol:

    # Creamos el constructor del objeto Arbol, el cual sera la clase agregada, mientras que los objetos nodos son objetos componentes de dicha composicion
    # Vamos a crear el arbol a partir del nodo Raiz
    def __init__(self, numeroFilas, numeroColumnas):
        #self.nodoRaiz = nodoRaiz
        self.nodos = []
        self.numeroFilas = numeroFilas
        self.numeroColumnas = numeroColumnas

        # Llamamos a los metodos de crearNodo y asignarVecinos
        self.crearNodo()
        self.asignarVecinos()
        

    # Ahora creamos el metodo para crear el arbol a partir de nodo raiz
    '''
    Para ello vamos a utilizar el algoritmo de busqueda en anchura, para ir creando el arbol al instanciar los distintos objetos nodos,
    los cuales determinaran el espacio de busqueda donde luego aplicaremos nuestro algortimo A*
    '''
    # En un principio solamente creamos los nodos con este metodo, luego con otro metodo asignaremos los vecinos a cada nodo

    def crearNodo(self):
        for filas in range(0, self.numeroFilas+1):
            for columnas in range(0, self.numeroColumnas+1):
                # Creamos la lista donde se guardaran todos los objetos nodo
                self.nodos.append(Nodo(columnas, filas, False))

    # Ahora creamos el metodo para asignar los vecinos a cada nodo
    def asignarVecinos(self):

        for nodo in self.nodos:
            # Condiciones (tomando como eje x positivo la posicion hacia la derecha y como y positivo la posicion hacia abajo)
            nodoDerecho = nodo.coordenadaX + 1, nodo.coordenadaY
            nodoIzquierdo = nodo.coordenadaX - 1, nodo.coordenadaY
            nodoArriba = nodo.coordenadaX, nodo.coordenadaY - 1
            nodoAbajo = nodo.coordenadaX, nodo.coordenadaY + 1
            
            # No me interesan los vecinos diagonales, solamente verticales u horizontales
            # Para poder asignar los valores creo un seeker o buscador que recorra la lista de nodos y me devuelva el nodo que cumpla con las condiciones
            for seeker in self.nodos:
                #Coordenadas del nodo actual del seeker (en una tupla)
                nodoActual = seeker.coordenadaX, seeker.coordenadaY
                if ((nodoActual == nodoDerecho) or (nodoActual == nodoIzquierdo) or (nodoActual == nodoArriba) or (nodoActual == nodoAbajo)):
                    nodo.vecinos.append(seeker)
                
                



