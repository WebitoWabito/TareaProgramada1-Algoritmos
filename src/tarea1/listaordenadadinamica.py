from tarea1.diccionario import Diccionario

class Nodo:
    def __init__(self, elemento:str=''):
        self.elemento = elemento
        self.siguiente: Nodo | None = None

class ListaOrdenadaDinámica(Diccionario):
    def __init__(self):
        self.__cabeza = Nodo()#cabeza vacía
        self.__tamaño = 0

    def __len__(self):
        return self.__tamaño

    def __getitem__(self, indice):
        if indice < 0 or indice >= self.__tamaño:
            raise IndexError("índice fuera de rango.")
        actual = self.__cabeza.siguiente
        for _ in range(indice):
            actual = actual.siguiente
        return actual.elemento

    def inserte(self, elemento):
        anterior = self.__cabeza #se inserta de manera ordenada
        actual = anterior.siguiente
        nuevo = Nodo(elemento)
        while actual is not None and actual.elemento < elemento: #busca la posición correcta para insertarlo
            anterior = actual
            actual = actual.siguiente
        nuevo.siguiente = actual #se inserta el nuevo entre anterior y actual
        anterior.siguiente = nuevo
        self.__tamaño += 1

    def borre(self, elemento):#se busca el nodo a borrar y si existe se borra
        anterior = self.__cabeza
        actual = anterior.siguiente
        while actual is not None and actual.elemento != elemento:
            anterior = actual
            actual = actual.siguiente

        if actual is None:
            return False #no existe
        anterior.siguiente = actual.siguiente
        self.__tamaño -= 1
        return True

    def limpie(self): #vacía la lista
        self.__cabeza.siguiente = None
        self.__tamaño = 0

    def miembro(self, elemento): #verifica que el elemento está
        actual = self.__cabeza.siguiente
        while actual is not None:
            if actual.elemento == elemento:
                return True
            elif actual.elemento > elemento:
                return False #ya pasó el posible lugar
            actual = actual.siguiente
        return False

    def imprima(self):
        print(self)

    def __str__(self) -> str:
        elementos = []
        actual = self.__cabeza.siguiente
        while actual is not None:
            elementos.append(actual.elemento)
            actual = actual.siguiente
        if len(elementos) == 0:
            return "[Lista vacía]"
        return " -> ".join(elementos)

    def __del__(self): #se liberan los nodos
        self.limpie()
