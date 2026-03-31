a = float(input("Numero A: "))
b = float(input("Numero B: "))
c = float(input("Numero C: "))

if a >= b:
    if a >= c:
        mayor = a
    else:
        mayor = c
        
else: 
    if b >= c:
        mayor = b
    else:
        mayor = c
        
print(f"el numero mas grande de los tres es {mayor}")