def filtrar_hemisferio_norte(lista_tuplas):
    norteños = []
    
    for coord in lista_tuplas:
        latitud = coord[0]
        longitud = coord[1]
        
        if latitud > 0:
            dicc_coord = {"lat": latitud, "lng": longitud}
            norteños.append(dicc_coord)
            
    return norteños

puntos = [(19.43, -99.13), (-34.60, -58.38), (40.41, -3.70), (-12.04, -77.02)]
solo_norte = filtrar_hemisferio_norte(puntos)
print(f"Coordenadas del Norte: {solo_norte}")