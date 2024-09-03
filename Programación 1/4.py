'''Escribe una función que tome dos números enteros
como argumentos y devuleva una martriz con númreos aleatroios entre 0 y 10'''
import random
def crear_matriz(filas,columnas):
    matriz = []
    for fila in range(filas):
        matriz.append([])
        for columna in range(columnas):
            matriz[fila].append(random.randint(0,10))
            
    return matriz

def main():
    
    filas = int(input("Ingrese la cantidad de filas: "))
    columnas = int(input("Ingrese la cantidad de columnas: "))
    matriz = crear_matriz(filas,columnas)
    print(matriz)
    
    
main()