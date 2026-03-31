usuario = input("Usuario: ")
clave = input("Contraseña: ")

if usuario == "admin" and clave == "1234":
    print("Acceso concedido. Bienvenido jefe")
    
else:
    print("Acceso denegado, credenciales incorrectas")