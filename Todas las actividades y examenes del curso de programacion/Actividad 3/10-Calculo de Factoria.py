n = int(input("Ingresa un número entero positivo: "))

if n < 0:
    print("Error: El número debe ser positivo.")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f"El factorial de {n}! es: {factorial}")