import math

x = int(input("Introduzca un valor de x: "))
y = 4

print("""e a la x\taproximacion\tdiferencia
---------\t------------\t----------""")

for numero in range(y):
    aproximacion = sum([(x ** numero_2) / math.factorial(numero_2) for numero_2 in range(numero + 1)])
    diferencia = math.exp(x) - aproximacion
    print(f"{math.exp(x):>1.5f}{aproximacion:>20.5f}{diferencia:>15.5f}")