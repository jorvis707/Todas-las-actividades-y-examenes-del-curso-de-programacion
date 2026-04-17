#include <iostream>
#include <string>

using namespace std;

// Clase Base
class InstalacionIndustrial {
protected:
    int idInstalacion;
public:
    InstalacionIndustrial(int id) : idInstalacion(id) {}
};

// Clase Hija
class ReactorQuimico : public InstalacionIndustrial {
private:
    double presionInterna; // Encapsulamiento privado

public:
    // Constructor con inicializacion directa para evitar basura en memoria
    ReactorQuimico(int id) : InstalacionIndustrial(id), presionInterna(10.0) {}

    // Funcion con return y switch que devuelve la presion maxima permitida
    double obtenerPresionLimite(int fase) {
        switch(fase) {
            case 1: // Calentamiento
                return 45.0;
            case 2: // Fusion
                return 90.0;
            case 3: // Enfriamiento
                return 30.0;
            default:
                return 20.0; // Valor de seguridad por defecto
        }
    }

    // Funcion void con if-else para validar inyecciones
    void inyectarReactivo(double cantidad, int faseActual) {
        double limite = obtenerPresionLimite(faseActual);

        // Validacion de sobrepresion
        if (presionInterna + cantidad > limite) {
            cout << "[ALERTA] Inyeccion rechazada: Superaria el limite de " << limite << " PSI." << endl;
        } else {
            presionInterna += cantidad;
            cout << "[OK] Inyeccion realizada. Presion actual: " << presionInterna << " PSI." << endl;
        }
    }

    void cicloOperativo() {
        int codigoApagado = 0;
        int faseElegida = 0;
        double cantidadInyectar = 0.0;

        cout << "--- Sistema de Control Reactor ID: " << idInstalacion << " ---" << endl;

        // Bucle do-while para mantener el reactor operando
        do {
            cout << "\nPresion Interna: " << presionInterna << " PSI" << endl;
            cout << "Fases: 1.Calentamiento | 2.Fusion | 3.Enfriamiento" << endl;
            cout << "Seleccione fase o ingrese 999 para cerrar sistema: ";
            cin >> faseElegida;

            if (faseElegida == 999) {
                codigoApagado = 999;
            } else {
                cout << "Cantidad de reactivo a inyectar: ";
                cin >> cantidadInyectar;
                
                // Llamada a la funcion de validacion
                inyectarReactivo(cantidadInyectar, faseElegida);
            }

        } while (codigoApagado != 999);

        cout << "\nCodigo de apagado recibido. Despresurizando reactor..." << endl;
        cout << "Sistema fuera de linea de forma segura." << endl;
    }
};

int main() {
    // Instancia del Reactor con ID 505
    ReactorQuimico miReactor(505);

    // Inicio del bucle de control
    miReactor.cicloOperativo();

    return 0;
}