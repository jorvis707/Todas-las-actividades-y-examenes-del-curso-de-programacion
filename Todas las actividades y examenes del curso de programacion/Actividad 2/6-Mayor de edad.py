edad = int(input("Cuantos años tienes?: "))
if edad >= 18:
    print(f"Puedes pasar, eres mayor de edad")
else:
    print(f"No puedes pasar, te falta {18 - edad} años para poder entrar.")