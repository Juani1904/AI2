from Arbol import Arbol
from Estanterias import Estanteria
from TempleSimulado import TempleSimulado

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

#Posicion del camion. Puede estar en cualquier esquina del espacio de busqueda
print("Ingrese numero de estacionamiento de camion de carga: ")
print("1. Esquina superior izquierda")
print("2. Esquina superior derecha")
print("3. Esquina inferior izquierda")
print("4. Esquina inferior derecha")
camionEstacionamiento = int(input())
if camionEstacionamiento == 1:
    nodoEstacionamiento = arbol.nodos[0]
elif camionEstacionamiento == 2:
    nodoEstacionamiento = arbol.nodos[columnas-1]
elif camionEstacionamiento == 3:
    nodoEstacionamiento = arbol.nodos[(filas-1)*columnas]
elif camionEstacionamiento == 4:
    nodoEstacionamiento = arbol.nodos[(filas*columnas)-1]

# Ingreso de lista de productos
print(f"En el espacio generado existen {Estanteria.cantidad} ESTANTERIAS")
cantidadCajas= lambda estanterias: sum([len(estanteria.cajas) for estanteria in estanterias])
listaProductos=[]
while True:
    inicio=int(input(f"Ingrese el ID del producto del 1 al {cantidadCajas(arbol.estanteria)} a cargar en el camion. Al finalizar escriba 0: "))
    if inicio==0:
        break
    else:
        listaProductos.append(idACoordenada(inicio))


#Finalmente le pasamos los parametros al objeto algoritmo TempleSimulado

templeSimulado=TempleSimulado(nodoEstacionamiento, listaProductos)






