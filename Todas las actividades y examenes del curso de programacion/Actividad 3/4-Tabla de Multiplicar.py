n = int(input("¿De qué número quieres la tabla?: "))

for i in range(1, 11):
    resultado = n * i
    print(f"{n} x {i} = {resultado}")