# ==========================================
# --- SIMULADOR DE CESTA DE COMPRA ---
# ==========================================
print("==========================================")
print("---- SIMULADOR DE CESTA DE COMPRA -----")
print("==========================================")
print("\n¡Bienvenido al Supermercado EL SOBREVIVIENTE!")
print("Gestiona tu cesta antes de que se acaben las provisiones.")

# Listas para almacenar la información (Sincronizadas por índice)
productos = []
precios = []
opcion = ""

while opcion != "5":
    print("\n------------------------------------------------------")
    print("1.Agregar - 2.Mostrar - 3.Eliminar - 4.Total - 5.Salir")
    print("------------------------------------------------------")
    opcion = input("Opción: ")

    if opcion == "1":
        productos.append(input("Producto: "))
        precios.append(float(input("Precio: ")))
    
    elif opcion == "2":
        for i in range(len(productos)):
            print(f"{i+1}-{productos[i]}: ${precios[i]}")
            
    elif opcion == "3":
        idx = int(input("Número a borrar: ")) - 1
        productos.pop(idx)
        precios.pop(idx)
        
    elif opcion == "4":
        print(f"Total: ${sum(precios)}")

print("\nGracias por comprar en EL SOBREVIVIENTE. ¡Vuelve pronto!")