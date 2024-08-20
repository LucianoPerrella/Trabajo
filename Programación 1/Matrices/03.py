'''Desarrollar una función que tome una matriz de números y devuelva la suma
de todos sus elementos'''

def suma_elementos_matriz(matriz):
    suma_total = 0

    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            suma_total += matriz[fila][columna]

    return suma_total

#Programa

matriz = [[1,2,3],[4,5,6]]
suma = suma_elementos_matriz(matriz)

print(matriz)
print("-----")
print(suma)