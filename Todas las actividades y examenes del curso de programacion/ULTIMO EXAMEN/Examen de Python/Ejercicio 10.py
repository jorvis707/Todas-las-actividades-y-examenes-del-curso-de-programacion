def es_segura(password):
    if len(password) <= 8:
        return False
    
    tiene_mayuscula = any(c.isupper() for c in password)
    tiene_numero = any(c.isdigit() for c in password)
    
    if tiene_mayuscula and tiene_numero:
        return True
    return False

# Prueba
print(f"¿Es segura 'La ford 4x4'?: {es_segura('La ford 4x4')}")