import random

def BuscarPrimerPalabra(lista):
    '''Esta función eligirá la primera letra de maner aleatoría y la retornará como la primer posición de la lista para iniciar la construcción del crucigrama por cada partida'''
    palabras_para_jugar = []
    while len(palabras_para_jugar) == 0:
        palabra = random.choice(lista)
        if len(palabra) >= 7:
            palabras_para_jugar.append(palabra)
    return palabras_para_jugar

def LogicaConstruccion(lista_palabras,diccionario_coincidencias):
    '''Esta función delimitará la lógica de construcción partida a partida a partir del primer 
    llamado a la función anterior: "BuscarPrimerPalabra" que devolverá una palabra que minimamente tenga 7 caracteres o más. La palabras irán de a pares: Horizontales y Verticales'''
    
    #La primer palabra siempre se utilizará de manera horizontal
    palabras_partida = BuscarPrimerPalabra(lista_palabras)
    while len(palabras_partida) != 10:
        flag_direccion = ""
        if len(palabras_partida) == 1:
            indice_palabra = random.randint(0,2)
            letra_palabra = palabras_partida[0][indice_palabra]
            siguiente_palabra = random.choice(diccionario_coincidencias.get((letra_palabra)))
            #indice_coincidencia = tiene que ser igual al índice de coincidencia que tendría del diccionario de coincidencias
           # if len(siguiente_palabra[:indice_coincidencia - 1]) > len(siguiente_palabra[indice:]): flag_direccion = "norte"
           #elif len(siguiente_palabra[:indice_coincidencia - 1]) == len(siguiente_palabra[indice:]): flag_direccion = "equivalente"
           #else: flag_direccion = "sur"
    
    '''La segunda y tercer palabra se construirán de manera vertical buscando coincidencia con las letras de la primera'''
    




#Main
lista = ["perro","gato","helicopetro", "mandril", "hidrovía", "vivienda","día", "forma"]

palabra = BuscarPrimerPalabra(lista)
print(palabra)