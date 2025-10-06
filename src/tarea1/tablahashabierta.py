from tarea1.diccionario import Diccionario

class TablaHashAbierta(Diccionario):
    def __init__(self, tamaño_inicial=11):
        self.__tamaño = tamaño_inicial #se crea la tabla de listas vacías
        self.__tabla = [[] for _ in range(self.__tamaño)]
        self.__cantidad = 0

    def __hash_func(self, clave: str) -> int:
        """Función hash simple tipo multiplicativa"""
        h = 0
        for c in clave:
            h = (h * 31 + ord(c)) % self.__tamaño
        return h

    def __factor_carga(self) -> float:
        return self.__cantidad / self.__tamaño

    def __rehash(self):
        """Duplica el tamaño de la tabla y reubica los elementos"""
        vieja_tabla = self.__tabla
        self.__tamaño = self.__tamaño * 2 + 1 
        self.__tabla = [[] for _ in range(self.__tamaño)]
        self.__cantidad = 0
        for lista in vieja_tabla:
            for elemento in lista:
                self.inserte(elemento)

    def inserte(self, elemento: str):
        """Inserta un elemento en la tabla"""
        indice = self.__hash_func(elemento)
        lista = self.__tabla[indice]

        if elemento not in lista: # si no está, se inserta, aunque el modelo permite duplicados
            lista.append(elemento)
            self.__cantidad += 1

        if self.__factor_carga() > 0.75: #se verifica si hay que hacer rehash al 75%
            self.__rehash()

    def borre(self, elemento: str) -> bool:
        """Elimina un elemento si existe"""
        indice = self.__hash_func(elemento)
        lista = self.__tabla[indice]
        if elemento in lista:
            lista.remove(elemento)
            self.__cantidad -= 1
            return True
        return False

    def miembro(self, elemento: str) -> bool:
        """Verifica si un elemento está en la tabla"""
        indice = self.__hash_func(elemento)
        lista = self.__tabla[indice]
        return elemento in lista

    def limpie(self):
        """Vacía completamente la tabla"""
        self.__tabla = [[] for _ in range(self.__tamaño)]
        self.__cantidad = 0

    def imprima(self):
        print(self)

    def __str__(self):
        salida = []
        for i, lista in enumerate(self.__tabla):
            if lista:
                salida.append(f"{i}: {', '.join(lista)}")
        if not salida:
            return "[Tabla vacía]"
        return "\n".join(salida)

    def __del__(self):
        self.limpie()