def verificar_paridad(numero):
    if numero % 2 == 0:
        return "El numero es par"
    else:
        return "El numero es impar"

# Prueba
print(verificar_paridad(7))