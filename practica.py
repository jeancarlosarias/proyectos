""" 
        Ejercicio 1

meses = {1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"}
dias = list(range(1, 31 + 1))


mes= int(input("Introduce un mes (1 para Enero, etc.): "))
dia = int(input("Introduce un dia: "))

if mes in meses:
    print(f"{meses[mes]}")
else:
    print("Se ha introducido un mes invalido.")
    
if dia in dias:
    print(f"{dia}")
else:
    print("Se ha introducido un dia invalido.")
    
    """
  
  
  
  
 
        #Ejercicio 2

meses = {1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"}

mes = int(input("Introduce un mes (1 para Enero, etc.): "))
dia = int(input("Introduce un día: "))

if mes < 1 or mes > 12:
    print("¡Mes inválido!")
elif mes == 2:  # Febrero
    if dia < 1 or dia > 28:
        print("¡Día inválido para Febrero!")
    else:
        nombre_mes = meses[mes]
        print(f"Has introducido el mes {nombre_mes} y el día {dia}.")
elif mes in [1, 3, 5, 7, 8, 10, 12]:  # Meses con 31 días
    if dia < 1 or dia > 31:
        print("¡Día inválido!")
    else:
        nombre_mes = meses[mes]
        print(f"Has introducido el mes {nombre_mes} y el día {dia}.")
else:  # Meses con 30 días
    if dia < 1 or dia > 30:
        print("¡Día inválido!")
    else:
        nombre_mes = meses[mes]
        print(f"Has introducido el mes {nombre_mes} y el día {dia}.")

        
        



"""
        Ejercicio 3
        
angulo_x = float(input("Introduce un angulo: "))


if angulo_x == 0 or angulo_x == 90 or angulo_x == 180 or angulo_x == 270 or angulo_x == 360:
    print("El angulo se escuentra en uno de los ejes.")
elif angulo_x > 0 and angulo_x < 90:
    print("El angulo se encuentra en el primer cuadrante.")
elif angulo_x > 90 and angulo_x < 180:
    print("El angulo se encuentra en el segundo cuadrante.")
elif angulo_x > 180 and angulo_x < 270:
    print("El angulo se encuentra en el tercer cuadrante.")
elif angulo_x > 270 and angulo_x < 360:
    print("El angulo se encuentra el cuarto cuadrante.")    
else:
    print("El angulo no es valido.")
    
"""



"""
        Ejercicio 4

año = int(input("Introduce un año: "))

if año % 400 == 0:
    print(f"El año {año} es bisiesto.")
elif año % 4 == 0 and año % 100 != 0:
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")
"""

"""
        Ejercicio 5
        
año = int(input("Introduce el año del automovil: "))
peso = float(input("Introduce el peso del automovil (en libras): "))

if año <= 1970:
    if peso < 2700:
        print(f"El automovil del año {año} y de peso {peso} lbs, es de clase '1' y la tarifa es de $16.50")
    elif peso >= 2700 and peso <= 3800:
        print(f"El automovil del año {año} y de peso {peso} lbs, es de clase '2' y la tarifa es de $25.50")
    elif peso > 3800:
        print(f"El automovil del año {año} y de peso {peso} lbs, es de clase '3' y la tarifa es de $46.50")
elif año == 1971 and año <= 1979:
    if peso < 2700:
        print(f"El automovil del año {año} y de peso {peso} lbs, es de clase '4' y la tarifa es de $27.00")
    elif peso >= 2700 and peso <= 3800:
        print(f"El automovil del año {año} y de peso {peso} lbs, es de clase '5' y la tarifa es de $30.50")
    elif peso > 3800:
        print(f"El automovil del año {año} y de peso {peso} lbs, es de clase '6' y la tarifa es de $52.50")
elif año >= 1980:
    if peso < 3500:
        print(f"El automovil del año {año} y de peso {peso} lbs, es de clase '7' y la tarifa es de $19.50")
    elif peso >= 3500:
        print(f"El automovil del año {año} y de peso {peso} lbs, es de clase '8' y la tarifa es de $52.50")
"""
