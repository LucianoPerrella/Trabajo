import random
def LeerDict(diccionario):
    lista_extraida = []
    for clave,valor in diccionario.items():
        lista_extraida.append([clave,valor])
    return lista_extraida


def cargarListas(lista):
    palabras = []
    definiciones_1 = []
    definiciones_2 = []
    definiciones_3 = []
    
    for i in range(len(lista)):
        palabras.append(lista[i][0])
        cantidad_definiciones = len(lista[i][1])
        if cantidad_definiciones > 2:
            definiciones_1.append(lista[i][1][0])
            definiciones_2.append(lista[i][1][1])
            definiciones_3.append(lista[i][1][2])
        elif cantidad_definiciones > 1:
            definiciones_1.append(lista[i][1][0])
            definiciones_2.append(lista[i][1][1])
            definiciones_3.append("-")
        else:
            definiciones_1.append(lista[i][1][0])
            definiciones_2.append("-")
            definiciones_3.append("-")
            
            
        
    return palabras,definiciones_1,definiciones_2,definiciones_3

# def cargarListas(lista):
#     '''Función que se va a encargar de llenar las N listas principales: - palabras = [] - definiciones1 = ["definición1"] - definiciones2 = ["definición2"] - definicionesN = ["definiciónN"]. 
#     En caso de solo llevar una definición, en su indice de la lista definiciones_2 se completará con un guión medio (-)'''
    
    

#     palabras = []
#     definiciones_1 = []
#     definiciones_2 = []

#     for i in range(len(lista)):
#         palabras.append(list(lista[i][0]))
#         if len(lista[i][1]) > 1:
#             definiciones_1.append(lista[i][1][0])
#             definiciones_2.append(lista[i][1][1])
#         else:
#             definiciones_1.append(lista[i][1][0])
#             definiciones_2.append("-")

   

#     return palabras,definiciones_1,definiciones_2






diccionario = {
  "perro": [
    "Mamífero doméstico de la familia de los cánidos, de tamaño, forma y pelaje muy diversos, según las razas, que tiene olfato muy fino y es inteligente y muy leal a su dueño. Usado en masculino referido a la especie.",
    "El mejor amigo del hombre",
    "Un capo sinceramente"
  ],
  "gato": [
    "Mamífero de la familia de los félidos, digitígrado, doméstico, de unos 50 centímetro(s) de largo desde la cabeza hasta el arranque de la cola, que por sí sola mide unos 20 centímetro(s), de cabeza redonda, lengua muy áspera, patas cortas y generalmente pelaje suave y espeso, de color blanco, gris, pardo, rojizo o negro, empleado en algunos lugares para cazar ratones. Usado en masculino referido a la especie.",
    "Minino"
  ],
  "banana": [
    "Fruta tropical procedente de la planta herbácea que recibe el mismo nombre o banano, perteneciente a la familia de las musáceas. Tiene forma alargada o ligeramente curvada"
  ],
  "pelota": [
    "Bola hecha de una materia que le permita botar, usada en diversos juegos y deportes.",
    "esférico"
  ]
}

# lista = LeerDict(diccionario)
# palabras,def_01,def_02,def_03 = cargarListas(lista)



# palabras,def_01,def_02 = cargarListas(diccionario)


# main



# for i in range(len(palabras)):
#     print(f"{palabras[i]}"
#         f"\n -Primer definición: {def_01[i]}",
#         f"\n -Segunda definición: {def_02[i]}",
#         f"\n -Tercera definición: {def_03[i]}")