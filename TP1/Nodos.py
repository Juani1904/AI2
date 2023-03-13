class Nodo:

    #Creamos el constructor del objeto nodo
    def __init__(self, coordenadaX, coordenadaY, estado):

        self.coordenadaX = coordenadaX
        self.coordenadaY = coordenadaY
        self.vecinos = []
        self.estado = estado #Si esta True es porque fue visitado, si es False es porque aun no fue visitado
        self.funcionF=0

    #Creamos metodo para obtener la distancia del manhattan
    def distanciaManhattan(self, nodoFinal):
            
        return abs(self.coordenadaX - nodoFinal.coordenadaX) + abs(self.coordenadaY - nodoFinal.coordenadaY)
    
    #Creamos un metodo para obtener el costo del camino g
 