#include <iostream>
#include <string>

using namespace std;

// Clase Base
class DispositivoRed {
protected:
    string hostname;
public:
    DispositivoRed(string host) : hostname(host) {}
};

// Clase Hija
class RouterCore : public DispositivoRed {
private:
    int paquetesDescartados; // Encapsulamiento privado
    int paquetesTotales;

public:
    // Inicializacion de variables en el constructor para evitar errores en VS Code
    RouterCore(string host) : DispositivoRed(host), paquetesDescartados(0), paquetesTotales(0) {}

    // Funcion void con switch por puertos para rutear el paquete
    void rutearPaquete(int puerto) {
        paquetesTotales++;
        switch(puerto) {
            case 80:
                cout << "[PUERTO 80] Trafico HTTP aceptado." << endl;
                break;
            case 21:
                cout << "[PUERTO 21] Trafico FTP aceptado." << endl;
                break;
            case 25:
                cout << "[PUERTO 25] Trafico SMTP aceptado." << endl;
                break;
            default:
                // Si el puerto no es 80, 21 o 25, se descarta el paquete
                paquetesDescartados++;
                cout << "[ADVERTENCIA] Puerto " << puerto << " bloqueado. Paquete descartado." << endl;
                break;
        }
    }

    // Funcion con return e if-else que evalua congestion (> 10%)
    string evaluarEstadoRed() {
        if (paquetesTotales == 0) {
            return "Red Inactiva";
        }

        // Calculo de porcentaje usando casting a double para precision
        double porcentajeDescarte = (static_cast<double>(paquetesDescartados) / paquetesTotales) * 100.0;

        if (porcentajeDescarte > 10.0) {
            return "Congestion Severa";
        } else {
            return "Red Estable";
        }
    }

    void procesarFlujoDatos() {
        int puertoEntrada = 0;
        cout << "--- Iniciando Router Core: " << hostname << " ---" << endl;

        // Bucle while que procesa paquetes mientras la red sea estable
        while (evaluarEstadoRed() != "Congestion Severa") {
            cout << "\nEstado actual: " << evaluarEstadoRed() << endl;
            cout << "Total: " << paquetesTotales << " | Descartados: " << paquetesDescartados << endl;
            cout << "Ingrese puerto del paquete (80, 21, 25) o 0 para apagar: ";
            cin >> puertoEntrada;

            if (puertoEntrada == 0) {
                break;
            }

            rutearPaquete(puertoEntrada);
        }

        // Mensaje final si se sale por congestion
        if (evaluarEstadoRed() == "Congestion Severa") {
            cout << "\n!!! ALERTA DE SEGURIDAD !!!" << endl;
            cout << "Se ha detectado Congestion Severa (>10% descartes)." << endl;
            cout << "Cierre de emergencia del Router Core ejecutado." << endl;
        } else {
            cout << "\nRouter apagado manualmente por el administrador." << endl;
        }
    }
};

int main() {
    // Creacion del objeto RouterCore
    RouterCore miRouter("Router-Principal-Zulia");

    // Inicio del procesamiento de paquetes
    miRouter.procesarFlujoDatos();

    return 0;
}