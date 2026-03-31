# ==========================================
# --- EL BUNKER: PROYECTO ABIGAIL ---
# ==========================================
print("=====================================")
print("--- EL BUNKER: PROYECTO ABIGAIL ---")
print("=====================================")

# --- INTRODUCCIÓN AL LORE ---
print("----------------------------------------------------------------")
print("ARCHIVO CLASIFICADO: CASO 731 - AREA 51")
print("Sujeto: Abigail Wester.")
print("Resumen: Lo que comenzó como un experimento para crear al")
print("super humano perfecto, terminó en una pesadilla biológica.")
print("La radiación y el hambre constante mutaron su cuerpo y su mente.")
print("El búnker fue sellado hace años... o eso creían todos.")
print("-----------------------------------------------------------------")
print("\nDespiertas en el suelo frío. El olor a metal y sangre te rodea.")

Z = input("preciona Y para empezar: ").lower()
if Z == "y":
# NIVEL 1: LA ENTRADA
 print("\nEstas en un bunquer supterranio abandonado, de pronto escuchas un ruido en una de las habitaciones")
 A = input("\nelijes IR A VER o BUSCAR LA SALIDA: ").lower()

# ---------------------------------------------------------------------------
# RAMA A: IR A VER (NIVEL 1)
# ---------------------------------------------------------------------------
if A == "ir a ver":
    print("\nTe encuentras con un soldado levemente herido.")
    
    # NIVEL 2: El Soldado
    B = input("¿LO AYUDAS o TOMAS LAS ARMAS y te vas?: ").lower()
    
    if B == "ayudas" or B == "lo ayudo":
        print("\nEl soldado te acompaña y te muestra un holograma de un cientifico explicando lo que paso.")
        
        # --- CÓDIGO DEL HOLOGRAMA ---
        print("---------------------------------------------------------------------------")
        print("EL HOLOGRAMA SE PROYECTA EN EL AIRE CON LUZ AZULADA...")
        print("Dr. Aris: Si alguien está viendo esto... es porque fallamos.")
        print("el experimento salio mal, todos estan muertos.")
        print("Intenté salvarla, pero la radiación destruyo todo lo que habia en ella")
        print("ella Ya no es humana... solo queda hambre")
        print("¡SI LA VES, NO DUDES! ¡CORRE O MÁTALA!")
        print("FIN DEL HOLOGRAMA...")
        print("----------------------------------------------------------------------------")

        # NIVEL 3: La Misión
        D2 = input("El soldado tiene como micion capturarla viva. ¿TE UNES A EL o BUSCAS LA SALIDA POR TU CUENTA? ").lower()
        
        if D2 == "te unes" or D2 == "me uno":
            print("\nel soldado te da un arma, y lo sigues")
            print("\n¡CUIDADO, A PARTIR DE AQUI TIENES QUE ELEJIR BIEN!!!!")
            
            D3 = input("Presiona Y para continuar: ")
            print("Caminan en silencio por un pasillo lleno de cables sueltos y chispas.")
            print("El soldado se detiene en seco. 'Escucha... está en el techo', susurra.")
            
            # NIVEL 4: Encuentro con Abigail
            D4 = input("\nAbigail salta frente a ustedes con un grito aterrador. ¿DISPARAS a las piernas o buscas el INTERRUPTOR?: ").lower()
            
            if D4 == "disparas" or D4 == "disparo":
                print("\n***************************************************************************")
                print("El tiro le da en la rodilla. Ella chilla y retrocede.")
                print("Soldado: ¡Buen tiro! Ahora, rápido, ayúdame a ponerle las esposas térmicas.")
                print("*****************************************************************************")
                
                # NIVEL 5: La Horda
                D5 = input("\nEsa cosa da un grito y se dan cuenta que hay mas. ¿HUYES o DISPARAS?: ").lower()
                if D5 == "disparas" or D5 == "disparo":
                    # NIVEL 6: Final Abierto
                    print("Disparas junto con el soldado pero son demasiados, el soldado cae...")
                    print("pero encuentras la forma de escapar pero gravemente herido...")
                    print("\nCONTINUARA... EL BUNKER: PROYECTO ABIGAIL")
                elif D5 == "huyes" or D5 == "huyo":
                    # NIVEL 6: Muerte
                    print("Te vas corriendo dejando al soldado atras, te topas con mas y no puedes escapar.")
                    print("\nGAME OVER")

            elif D4 == "interruptor":
                print("\nLa luz se enciende. Abigail se tapa los ojos, pero golpea al soldado.")
                print("El soldado cae inconsciente. Estás solo frente a ella, sin municion.")
                
                # NIVEL 5: El Duelo Final
                D6 = input("Solo tienes una NAVAJA o puedes correr a buscar el ARMA del soldado: ").lower()
                if D6 == "navaja" or D6 == "nabaja":
                    # NIVEL 6: Final Solo
                    print("Logras clavar la navaja en el craneo y la matas.")
                    print("ahora solo queda ayar la salida, el soldado murio estas solo...")
                    print("CONTINUARA...")
                elif D6 == "arma":
                    # NIVEL 6: Final de Victoria Heroica
                    print("\n========================================================================")
                    print("Corres y recojes el arma, le disparas en la cara y esa cosa cae.")
                    print("Ayudas al soldado a levantarse. Cojeando, avanzan por el último túnel...")
                    print("De pronto, una compuerta pesada se abre y la luz los ciega por un momento.")
                    print("==========================================================================")
                    
                    # ESCENA FINAL: EL CAMPO
                    print("==========================================================================")
                    print("\nSales del búnker y te encuentras en un campo bastante amplio.")
                    print("El cielo está nublado y corre un viento frío que agita la hierba alta.")
                    print("El aire se siente puro, pero el silencio es inquietante.")
                    print("==========================================================================")
                    
                    print("\nEl soldado se apoya en tu hombro, saca un detonador y te mira fijamente.")
                    print("Soldado: 'Vete de aquí... corre lo más lejos que puedas.'")
                    print("Soldado: 'Voy a volar este lugar. No puede quedar ni una sola evidencia de lo que hicieron aquí.'")
                    
                    final_decisión = input("\n¿(CORRES) hacia el horizonte o te quedas a (MIRAR)?: ").lower()
                    
                    if final_decisión == "corres" or final_decisión == "corro":
                        print("\nCorres con todas tus fuerzas mientras el viento golpea tu cara.")
                        print("A tus espaldas, una explosión ensordecedora sacude la tierra.")
                        print("No miras atrás. Eres libre... o eso crees.")
                    else:
                        print("\nTe quedas paralizado viendo cómo el búnker desaparece en una bola de fuego.")
                        print("El calor te golpea y el humo negro mancha el cielo nublado.")
                    
                    print("\n..............................................................")
                    print("EL JUEGO HA TERMINADO... POR AHORA.")
                    print("¿Realmente murió Abigail en la explosión?")
                    print("................................................................")
                    print("\n¡FELICIDADES! Lograste el FINAL VERDADERO.")
        
        else:
            # --- CONTINUACIÓN AGREGADA (NIVEL 4 RAMA SOLO) ---
            print("\nAbandonas al soldado. Caminas solo pero escuchas garras en las paredes.")
            D2_solo = input("¿Te ESCONDES en un casillero o CORRES hacia la ventilacion?: ").lower()
            if D2_solo == "escondes":
                print("Abigail pasa de largo. Logras encontrar una salida de emergencia. ¡Sobreviviste!")
            else:
                print("Eres muy ruidoso. Abigail te atrapa antes de subir. GAME OVER.")

    elif B == "tomas las armas" or B == "tomo las armas":
        # --- CONTINUACIÓN AGREGADA (NIVEL 3 RAMA REBELDE) ---
        print("\nEl soldado muere. Te adentras solo a investigar con tu nuevo equipo.")
        B_armas = input("Llegas a una sala de control. ¿REVISAS las camaras o destruyes el PANEL?: ").lower()
        if B_armas == "revisas":
            print("Ves a Abigail a traves de la pantalla... ella te esta mirando a TI. Ella viene.")
        else:
            print("El bunker entra en modo de autodestruccion. Tienes 2 minutos para huir.")

    else:
        print("\nNo hiciste nada y el silencio invade la sala.")

