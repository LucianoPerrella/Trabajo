def ConstruccionTableroVacio():
    '''Función encargada de generar un tablero vacio con el centro marcado con un *'''

    filas = 30
    columnas = 30
    tablero_vacio = [[list(" ") for i in range(columnas)] for i in range(filas)]

    tablero_vacio[9][9] = list("*")

    # for fila in tablero_vacio:
    #     print(fila)

    return tablero_vacio


tablero_vacio = ConstruccionTableroVacio()
["b","i","n","a","r","i","o"]

separado = [["b","a","n","a","n","a"],["b","i","n","a","r","i","o"],["a","n","a","n","a"],["a","t","i","s","b","o"],["n","a","c","i","o","n"],["a","t","r","a","v","e","s","a","r"],["a","t","u","e","n","d","o"]]
coincidencias = ["-",[1,3],[5,0],[0,4],[3,0],[1,1], [4,6]]
direcciones = ["-","vertical-norte","vertical-sur","horizontal-norte","horizontal-sur","vertical-sur","vertical-norte"]
coordenadas = []
print(separado)
print(len(separado))

def calcularFila(fila_anterior,indice,direccion):
    

    if direccion in ["horizontal-sur" ,"horizontal-norte"]:
        fila_siguiente = fila_anterior + indice
    
    else: 
        fila_siguiente = fila_anterior - indice  
    
   
    return fila_siguiente



def calcularColumna(columna_anterior,indice,direccion):
    if direccion in ["vertical-norte","vertical-sur"]:
        columna_siguiente = columna_anterior + indice 

    else:
        columna_siguiente = columna_anterior - indice


   
    return columna_siguiente

def ConstruirTablero(tablero,lista_palabras,lista_coincidencias,direccion):
    indice_fila_inicial = 9
    indice_columna_inicial = 9
    fila_anterior = indice_fila_inicial
    columna_anterior = indice_columna_inicial
    coordenadas = []
    for i in range(len(lista_palabras)):
        
        for j in range(len(lista_palabras[i])):
        
            print(coordenadas)

            if i == 0: #Primer Palabra - Horizontal
                fila_anterior = indice_fila_inicial
                columna_anterior =indice_columna_inicial 
                if len(coordenadas) == 0: #Guardo las coordenadas
                    coordenadas.append([fila_anterior,columna_anterior])
                
                tablero[fila_anterior][columna_anterior + j][0] = lista_palabras[i][j]

            elif i in [1,2]: #Segunda Palabra - Vertical - Depende de la Palabra N°1 /// #Tercera Palabra - Vertical - Depende de la Palabra N°1
                proxima_fila = calcularFila(coordenadas[0][0],coincidencias[i][1],direcciones[i])
                proxima_columna = calcularColumna(coordenadas[0][1],coincidencias[i][0],direcciones[i])
                if len(coordenadas) == i: #Guardo las coordenadas
                    coordenadas.append([proxima_fila,proxima_columna])
                tablero[proxima_fila + j][proxima_columna][0] = lista_palabras[i][j]
                

            elif i == 3: #Cuarta Palabra - Horizontal - Depende de la Palabra N° 2
                proxima_fila = calcularFila(coordenadas[1][0],coincidencias[i][0],direcciones[i])
                proxima_columna = calcularColumna(coordenadas[1][1],coincidencias[i][1],direcciones[i])
                if len(coordenadas) == 3: #Guardo las coordenadas
                    coordenadas.append([proxima_fila,proxima_columna])
                tablero[proxima_fila][proxima_columna + j][0] = lista_palabras[i][j]
                
            elif i == 4: #Quinta Palabra - Horizontal - Depende de la plabra N 3
                proxima_fila = calcularFila(coordenadas[2][0],coincidencias[i][0],direcciones[i])
                proxima_columna = calcularColumna(coordenadas[2][1],coincidencias[i][1],direcciones[i])
                if len(coordenadas) == 4: #Guardo las coordenadas
                    coordenadas.append([proxima_fila,proxima_columna])
                tablero[proxima_fila][proxima_columna + j][0] = lista_palabras[i][j]
                print(coordenadas)
            elif i == 5: #Sexta Palabra - Vertical - Depende de la plabra N 4
                proxima_fila = calcularFila(coordenadas[3][0],coincidencias[i][0],direcciones[i])
                proxima_columna = calcularColumna(coordenadas[3][1],coincidencias[i][1],direcciones[i])
                if len(coordenadas) == 5: #Guardo las coordenadas
                    coordenadas.append([proxima_fila,proxima_columna])
                tablero[proxima_fila + j][proxima_columna ][0] = lista_palabras[i][j]
            elif i == 6: #Séptima Palabra - Vertical - Depende de la plabra N 5
                proxima_fila = calcularFila(coordenadas[4][0],coincidencias[i][1],direcciones[i])
                proxima_columna = calcularColumna(coordenadas[4][1],coincidencias[i][0],direcciones[i])
                print(proxima_fila,proxima_columna)
                if len(coordenadas) == 6: #Guardo las coordenadas
                    coordenadas.append([proxima_fila,proxima_columna])
                tablero[proxima_fila + j][proxima_columna ][0] = lista_palabras[i][j]
                print(coordenadas)
                
          


                

          
                



    return tablero


tablero = ConstruirTablero(tablero_vacio,separado,coincidencias,direcciones)

for fila in tablero:
    print(fila)