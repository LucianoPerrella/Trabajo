'''Crear una función que tome una matriz numérica y devuelva una nueva matriz donde cada elemento se eleve al cuadrado'''

def elevar_cuadrado(matriz):
    
    nueva_matriz = []
    
    for fila in range(len(matriz)):
        nueva_matriz.append([])
        for columna in range(len(matriz[fila])):
            nueva_matriz[fila].append(matriz[fila][columna] ** 2)
            
    return nueva_matriz

def main():
    matriz = [[1,2,3,4,5],[2,3,4]]
    elevados_cuadrado = elevar_cuadrado(matriz)
    print(matriz)
    
    print(elevados_cuadrado)
    
main()