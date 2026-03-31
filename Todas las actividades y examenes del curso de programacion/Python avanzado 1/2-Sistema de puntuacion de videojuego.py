class Jugador:
    puntuacion_base = 100

    def __init__(self, nombre_usuario):

        self.nombre_usuario = nombre_usuario
        self.puntos_actuales = Jugador.puntuacion_base


    def ganar_puntos(self, cantidad):
        self.puntos_actuales += cantidad

class JugadorVIP(Jugador):
    def __init__(self, nombre_usuario, multiplicador):
        super().__init__(nombre_usuario)
        self.multiplicador = multiplicador #

    def ganar_puntos_vip(self, cantidad):
        puntos_ganados = cantidad * self.multiplicador
        self.puntos_actuales += puntos_ganados

def filtrar_mejores_jugadores(lista_jugadores, puntaje_minimo):
    mejores = []
    for j in lista_jugadores:
        if j.puntos_actuales >= puntaje_minimo:
            mejores.append(j.nombre_usuario)
    return mejores


j_normal = Jugador("Alejandro")
j_vip = JugadorVIP("Suarez_PRO", 5)

j_normal.ganar_puntos(20)      # 100 + 20 = 120
j_vip.ganar_puntos_vip(20)     # 100 + (20 * 5) = 200

ranking = filtrar_mejores_jugadores([j_normal, j_vip], 150)
print(f"jugadores nivel TOP (min 150 pts): {ranking}")