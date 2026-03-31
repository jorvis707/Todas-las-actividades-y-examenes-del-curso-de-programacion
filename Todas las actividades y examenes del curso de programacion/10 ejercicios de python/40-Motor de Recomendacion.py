def recomendar_peliculas(tupla_vistas, lista_catalogo_diccs):
    sugerencias = {}
    
    for pelicula in lista_catalogo_diccs:
        titulo = pelicula["titulo"]
        genero = pelicula["genero"]
        

        if titulo not in tupla_vistas:

            if genero not in sugerencias:
                sugerencias[genero] = []
            
            sugerencias[genero].append(titulo)
            
    return sugerencias

vistas = ("Inception", "Titanic", "Avatar")
catalogo = [
    {"titulo": "Inception", "genero": "Sci-Fi"},
    {"titulo": "Interstellar", "genero": "Sci-Fi"},
    {"titulo": "The Notebook", "genero": "Romance"},
    {"titulo": "Dune", "genero": "Sci-Fi"}
]

mis_recomendaciones = recomendar_peliculas(vistas, catalogo)
print(f"Películas recomendadas para ti: {mis_recomendaciones}")