from Arbol import Arbol
from Nodos import Nodo

class Aestrella:

    #Creamos el constructor de la clase

    def __init__(self, nodoInicial, nodoFinal, arbol): 

        self.nodoInicial = nodoInicial
        self.nodoFinal = nodoFinal
        self.arbol = arbol
        self.camino = []
        #self.nodosVisitados = []
        #self.nodosNoVisitados = []
        #self.nodosNoVisitados.append(self.nodoInicial)
        self.nodoActual = self.nodoInicial #Eh un principio el nodo actual sera el nodo inicial
        self.vecinoFmin = None
        #Ahora, una vez teniendo los parametros que necesitamos, creamos un metodo para implementar el algoritmo A*

    def buscador(self):

        '''
        Tenemos que hayar la forma de recorrer el arbol que creamos mediante el objeto arbol, calcular el g,h y f de cada nodo 
        y luego ir comparando los valores de f para ir eligiendo el nodo con menor f
        '''
        #Para ello primero debemos establecer la condicion de satisfaccion, es decir, cuando nuestro encuentra el test objeto, o nodo final
        while(self.nodoActual != self.nodoFinal):

            #Calculamos la funcion F de los vecinos del nodo actual
            valorFmin=100000 #Colocamos un valor muy alto para que el primer vecino que se encuentre tenga menor F
            for vecino in self.nodoActual.vecinos:

                #Si el vecino no fue visitado, proseguimos, si ya fue visitado lo ignoramos
                if (vecino.estado==False):
                    #Calculamos funcion F
                    vecino.funcionF=self.calculaF(vecino)
                    #Elegimos al nodo con menor F
                    if(vecino.funcionF<valorFmin):
                        valorFmin=vecino.funcionF
                        self.vecinoFmin=vecino
                    #Establecemos al vecino analizado como visado
                    vecino.estado=True

                else:
                    None
                
            #Actualizamos nodo actual al vecino con menor F y lo agregamos al camino
            self.camino.append(self.vecinoFmin)
            self.nodoActual=self.vecinoFmin
        
        return f"El camino es: {self.camino} y la distancia es {len(self.camino)} casillas"
                
            
            


        


    def calculaG(self):

        return len(self.camino)+1
    

    def calculaF(self,nodo):

        return self.calculaG() + self.calculaH(nodo)

    def calculaH(self,nodo):
        
        #Elijo como heuristica la distancia de Manhattan
        return abs(nodo.coordenadaX - self.nodoFinal.coordenadaX) + abs(nodo.coordenadaY - self.nodoFinal.coordenadaY)



