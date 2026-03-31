edad = int(input("Tu edad: "))
dinero = float(input("¿Cuanto dinero tienes?: "))

if edad >= 18 and dinero >= 10:
    print("Recomendacion: Pelicula de Accion.")
elif edad < 18 and dinero >= 10:
    print("Recomendacion: Pelicula de Animacion.")
else:
    print("Lo sentimos, puedes ver los tráilers en las pantallas del lobby.")