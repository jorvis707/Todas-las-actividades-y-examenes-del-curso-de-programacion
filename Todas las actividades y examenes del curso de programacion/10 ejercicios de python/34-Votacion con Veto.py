def procesar_votacion(lista_votos_tupla, tupla_vetados):
    conteo = {}
    
    for id_miembro, voto in lista_votos_tupla:
        
        if id_miembro not in tupla_vetados:
            if voto not in conteo:
                conteo[voto] = 0
            conteo[voto] += 1
        else:
            print(f"Voto anulado: Miembro {id_miembro} está vetado.")
            
    return conteo


votos = [(101, "SÍ"), (102, "NO"), (103, "SÍ"), (101, "SÍ"), (105, "SÍ")]
vetados = (101, 104)

resultados = procesar_votacion(votos, vetados)
print(f"Conteo final de votos válidos: {resultados}")