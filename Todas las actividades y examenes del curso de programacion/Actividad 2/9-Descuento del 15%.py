monto = float(input("cual es el total de su compra: "))

if monto > 100: 
    descuento = monto * 0.15
    final = monto - descuento
    print(f"Tiene un descuento del 15% y es {descuento}. total a pagar {final}")

else:
    print(f"no hay escuento, total a pagar: {monto}")