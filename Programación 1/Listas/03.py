'''Crear un programa que combine dos listas en un recorrido sucesivo de sus
índices en una tercera. Si las listas tienen diferentes longitudes, se debe
notificar en pantalla que el proceso no se puede realizar. Ejemplo:
Lista1 = [“Hola”,”nombre”,”juan”]
Lista2 = [“mi”,”es”,”Perez”]
Resultado esperado=[“Hola”,”mi”,”nombre”,”es”,”juan”,”perez”]
'''

def intercalar_listas(lista_1,lista_2):
    lista_nueva = []
    indice = 0
    if len(lista_1) != len(lista_2):
        print("Las listas tienen distinta longitud, no se puede realizar.")
    else:
        while indice < len(lista_1) and len(lista_2):
            lista_nueva.append(lista_1[indice])
            lista_nueva.append(lista_2[indice])
            indice += 1
        return lista_nueva
    

#Programa principal
lista1 = ["Hola", "nombre ", " Juan"]
          
lista2 = [" mi ", " es ", " Perez"]

lista_nueva = intercalar_listas(lista1,lista2)
print(lista_nueva)