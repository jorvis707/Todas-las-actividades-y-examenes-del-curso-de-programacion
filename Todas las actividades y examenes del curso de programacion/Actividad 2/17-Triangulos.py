lado1 = float(input("Lado 1: "))
lado2 = float(input("Lado 2: "))
lado3 = float(input("Lado 3: "))

if lado1 == lado2 == lado3:
    print("Es un triangulo Equilatero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Es un triangulo Isosceles.")
else:
    print("Es un triangulo Escaleno.")