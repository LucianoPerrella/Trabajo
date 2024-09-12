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
# indice_palabra = random.randint(0,2)
# letra_palabra = string[indice_palabra]
# siguiente_palabra = random.choice(diccionario.get((letra_palabra)))
# print(letra_palabra)
# print(siguiente_palabra)


palabra = "mandril"
indice = 4



inicio= palabra[:indice -1]
fin = palabra[indice: ]
print(inicio)
print(fin)