# ---------------------------------------------------------------------------
# RAMA B: BUSCAR LA SALIDA (NIVEL 1)
# ---------------------------------------------------------------------------
elif A == "buscar la salida":
    print("\nTodo es un laberinto, y de pronto escuchas un grito agudo y agonozante.")
    
    # NIVEL 2: Escape
    C = input("¿SALES CORRIENDO o TE ESCONDES?: ").lower()
    
    if C == "sales corriendo" or C == "salgo corriendo":
        print("\nCorres pero sientes que algo viene detras de ti, te tropiesas, caes y ves esa cosa cara a cara.")
        
        # NIVEL 3: El Tubo
        D = input("Encuentras un tubo tirado. ¿TE DEFIENDES o TE ARRASTRAS?: ").lower()
        
        if D == "te defiendes" or D == "me defiendo":
            print("\nGolpeas esa cosa con el tubo. Por un momento crees que la matas y ves de cerca...")
            print("¡ES ABIGAIL!!!! Te agarra de un braso pero logras escapar hacia la oscuridad.")
            
            # --- CONTINUACIÓN AGREGADA (NIVEL 4 RAMA TUBO) ---
            D_tubo = input("Estas herido y sangrando. ¿Buscas un BOTIQUIN o sigues CORRIENDO?: ").lower()
            if D_tubo == "botiquin":
                print("Encuentras vendas, pero el olor de la sangre atrajo a Abigail. GAME OVER.")
            else:
                print("Tu adrenalina te hace llegar a una puerta de salida. ¡Escapaste de milagro!")
                
        elif D == "te arrastras" or D == "me arrastro":
            print("\nEsa cosa te toma del tobillo y te arrastra hacia las sombras... GAME OVER.")
        else:
            print("\nEl miedo te paraliza y la criatura se acerca...")

    elif C == "te escondes" or C == "me escondo":
        print("\nVes como pasa algo que parece un humanoide deforme y de gran altura frente a ti.")
        
        # --- CONTINUACIÓN AGREGADA (NIVEL 3 RAMA SIGILO) ---
        C_sigilo = input("El humanoide se detiene a oler el aire. ¿Lanzas una PIEDRA para distraerlo o te quedas INMOVIL?: ").lower()
        if C_sigilo == "piedra":
            print("La criatura se distrae y logras pasar por detras hacia la libertad.")
        else:
            print("Te escucho respirar... Abigail te encontro. GAME OVER.")
    
    else:
        print("\nTe quedaste quieto en medio del pasillo y algo te encontró.")

# CIERRE FINAL
else:
    print("\nEsa no es una opción válida. Te quedaste atrapado en la entrada del búnker.")

print("\n--- Gracias por jugar ---")