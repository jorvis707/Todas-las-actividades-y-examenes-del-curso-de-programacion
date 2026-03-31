def convertir_monedas(lista_precios, dicc_tasas):
    resultado = []
    
    for precio_usd in lista_precios:
        conversiones = {}
       
        for moneda, tasa in dicc_tasas.items():
            valor_convertido = precio_usd * tasa
            conversiones[moneda] = valor_convertido
        
        resultado.append((precio_usd, conversiones))
        
    return resultado

precios_usd = [10, 50, 100]
tasas = {"EUR": 0.92, "MXN": 17.10, "GBP": 0.79}

reporte = convertir_monedas(precios_usd, tasas)
print(f"Reporte de conversiones: {reporte}")