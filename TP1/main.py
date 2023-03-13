from Arbol import Arbol
from Nodos import Nodo
from Aestrella import Aestrella

#Creamos el arbol
#Ingreso tamaño del arbol
columnas=int(input("Ingrese numero de columnas del espacio de busqueda: "))
filas=int(input("Ingrese numero de filas del espacio de busqueda: "))
arbol = Arbol(columnas, filas)

#Creamos los nodos inicial y final
#Ingreso de coordenadas
coordenadaXinicial = int(input("Ingrese la coordenada X del nodo inicial: "))
coordenadaYinicial = int(input("Ingrese la coordenada Y del nodo inicial: "))
coordenadaXfinal = int(input("Ingrese la coordenada X del nodo final: "))
coordenadaYfinal = int(input("Ingrese la coordenada Y del nodo final: "))

for nodos in arbol.nodos:
    if nodos.coordenadaX == coordenadaXinicial and nodos.coordenadaY == coordenadaYinicial:
        nodoInicial = nodos
    if nodos.coordenadaX == coordenadaXfinal and nodos.coordenadaY == coordenadaYfinal:
        nodoFinal = nodos

#Creamos el objeto A*
aestrella = Aestrella(nodoInicial, nodoFinal, arbol)

#Ejecutamos el algoritmo
print(aestrella.buscador())