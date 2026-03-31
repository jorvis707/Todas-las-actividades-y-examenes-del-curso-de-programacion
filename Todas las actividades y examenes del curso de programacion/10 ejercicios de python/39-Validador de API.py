def validar_esquema(payload_dicc, esquema_dicc):
    lista_errores = []
    valido = True
    
    for clave, tipo_esperado in esquema_dicc.items():
    
        if clave not in payload_dicc:
            valido = False
            lista_errores.append(f"Falta la clave: {clave}")
        else:
        
            if not isinstance(payload_dicc[clave], tipo_esperado):
                valido = False
                lista_errores.append(f"Tipo incorrecto en {clave}")
                
    return (valido, lista_errores)

mi_esquema = {"id": int, "nombre": str, "activo": bool}
mi_data = {"id": 101, "nombre": "Alejandro", "activo": "Si"}

resultado_api = validar_esquema(mi_data, mi_esquema)
print(f"¿Datos válidos?: {resultado_api[0]} | Errores: {resultado_api[1]}")