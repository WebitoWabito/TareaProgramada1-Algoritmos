from .diccionario import Diccionario

class ABBVectorHeap(Diccionario):
    def __init__(self, tamaño_inicial=15):
        self.__vector = [None] * tamaño_inicial
        self.__cantidad = 0

    def __len__(self):
        return self.__cantidad

    def __asegurar_tamaño(self, índice): #aumenta el tamaño del vector si hace falta
        while índice >= len(self.__vector):
            self.__vector.extend([None] * len(self.__vector))

    def __insertar(self, índice, elemento):#inserta elemento si hace falta
        self.__asegurar_tamaño(índice)
        valor = self.__vector[índice]

        if valor is None:
            self.__vector[índice] = elemento
            self.__cantidad += 1
            return

        if elemento < valor:
            self.__insertar(2 * índice + 1, elemento)
        else:
            self.__insertar(2 * índice + 2, elemento)

    def inserte(self, elemento):
        if not isinstance(elemento, str):
            raise ValueError("Solo se permiten cadenas.")
        self.__insertar(0, elemento)

    def __buscar(self, índice, elemento):
        if índice >= len(self.__vector):
            return False
        valor = self.__vector[índice]
        if valor is None:
            return False
        if valor == elemento:
            return True
        if elemento < valor:
            return self.__buscar(2 * índice + 1, elemento)
        else:
            return self.__buscar(2 * índice + 2, elemento)

    def miembro(self, elemento):
        return self.__buscar(0, elemento)

    def __borrar(self, índice, elemento):#borra el elemento si es que se encuentra 
        if índice >= len(self.__vector) or self.__vector[índice] is None:
            return False
        valor = self.__vector[índice]
        if elemento < valor:
            return self.__borrar(2 * índice + 1, elemento)
        elif elemento > valor:
            return self.__borrar(2 * índice + 2, elemento)
        else:
            subarbol = self.__recolectar_subarbol(índice) #borra el nodo y reinserta sus "hijos"
            self.__vector[índice] = None
            self.__cantidad -= 1
            for e in subarbol:
                self.inserte(e)
            return True

    def __recolectar_subarbol(self, índice): # devuelve una lista con los valores
        valores = []
        izq = 2 * índice + 1
        der = 2 * índice + 2
        if izq < len(self.__vector) and self.__vector[izq] is not None:
            valores.append(self.__vector[izq])
            valores += self.__recolectar_subarbol(izq)
        if der < len(self.__vector) and self.__vector[der] is not None:
            valores.append(self.__vector[der])
            valores += self.__recolectar_subarbol(der)
        return valores

    def borre(self, elemento):
        return self.__borrar(0, elemento)

    def limpie(self):
        self.__vector = [None] * len(self.__vector)
        self.__cantidad = 0

    def __inorden(self, índice, resultado):
        if índice >= len(self.__vector):
            return
        if self.__vector[índice] is None:
            return
        self.__inorden(2 * índice + 1, resultado)
        resultado.append(self.__vector[índice])
        self.__inorden(2 * índice + 2, resultado)

    def imprima(self):
        print(self)

    def __str__(self):
        resultado = []
        self.__inorden(0, resultado)
        if not resultado:
            return "[ABB vector vacío]"
        return " | ".join(resultado)

    def __del__(self):
        self.limpie()