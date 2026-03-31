secuencia = "AAAABBBCCDAA"
print(f"Cadena original: {secuencia}")

comprimido = ""
contador = 1
for i in range(1, len(secuencia)):
    if secuencia[i] == secuencia[i-1]:
        contador += 1
    else:
    
        comprimido += str(contador) + secuencia[i-1]
        contador = 1
comprimido += str(contador) + secuencia[-1]
print(f"Cadena comprimida: {comprimido}")

descomprimido = ""
posicion = 0

while posicion < len(comprimido):
  
    repeticiones = int(comprimido[posicion])

    letra = comprimido[posicion + 1]
    
    for _ in range(repeticiones):
        descomprimido += letra
        
    posicion += 2
print(f"Cadena descomprimida: {descomprimido}")