def revisar_suscripciones(dicc_usuarios, mes_actual):
    vencidos = []
    
    for email, datos in dicc_usuarios.items():
      
        if datos["mes_vencimiento"] < mes_actual:
           
            vencidos.append((email, datos["plan"]))
            
    return vencidos

usuarios = {
    "ale@mail.com": {"plan": "Premium", "mes_vencimiento": 2},
    "suarez@mail.com": {"plan": "Free", "mes_vencimiento": 5},
    "test@mail.com": {"plan": "Pro", "mes_vencimiento": 1}
}
mes_hoy = 3 # Estamos en Marzo

lista_vencidos = revisar_suscripciones(usuarios, mes_hoy)
print(f"Cuentas vencidas: {lista_vencidos}")