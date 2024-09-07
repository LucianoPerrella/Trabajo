# bandera = True

# while bandera:
#     lado = int(input("Ingrese la longitud del lado del cuadrado: "))
#     if lado < 3:
#         print("Longitud inválida, ingrese una longitud válida")
#     else:
#         bandera = False



# relleno = "X"+(" "*(lado-2)+"X")

# print("X"*lado)
      
# for i in range(lado-2):
#     print(relleno)
# print("X"*lado)


##################################################

#chr toma un número entero como un argumento, y devuelve el caracter que representa
#ord toma un caracter como argumento, y devuelve el entero ASCII que representa


# for i in range(65,75):
#     print(i,chr(i))
    
# numero = 10

# numero1 = str(numero)



#################################################

# con_tilde = "ÁÉÍÓÚáéíóú"
# sin_tilde = "AEIOUaeiou"

# frase = input("Ingrese una frase para ser evaluada: ")

# con_reemplazo = ""

# for caracter in frase:
#     if caracter in con_tilde:
#         posición = con_tilde.index(caracter)
#         con_reemplazo = con_reemplazo + sin_tilde[posición]
#     else:
#         con_reemplazo = con_reemplazo + caracter
    
# print(con_reemplazo)

#################################################

#Métodos str interrogativos

# cadena = "Clase programación"

# print(cadena.isalpha())

# pi = "314"

# print(pi.isdigit())

# nombre = "juan"

#################################################

# def separar_cadenas(cadena):
#     indice_inicial = 0
    
#     while indice_inicial < len(cadena) and not cadena[indice_inicial].isalpha():
#         indice_inicial += 1
        
#     inicio = cadena[:indice_inicial]
#     indice_final = len(cadena) - 1
    
#     while indice_final > indice_inicial and not cadena[indice_final].isalpha():
#         indice_final -= 1
#     final = cadena[indice_final + 1:]
    
#     return inicio,final



# entidad = input("Ingrese el nombre de su entidad a evaluar: ")

# lista_palabras = entidad.split(" ")
# siglas = ""

# for palabra in lista_palabras:
#     siglas = siglas + palabra[0].upper()

# print(f"Nombre empresa: {entidad}\n"
#       f"y la sigla correspondiente: {siglas}")


    