import random
import time
import matplotlib.pyplot as plt
import pandas as pd

# Importa implementaciones de las estructuras de datos
from diccionario_lista import DiccionarioLista
from diccionario_abb import DiccionarioABB
from diccionario_trie import DiccionarioTrie
from diccionario_hash import DiccionarioHash


# Genera palabra aleatoria de 5 letras
def generar_palabra():
    letras = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(random.choice(letras) for _ in range(5))


# Genera lista de palabras aleatorias
def generar_lista_palabras(cantidad):
    return [generar_palabra() for _ in range(cantidad)]


# Se mide el tiempo que tarda en ejecutar una operación
def medir_tiempo(funcion):
    inicio = time.perf_counter()
    funcion()
    fin = time.perf_counter()
    return (fin - inicio) * 1000  # se devuelve en milisegundos


def main():
    # tam de prueba
    tamanos = [10, 100, 10000]

    # cantidad de repeticiones por prueba
    repeticiones = 10

    # Listado de estructuras a probar
    estructuras = [
        ("Lista Ordenada", DiccionarioLista),
        ("Árbol Binario", DiccionarioABB),
        ("Trie", DiccionarioTrie),
        ("Tabla Hash", DiccionarioHash)
    ]

    # Resultados de las pruebas
    resultados = [] 

    for tam in tamanos:
        print(f"\n=== Pruebas con {tam} palabras ===")

        # Se generan palabras aleatorias para esta ronda de pruebas 
        palabras = generar_lista_palabras(tam)

        for nombre, Clase in estructuras:
            # Mediciones de tiempo para cada operación
            tiempos = {"Init": 0, "Insert": 0, "Member": 0, "Delete": 0, "Print": 0, "Done": 0}

            # Se repiten las pruebas para promediar los tiempos
            for _ in range(repeticiones):
                diccionario = Clase()

                # Tiempo de Init
                tiempos["Init"] += medir_tiempo(lambda: diccionario.Init())

                # Tiempo de Insert
                tiempos["Insert"] += medir_tiempo(lambda: [diccionario.Insert(p) for p in palabras])

                # Tiempo de Member
                tiempos["Member"] += medir_tiempo(lambda: [diccionario.Member(p) for p in palabras])

                # Tiempo de Delete
                tiempos["Delete"] += medir_tiempo(lambda: [diccionario.Delete(p) for p in palabras])

                # Tiempo de Print
                tiempos["Print"] += medir_tiempo(lambda: diccionario.Print())

                # Tiempo de Done
                tiempos["Done"] += medir_tiempo(lambda: diccionario.Done())

            # Se calcula el promedio dividiendo entre el número de repeticiones
            for clave in tiempos:
                tiempos[clave] /= repeticiones

            # Se muestran los resultados en consola
            print(f"\nEstructura: {nombre}")
            for op, t in tiempos.items():
                print(f"{op}: {t:.4f} ms")

            # Se almacenan los res para un analisis que se hara luego
            resultados.append({
                "Estructura": nombre,
                "Tamaño": tam,
                **tiempos
            })

    # se crea un cuadro de pandas con los resultados para facilitar el analisis de datos
    df = pd.DataFrame(resultados)
    print("\n=== Resultados generales ===")
    print(df)

    # se guardan los resultados en un archivo CSV
    df.to_csv("resultadosPruebas.csv", index=False)
    print("\nLos resultados se guardaron en 'resultadosPruebas.csv'.")

    # Se generan graficos para cada operacion
    operaciones = ["Init", "Insert", "Member", "Delete", "Print", "Done"]
    for op in operaciones:
        plt.figure()
        for tam in tamanos:
            subset = df[df["Tamaño"] == tam]
            plt.plot(subset["Estructura"], subset[op], marker="o", label=f"{tam} palabras")
        plt.title(f"Tiempos promedio de {op}")
        plt.xlabel("Estructura de Datos")
        plt.ylabel("Tiempo (ms)")
        plt.legend()
        plt.tight_layout()
        plt.savefig(f"grafico_{op.lower()}.png")
        plt.close()

    print("\nGráficos generados y guardados como 'grafico_init.png', 'grafico_insert.png', etc.")


if __name__ == "__main__":
    main()
