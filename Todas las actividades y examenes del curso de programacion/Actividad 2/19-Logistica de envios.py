destino = input("¿El envio es nacional o internacional?: ").lower()
peso = float(input("Peso del paquete en kg: "))

if destino == "nacional":
    precio = peso * 5
elif destino == "internacional":
    precio = peso * 15
else:
    precio = 0
    print("Destino no valido.")

if precio > 0:
    print(f"El costo de envio es: {precio}$")