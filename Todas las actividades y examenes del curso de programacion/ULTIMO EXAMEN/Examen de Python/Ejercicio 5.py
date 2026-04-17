def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in texto:
        if letra in vocales:
            contador += 1
    return contador

# Prueba
print(f"Vocales encontradas: {contar_vocales('El precio del mañana')}")