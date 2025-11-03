from .diccionario import Diccionario

class ABBVectorHeap(Diccionario):
    def __init__(self, tamaño_inicial=15):
        self.__vector = [None] * tamaño_inicial
        self.__cantidad = 0

    def __len__(self):
        return self.__cantidad

    def __asegurar_tamaño(self, índice):
        while índice >= len(self.__vector):
            self.__vector.extend([None] * len(self.__vector))

    def __insertar(self, índice, elemento):
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

    def __encontrar_sucesor(self, índice): #se busca el nodo más a la izquierda en el subárbol derecho
        actual = 2 * índice + 2
        while actual < len(self.__vector) and self.__vector[actual] is not None:
            izq = 2 * actual + 1
            if izq < len(self.__vector) and self.__vector[izq] is not None:
                actual = izq
            else:
                break
        return actual if actual < len(self.__vector) else None

    def __borrar(self, índice, elemento):
        if índice >= len(self.__vector) or self.__vector[índice] is None:
            return False
            
        valor = self.__vector[índice]
        if elemento < valor:
            return self.__borrar(2 * índice + 1, elemento)
        elif elemento > valor:
            return self.__borrar(2 * índice + 2, elemento)
        
        #caso 1: Nodo hoja
        izq = 2 * índice + 1
        der = 2 * índice + 2
        if (izq >= len(self.__vector) or self.__vector[izq] is None) and \
           (der >= len(self.__vector) or self.__vector[der] is None):
            self.__vector[índice] = None
            self.__cantidad -= 1
            return True
            
        #Caso 2: hijo único
        if izq >= len(self.__vector) or self.__vector[izq] is None:
            self.__vector[índice] = self.__vector[der]
            self.__vector[der] = None
            self.__cantidad -= 1
            return True
        if der >= len(self.__vector) or self.__vector[der] is None:
            self.__vector[índice] = self.__vector[izq]
            self.__vector[izq] = None
            self.__cantidad -= 1
            return True
        
        #caso 3: dos hijos
        sucesor_idx = self.__encontrar_sucesor(índice)
        if sucesor_idx:
            self.__vector[índice] = self.__vector[sucesor_idx]
            self.__vector[sucesor_idx] = None
            self.__cantidad -= 1
            return True
        return False

    def borre(self, elemento):
        return self.__borrar(0, elemento)

    def limpie(self):
        self.__vector = [None] * len(self.__vector)
        self.__cantidad = 0

    def imprima(self):
        print(self)

    def __str__(self):
        resultado = []
        self.__inorden(0, resultado)
        if not resultado:
            return "[ABB vector vacío]"
        return " | ".join(resultado)

    def __inorden(self, índice, resultado):
        if índice >= len(self.__vector):
            return
        if self.__vector[índice] is None:
            return
        self.__inorden(2 * índice + 1, resultado)
        resultado.append(self.__vector[índice])
        self.__inorden(2 * índice + 2, resultado)

    def __del__(self):
        self.limpie()