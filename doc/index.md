Primera etapa - Tarea programada 1

Adrián Arias Vargas - C30749
Jimena Bejarano Sánchez - C31074

----- Descripciones -----

1. Modelo Diccionario: 
-Consiste básicamente en una estructura donde se van a guardar datos que van a ser identificados por una clave, en este caso strings de máximo 20 letras minúsculas. 
-Cuenta con funciones como: Init (inicializar), Insert (insertar un elemento), Delete (borrar uno), Member (ver si existe), Clear (vaciar todo), Print (imprimir el contenido) y Done (terminar). 
-El costo y forma de las opreaciones van a variar dependiendo de la estructura que se use dentro de este.

2. Lista ordenada:
-Lista que siempre va a mantener todos los elementos en cierto orden, cada vez que se le agrega un elemento se le busca su respectivo lugar respetando el orden. Se puede trabajar por arreglo o por punteros (estática y dinámica).
-Va a tener funciones como : insertar, borrar, buscar, imprimir y limpiar. 
-En general todas estas operaciones van a tardar O(n) en el peor de los casos porque habría que recorrer toda la lista, lo bueno es que siempre está ordenada entonces solo sería un poco lento cuando tenga demasiados datos.

3. Lista ordenadoa por punteros:
-Esta versión de la lista usa nodos enlazados los cuales contienen el dato y un puntero al siguiente. 
-Su tamaño no es fijo, puede seguir creciendo de manera dinámica.
-A la hora de insertar elementos solo se reajustan los punteros, como colar a alguien en una fila.
-Al igual que borrar, solo se reajustan los punteros y el elemento queda fuera de la lista.
-La mayoría de las operaciones tienen un costo de O(n), pero es fácil de manejar y no se desperdicia espacio como con arreglos.

4. Lista ordenada por arreglos:
-En esta versión de la lista se usa un arreglo con un tamaño máximo y los elementos se guardan contiguos 
y ordenados.
-Si hay que insertar algo nuevo, se corren los elementos de lugar  para abrir el espacio, al igual que cuando se borra, hay que correr los demás hacia la izquierda.
-Es más rápida para acceder a posiciones, pero menos flexible porque el tamaño está fijo. 
-Si tenemos muchos datos la inserción y eliminación de elementos puede ser pesada.

5. Tabla Hash: 
-Esta estructura va a convertir las claves en posiciones dentro de una tabla, permitiendop buscar o borrar en tiempo promedio constante.
-Se le debe encontrar el truco para hashear de manera que los elementos se repartan bien y esta sea funcional.

6. Tabla Hash abierta:
-En esta versión abierta, cada posición de la tabla tiene una lista con todos los elementos 
que entran ahí. Si dos claves tienen el mismo hash, se guardan en esa lista, lo cual sería una colisión que se maneja con listas enlaxzadas.
-Insertar, borrar y buscar son operaciones rápidas O(1) en promedio, pero en el peor caso si hay muchas colisiones puede tardar O(n).

7. Hash y aleatoriedad:
-La función hash va a convertir la hilera en un número. Una forma simple que funciona bien es multiplicar por un número primo y usar el valor ASCII de cada letra y así se obtiene un número que se usa como índice de la tabla.

8. Redistribución/rehash:
-Cuando la tabla hash se llena, se va a crear una tabla más grande y se vuelven a meter todos los elementos.
-Puede tardar O(n) pero solo pasa de vez en cuando y ayuda a que la tabla no sea tan lenta.


*Básicamente, el modelo diccionario se puede implementar con varias distintas estructuras, algunas con puntos más fuertes o ébiles que otras. 
*En esta primera etapa se implementan la lista ordenada dinámica, la lista ordenada estática y la tabla hash abierta.


----- Segunda etapa------


1. ABB Genérico

En el arbol de búsqueda binaria cada nodo tiene como máximo dos hijos: izquierdo y derecho. En el hijo izquierdo van a estar los menores y ewn el hijo derecho van a estar los mayores o iguales.
Esta estructurab permite buscar, insertar o borrar elementos de forma más rápida que una lista, porque n9o necesitamos revisar todos los elementos, sino que podemos ir  descendiendo por el árbol siguiendo la regla de menor/mayor.

2. ABB por punteros

En esta implementación, cada nodo del árbol tiene un puntero al hijo izquierdo y otro al hijo derecho. Se usan referencias. Este va a ser más flexible porque podemos crecer el árbol dinámicamente sin preocuparnos del tamaño, pero cada nodo ocupa memoria extra para los punteros.
La clase NodoABB define un nodo con elemento, izq y der.
La clase AbbPunteros controla la raíz, inserción, borrado y búsqueda recursivamente.

3. ABB por vector

En esta implementación, el ABB se guarda en un vector o arreglo, donde cada posición representa un nodo. Cuando se inserta o borra, se mueven elementos según su relación. El vector crece dinámicamente si se necesita más espacio. Entres sus ventajas, se ocupa menos memoria por nodo porque no hay punteros y sus desventajas, si el árbol está muy desbalanceado, se desperdicia mucho espacio en el vector.

4. Trie genérico

Este es un árbol especial para almacenar cadenas de caracteres. Cada nodo representa una letra, y el camino desde la raíz hasta un nodo marcado como el último forma una palabra válida. Este es muy eficiente para buscar palabras o prefijos, pero puede usar más memoria que otros árboles porque cada nodo tiene muchos hijos posibles, uno por letra.

5. Trie por punteros

En esta versión del trie, cada nodo tiene un arreglo de punteros a sus hijos y un booleano que indica si el nodo marca el fin de una palabra.
Se crea un nodo raíz vacío y se insertan palabras letra por letra. Para buscar se siguen los punteros según las letras de la palabra.

6. Trie por arreglos

En este se usan arreglos de enteros para indicar las posiciones de los hijos en una lista de nodos, en vez de punteros. Cada nodo va a ser un arreglo de 26 posiciones, con -1 si no hay hijo.
Para insertar, se buscan o crean los nodos necesarios.
Para borrar, simplemente se marca que ya no es final de palabra.

*Nota: agregué el main.py solemente para poder coprrerlo de manera más sencilla con el - python -m tarea1

-------- Tercera etapa ----------
En esta entrega lo que se hace es la comparación del rendimiento de las distintas versiones del modelo Diccionario 

Nuestro objetivo es medir cuánto tarda cada operación básica (Init, Insert, member, Delete, print, Done) en las distintas estructuras: 
- Lista ordenada por arreglos o punteros 
- Árbol Binario de Búsqueda (ABB)
- Trie 
- tabla Hash
Y comparar sus tiempos de ejecución con distintos tamaños 

-- Código --
1. Librerias importadas 
random: para generar las palabras aleatorias
time: para medir cuánto tarda cada operación 
pandas: para organizar los resultados en una tabla 
matplotlib: para graficar los resultados 

2. generar_palabras()
Crea hileras (palabras) que se usarán como claves a insertar en los diccionarios

3. medir_tiempo 
calcula tiempo en milisegundos para cada una de las pruebas 

4. Se ejecutan las pruebas en diferentes estructuras y tamaños, para cada una: se crea el diccionario, se insertan palabras, busca con Member, borra conDelete, imprime con Print, termina con Done y guarda el tiempo promedio de vcada operación 

5. Resultados 
Se genera un archivo CSV con los tiempos promedio por operación y estructura 

6. Gráficos de comparación
Para cada una de las operaciones se hace un gráfico de lineas mostrando la diferencia de los tiempos dependiendo del tamaño de la prueba y la estructura de esta 

