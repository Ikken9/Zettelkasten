# Elementary Operations (Matrix)

In a [[Matrix|matrix]], the following transformations are considered elementary row operations:

1. Swapping two rows with each other. This can be represented as $F_i \leftrightarrow F_j$, where $F_i$ and $F_j$ are two rows of the matrix.
2. Multiplying a row by a non-zero real number. This can be represented as $F_i \rightarrow t \cdot F_i$.
3. Replacing a row by the sum of itself and the product of another row by a real number. This can be represented as $F_i \rightarrow F_i + t \cdot F_j$.

**Definition**: Two matrices are equivalent if one can be obtained from the other through a finite number of elementary operations. If $A$ and $B$ are equivalent, we will denote it as $A \equiv B$.

La **forma escalonada** y la **forma escalonada reducida** son conceptos importantes en álgebra lineal para representar matrices de manera simplificada. Se utilizan para resolver sistemas de ecuaciones lineales, encontrar rangos de matrices y analizar otras propiedades.


## **Forma Escalonada** (o Forma Escalonada de Fila)
Una matriz está en forma escalonada si cumple las siguientes condiciones:

1. **Los ceros a la izquierda:** En cada fila, el primer número no cero (llamado pivote) está a la derecha del primer número no cero de la fila anterior. Esto significa que cada fila comienza con más ceros que la fila anterior.
2. **Filas cero al final:** Todas las filas de ceros completos están en la parte inferior de la matriz.
3. **Pivote distinto de cero:** Los elementos debajo de un pivote (en la misma columna) son todos ceros.

#### Ejemplo
$$
\begin{bmatrix}
1 & 2 & 3 & 4 \\
0 & 1 & -2 & 3 \\
0 & 0 & 1 & 5 \\
0 & 0 & 0 & 0
\end{bmatrix}
$$


Esta matriz está en forma escalonada porque cada fila comienza con más ceros que la anterior y los elementos debajo de los pivotes son ceros.

## **Forma Escalonada Reducida** (o Forma Escalonada de Fila Reducida)
Una matriz está en forma escalonada reducida si, además de cumplir con las condiciones de la forma escalonada, también cumple con estas:

1. **Pivotes como 1:** El primer elemento no cero (pivote) de cada fila es 1.
2. **Ceros en la columna del pivote:** En cada columna que contiene un pivote, todos los demás elementos son cero (tanto arriba como abajo del pivote).

#### Ejemplo
$$
\begin{bmatrix}
1 & 0 & 0 & 2 \\
0 & 1 & 0 & 3 \\
0 & 0 & 1 & 5 \\
0 & 0 & 0 & 0
\end{bmatrix}
$$


Esta matriz está en forma escalonada reducida porque cada pivote es 1 y es el único elemento no cero en su columna.

### **Cómo Calcular la Forma Escalonada y la Forma Escalonada Reducida**

#### Forma Escalonada
1. **Seleccionar un pivote:** Comenzar en la primera fila y la primera columna con el primer elemento no cero como pivote.
2. **Crear ceros debajo del pivote:** Restar múltiplos de la fila con el pivote de las filas de abajo para que todos los elementos debajo del pivote se conviertan en cero.
3. **Repetir en submatrices:** Moverse a la siguiente fila y columna (más a la derecha) y repetir el proceso en la submatriz formada por las filas y columnas restantes.
4. **Ordenar filas cero:** Si hay filas que son completamente ceros, moverlas a la parte inferior de la matriz.

#### Forma Escalonada Reducida
1. **Primero calcular la forma escalonada.**
2. **Convertir pivotes a 1:** Si un pivote no es 1, dividir toda la fila por el valor del pivote.
3. **Crear ceros arriba del pivote:** Restar múltiplos de la fila pivote de las filas de arriba para que todos los elementos en la columna del pivote se conviertan en cero, excepto el propio pivote.
4. **Repetir:** Aplicar este procedimiento para cada fila, asegurándose de que todos los pivotes sean 1 y no haya otros valores no cero en las columnas de los pivotes.

### Ejemplo de Cálculo
Dada la matriz:

$$
\begin{bmatrix}
2 & 4 & -2 \\
4 & 9 & -3 \\
-2 & -3 & 7
\end{bmatrix}
$$

1. **Convertir a forma escalonada:**
    - Usamos la primera fila como referencia y hacemos cero los elementos en las filas 2 y 3 debajo del pivote 2 en la primera columna.

2. **Obtenemos:**
$$
\begin{bmatrix}
2 & 4 & -2 \\
0 & 1 & 1 \\
0 & 1 & 6
\end{bmatrix}
$$

3. **Seguir con la segunda fila:**
    - Usamos el pivote de la segunda fila (1) para hacer cero el elemento 1 en la tercera fila en la columna 2.

4. **Forma Escalonada Final:**

$$
\begin{bmatrix}
2 & 4 & -2 \\
0 & 1 & 1 \\
0 & 0 & 5
\end{bmatrix}
$$

5. **Convertir a forma escalonada reducida:**
    - Hacer que el pivote de la tercera fila sea 1 dividiendo por 5 y luego eliminar todos los elementos arriba del pivote en su columna.

6. **Forma Escalonada Reducida:**

$$
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

En este caso, la matriz es la identidad.


https://youtu.be/kEJ24G1wRZQ

