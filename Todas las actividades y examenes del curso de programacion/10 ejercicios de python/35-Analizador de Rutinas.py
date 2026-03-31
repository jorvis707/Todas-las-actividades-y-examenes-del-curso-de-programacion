def evaluar_rutina(lista_diccs, meta):
    total_calorias = 0
    
    for dia in lista_diccs:
        total_calorias += dia["calorias"]
    
    cumplio = False
    if total_calorias >= meta:
        cumplio = True
        
    return (total_calorias, cumplio)

historial = [
    {"dia": "Lunes", "calorias": 500},
    {"dia": "Martes", "calorias": 650},
    {"dia": "Miercoles", "calorias": 480}
]
meta_semanal = 1500

resultado = evaluar_rutina(historial, meta_semanal)
print(f"Resultado rutina (Total, Meta cumplida): {resultado}")