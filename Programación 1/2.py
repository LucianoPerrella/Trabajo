'''Crear un programa que solicite al usuario ingresar
un número y busque la cantidad de corurrencias que esxiste en la lista ya cargada'''
import random

def buscar_cantidad_coincidencias(lista):
    
   num = int(input("Ingrese el número a buscar: "))
    
   ocurrencias = lista.count(num)
   
   return ocurrencias
    



#Programa principal
def main():
    lista = [1,2,3,4,10,2,3,4,10,24,10,23, 50, 50 , 50 ,50]

    repetidos = buscar_cantidad_coincidencias(lista)

    print(repetidos)
    
main()