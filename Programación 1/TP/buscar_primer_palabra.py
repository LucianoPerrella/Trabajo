import random

def BuscarPrimerPalabra(lista):
    '''Esta función eligirá la primera letra de maner aleatoría y la retornará como la primer posición de la lista para iniciar la construcción del crucigrama por cada partida'''
    palabras_para_jugar = []
    while len(palabras_para_jugar) == 0:
        palabra = random.choice(lista)
        if len(palabra) >= 7:
            palabras_para_jugar.append(palabra)
    return palabras_para_jugar

def definir_direccion(palabra,indice_coincidencia): 
    '''Función para definir la dirección de la palabra evaluando la cantidad de letra correspondientes antes y despues de la letra coincidente'''
    flag_direccion = ""
    if len(palabra[:indice_coincidencia]) > len(palabra[indice_coincidencia + 1:]): 
        flag_direccion = "norte" 
    elif len(palabra[:indice_coincidencia]) == len(palabra[indice_coincidencia + 1:]): 
        
        random_flag = random.randint(1,2)
        if random_flag == 1:
            flag_direccion = "norte"
        else:
            flag_direccion = "sur"
            
    else: flag_direccion = "sur"
    return flag_direccion
            






def LogicaConstruccion(lista_palabras,diccionario_coincidencias):
    '''Esta función delimitará la lógica de construcción partida a partida a partir del primer 
    llamado a la función anterior: "BuscarPrimerPalabra" que devolverá una palabra que minimamente tenga 7 caracteres o más. La palabras irán de a pares: Horizontales y Verticales'''
    
    #La primer palabra siempre se utilizará de manera horizontal
    palabras_partida = BuscarPrimerPalabra(lista_palabras)
    lista_direcciones = ["-"]
    
    flag_direccion = ""
    while len(palabras_partida) != 5:
        if len(palabras_partida) == 1:
            indice_letra_a_buscar = random.randint(0,2)
            letra_palabra = palabras_partida[0][indice_letra_a_buscar]
            siguiente_palabra = random.choice(diccionario_coincidencias.get((letra_palabra)))
            #indice_coincidencia = #índice que tiene la letra de la palabra que voy a traer del diccionario de coincidencias
            # flag_direccion = definir_direccion(siguiente_palabra,indice_coincidencia)
            #lista_direcciones.append(flag_direccion)
        if len(palabras_partida) == 2:
            if lista_direcciones[1] == "norte":
                flag_direccion = "sur"
                lista_direcciones.append(flag_direccion)
                indice_letra_a_buscar = -1
                letra_palabra = palabras_partida[0][indice_letra_a_buscar]
                siguiente_palabra = random.choice(diccionario_coincidencias.get((letra_palabra))) #esto tendría que ser una palabra que empiece con la última letra de la primer palabra horizontal
            else:
                flag_direccion = "norte"
                lista_direcciones.append(flag_direccion)
                indice_letra_a_buscar = -1
                letra_palabra = palabras_partida[0][indice_letra_a_buscar]
                siguiente_palabra = random.choice(diccionario_coincidencias.get((letra_palabra))) #esto tendría que ser una palabra que termine con la última letra de la primer palabra horizontal
        if len(palabras_partida) == 3:
            if lista_direcciones[1] == "norte":
                indice_letra_a_buscar = 0
                letra_palabra = palabras_partida[1][indice_letra_a_buscar]
                siguiente_palabra = random.choice(diccionario_coincidencias.get((letra_palabra))) #se buscará un coincidencia con la primer letra de la palabra N° 2
                #indice_coincidencia = #índice que tiene la letra de la palabra que voy a traer del diccionario de coincidencias
                # flag_direccion = definir_direccion(siguiente_palabra,indice_coincidencia)
                #lista_direcciones.append(flag_direccion)
           
            else:
                indice_letra_a_buscar = -1
                letra_palabra = palabras_partida[1][indice_letra_a_buscar]
                siguiente_palabra = random.choice(diccionario_coincidencias.get((letra_palabra))) #Se buscará una coincidencia con la última letra de la palabra N°2
                #indice_coincidencia = #índice que tiene la letra de la palabra que voy a traer del diccionario de coincidencias
                # flag_direccion = definir_direccion(siguiente_palabra,indice_coincidencia)
                #lista_direcciones.append(flag_direccion)
        if len(palabras_partida) == 4:
            if lista_direcciones[2] == "norte":
                indice_letra_a_buscar = 0
                letra_palabra = palabras_partida[2][indice_letra_a_buscar]
                siguiente_palabra = random.choice(diccionario_coincidencias.get(letra_palabra)) #se buscará una coincidencia con la primer letra
                #indice_coincidencia = #índice que tiene la letra de la palabra que voy a traer del diccionario de coincidencias
                # flag_direccion = definir_direccion(siguiente_palabra,indice_coincidencia)
                #lista_direcciones.append(flag_direccion)
            else:
                indice_letra_a_buscar = -1
                letra_palabra = palabras_partida[2][indice_letra_a_buscar]
                siguiente_palabra = random.choice(diccionario_coincidencias.get(letra_palabra))  #se buscará coincidencia con la última letra
                #indice_coincidencia = #índice que tiene la letra de la palabra que voy a traer del diccionario de coincidencias
                # flag_direccion = definir_direccion(siguiente_palabra,indice_coincidencia)
                #lista_direcciones.append(flag_direccion)



                


    

    




#Main
lista = ["perro","gato","helicopetro", "mandril", "hidrovía", "vivienda","día", "forma"]

palabra = BuscarPrimerPalabra(lista)
print(palabra)