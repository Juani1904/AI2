from Nodos import NodoCamino
from Nodos import NodoCaja
from Estanterias import Estanteria

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
        #Le asignamos el id a los nodos caja
        self.asignarId()
        #Asignamos los vecinos a cada nodo
        self.asignarVecinos()
        
    # Ahora creamos el metodo para crear el arbol a partir de nodo raiz
    '''
    Para ello vamos a utilizar el algoritmo de busqueda en anchura, para ir creando el arbol al instanciar los distintos objetos nodos,
    los cuales determinaran el espacio de busqueda donde luego aplicaremos nuestro algortimo A*
    '''
    # En un principio solamente creamos los nodos con este metodo, luego con otro metodo asignaremos los vecinos a cada nodo

    def crearNodo(self):
        self.estanteria=[] #Definimos la lista donde se guardaran las estanterias
        for filas in range(0, self.numeroFilas+1):
            contadorEstanteria=0 #Definimos el contador de las estanterias. Lo definimos aca para que se reinicie a 0 cada vez que empieza una fila nueva
            for columnas in range(0, self.numeroColumnas+1):
                # Creamos la lista donde se guardaran todos los objetos nodo
                #Para generar los obstaculos generamos las siguientes condiciones mediante el operador modulo
                #Primero verificamos las filas
                if(not(filas % 6 < 2) or (filas % 6 >= 4)): #Si esta condicion se cumple, algunos seran camino y otros obstaculo, esto queda regido por el eje X

                    if ((columnas % 4 < 2)): #Si esta condicion se cumple, el nodo sera camino
                        self.nodos.append(NodoCamino(columnas, filas, False))

                    else: #Si esta condicion se cumple el nodo sera obstaculo (caja)
                        nodoCaja=NodoCaja(columnas, filas, False)
                        self.nodos.append(nodoCaja)

                        #Ahora instanciamos los objetos estanterias, donde se encontraran los objetos caja
                        if (filas % 6 ==2) and (columnas % 2 ==0): #Si esta condicion se cumple, es porque se esta en la primera fila de estanterias, solo aca se instancia el objeto estanteria
                            self.estanteria.append(Estanteria(contadorEstanteria+1))

                        if ((columnas % 2 ==0)): #En este caso para valores pares de columnas, se agregan las cajas a la estanteria pero no se incrementa el contador
                            self.estanteria[contadorEstanteria].cajas.append(nodoCaja)
                            
                        else: #Si el valor de columna es impar, significa que estamos por pasar a un nodo camino, en ese caso se agrega la caja y se incrementa el contador
                            self.estanteria[contadorEstanteria].cajas.append(nodoCaja)
                            contadorEstanteria+=1

                else: #Si no se cumple la condicion anterior, todos seran camino
                    self.nodos.append(NodoCamino(columnas, filas, False))
        
        

                
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
                # Coordenadas del nodo actual del seeker (en una tupla)
                nodoActual = seeker.coordenadaX, seeker.coordenadaY
                if ((nodoActual == nodoDerecho) or (nodoActual == nodoIzquierdo) or (nodoActual == nodoArriba) or (nodoActual == nodoAbajo)):
                    nodo.vecinos.append(seeker)
    

    #Creamos un metodo para asignar valores de id a los nodos caja
    #La dificultad de esto reside en que decesitamos numerar a los nodos en el orden en que se encuentran en la estanteria
    #Como estan colocados en la lista me los va a numerar mal, por lo que necesito un metodo que me los ordene de acuerdo a su posicion en la estanteria
    def asignarId(self):

        #Para asignar el id vamos a tomar las estanterias en orden y luego los nodos caja dentro de cada estanteria
        contador=1
        for estanteria in self.estanteria:
            for caja in estanteria.cajas:
                caja.id=contador
                contador+=1

    
    #Definimos un metodo para referenciar los ids a las coordenadas en el arbol
    #Creamos una funcion para referenciar el id de la caja a la coordenada en el camino
    def idACoordenada(self,id):
        #Ahora establecemos la condicion para relacionarlo con la coordenada junto al espacio con el id determinado
        if (id==0):
            return self.nodos[0]
        else:
            for estanteria in self.estanteria:
                for caja in estanteria.cajas:
                    if (caja.id == id) and (id % 2 != 0):
                        coordenadaXReferencia=caja.coordenadaX-1
                        for nodo in self.nodos:
                            if nodo.coordenadaX == coordenadaXReferencia and nodo.coordenadaY == caja.coordenadaY:
                                return nodo
                    elif (caja.id == id) and (id % 2 == 0):
                        coordenadaXReferencia=caja.coordenadaX+1
                        for nodo in self.nodos:
                            if nodo.coordenadaX == coordenadaXReferencia and nodo.coordenadaY == caja.coordenadaY:
                                return nodo
                            

    
    #Creamos un nodo que me resetee el estado de los nodos del arbol
    def resetNodos(self):
        for nodo in self.nodos:
            nodo.estado = False
            nodo.funcion=0


        



        


