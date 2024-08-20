import random
'''Escribe una función que tome dos números enteros como argumentos (filas y
columnas) y devuelva una matriz completa con números aleatorios entre 0 y
10.
'''

def construir_matriz(filas,columnas):
    
    matriz = []

    for fila in range(filas):
        matriz.append([])
        for columna in range(columnas):
            matriz[fila].append(random.randint(0,10))

    return matriz

#Programa principal
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))
matriz = construir_matriz(filas,columnas)
print(matriz)