def emparejar_jugadores(lista_jugadores):
    parejas = []
    
    # Comparamos cada jugador (i) con el siguiente (j) para no repetir parejas
    for i in range(len(lista_jugadores)):
        for j in range(i + 1, len(lista_jugadores)):
            p1 = lista_jugadores[i]
            p2 = lista_jugadores[j]
            
            misma_region = p1["region"] == p2["region"]
            nivel_cercano = abs(p1["nivel"] - p2["nivel"]) <= 5
            
            if misma_region and nivel_cercano:
                parejas.append((p1["id"], p2["id"]))
                
    return parejas

jugadores = [
    {"id": "Ale", "region": "LATAM", "nivel": 10},
    {"id": "Sua", "region": "LATAM", "nivel": 12},
    {"id": "Rex", "region": "EU", "nivel": 11},
    {"id": "Gus", "region": "LATAM", "nivel": 25}
]

lista_parejas = emparejar_jugadores(jugadores)
print(f"Parejas encontradas: {lista_parejas}")