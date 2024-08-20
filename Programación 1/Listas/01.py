'''. Crear un programa que solicite al usuario ingresar un número y busque la
cantidad de ocurrencias que existen sobre una lista ya cargada.
'''

def obetener_cantidad_ocurrencias(lista):
    n = int(input("Ingrese el número del que desea conocer la cantidad de veces que se repite en la lista: "))
    ocurrencias = 0
    for num in lista:
        if num == n:
            ocurrencias += 1
    return ocurrencias


# Programa principal

lista = [1,4,5,6,2,4,1,2,5,6,7,4]
ocurrencias = obetener_cantidad_ocurrencias(lista)

if ocurrencias == 0:
    print("El número no se encuentra en la lista")
else:
    print(f"El número se encuentra {ocurrencias} de veces")