class Dispositivo:
    cantidad_total_registrada = 0

    def __init__(self, marca, modelo):
       
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
        Dispositivo.cantidad_total_registrada += 1

    def cambiar_estado(self):
        if self.encendido == False:
            self.encendido = True
        else:
            self.encendido = False

class Telefono(Dispositivo): 
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.aplicaciones = []

    def instalar_app(self, nombre_app):
        self.aplicaciones.append(nombre_app)

def mostrar_telefonos_encendidos(lista_telefonos):
    print("--- TELÉFONOS ENCENDIDOS ---")
    for t in lista_telefonos:
        if t.encendido:
            print(f"📱 {t.marca} {t.modelo}")

t1 = Telefono("Apple", "iPhone 15")
t2 = Telefono("Samsung", "S24")
t1.cambiar_estado()
t1.instalar_app("WhatsApp")

mostrar_telefonos_encendidos([t1, t2])
print(f"Dispositivos totales: {Dispositivo.cantidad_total_registrada}")