class Nodo:

    #Creamos el constructor del objeto nodo
    def __init__(self, coordenadaX, coordenadaY, vecinos, estado, funcionG):

        self.coordenadaX = coordenadaX
        self.coordenadaY = coordenadaY
        self.vecinos = vecinos
        self.estado = estado
        self.funcionG = funcionG

    #Creamos metodo para obtener la distancia del manhattan
    def distanciaManhattan(self, nodoFinal):
            
        return abs(self.coordenadaX - nodoFinal.coordenadaX) + abs(self.coordenadaY - nodoFinal.coordenadaY)