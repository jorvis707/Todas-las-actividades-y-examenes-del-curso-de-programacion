conteo_positivos = 0
numero = 0

while numero >= 0:
    numero = int(input("Ingresa un número (negativo para terminar): "))
    if numero >= 0:
        conteo_positivos += 1

print(f"Ingresaste {conteo_positivos} números positivos.")