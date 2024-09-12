import json


def LeerJSON(archivo):
    lista_json = []
    with open(f"{archivo}", "r", encoding="utf-8") as file:
        data = json.load(file)
        
        for clave in data.items():
            lista_json.append(list(clave))


    return lista_json

def LeerDict(diccionario):
    lista_extraida = []
    for clave,valor in diccionario.items():
        lista_extraida.append([clave,valor])
    return lista_extraida






def cargarListas(lista):
    '''Función que se va a encargar de llenar las N listas principales: - palabras = [] - definiciones1 = ["definición1"] - definiciones2 = ["definición2"] - definicionesN = ["definiciónN"]. 
    En caso de solo llevar una definición, en su indice de la lista definiciones_2 se completará con un guión medio (-)'''
    
    

    palabras = []
    definiciones_1 = []
    definiciones_2 = []

    for i in range(len(lista)):
        palabras.append(list(lista[i][0]))
        if len(lista[i][1]) > 1:
            definiciones_1.append(lista[i][1][0])
            definiciones_2.append(lista[i][1][1])
        else:
            definiciones_1.append(lista[i][1][0])
            definiciones_2.append("-")

   

    return palabras,definiciones_1,definiciones_2


#main
ruta_json = r"C:\Users\lucia\Desktop\Trabajo\Trabajo\Programación 1\palabras.json"
lista_json = LeerJSON(ruta_json)

# print(lista_json)

palabras_nuevas,primer_deficion,segunda_definicion = cargarListas(lista_json)
print(palabras_nuevas)
print(segunda_definicion)


# for i in range(len(palabras_nuevas)):
#     print(f"{palabras_nuevas[i]}"
#         f"\n -Primer definición: {primer_deficion[i]}",
#         f"\n -Segunda definición: {segunda_definicion[i]}")

