def agrupar_por_longitud(tupla_palabras):
    resultado = {}
    
    for palabra in tupla_palabras:
        largo = len(palabra)
       
        if largo not in resultado:
            resultado[largo] = []
        
       
        resultado[largo].append(palabra)
        
    return resultado

datos = ("sol", "casa", "luna", "mar", "python", "paz")
agrupados = agrupar_por_longitud(datos)
print(f"Grupos por longitud: {agrupados}")