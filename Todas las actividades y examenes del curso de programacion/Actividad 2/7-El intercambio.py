print("INTERCAMBIO DE BEBIDAS SIN MEZCLAR")
a = input("Ingresa la primera bebida para el baso 1: ")
b = input("Ingresa la segunda bebida para en baso 2: ")
print(f"Originalmente: la bebida del baso 1 es {a} y la del baso 2 es {b}")

temporal = a
a = b
b = temporal

print(f"Intercanbio hecho: la primera bebida {b} ahora esta en el segundo baso, donde avia {a} y la seguda bebida {a} ahora esta en el primer baso donde avia {b}")