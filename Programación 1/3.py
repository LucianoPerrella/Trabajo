'''Crear un programa que intercambie el primer y el último elemento de una lista precargada'''

def cambiar_posiciones(lista):
    
    nueva_lista = lista.copy() 

    aux = nueva_lista[-1]
    nueva_lista[0] = nueva_lista[-1]
    nueva_lista[-1] = aux
    
    return nueva_lista


#Programa principal

def main():
    lista = [1,2,3,4,5,6]
    nueva_lista = cambiar_posiciones(lista)
    print(lista)
    print(nueva_lista)
    

main()