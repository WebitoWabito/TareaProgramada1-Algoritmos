Primera etapa - Tarea programada 1

Adrián Arias Vargas - C30749
Jimena Bejarano Sánchez - C31074

-----Descripciones-----

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



