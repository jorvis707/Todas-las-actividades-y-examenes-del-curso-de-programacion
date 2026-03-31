clave_real = "python123"
intentos = 3

while intentos > 0:
    password = input(f"Contraseña (intentos restantes {intentos}): ")
    
    if password == clave_real:
        print("Acceso concedido.")
        break
    else:
        intentos -= 1
        if intentos > 0:
            print("Incorrecto. Intenta de nuevo.")
        else:
            print("Se agotaron los intentos. Cuenta bloqueada.")