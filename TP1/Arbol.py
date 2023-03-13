class Arbol:

    #Creamos el constructor del objeto Arbol, el cual sera la clase agregada, mientras que los objetos nodos son objetos componentes de dicha composicion
    #Vamos a crear el arbol a partir del nodo Raiz
    def __init__(self, nodoRaiz):
        self.nodoRaiz = nodoRaiz
        self.nodosVisitados = [nodoRaiz]
        self.nodosNoVisitados = []

    #Ahora creamos el metodo para crear el arbol a partir de nodo raiz
    '''
    Para ello vamos a utilizar el algoritmo de busqueda en anchura, para ir creando el arbol al instanciar los distintos objetos nodos,
    los cuales determinaran el espacio de busqueda donde luego aplicaremos nuestro algortimo A*
    '''
    def crearArbol(self, nodoRaiz):
