proyectos = [("Web Design", 5), ("Music Prod", 12), ("Cybersecurity", 8)]

def obtener_segundo(tupla):
    return tupla[1]

proyectos.sort(key=obtener_segundo)

print(f"Proyectos ordenados por prioridad/valor: {proyectos}")