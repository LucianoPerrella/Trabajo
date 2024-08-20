'''Crear una función que tome una matriz numérica y devuelva una nueva
matriz donde cada elemento se eleve al cuadrado'''

def elevar_elementos_al_cuadrado(matriz):
    nueva_matriz = []

    for fila in range(len(matriz)):
        nueva_matriz.append([])
        for columna in range(len(matriz[fila])):
            nueva_matriz[fila].append(0)

    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            nueva_matriz[fila][columna] = matriz[fila][columna] ** 2

    return nueva_matriz

#Programa

lista = [[1,2,3], [4,5,6], [7,8,9]]
lista_elevada = elevar_elementos_al_cuadrado(lista)
print(lista)
print("-----")
print(lista_elevada)