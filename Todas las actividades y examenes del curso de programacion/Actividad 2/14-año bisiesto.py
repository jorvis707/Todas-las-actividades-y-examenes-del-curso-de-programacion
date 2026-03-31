año = int(input("Ingresa un año para saber si es bisiesto: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año {año} es bisiesto Febrero tiene 29 dias.")
else:
    print(f"El año {año} es un año comun (365 dias).")