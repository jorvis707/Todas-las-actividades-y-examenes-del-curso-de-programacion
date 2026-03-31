nota1 = float(input("Ingresa la primera nota: "))
nota2 = float(input("Ingresa la segunda nota: "))
nota3 = float(input("Ingresa la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 60:
    print(f"Promedio: {promedio:.2f}. Aprobado")
else:
    print(f"Promedio: {promedio:.2f}. Reprobado")