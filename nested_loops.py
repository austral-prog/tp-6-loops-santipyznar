# Replace the "ANSWER HERE" for your answer

def flatten(matrix):
    """
    Dada una lista de listas (matriz), retorna una unica lista
    con todos los elementos en orden.

    Ejemplo: flatten([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    """
    resultado = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            resultado.append(matrix[i][j])

    return resultado


def row_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la fila correspondiente.

    Ejemplo: row_sums([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
    """
    resultado = []
   
    for i in range(len(matrix)):
        suma = 0
        for j in range(len(matrix[i])):
            suma += matrix[i][j]
        resultado.append(suma)
    return resultado

def col_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la columna correspondiente.
    Se asume que todas las filas tienen la misma longitud.

    Ejemplo: col_sums([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
    """
    resultado = []

    filas = len(matrix)
    columnas = len(matrix[0])

    for j in range(columnas):
        suma = 0
        for i in range(filas):
            suma += matrix[i][j]
        resultado.append(suma)
    return resultado