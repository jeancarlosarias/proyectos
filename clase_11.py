"""
Un sistema de instruccion Asistido por Computadora(CAI) Se refiere al uso de la computadora en la educacion.
Escriba un programa que tenga una funcion que de manera aleatoria genere y retorne un par (una tupla) de dos numeros enteros no negativos
de 1 digito cada uno. Use el resultado de la funcion para mostrar el siguiente mensaje al usuario:

Cuanto es 6 multiplicado por 7:?

Si la respuesta del usuario es correcta, muestre un mensaje entre los siguientes:
Muy Bien!
Buen Trabajo!
Continua haciendo un buen trabajo!

Para respuestas incorrectas:
No, Intenta de nuevo
Incorrecto, trata una vez mas

Si la respuesta es incorrecta, debe continuar realizando la misma pregunta al usuario repetidamente hasta que conteste de manera adecuada.

"""
import random

Buena = ["Muy Bien!.", "Buen Trabajo!.", "Continua haciendo un buen trabajo!."]
Mal = ["No, Intenta de nuevo.", "Incorrecto, Trata una vez mas."]


def Operacion():
    numero_1 = random.randint(0, 9)
    numero_2 = random.randint(0, 9)
    
    numeros = (numero_1, numero_2)
    
    conteo = True
    
    while conteo == True:
        x = int(input(f"Cuanto es {numeros[0]} multiplicado por {numeros[1]}? "))
        
        if x == (numero_1*numero_2):
            respuesta_alt = random.choice(Buena)
            print(respuesta_alt)
            conteo = False
            
        elif x != (numero_1*numero_2):
            respuesta_alt = random.choice(Mal)
            print(respuesta_alt)
            conteo = True
        
      
Operacion()
            
    
    
    