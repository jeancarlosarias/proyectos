import math

print("""
      Introduce los coeficientes a, b y c
      """)
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a and b == 0.0:
    print("La ecuacion es degenerada. No tiene solucion")
elif a == 0.0:
    x = -c/b
    print(f"La ecuacion tiene raiz unica x = {x}")
else:
    discr = (b*b) -4 +a * c
    if discr > 0:
        x1 = (-b + math.sqrt(discr) / (2*a)) 
        x2 = (-b - math.sqrt(discr) / (2*a)) 
        print(f"La raiz de X1 es {x1}")
        print(f"La raiz de x2 es {x2}")
    elif discr == 0:
        x = -b/(2*a)
        print(f"Ambas raices son reales e iguales a {x}")
    else:
        print("Las raices son complejas y conjugadas")
    
    
    
    