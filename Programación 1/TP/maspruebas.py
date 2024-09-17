def ConstruccionTableroVacio():
    '''Función encargada de generar un tablero vacio con el centro marcado con un *'''

    filas = 20
    columnas = 20
    tablero_vacio = [[list(" ") for i in range(columnas)] for i in range(filas)]

    tablero_vacio[9][9] = list("*")

    # for fila in tablero_vacio:
    #     print(fila)

    return tablero_vacio


tablero_vacio = ConstruccionTableroVacio()
["b","i","n","a","r","i","o"]

separado = [["b","a","n","a","n","a"],["b","i","n","a","r","i","o"],["a","n","a","n","a"],["b","o","r","r","a","c","h","o"]]
coincidencias = ["-",[1,3],[5,0],[0,0]]
direcciones = ["-","vertical-norte","vertical-sur","horizontal-sur"]
print(separado)
print(len(separado))

def calcularFila(fila_anterior,indice,direccion):
    if direccion == "vertical-norte": 
        fila_siguiente = fila_anterior - indice  

    elif direccion == "vertical-sur":
        fila_siguiente = fila_anterior + indice
    
    else:
        fila_siguiente = fila_anterior
    return fila_siguiente

   

def calcularColumna(columna_anterior,indice,direccion):
    if direccion == "vertical-norte" or "vertical-sur":
        columna_siguiente = columna_anterior + indice 

    elif direccion == "horizontal-norte":
        columna_siguiente = columna_anterior - indice


    else: 
        columna_siguiente = columna_anterior  + indice
    return columna_siguiente

def ConstruirTablero(tablero,lista_palabras,lista_coincidencias,direccion):
    indice_fila_inicial = 9
    indice_columna_inicial = 5
    fila_anterior = indice_fila_inicial
    columna_anterior = indice_columna_inicial
    for i in range(len(lista_palabras)):
        
        for j in range(len(lista_palabras[i])):

            if i == 0:
                fila_anterior = indice_fila_inicial
                columna_anterior =indice_columna_inicial 
                
                tablero[fila_anterior][columna_anterior + j][0] = lista_palabras[i][j]

            elif i == 1:
                proxima_columna = calcularColumna(columna_anterior,coincidencias[i][0],direcciones[i])
                proxima_fila = calcularFila(fila_anterior,coincidencias[i][1],direcciones[i])
                tablero[proxima_fila + j][proxima_columna][0] = lista_palabras[i][j]
                

            elif i == 2:
                
                proxima_columna = calcularColumna(columna_anterior,coincidencias[i][0],direcciones[i])
                proxima_fila = proxima_fila = calcularFila(fila_anterior,coincidencias[i][1],direcciones[i])
                tablero[proxima_fila + j][proxima_columna][0] = lista_palabras[i][j]
          


                

          
                



    return tablero


tablero = ConstruirTablero(tablero_vacio,separado,coincidencias,direcciones)

for fila in tablero:
    print(fila)