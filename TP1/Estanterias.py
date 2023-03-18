class Estanteria:

    #Definimos un atributo de clase que servira para contar la cantidad de estanterias que se crean
    cantidad=0

    #Definimos el constructor de la clase
    def __init__(self,idEstanteria):

        self.id=idEstanteria
        self.cajas=[]
        self.cantidad+=1 #Aumentamos en 1 la cantidad de estanterias que se crean
