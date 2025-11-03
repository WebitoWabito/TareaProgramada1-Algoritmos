from .diccionario import Diccionario

class NodoTrie:
    def __init__(self):
        self.hijos = [None] * 26  
        self.es_palabra = False

def indice_letra(c):
    return ord(c) - ord('a')

class TriePunteros(Diccionario):
    def __init__(self):
        self.__raiz = NodoTrie()
        self.__cantidad = 0

    def inserte(self, palabra: str): #inserta la palabra en el trie
        nodo = self.__raiz
        for c in palabra:
            i = indice_letra(c)
            if nodo.hijos[i] is None:
                nodo.hijos[i] = NodoTrie()
            nodo = nodo.hijos[i]
        if not nodo.es_palabra:
            nodo.es_palabra = True
            self.__cantidad += 1

    def miembro(self, palabra: str) -> bool: #se verifica si la palabra está en el trie
        nodo = self.__raiz
        for c in palabra:
            i = indice_letra(c)
            if nodo.hijos[i] is None:
                return False
            nodo = nodo.hijos[i]
        return nodo.es_palabra

    def __borrar_rec(self, nodo, palabra, profundidad): #se borra el nodo si es que se encuentra
        if nodo is None:
            return False
        if profundidad == len(palabra):
            if nodo.es_palabra:
                nodo.es_palabra = False
                self.__cantidad -= 1
                return all(h is None for h in nodo.hijos)
            return False
        i = indice_letra(palabra[profundidad])
        borrar_hijo = self.__borrar_rec(nodo.hijos[i], palabra, profundidad + 1)
        if borrar_hijo:
            nodo.hijos[i] = None
            return not nodo.es_palabra and all(h is None for h in nodo.hijos)
        return False

    def borre(self, palabra):
        return self.__borrar_rec(self.__raiz, palabra, 0)

    def limpie(self):
        self.__raiz = NodoTrie()
        self.__cantidad = 0

    def __listar(self, nodo, prefijo, lista):
        if nodo is None:
            return
        if nodo.es_palabra:
            lista.append(prefijo)
        for i in range(26):
            if nodo.hijos[i] is not None:
                self.__listar(nodo.hijos[i], prefijo + chr(i + ord('a')), lista)

    def imprima(self):
        print(self)

    def __str__(self):
        palabras = []
        self.__listar(self.__raiz, "", palabras)
        if not palabras:
            return "[Trie vacío]"
        return " | ".join(palabras)

    def __len__(self):
        return self.__cantidad

    def __del__(self):
        self.limpie()