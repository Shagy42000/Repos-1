# Búsqueda en Arreglo Multidimensional
def buscar_valor_en_matriz(matriz, valor_a_buscar):
    """
    Busca un valor específico en una matriz bidimensional y devuelve la posición si se encuentra.

    :param matriz: Lista de listas que representa una matriz bidimensional.
    :param valor_a_buscar: El valor numérico que se desea buscar en la matriz.
    :return: Una tupla con la posición (fila, columna) si se encuentra, o None si no se encuentra.
    """
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor == valor_a_buscar:
                return i, j
    return None

# Matriz 3x3
matriz = [
    [6, 5, 6],
    [7, 8, 9],
    [5, 2, 3]
]

# Valor a buscar en la matriz
valor = 8

# Buscar el valor en la matriz
resultado = buscar_valor_en_matriz(matriz, valor)

if resultado:
    print(f"Valor {valor} encontrado en la posición: fila {resultado[0]}, columna {resultado[1]}")
else:
    print(f"Valor {valor} no encontrado en la matriz.")
# Función buscar_valor_en_matriz: Toma una matriz y un valor como parámetros. Utiliza un bucle doble para recorrer la matriz. Si encuentra el valor, devuelve su posición (fila, columna); de lo contrario, devuelve None.

# Matriz de Ejemplo: Una matriz de 3x3 se utiliza para la búsqueda.

# Salida del Programa: Imprime la posición del valor encontrado o un mensaje de que no se encontró.


# Ordenación de Arreglo Multidimensional

def bubble_sort_fila(fila):
    """
    Ordena una lista utilizando el algoritmo Bubble Sort.

    :param fila: Lista de números que se desea ordenar.
    :return: La lista ordenada en orden ascendente.
    """
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    return fila

# Matriz 3x3 de ejemplo
matriz = [
    [4, 5, 6],
    [7, 8, 9],
    [1, 2, 3]
]

# Fila a ordenar (por ejemplo, la fila en el índice 1)
fila_a_ordenar = 1

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la fila específica
matriz[fila_a_ordenar] = bubble_sort_fila(matriz[fila_a_ordenar])

# Mostrar la matriz después de ordenar la fila
print("\nMatriz después de ordenar la fila:")
for fila in matriz:
    print(fila)
# Función bubble_sort_fila: Implementa el algoritmo Bubble Sort para ordenar una lista de números en orden ascendente.

# Matriz de Ejemplo: Una matriz de 3x3 se utiliza para demostrar la funcionalidad de ordenación.

# Fila a Ordenar: Se especifica la fila de la matriz que se desea ordenar.

# Salida del Programa: Muestra la matriz original y la matriz después de ordenar la fila seleccionada.

