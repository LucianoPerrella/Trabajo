'''Crear una función que retorne una lista que tenga los valores pares que se
encuentren dentro de un rango dado (dicho rango se recibe como parámetro
de la función: desde/hasta)'''

def retornar_valores_pares_entre_limites(desde,hasta):
    '''Esta función recibirá dos parámetros: desde y hasta que funcionan como límites de números. Desde este rango eligirá los valores pares y lo añidara en una lista'''
    lista = []
    for i in range(desde,hasta + 1):
        if i % 2 == 0:
            lista.append(i)
    return lista

'''Crear una función que elimine los elementos de una lista que tenga
determinado valor'''

# def eliminar_valor_de_lista(lista,valor):
#     while valor in lista:
#         lista.remove(valor)
#     return lista


def eliminar_valor_de_lista(lista,valor):
    for num in lista:
        if num == valor:
            lista.remove(num)
    return lista

#Programa principal

# limite_menor = int(input("Ingrese el límite menor: "))
# print("-----")
# limite_mayor = int(input("Ingrese el límite mayor: "))
# while limite_menor >= limite_mayor:
#     print("El límite menor no puede ser mayor")
#     limite_mayor = int(input("Ingrese el límite mayor: "))

# lista_resultado = retornar_valores_pares_entre_limites(limite_menor,limite_mayor)
# print(lista_resultado)

####
lista = [1,2,2,2,3,3,3,4,4,4,4,5]
print(lista)
num_a_eliminar = int(input("Ingre el valor que desea eliminar: "))
lista_corregida = eliminar_valor_de_lista(lista, num_a_eliminar)

print(lista_corregida)
