inventario = {"Procesadores": 10, "Memorias RAM": 5}

def agregar_stock(producto, cantidad):
    if producto in inventario:
        inventario[producto] += cantidad
    else:
        inventario[producto] = cantidad

def vender(producto, cantidad):
    if producto in inventario and inventario[producto] >= cantidad:
        inventario[producto] -= cantidad
        print(f"Venta exitosa de {producto}.")
    else:
        print(f"Error: Stock insuficiente de {producto}.")

agregar_stock("Procesadores", 5)
vender("Memorias RAM", 3)
print(f"Inventario final: {inventario}")