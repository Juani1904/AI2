from Arbol import Arbol
from Nodos import NodoCamino
from Nodos import NodoCaja
from Aestrella import Aestrella
from nodosException import nodosException
from Estanterias import Estanteria

#Creamos una funcion para referenciar el id de la caja a la coordenada en el camino
def idACoordenada(id):
    #Ahora establecemos la condicion para relacionarlo con la coordenada junto al espacio con el id determinado
    if (id==0):
        return arbol.nodos[0]
    else:
        for estanteria in arbol.estanteria:
            for caja in estanteria.cajas:
                if (caja.id == id) and (id % 2 != 0):
                    coordenadaXReferencia=caja.coordenadaX-1
                    for nodo in arbol.nodos:
                        if nodo.coordenadaX == coordenadaXReferencia and nodo.coordenadaY == caja.coordenadaY:
                            return nodo
                elif (caja.id == id) and (id % 2 == 0):
                    coordenadaXReferencia=caja.coordenadaX+1
                    for nodo in arbol.nodos:
                        if nodo.coordenadaX == coordenadaXReferencia and nodo.coordenadaY == caja.coordenadaY:
                            return nodo





# Creamos el arbol
# Ingreso tamaño del arbol
columnas = int(input("Ingrese numero de columnas del espacio de busqueda: "))
filas = int(input("Ingrese numero de filas del espacio de busqueda: "))
arbol = Arbol(columnas, filas)

# Creamos los nodos inicial y final
#Le preguntamos al usuario si quiere referenciar el inicio y el final con coordenadas o con id de caja en estanteria
print("Ingrese 1 si desea referenciar el inicio y el final con COORDENADAS")
print("Ingrese 2 si desea referenciar el inicio y el final con ID")
opcion = int(input("Opcion(1/2): "))
if (opcion == 1):
    
    # Ingreso por coordenadas
    try:
        coordenadaXinicial = int(input("Ingrese la coordenada X del nodo inicial: "))
        coordenadaYinicial = int(input("Ingrese la coordenada Y del nodo inicial: "))
        coordenadaXfinal = int(input("Ingrese la coordenada X del nodo final: "))
        coordenadaYfinal = int(input("Ingrese la coordenada Y del nodo final: "))
        for nodo in arbol.nodos:
            if nodo.coordenadaX == coordenadaXinicial and nodo.coordenadaY == coordenadaYinicial:
                if isinstance(nodo,NodoCaja) == True:
                    raise nodosException("El nodo inicial ingresado corresponde a una repisa, modifiquelo")
                
            if nodo.coordenadaX == coordenadaXfinal and nodo.coordenadaY == coordenadaYfinal:
                if isinstance(nodo,NodoCaja) == True:
                    raise nodosException("El nodo final ingresado corresponde a una repisa, modifiquelo")
    except nodosException as error:
        print(error)
        exit()

    for nodos in arbol.nodos:
        if nodos.coordenadaX == coordenadaXinicial and nodos.coordenadaY == coordenadaYinicial:
            nodoInicial = nodos
        if nodos.coordenadaX == coordenadaXfinal and nodos.coordenadaY == coordenadaYfinal:
            nodoFinal = nodos

elif (opcion == 2):
    print("Ingrese el id de la caja en estanteria que desea como nodo inicial: ")
    print(f"En el espacio generado existen {Estanteria.cantidad} ESTANTERIAS")
    cantidadCajas= lambda estanterias: sum([len(estanteria.cajas) for estanteria in estanterias])
    inicio=int(input(f"Ingrese un id del espacio de caja INICIAL del 1 al {cantidadCajas(arbol.estanteria)}. Ingrese 0 para area de carga/descarga: "))
    final=int(input(f"Ingrese un id del espacio de caja FINAL del 1 al {cantidadCajas(arbol.estanteria)}. Ingrese 0 para area de carga/descarga: "))

    #Convertimos el id ingresado a coordinada mediante la funcion creada al principio, la cual nos retorna un objeto nodo
    nodoInicial=idACoordenada(inicio)
    nodoFinal=idACoordenada(final)


# Creamos el objeto A*
aestrella = Aestrella(nodoInicial, nodoFinal, arbol)

# Ejecutamos el algoritmo
print(aestrella.buscador())
#Finalmente ploteamos el camino, nodos de busqueda y espacio prohibido
aestrella.plotear()




