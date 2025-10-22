from tarea1.diccionario import Diccionario

class TrieArreglos(Diccionario):
    def __init__(self):
        self.__nodos = [[-1] * 26]
        self.__fin = [False]
        self.__cantidad = 0

    def __nuevo_nodo(self):
        self.__nodos.append([-1] * 26)
        self.__fin.append(False)
        return len(self.__nodos) - 1

    def inserte(self, palabra: str): #inserta la palabra en el trie
        nodo = 0
        for c in palabra:
            i = ord(c) - ord('a')
            if self.__nodos[nodo][i] == -1:
                self.__nodos[nodo][i] = self.__nuevo_nodo()
            nodo = self.__nodos[nodo][i]
        if not self.__fin[nodo]:
            self.__fin[nodo] = True
            self.__cantidad += 1

    def miembro(self, palabra: str) -> bool: #verifica si la palabra está en el trie
        nodo = 0
        for c in palabra:
            i = ord(c) - ord('a')
            if self.__nodos[nodo][i] == -1:
                return False
            nodo = self.__nodos[nodo][i]
        return self.__fin[nodo]

    def borre(self, palabra: str) -> bool: #borra la palabra del trie si es que existe
        nodo = 0
        pila = []
        for c in palabra:
            i = ord(c) - ord('a')
            if self.__nodos[nodo][i] == -1:
                return False
            pila.append((nodo, i))
            nodo = self.__nodos[nodo][i]
        if not self.__fin[nodo]:
            return False
        self.__fin[nodo] = False
        self.__cantidad -= 1
        return True

    def limpie(self):
        self.__nodos = [[-1] * 26]
        self.__fin = [False]
        self.__cantidad = 0

    def __listar(self, nodo, prefijo, lista):
        if self.__fin[nodo]:
            lista.append(prefijo)
        for i in range(26):
            hijo = self.__nodos[nodo][i]
            if hijo != -1:
                self.__listar(hijo, prefijo + chr(i + ord('a')), lista)

    def imprima(self):
        print(self)

    def __str__(self):
        lista = []
        self.__listar(0, "", lista)
        if not lista:
            return "[Trie vacío]"
        return " | ".join(lista)

    def __len__(self):
        return self.__cantidad

    def __del__(self):
        self.limpie()