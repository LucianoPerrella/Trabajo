"""Crear un programa que pida un número al usuario un número de mes y diga cuantos dias tiene, debes usar matriz para la parametrización y una función para el recupero de dato"""

def retornar_cantidad_dias(matriz,mes):
    
    for i in range(len(matriz)):
        if matriz[i][0] == mes:
            cantidad = matriz[i]
            return cantidad
    



año = [[1,31],[2,28],[3,31],[4,30],[5,31],[6,30],[7,31],[8,31], [9,30],[10,31],[11,30],[12,31]]
dias = retornar_cantidad_dias(año, 2)
print(dias)