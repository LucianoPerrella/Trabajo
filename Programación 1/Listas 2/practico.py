'''Cargar una lista con números al azar de cuatro dígitos. 
a cantidad de elementos también será un número al azar de dos dígitos. 
Realice la composición de la lista por 
comprensión y de la forma habitual (tendrá dos funciones distintas). '''
import random
def lista_por_comprension():
    lista = [random.randint(1000,9999) for i in range(random.randint(10,99))]
    return lista

def lista_tradicional():
    lista = []
    for i in range(random.randint(10,99)):
        num_random = random.randint(1000,9999)
        lista.append(num_random)
    return lista


def sumar_elementos(lista):
    suma = sum(lista)
    return suma
    

def eliminar_valor(lista,valor):
    lista_corregida = [numero for numero in lista if numero != valor]
    return lista_corregida

def determinar_si_es_capicua(lista):
    es_capicua = False
    if lista == lista[::-1]:
       es_capicua = True

    return es_capicua


def main():
    # lista = lista_por_comprension()
    # sumatoria = sumar_elementos(lista)
    # print(len(lista))
    # print(lista)
    # print(sumatoria)

    # valor_a_eliminar = int(input("Ingrese el valor a eliminar: "))
    # lista_sin_valor = eliminar_valor(lista,valor_a_eliminar)
    # print(len(lista_sin_valor))
    # print(lista_sin_valor)

    listita = [1,2,3,4,3,2,1]

    capicua = determinar_si_es_capicua(listita)

    if capicua:
        print("Es capicua")
    else:
        print("No es capicua")
main()