peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = peso / (altura ** 2)

print(f"Tu IMC es: {imc:.2f}")

if imc < 18.5:
    print("Estado: Bajo peso")
elif imc < 25:
    print("Estado: Peso normal (Saludable)")
elif imc < 30:
    print("Estado: Sobrepeso")
else:
    print("Estado: Obesidad")