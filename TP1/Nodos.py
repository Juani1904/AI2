class NodoCamino:

    # Creamos el constructor del objeto nodo
    def __init__(self, coordenadaX, coordenadaY, estado):

        self.coordenadaX = coordenadaX
        self.coordenadaY = coordenadaY
        self.vecinos = []
        # Si esta True es porque fue visitado, si es False es porque aun no fue visitado
        self.estado = estado
        self.funcionF = 0
        self.funcionG = 0
        self.vengoDe = None

    # Creamos metodo para obtener la distancia del manhattan
    def distanciaManhattan(self, nodoFinal):

        return abs(self.coordenadaX - nodoFinal.coordenadaX) + abs(self.coordenadaY - nodoFinal.coordenadaY)
    
    
    
    




#Ahora vamos a crear una clase heredada de Nodo, la cual tendra aparte de los atributos del Nodo un numero de id para identificar de que caja se trata

class NodoCaja(NodoCamino):

    #Creamos el constructor de la clase

    def __init__(self, coordenadaX, coordenadaY, id):

        #Llamamos al constructor de la clase padre

        super().__init__(coordenadaX, coordenadaY, False)

        #Asignamos valor al id
        
        self.id = id    
    





