#Palabra 1 ---> Horizontal = Primero se debe elegir la primer palabra que irá en horizontal: necesita tener de 7 hasta 9 letras 

'''Palabra 2 y 3 ---> Verticales = Se elige de manera aleatoria entre la primer y la tercer letra (índices 0 y 2) y busca una palabra que coincida con la letra.
Se puede calcular si la mayoria de las letras quedan por arriba del meridiano para demarcar el orden de la siguiente.
En caso de quedar mas de %60 por encima del meridiano: la palabra N°3 buscara ser aquella que empieza con la primer letra de las ultimas
2(índices -1 u -2) letras de la primer palabra y se escribirá hacia abajo
En caso de quedar más del %60 por debajo del meridiano: la palabra N°3 buscará ser aquella que termine con la primera letra de las últimas 3 
letras de la primer palabra y se escribirá hacia arriba.   Podría ser una flag que índicase el modo

          a   
          horizonte
          o
          r
          a
    
    Ejemplo: seguna palabra con mas del 60% por debajo del meridiano, próxima palabra se hace con una palabra que termine con alguna de las 2 últimas letras
                  
                  e
                  l
                  e
                  f
                  a
                  n
          a       t
          horizonte
          o
          r
          a
'''


'''Palabras 4 y 5 ---> Horizontales = La palabra N° 4 se construye sobre la palabra N°2. 
En caso de que la palabra N°2 contenga la mayoría de las letras por debajo del meridiano, se eligirán las últimas dos letra para construir. 
Por otro lado, en caso de que la palabra N° 2 contenga la mayoria de letras por encima del meridiano se elegirán las primeras dos letras para construir
La palabra N° 4 usara de la palabra N° 2 según la posición la anteúltima o la última letra
Todo lo anterior aplica para 5


                  e l e c t r i c i d a d
                  l
                  e
                  f
                  a
                  n
          a       t
          horizonte
          o
          r
    v a c a
'''


palabras = ["horizonte","pajaros","arboles","zanahoria","radicheta","poliforme","masonería","barrabrava"]

def crearTablero():
    tablero_vacio = []
    filas = 50
    columnas = 50
    for fila in range(filas):
        tablero_vacio.append([])
        tablero_vacio[fila].append("*")
    return tablero_vacio


tablero_vacia = crearTablero()
print(tablero_vacia, end = " ")
# def armarTablero():

