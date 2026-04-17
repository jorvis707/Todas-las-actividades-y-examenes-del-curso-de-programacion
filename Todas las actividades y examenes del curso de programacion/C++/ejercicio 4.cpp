#include <iostream>
#include <string>

using namespace std;

// Clase Base
class NaveExploracion {
protected:
    double combustible;
public:
    NaveExploracion(double fuel) : combustible(fuel) {}
};

// Clase Hija
class SondaAutonoma : public NaveExploracion {
private:
    double desviacionTrayectoria; // Encapsulamiento privado

public:
    SondaAutonoma(double fuel) : NaveExploracion(fuel), desviacionTrayectoria(0.0) {}

    // Funcion void con if-else para activar propulsores
    void activarPropulsor(double correccion) {
        // Si la desviacion es positiva, empujamos hacia el otro lado
        if (correccion > 0) {
            cout << ">>> Propulsor IZQUIERDO activo. Corrigiendo: -" << correccion << " grados." << endl;
            desviacionTrayectoria -= correccion;
        } 
        // Si es negativa, el empuje debe ser positivo
        else if (correccion < 0) {
            cout << ">>> Propulsor DERECHO activo. Corrigiendo: +" << -correccion << " grados." << endl;
            desviacionTrayectoria += (-correccion);
        }
        
        // El objetivo es que desviacionTrayectoria vuelva a 0.0
    }

    // Funcion con return y switch para calcular la correccion necesaria
    double calcularCorreccion(int tipoAnomalia) {
        double factor = 0.0;
        switch(tipoAnomalia) {
            case 1: // Planeta
                factor = 12.5;
                break;
            case 2: // Asteroide
                factor = 3.2;
                break;
            case 3: // Agujero Negro
                factor = 45.0;
                break;
            default:
                factor = 0.0;
                break;
        }
        return factor;
    }

    void misionEscaneo() {
        int anomalia = 0;
        
        cout << "--- Sistema de Navegacion Sonda Autonoma ---" << endl;
        cout << "Combustible disponible: " << combustible << " unidades." << endl;

        // Bucle for estricto para 15 ciclos de escaneo y correccion
        for (int i = 1; i <= 15; i++) {
            cout << "\n[Ciclo de Escaneo " << i << "/15]" << endl;
            cout << "Detectar anomalia (1:Planeta, 2:Asteroide, 3:Agujero Negro, 0:Vacio): ";
            cin >> anomalia;

            if (anomalia != 0) {
                // Se calcula cuanto nos desvia el objeto
                double impacto = calcularCorreccion(anomalia);
                desviacionTrayectoria += impacto;
                
                cout << "Alerta: Desviacion detectada de " << desviacionTrayectoria << " grados." << endl;
                
                // Se activa el propulsor para compensar la desviacion exacta
                activarPropulsor(desviacionTrayectoria);
                
                cout << "Trayectoria estabilizada. Desviacion residual: " << desviacionTrayectoria << endl;
            } else {
                cout << "Escaneo completado: No se detectaron anomalias gravitacionales." << endl;
            }
        }

        cout << "\n--- Final de los 15 ciclos de mision ---" << endl;
        cout << "Sonda en posicion segura." << endl;
    }
};

int main() {
    // Se inicializa la sonda con combustible inicial
    SondaAutonoma sonda(5000.0);
    
    // Inicia el proceso de escaneo y correccion
    sonda.misionEscaneo();

    return 0;
}