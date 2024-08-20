''' Modifique el ejercicio anterior para que, en caso de que una de las listas
tenga más elementos que la otra, se sumen dichos elementos al final de la
nueva lista.'''


def intercalar_listas(lista_1,lista_2):
    lista_nueva = []
    lista_mayor = []
    lista_menor = []

  

    if len(lista1) >= len(lista2):
        lista_mayor = lista_1
        lista_menor = lista_2
    else:
        lista_mayor = lista_2
        lista_menor = lista_1

    for i in range(len(lista_mayor)):
        if i < len(lista_mayor)  and i < len(lista_menor) :
            lista_nueva.append(lista_1[i])
            lista_nueva.append(lista_2[i])
        elif i >= len(lista_menor):
            lista_nueva.append(lista_mayor[i])
    return lista_nueva

    
    
    

#Programa principal
lista1 = ["Hola", "nombre ", " Juan", " y ", " programo"]
          
lista2 = [" mi ", " es ", " Perez"]

lista_nueva = intercalar_listas(lista2,lista1)
print(lista_nueva)