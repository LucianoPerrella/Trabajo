import random
# diccionario = {
#   "a": [
#     "Mamífero doméstico de la familia de los cánidos, de tamaño, forma y pelaje muy diversos, según las razas, que tiene olfato muy fino y es inteligente y muy leal a su dueño. Usado en masculino referido a la especie.",
#     "El mejor amigo del hombre",
#     "Un capo sinceramente"
#   ],
#   "g": [
#     "Mamífero de la familia de los félidos, digitígrado, doméstico, de unos 50 centímetro(s) de largo desde la cabeza hasta el arranque de la cola, que por sí sola mide unos 20 centímetro(s), de cabeza redonda, lengua muy áspera, patas cortas y generalmente pelaje suave y espeso, de color blanco, gris, pardo, rojizo o negro, empleado en algunos lugares para cazar ratones. Usado en masculino referido a la especie.",
#     "Minino"
#   ],
#   "u": [
#     "Fruta tropical procedente de la planta herbácea que recibe el mismo nombre o banano, perteneciente a la familia de las musáceas. Tiene forma alargada o ligeramente curvada"
#   ],
#   "d": [
#     "Bola hecha de una materia que le permita botar, usada en diversos juegos y deportes.",
#     "esférico"
#   ]
# }

# string = "agua"
# indice__coincidencia_palabra = random.randint(0,2)
# letra_palabra = string[indice__coincidencia_palabra]
# palabra = random.choice(diccionario.get((letra_palabra)))
# print(letra_palabra)
# print(palabra)


# palabra = "mandril"
# indice__coincidencia = 4



# inicio= palabra[:indice__coincidencia -1]
# fin = palabra[indice__coincidencia: ]
# print(inicio)
# print(fin)

# def ConstruccionTableroVacio():
#     '''Función encargada de generar un tablero vacio con el centro marcado con un *'''

#     filas = 20
#     columnas = 20
#     tablero_vacio = [[list(" ") for i in range(columnas)] for i in range(filas)]

#     tablero_vacio[9][9] = list("*")

#     # for fila in tablero_vacio:
#     #     print(fila)

#     return tablero_vacio


# tablero = ConstruccionTableroVacio()

# tablero[9][7][0]= "1"
# tablero[9][8][0] = "-"
# tablero[9][9][0] = "h"
# tablero[9][10][0] = "o"
# for fila in tablero:
#          print(fila)
# def definir_direccion(palabra,indice_coincidencia): 
#     flag_direccion = ""
#     if len(palabra[:indice_coincidencia]) > len(palabra[indice_coincidencia + 1:]): 
#         flag_direccion = "norte" 
#     elif len(palabra[:indice_coincidencia]) == len(palabra[indice_coincidencia + 1:]): 
        
#         random_flag = random.randint(1,2)
#         if random_flag == 1:
#             flag_direccion = "norte"
#         else:
#             flag_direccion = "sur"
            
#     else: flag_direccion = "sur"
#     return flag_direccion
            

# palabra = "casan"
# indice = 2

# direccion = definir_direccion(palabra,indice)

# print(direccion)
["2","-","b","i","n","a","r","i","o"]

separado = [["1","-","b","a","n","a","n","a"]]
coincidencias = ["-",[1,3]]
print(separado)
print(len(separado))

indice_fila_inicial = 9
indice_fila= indice_fila_inicial - (len(separado[:(coincidencias[i][1] + 3)]))