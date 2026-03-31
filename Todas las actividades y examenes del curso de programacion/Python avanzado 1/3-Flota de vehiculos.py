class Vehiculo:
    costo_por_litro = 25

    def __init__(self, matricula, combustible_litros):

        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.en_ruta = True

    def viajar(self, kilometros):
        consumo = kilometros / 10
        if self.combustible_litros >= consumo:
            self.combustible_litros -= consumo
        else:
            self.combustible_litros = 0
            self.en_ruta = False
            print(f"{self.matricula} sin gasolina en mitad del camino.")

class Camion(Vehiculo):
    def __init__(self, matricula, combustible_litros, cargas):
        super().__init__(matricula, combustible_litros)
        self.cargas_entregadas = cargas


    def entregar_carga(self):
        if len(self.cargas_entregadas) > 0:
            paquete = self.cargas_entregadas.pop()
            print(f"Paquete {paquete} entregado por {self.matricula}")

def simular_jornada(lista_vehiculos, distancias_a_recorrer):
    for i in range(len(lista_vehiculos)):
        vehiculo = lista_vehiculos[i]
        distancia = distancias_a_recorrer[i]
        
        vehiculo.viajar(distancia)
        
        if isinstance(vehiculo, Camion) and vehiculo.en_ruta:
            vehiculo.entregar_carga()

mi_camion = Camion("VEH-789", 30, ["Pizza", "Bebida"])

simular_jornada([mi_camion], [50]) 

print(f"Estado final {mi_camion.matricula}: {mi_camion.combustible_litros}L restantes.")