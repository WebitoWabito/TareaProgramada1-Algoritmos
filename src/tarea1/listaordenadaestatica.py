from tarea1.diccionario import Diccionario

class Array:
    def __init__(self, valor_inicial=None, tamaño=None):
        if not isinstance(tamaño, int) or tamaño < 0:
            raise ValueError("El tamaño debe ser un entero positivo.")
        if not isinstance(valor_inicial, list):
            self.__lista = [valor_inicial] * tamaño
            self.__tamaño = tamaño
        else:
            self.__lista = valor_inicial
            self.__tamaño = len(valor_inicial)        

    def __getitem__(self, índice):
        if not (0 <= índice < self.__tamaño):
            raise IndexError("Índice de arreglo fuera de los límites.")
        return self.__lista[índice]

    def __setitem__(self, índice, value):
        if not (0 <= índice < self.__tamaño):
            raise IndexError("Índice de arreglo fuera de los límites.")
        self.__lista[índice] = value

    def __len__(self):
        return self.__tamaño

    def __repr__(self):
        return f"Array({self.__lista})"

    def __str__(self) -> str:
        return str(self.__lista)

class ListaOrdenadaEstática(Diccionario):
    def __init__(self, tamaño):
        self.__arreglo: Array = Array(valor_inicial=0, tamaño=tamaño)
        self.__último: int | None = None

    def __len__(self):
        if self.__último is None:
            return 0
        else:
            return self.__último + 1
    
    def __getitem__(self, índice):
        if self.__último is None or índice > self.__último:
            raise IndexError("Índice fuera de rango.")
        return self.__arreglo[índice]

    def inserte(self, elemento):
        if self.__último is None: #si la lista está vacía
            self.__arreglo[0] = elemento
            self.__último = 0
            return
        if self.__último + 1 >= len(self.__arreglo):#se revisa si está llena
            print("Error: la lista está llena.")
            return
    
        i = 0 #busca posición para insertar
        while i <= self.__último and self.__arreglo[i] < elemento:
            i += 1

        for j in range(self.__último, i - 1, -1):#se corren los demás elementos para la derecha
            self.__arreglo[j + 1] = self.__arreglo[j]
        self.__arreglo[i] = elemento
        self.__último += 1

    def borre(self, elemento):
        if self.__último is None:
            return False
        i = 0
        while i <= self.__último and self.__arreglo[i] != elemento: #se busca el elemento
            i += 1

        if i > self.__último:
            return False #no está

        for j in range(i, self.__último):#se corren los demás para la izquierda
            self.__arreglo[j] = self.__arreglo[j + 1]

        self.__arreglo[self.__último] = ''
        self.__último -= 1

        if self.__último < 0:
            self.__último = None
        return True

    def limpie(self):
        for i in range(len(self.__arreglo)):
            self.__arreglo[i] = ''
        self.__último = None

    def miembro(self, elemento):
        if self.__último is None:
            return False
        for i in range(self.__último + 1):
            if self.__arreglo[i] == elemento:
                return True
            elif self.__arreglo[i] > elemento:
                return False
        return False

    def imprima(self):
        print(self)

    def __str__(self) -> str:
        if self.__último is None:
            return "[Lista vacía]"
        return " -> ".join(
            [self.__arreglo[i] for i in range(self.__último + 1) if self.__arreglo[i] != '']
        )

    def __del__(self):
        self.limpie()