import random
import string
import time
import matplotlib.pyplot as plt 
import pandas as pd

# Importaciones corregidas
from .listaordenadadinamica import ListaOrdenadaDinámica
from .abbpunteros import AbbPunteros
from .triepunteros import TriePunteros
from .tablahashabierta import TablaHashAbierta
from .listaordenadaestatica import ListaOrdenadaEstática
from .abbvectorheap import ABBVectorHeap
from .triearreglos import TrieArreglos

def generar_lista_palabras(n: int) -> list[str]:
    """Genera una lista de n palabras aleatorias."""
    palabras = []
    for _ in range(n):
        longitud = random.randint(1, 20)
        palabra = ''.join(random.choices(string.ascii_lowercase, k=longitud))
        palabras.append(palabra)
    return palabras

def medir_tiempo(funcion):
    """Mide el tiempo de ejecución de una función en milisegundos."""
    inicio = time.time()
    funcion()
    fin = time.time()
    return (fin - inicio) * 1000  # Convertir a milisegundos

def main():
    # Tamaños de prueba
    tamanos = [10, 50, 100] #se pueden probar con los parámetros del doc(100, 50mil, 1millón) pero se tarda bastante
    
    # Cantidad de repeticiones por prueba
    repeticiones = 10

    # Listado actualizado de estructuras a probar
    estructuras = [
        ("Lista Ordenada Dinámica", ListaOrdenadaDinámica),
        ("Lista Ordenada Estática", ListaOrdenadaEstática),
        ("ABB Punteros", AbbPunteros),
        ("ABB Vector Heap", ABBVectorHeap),
        ("Trie Punteros", TriePunteros),
        ("Trie Arreglos", TrieArreglos),
        ("Tabla Hash Abierta", TablaHashAbierta)
    ]

    # Resultados de las pruebas
    resultados = []

    for tam in tamanos:
        print(f"\n=== Pruebas con {tam} palabras ===")

        palabras = generar_lista_palabras(tam)

        for nombre, Clase in estructuras:
            tiempos = {}

            for _ in range(repeticiones):
                if nombre == "Lista Ordenada Estática":
                    diccionario = Clase(tam)  # Pasar el tamaño
                else:
                    diccionario = Clase()  # Resto de estructuras sin parámetros
                
                tiempos["Agregar"] = medir_tiempo(lambda: [diccionario.inserte(p) for p in palabras])
                tiempos["Miembro"] = medir_tiempo(lambda: [diccionario.miembro(p) for p in palabras])
                tiempos["Imprimir"] = medir_tiempo(lambda: diccionario.imprima())
                tiempos["Borrar"] = medir_tiempo(lambda: [diccionario.borre(p) for p in palabras])
                tiempos["Limpiar"] = medir_tiempo(lambda: diccionario.limpie())

            # Calcula promedios
            for clave in tiempos:
                tiempos[clave] /= repeticiones

            print(f"\nEstructura: {nombre}")
            for op, t in tiempos.items():
                print(f"{op}: {t:.4f} ms")

            resultados.append({
                "Estructura": nombre,
                "Tamaño": tam,
                **tiempos
            })

    # Crear DataFrame y generar reportes
    df = pd.DataFrame(resultados)
    df.to_csv("resultados_pruebas.csv", index=False)
    print("\nResultados guardados en 'resultados_pruebas.csv'")

    # Generar gráficos para cada operación
    operaciones = ["Agregar", "Miembro", "Borrar", "Imprimir", "Limpiar"]
    for op in operaciones:
        plt.figure(figsize=(10, 6))
        for tam in tamanos:
            subset = df[df["Tamaño"] == tam]
            plt.plot(subset["Estructura"], subset[op], marker="o", label=f"{tam} palabras")
        plt.title(f"Tiempos promedio de {op}")
        plt.xlabel("Estructura de Datos")
        plt.ylabel("Tiempo (ms)")
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f"grafico_{op.lower()}.png")
        plt.close()

    print("\nGráficos generados para cada operación")

if __name__ == "__main__":
    main()