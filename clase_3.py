print("""Teniendo en cuenta la ecuacion ax^2+bx+c
----------------------------------------""")
a1 = float(input("Introduce el valor de a1: "))
b1 = float(input("Introduce el valor de b1: "))
c1 = float(input("Introduce el valor de c1: "))
a2 = float(input("Introduce el valor de a2: "))
b2 = float(input("Introduce el valor de b2: "))
c2 = float(input("Introduce el valor de c2: "))

#Vamos a calcula el discriminante de los dos

X1 = (b1*b1) - 4*a1*c1
X2 = (b2*b2) - 4*a2*c2

#Comprobamos 

if X1 < 0:
    print("X1 no tiene raices reales")
else:
    print(f"La raiz de X1 es: {X1}")

if X2 < 0:
    print("X2 no tiene raices reales")
else:
    print(f"La raiz de X2 es: {X2}")
