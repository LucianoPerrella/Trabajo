'''Desarrollar cada una de las siguiente funciones y escribir un programa que permita verificar su funcionamiento imrpimiendo la lista luego de invocar a cafa función'''

'''Cargar una lista con números al azar de cuatro dígitos. La ccantidad de elementos también será un número al azar de dos dígitos. Realive la composición de la lista por comprensi+on y de la forma habitual.'''
import random
def crear_lista():
    lista = []
    longitud = random.randint(10,99)
    for i in range(longitud):
        lista.append(random.randint(0,9999))
        
    return lista

def crear_lista_comprension():
    longitud = random.randint(10,99)
    lista = [random.randint(0,9999) for i in range(longitud)]
    return lista

def sumar_elementos(lista):
    lista_suma = sum(lista)
    return lista_suma

def es_capicua(lista):
    es_capicua = False
    lista_invertida = reversed(lista)
    if lista == lista_invertida:
        es_capicua = True
    return es_capicua

lista = [1,2,2,1]
capicua = es_capicua(lista)
if capicua == True:
    print("Es capicua")
else:
    print("No lo es")



# #Programa principal
# lista = crear_lista()
# lista_comprension = crear_lista_comprension()
# sumas = sumar_elementos(lista_comprension)
# print(lista)
# print(lista_comprension)
# print(sumas)