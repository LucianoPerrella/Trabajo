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


# def eliminar_valor_de_lista(lista,valor):
#     for num in lista:
#         if num == valor:
#             lista.remove(num)
#     return lista


''' Crear una función que reciba como parámetro un valor numérico. En caso de
que ese valor recibido como parámetro sea múltiplo de 3, se debe retornar el
resultado de su cubo (para calcular el cubo de dicho valor, utilizar otra
función). De no ser múltiplo de 3, retornar -1
'''

# def calcular_multiplo(n):
#     resultado = n ** 3
#     return resultado

# def verificar_multiplo_de_3(n):
#     if n % 3 != 0:
#         return -1
#     else:
#         resultado = calcular_multiplo(n)
#         return resultado



'''Escriba una función que dada una lista con notas entre 0 y 10, retorne otra
lista indicando su resultado por cada posición, utilizando una función que al
recibir una nota retorne:
0: Ausente, entre 1 y 3 Desaprobado, entre 4 y 6 aprobado, entre 7 y
10 promocionad'''

def evaluar_notas(lista):
    lista_evaluada = []
    for nota in lista:
        if nota < 0 or nota > 10:
            lista_evaluada.append("No se puede evaluar una nota menor a 0 o mayor a 10")
        elif nota < 1:
            lista_evaluada.append("Ausente")
        elif nota >= 1 and nota <= 3:
            lista_evaluada.append("Desaprobado")
        elif nota >= 4 and nota <= 6:
            lista_evaluada.append("Aprobado")
        else:
            lista_evaluada.append("Promoción")
    return lista_evaluada



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
# lista = [1,2,2,2,3,3,3,4,4,4,4,5]
# print(lista)
# num_a_eliminar = int(input("Ingre el valor que desea eliminar: "))
# lista_corregida = eliminar_valor_de_lista(lista, num_a_eliminar)


lista = [10,9,0,2,3,4,7,10, -1, 11, 5, 6]
evaluacion = evaluar_notas(lista)

print(evaluacion)
# numero = int(input("Ingrese un número para verificar si es multiplo de 3 y obtener su cubo: "))
# resultado = verificar_multiplo_de_3(numero)

# if resultado == -1:
#     print("El número no es múltiplo de 3")
# else:
#     print(f"El número {numero} es multiplo de 3 y su cubo es = {resultado} ")
