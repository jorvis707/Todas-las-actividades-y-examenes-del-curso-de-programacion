edad = int(input("Introdice tu edad: "))

if edad < 16 and edad >= 0:
    print("Eres un niño")
    
elif edad <18 and edad >= 16:
    print("Eres un preadolecente")
    
elif edad >= 18 and edad < 20:
    print("Eres un adolecente mayor de edad")
    
elif edad >= 20 and edad < 30:
    print("Eres un adulto joven")

elif edad >= 30 and edad < 60:
    print("Eres un adulto de mediana edad")
    
elif edad >= 60 and edad < 100:
    print("Eres un adulto de tersera edad")

else:
    print("edad no VALIDA, introdusca una edad corecta")