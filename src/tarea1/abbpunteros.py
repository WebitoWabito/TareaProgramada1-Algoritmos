from .diccionario import Diccionario

class NodoABB:
    def __init__(self, elemento: str):
        self.elemento = elemento
        self.izq: NodoABB | None = None
        self.der: NodoABB | None = None

class AbbPunteros(Diccionario):
    def __init__(self):
        self.__raiz: NodoABB | None = None
        self.__cantidad = 0

    def __insertar_nodo(self, nodo: NodoABB | None, elemento: str) -> NodoABB:
        if nodo is None:  # caso base, se inserta aquí
            self.__cantidad += 1
            return NodoABB(elemento)
        if elemento < nodo.elemento:
            nodo.izq = self.__insertar_nodo(nodo.izq, elemento) # se inserta a la izquierda si es menor
        else:
            nodo.der = self.__insertar_nodo(nodo.der, elemento) # se inserta a la derecha si es igual o mayor
        return nodo

    def __miembro_nodo(self, nodo: NodoABB | None, elemento: str) -> bool:
        if nodo is None:
            return False
        if elemento == nodo.elemento:
            return True
        if elemento < nodo.elemento:
            return self.__miembro_nodo(nodo.izq, elemento)
        else:
            return self.__miembro_nodo(nodo.der, elemento)

    def __minimo_nodo(self, nodo: NodoABB) -> NodoABB:
        current = nodo
        while current.izq is not None:
            current = current.izq
        return current

    def __borrar_nodo(self, nodo: NodoABB | None, elemento: str) -> (NodoABB | None, bool): # devuelve el nodo modificado y si se borró algo
        if nodo is None:
            return None, False
        if elemento < nodo.elemento:
            nodo.izq, borrado = self.__borrar_nodo(nodo.izq, elemento)
            return nodo, borrado
        elif elemento > nodo.elemento:
            nodo.der, borrado = self.__borrar_nodo(nodo.der, elemento)
            return nodo, borrado
        else:
            if nodo.izq is None and nodo.der is None:#
                return None, True
            if nodo.izq is None:
                return nodo.der, True
            if nodo.der is None:
                return nodo.izq, True
            sucesor = self.__minimo_nodo(nodo.der)
            nodo.elemento = sucesor.elemento
            nodo.der, _ = self.__borrar_nodo(nodo.der, sucesor.elemento)
            return nodo, True

    def __recorrer_inorden(self, nodo: NodoABB | None, resultado: list):
        if nodo is None:
            return
        self.__recorrer_inorden(nodo.izq, resultado)
        resultado.append(nodo.elemento)
        self.__recorrer_inorden(nodo.der, resultado)
        
    def inserte(self, elemento: str):
        """Inserta elemento en el ABB."""
        if not isinstance(elemento, str):
            raise ValueError("Elemento debe ser string")
        self.__raiz = self.__insertar_nodo(self.__raiz, elemento)

    def borre(self, elemento: str) -> bool:
        """Borra elemento si existe. Devuelve True si borró, False si no existía."""
        self.__raiz, borrado = self.__borrar_nodo(self.__raiz, elemento)
        if borrado:
            self.__cantidad -= 1
        return borrado

    def limpie(self):
        """Limpia todo el árbol."""
        self.__raiz = None
        self.__cantidad = 0

    def miembro(self, elemento: str) -> bool:
        return self.__miembro_nodo(self.__raiz, elemento)

    def imprima(self):
        print(self)

    def __str__(self) -> str:
        if self.__raiz is None:
            return "[ABB vacío]"
        elems: list[str] = []
        self.__recorrer_inorden(self.__raiz, elems)
        return " | ".join(elems)

    def __len__(self):
        return self.__cantidad

    def __del__(self):
        self.limpie()