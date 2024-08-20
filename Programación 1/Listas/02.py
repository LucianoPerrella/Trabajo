'''Crear un programa que intercambie el primer y último elemento de una lista
precargada
'''

def intercambiar_primer_y_ultimo_valor(lista):
    
    aux = lista[0]
    lista[0] = lista[-1]
    lista[-1] = aux

    return lista

# Programa principal

lista = [1,2,3,4,5,6]

lista_nueva = intercambiar_primer_y_ultimo_valor(lista)

print(lista_nueva)