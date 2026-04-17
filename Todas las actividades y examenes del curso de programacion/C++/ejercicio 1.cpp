#include <iostream>
#include <string>

using namespace std;

// Clase Base
class EstacionMonitoreo {
protected:
    string nombreEstacion;
public:
    // Constructor con inicializacion de string
    EstacionMonitoreo(string nombre) : nombreEstacion(nombre) {}
};

// Clase Hija
class NodoCentralSismico : public EstacionMonitoreo {
private:
    double energiaAcumulada; // Encapsulamiento privado estricto

public:
    // Constructor que inicializa la clase base y la energia en 0
    NodoCentralSismico(string nombre) : EstacionMonitoreo(nombre), energiaAcumulada(0.0) {}

    // Funcion void con switch para clasificar ondas y sumar energia
    void registrarOnda(int tipo) {
        switch(tipo) {
            case 1: // Onda P (Primaria)
                energiaAcumulada += 2.5;
                cout << "[INFO] Onda P detectada. +2.5 de energia." << endl;
                break;
            case 2: // Onda S (Secundaria)
                energiaAcumulada += 5.0;
                cout << "[INFO] Onda S detectada. +5.0 de energia." << endl;
                break;
            case 3: // Onda Superficial
                energiaAcumulada += 10.5;
                cout << "[ALERTA] Onda Superficial detectada. +10.5 de energia." << endl;
                break;
            default:
                cout << "[ERROR] Tipo de onda desconocido. No se suma energia." << endl;
                break;
        }
    }

    // Funcion con return e if-else para evaluar el umbral critico
    bool hayRiesgoCritico() {
        // Umbral critico definido en 25.0 unidades de energia
        if (energiaAcumulada >= 25.0) {
            return true;
        } else {
            return false;
        }
    }

    void iniciarSistema() {
        int entradaOnda = 0;

        cout << "--- Sistema de Monitoreo: " << nombreEstacion << " ---" << endl;

        // Bucle for para 5 lecturas de calibracion inicial
        for (int i = 1; i <= 5; i++) {
            cout << "Calibrando sensor de nodo #" << i << "... OK" << endl;
        }

        cout << "\nCalibracion terminada. Iniciando monitoreo en tiempo real." << endl;

        // Bucle while para monitoreo continuo hasta detectar riesgo
        while (!hayRiesgoCritico()) {
            cout << "\nEnergia Acumulada: " << energiaAcumulada << " / 25.0" << endl;
            cout << "Ingrese tipo de onda detectada (1:P, 2:S, 3:Superficial): ";
            cin >> entradaOnda;

            registrarOnda(entradaOnda);
        }

        // Mensaje final al romper el bucle por riesgo critico
        cout << "\n!!! EMERGENCIA SISMICA !!!" << endl;
        cout << "Energia acumulada: " << energiaAcumulada << " supero el umbral de seguridad." << endl;
        cout << "Nodo Central Sismico activando protocolos de evacuacion." << endl;
    }
};

int main() {
    // Instancia del objeto en el año 12,026
    NodoCentralSismico miNodo("Estacion-Central-Zulia");

    // Ejecucion del proceso principal
    miNodo.iniciarSistema();

    return 0;
}