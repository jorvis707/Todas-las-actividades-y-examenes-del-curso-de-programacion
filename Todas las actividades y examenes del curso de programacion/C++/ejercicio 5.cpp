#include <iostream>
#include <string>

using namespace std;

// Clase Base
class MaquinariaPesada {
protected:
    string modelo;
public:
    MaquinariaPesada(string mod) : modelo(mod) {}
};

// Clase Hija
class IncineradorInteligente : public MaquinariaPesada {
private:
    double temperaturaHorno; // Encapsulamiento estricto privado

public:
    IncineradorInteligente(string mod) : MaquinariaPesada(mod), temperaturaHorno(25.0) {}

    // Funcion void que usa un while interno para precalentar
    void precalentar(double tempObjetivo) {
        cout << "Iniciando precalentamiento del modelo: " << modelo << endl;
        while(temperaturaHorno < tempObjetivo) {
            temperaturaHorno += 50.5; // Incremento gradual de calor
            cout << "Temperatura actual: " << temperaturaHorno << " C" << endl;
        }
        cout << "Punto minimo de incineracion alcanzado." << endl;
    }

    // Funcion con return, switch por material e if-else anidado
    string procesarMaterial(int tipoMaterial, double volumen) {
        bool exito = false;
        string nombreMaterial = "";

        switch(tipoMaterial) {
            case 1: // Plastico
                nombreMaterial = "Plastico";
                if(temperaturaHorno >= 400.0 && volumen < 100.0) {
                    exito = true;
                }
                break;
            case 2: // Metal
                nombreMaterial = "Metal";
                if(temperaturaHorno >= 1000.0 && volumen < 50.0) {
                    exito = true;
                }
                break;
            case 3: // Organico
                nombreMaterial = "Organico";
                if(temperaturaHorno >= 200.0) {
                    exito = true;
                }
                break;
            default:
                return "Error: Material no reconocido.";
        }

        if(exito) {
            return "Incineracion de " + nombreMaterial + " EXITOSA.";
        } else {
            return "Incineracion de " + nombreMaterial + " FALLIDA: Insuficiente calor o exceso de volumen.";
        }
    }

    void controlCintaTransportadora() {
        int opcion;
        double volCarga;
        int turnoActivo = 1;

        // Bucle do-while controlando el turno laboral
        do {
            cout << "\n--- Turno Laboral Activo (Incinerador " << modelo << ") ---" << endl;
            cout << "1. Plastico | 2. Metal | 3. Organico | 0. Finalizar Turno" << endl;
            cout << "Seleccione material: ";
            cin >> opcion;

            if(opcion != 0) {
                cout << "Ingrese volumen de carga: ";
                cin >> volCarga;
                
                // Llamada a la funcion con return y muestra de resultado
                cout << procesarMaterial(opcion, volCarga) << endl;
            } else {
                turnoActivo = 0;
            }

        } while(turnoActivo != 0);

        cout << "Cinta transportadora detenida. Fin del turno laboral." << endl;
    }
};

int main() {
    // Instancia de la clase hija
    IncineradorInteligente miIncinerador("Termo-X-12000");

    // Precalentamiento minimo requerido para operar
    miIncinerador.precalentar(500.0);

    // Inicio del ciclo de trabajo
    miIncinerador.controlCintaTransportadora();

    return 0;
}