entrada = input("Introduce una secuencia de numeros (separados por ','): ").split(",")
entrada = [int(num) for num in entrada]

y = "Falso"
z = 0
while range(entrada):
    if entrada == 1:
        if entrada == 2:
            if entrada ==3:
                y = "Verdadero"
                z = 1
                break
        
        
    
if z == 1:
    print("Verdadero")
else:
    print(y)
        
""""
a = int(input("Introduce a: "))
b = int(input("Introduce b: "))
c = int(input("Introduce c: "))

x = a+b+c

if x == 15 or x == 16:
    
    print("es Adolescente")
elif x > 13 and x < 19:
    x = 0
    print(f"es {x}")
    
        
else:
    print("No es adolescente")
    """
    
"""
ent = input("Introduce una secuencia de numeros (separados por ','): :) ").split(",")

it = [int(num) for num in ent]
li = []

it = [int(num) for num in ent]
pares = [num for num in it if num % 2 == 0]

print("Números pares:")
print(pares)
"""