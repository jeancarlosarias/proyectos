import random

print("""
======================================================================
   BIENVENIDO AL JUEGO DE !!!ADIVINA EL NUMERO!!!! 
            
   EL NUMERO QUE ESTOY PENSANDO ESTA ENTRE EL 1 Y 100

   PUEDES ELEGIR ENTRE EL MODO FACIL Y DIFICIL 
======================================================================
""")

numero_aleatorio = random.randint(1, 100)

intentos = 0

while True:
    dificultad = input("Ingresa la dificultad (facil/dificil): ")
    
    if dificultad == "facil":
        intentos = 10
        break
    elif dificultad == "dificil":
        intentos = 5
        break
    else:
        print("Opción no válida. Elige 'facil' o 'dificil'.")

print(numero_aleatorio)

while intentos > 0:
    dado = int(input("Ingresa el número que piensas: "))
    
    if dado == numero_aleatorio:
        print("¡GANASTE!")
        intentos = 0
    elif dado > numero_aleatorio:
        print("El número que ingresaste es muy alto.")
    elif dado < numero_aleatorio:
        print("El número que ingresaste es muy bajo.")
    
    intentos -= 1
    
    if intentos > 0:
        print(f"Tienes {intentos} intentos restantes.")
    else:
        print("¡GAME OVER!")
        volver_a_jugar = input("¿Quieres volver a jugar? (si/no): ")
        if volver_a_jugar.lower() != "si":
            break
        else:
            numero_aleatorio = random.randint(1, 100)
            intentos = 0

        
        

        
        