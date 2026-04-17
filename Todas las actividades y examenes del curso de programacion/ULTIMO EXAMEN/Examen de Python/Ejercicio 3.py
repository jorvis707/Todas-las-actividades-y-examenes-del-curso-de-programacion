personas = {"Hernesto": 18, "Ana": 23, "Luis": 15, "Veronica": 25}

print("Mayores de edad:")
for nombre, edad in personas.items():
    if edad >= 18:
        print(f"- {nombre} tiene {edad} años.")