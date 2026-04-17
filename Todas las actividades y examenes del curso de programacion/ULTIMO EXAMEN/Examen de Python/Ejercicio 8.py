frase = "La musica Elctronica es la musica del futuro"
palabras = frase.lower().split()
frecuencias = {}

for p in palabras:
    if p in frecuencias:
        frecuencias[p] += 1
    else:
        frecuencias[p] = 1

print(f"Frecuencias: {frecuencias}")