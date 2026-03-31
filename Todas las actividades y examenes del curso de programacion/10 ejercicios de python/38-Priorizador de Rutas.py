def optimizar_ruta(lista_paquetes):
    rutas = {"prioritaria": [], "normal": []}
    
    for p in lista_paquetes:
        datos_paquete = (p["distancia"], p["id"])
        
        if p["urgente"]:
            rutas["prioritaria"].append(datos_paquete)
        else:
            rutas["normal"].append(datos_paquete)
    
    rutas["prioritaria"].sort()
    rutas["normal"].sort()
    
    return rutas

envios = [
    {"id": "P1", "distancia": 50, "urgente": False},
    {"id": "P2", "distancia": 10, "urgente": True},
    {"id": "P3", "distancia": 5, "urgente": True},
    {"id": "P4", "distancia": 20, "urgente": False}
]

plan_ruta = optimizar_ruta(envios)
print(f"Rutas optimizadas: {plan_ruta}")