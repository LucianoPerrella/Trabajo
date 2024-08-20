'''Escribe una función que tome una matriz de números y devuelva el valor
máximo encontrado en ella'''

def encontrar_num_mayor(matriz):
    num_mayor = 0

    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] > num_mayor:
                num_mayor = matriz[fila][columna]
    return num_mayor


#Programa principal

lista = [[23,67,100],[200,56],[1000,1111]]
num_mayor = encontrar_num_mayor(lista)
print(lista)
print("-----")
print(num_mayor)