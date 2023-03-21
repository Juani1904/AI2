from Arbol import Arbol
from Estanterias import Estanteria
from TempleSimulado import TempleSimulado

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
#Utilizamos esta funcion lambda para obtener los nodos de las esquinas del espacio de busqueda
#Utilizamos la funcion next ya que la funcion nos devuelve una lista de 1 elemento y yo solo quiero el elemento
indicaPosicion = lambda coordX, coordY: next((elemento for elemento in arbol.nodos if (elemento.coordenadaX == coordX and elemento.coordenadaY == coordY)), None)
if camionEstacionamiento == 1:
    nodoEstacionamiento = indicaPosicion(0,0)
elif camionEstacionamiento == 2:
    nodoEstacionamiento = indicaPosicion(columnas,0)
elif camionEstacionamiento == 3:
    nodoEstacionamiento = indicaPosicion(0,filas)
elif camionEstacionamiento == 4:
    nodoEstacionamiento = arbol.nodos[-1]

# Ingreso de lista de productos
print(f"En el espacio generado existen {Estanteria.cantidad} ESTANTERIAS")
cantidadCajas= lambda estanterias: sum([len(estanteria.cajas) for estanteria in estanterias])
listaProductos=[]
while True:
    inicio=int(input(f"Ingrese el ID del producto del 1 al {cantidadCajas(arbol.estanteria)} a cargar en el camion. Al finalizar escriba 0: "))
    if inicio==0:
        break
    else:
        listaProductos.append(arbol.idACoordenada(inicio))


#Finalmente le pasamos los parametros al objeto algoritmo TempleSimulado
numeroIteraciones=int(input("Ingrese numero de iteraciones: "))
temperaturaInicial=int(input("Ingrese temperatura inicial: "))

templeSimulado=TempleSimulado(arbol,nodoEstacionamiento, listaProductos,temperaturaInicial,numeroIteraciones)






