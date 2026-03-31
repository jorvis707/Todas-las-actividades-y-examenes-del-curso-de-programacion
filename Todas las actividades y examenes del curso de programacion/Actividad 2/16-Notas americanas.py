nota = int(input("Ingresa la calificacion (0-100): "))

if nota >= 90:
    letra = "A"
elif nota >= 80:
    letra = "B"
elif nota >= 70:
    letra = "C"
elif nota >= 60:
    letra = "D"
else:
    letra = "F"

print(f"Tu calificacion final es: {letra}")