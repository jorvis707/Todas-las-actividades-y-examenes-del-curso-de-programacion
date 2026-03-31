limite = int(input("Ingresa el valor limite: "))

suma_total = 0
contador_numeros = 0
numero_actual = 1

while suma_total < limite:
    suma_total += numero_actual
    numero_actual += 1
    contador_numeros += 1

print(f"Suma total: {suma_total}")
print(f"Cantidad de números sumados: {contador_numeros}")