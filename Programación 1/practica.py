def calcular_fecha(mes,año):
    mes_31_dias = [1,3,5,7,8,10,12]
    mes_30_dias = [4,6,9,11]
    dias_disponibles = 0
    es_bisiesto = False
   
    if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
        es_bisiesto = True
    
    if mes in mes_31_dias:
        dias_disponibles = 31
        return dias_disponibles
    elif mes in mes_30_dias:
        dias_disponibles = 30
        return dias_disponibles
    
        
    if mes == 2 and es_bisiesto:
        dias_disponibles = 29
        return dias_disponibles
    else:
        dias_disponibles = 28
        return dias_disponibles
    
        
    
print(calcular_fecha(2,2024))