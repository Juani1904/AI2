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
        self.nodoPadre = None
        self.nodosVisitados = []
        self.contadorColores=0

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
        self.nodoActual.funcionF=self.calculaH(self.nodoInicial)
        '''
        Tenemos que hayar la forma de recorrer el arbol que creamos mediante el objeto arbol, calcular el g,h y f de cada nodo 
        y luego ir comparando los valores de f para ir eligiendo el nodo con menor f
        '''
        
        # Debemos establecer la condicion de satisfaccion, es decir, cuando nuestro encuentra el test objeto, o nodo final
        while (self.nodoActual != self.nodoFinal):

            self.nodoActual.estado=True #Establecemos el estado del nodo actual como visitado
            self.nodosVisitados.append(self.nodoActual) #Agregamos el nodo actual a la lista de nodos visitados
            #Llamamos al metodo que calcula el minimo F de los vecinos de un nodo que le pase como parametro
            #A su vez este metodo tambien asigna a los nodos del arbol el valor de F y G
            #Este metodo retorna el nodo con menor F
            self.nodoPadre,_=self.calculaFmin(self.nodoActual)
            
            #Una vez teniendo el nodo hijo con F minima, lo expandimos, calculamos el valor Fmin de sus hijos, y chequeamos que dicho valor sea menor al Fmin de los nodos hermanos del nodo padre
            #Si es menor, entonces el nodo actual (nodo abuelo), pasa a ser el nodo padre
            #Si no, el nodo abuelo pasa a ser el hermano del nodo padre (el que tenia F menor que el hijo de su hermano)

            #Adicionalmente verificamos que el valor de F no sea mayor a ninguno de los nodos ya expandidos pero no visitados no tengan un F menor
            if (self.nodoPadre.funcionF > self.nodoActual.funcionF) and (self.nodoActual != self.nodoInicial):
                
                nodosVisitadosInvertida=self.nodosVisitados[::-1]
                for nodoExpandido in nodosVisitadosInvertida:
                    for nodoVecino in nodoExpandido.vecinos:
                        if (nodoVecino.estado == False) and (type(nodoVecino) is NodoCamino):
                            if (nodoVecino.funcionF < self.nodoPadre.funcionF):
                                self.nodoActual=nodoVecino
                                break
                    else:
                        continue

                    break
            else:

                self.nodoHijo,FminHijo=self.calculaFmin(self.nodoPadre,True)

                for nodoHermano in self.nodoActual.vecinos:
                    if (nodoHermano != self.nodoPadre) and (type(nodoHermano) != NodoCaja) and (nodoHermano.estado == False):

                        if(nodoHermano.funcionF < FminHijo):
                            self.nodoActual=nodoHermano
                            
                            
                    else:
                        self.nodoActual=self.nodoPadre
            
            
                        
        
            #Establecemos el estado del nodo actual como visado y lo agregamos al camino
            
            self.camino.append(self.nodoActual)
            #Hacemos el tratamiento al camino para que no incluya los caminos que no se terminaron de recorrer
            caminoInvertido=self.camino[::-1]
            for paso in caminoInvertido:
                if (paso != caminoInvertido[-1]):
                    try:
                        
                        while(paso.vengoDe != caminoInvertido[caminoInvertido.index(paso)+1]):
                        
                            pasoErroneo=caminoInvertido[caminoInvertido.index(paso)+1]
                            caminoInvertido.remove(pasoErroneo)
                            pasoErroneo.estado==True

                        #self.calculaFmin(caminoInvertido[caminoInvertido.index(paso)+1])
                        
                    except IndexError:
                        break
            self.camino=caminoInvertido[::-1]
                
        #Finalmente agregamos el nodo final e inicial al camino
        self.camino.insert(0,self.nodoInicial)
        self.camino.append(self.nodoFinal)

        
                    


        #Asignamos la distancia recorrida al atributo
        self.distanciaRecorrida = len(self.camino)-2

        #Llamamos al metodo ruta para que me genere las instrucciones y me mande las coordenadas del camino a los atributos correspondientes
        self.ruta()

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
        self.nodosVisitados = []

        #Reseteo de valores de los nodos
        for nodo in self.arbol.nodos:
            nodo.estado = False
            nodo.funcionF = 0
            nodo.funcionG = 0
    
    #Creamos sobrecarga de metodos F y G para nodos hijos
    def calculaG(self, numero=1):
        
        return len(self.camino)+numero

    
    def calculaF(self, nodo, activador=None,numero=1):
        
        if activador!=None:
            valorG=self.calculaG(numero)
            valorH=self.calculaH(nodo)
            return valorG + valorH
        else:
            valorG=self.calculaG()
            valorH=self.calculaH(nodo)
            if nodo.funcionG==0:
                nodo.funcionG=valorG
            if nodo.funcionF==0:
                nodo.funcionF=valorG+valorH
            return valorG + valorH
        

    def calculaH(self, nodo):

        # Elijo como heuristica la distancia de Manhattan
        return abs(nodo.coordenadaX - self.nodoFinal.coordenadaX) + abs(nodo.coordenadaY - self.nodoFinal.coordenadaY)
    

    #Creamos un metodo que me permita calcular el valor F minimo de los vecinos de un nodo que le pase como parametro
    #Este metodo me retornara el nodo con el valor F minimo
    #Creamos una sobrecarga de metodo para cuando este metodo se aplica para extender nodos hijos
    #Esto es porque, como esta hecha nuestra implementacion, cuando expandimos el nodo padre para chequear que los nodos hijos no tengan un F menor que el Fmin de los nodos hermanos del nodo padre,
    #no metemos el nodos padre en la lista camino, por lo que la funcion G de los nodos hijos no se calcula correctamente
    def calculaFmin(self, nodo, activador=None,numero=1):
            
        #Creamos una lista de valores F de los vecinos del nodo
        listaF=[]
        for vecino in nodo.vecinos:
            # Si el vecino no fue visitado, proseguimos, si ya fue visitado lo ignoramos
            #Ademas establecemos la condicion de que lo ignore si es un nodo obstaculo (caja)
            #Para ello verificamos si el vecino es una instancia de la clase NodoCamino, ya que si es una instancia de la clase NodoCaja, no es un nodo camino
            if (vecino.estado == False) and (type(vecino) is NodoCamino):
                if activador != None:
                    listaF.append(self.calculaF(vecino,activador,numero))
                else:

                    if vecino.vengoDe==None:
                        vecino.vengoDe=nodo
    
                    listaF.append(self.calculaF(vecino))
            else:
                listaF.append(1000) #Si el vecino ya fue visitado, le asignamos un valor F muy alto para que no sea elegido
        
        #Buscamos el valor minimo de la lista
        valorMinimoF=min(listaF)
        indiceMinimo=listaF.index(valorMinimoF)
                
        return nodo.vecinos[indiceMinimo], valorMinimoF
            
            

    

    # Creamos un metodo que me indique en que direccion se desplazo el algoritmo y lo coloque en la hoja de ruta

    def ruta(self):

        for i,nodo in enumerate(self.camino):

            if (i==0):

                variacionX = self.camino[1].coordenadaX-nodo.coordenadaX
                variacionY = self.camino[1].coordenadaY-nodo.coordenadaY

            else:
                variacionX = self.camino[i].coordenadaX-self.camino[i-1].coordenadaX
                variacionY = self.camino[i].coordenadaY-self.camino[i-1].coordenadaY

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
            self.coordenadasX.append(nodo.coordenadaX)
            self.coordenadasY.append(nodo.coordenadaY)

    
    #Creamos un metodo para plotear el camino realizado por el algoritmo
    def plotear(self):
        #Creamos una lista de colores
        colores = ['red','blue','green','yellow','orange','purple','pink','brown','olive','cyan']
        colores.extend(colores)
        plt.figure("Roadmap",figsize=(10,10))
        plt.xlabel("Coordenada X")
        plt.ylabel("Coordenada Y")
        plt.plot(self.coordenadasX, self.coordenadasY,linewidth=10.0,color=colores[self.contadorColores])
        self.contadorColores+=1
        #Tambien vamos a plotear los nodos prohibidos en color negro con un grosor grande y rectangulos
        for nodo in self.arbol.nodos:
            if type(nodo) is NodoCaja:
                plt.plot(nodo.coordenadaX, nodo.coordenadaY, marker='s', markersize=25, markerfacecolor='gray', markeredgecolor='black')
                #Asignacion del numero de nodo a cada caja
                plt.text(nodo.coordenadaX, nodo.coordenadaY, str(nodo.id), color='white', fontsize=10, ha='center', va='center')
            if type(nodo) is NodoCamino:
                plt.text(nodo.coordenadaX, nodo.coordenadaY, str(f"{nodo.funcionG},{nodo.funcionF}"), color='white', fontsize=8, ha='center', va='center')
        
