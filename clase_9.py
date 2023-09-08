"""
Se deja caer una pelota desde una altura inicial. La pelota golpea el suelo a una velocidad dada por la ecuacion 
V = 2gh, siendo g = 9.81 m/s2 y h altura desde la que cayo. La pelota rebota entonces 2/3 desde la altura anterior.
Escriba un programa que muestre la velocidad de impacto y la altura que alcanza la pelota en cada rebote hasta que se
quede en el suelo
"""
#h = int(input("Introduzca una altura inicial: "))

#while h > 0:
    #V = 2*(9.81*h)
    #print(f"Miestras altura {h} m, la velocidad de caida es: {V:.2f}m/s")
    #h -=1



"""
Escriba un programa que calcule el promedio de calificaciones para 10 estudiantes, donde cada uno tiene 4 examenes.
Su programa debe pedir para cada estudiante sus 4 examenes, e imprimir el promedio correspondiente.
"""
estudiante = 0
promedios = []

while estudiante < 10:
    calificaciones = input(f"Ingrese las calificaciones del estudiante {estudiante + 1} (separadas por ','): ").split(",")
    calificaciones = [int(calificacion) for calificacion in calificaciones]
    promedio = sum(calificaciones) / len(calificaciones)
    promedios.append(promedio)
    estudiante += 1

resultado = ""
for i, promedio in enumerate(promedios, start=1):
    resultado += f"El promedio del estudiante {i} es: {promedio}\n"

print(f"""
----------------------------------------------------------
Promedio de las 10 calificaciones

{resultado}
--------------------------------------------------------
""")







        
        