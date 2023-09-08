import random, string

"""
Escriba un programa que permita generar contraseñas de forma automatica.
Su programa debe pedir al usuario la cantidad de letras que desee que tenga su contraseña, la cantidad de digitos
y las cantidad de caracteres especiales.

Ejemplo:

Introduzca la cantidad de letras que desee que tenga la contraseña: xx
Introduzca la cantidad de digitos que desee que tenga la contraseña: xx
Introduzca la cantidad de caracteres especiales que desee que tenga la contraseña: xx

"""

letras = list(string.ascii_letters)
numeros = list(string.digits)
caracteres = list(string.punctuation)


print("""
    ---------------------------------
        Generador de contraseñas
    ---------------------------------
          """)


le = int(input("Intrduzca la cantidad de letras que desee que tenga la contraseña: "))
di = int(input("Introduzca la cantidad de digitos que desee que tenga la contraseña: "))
ca = int(input("Introduzca la cantidad caracteres que desee que tenga la contraseña: "))

L = random.sample(letras, k = le)
N = random.sample(numeros, k =di)
C = random.sample(caracteres, k = ca)

vacia = L+N+C
random.shuffle(vacia)
sv = ''.join(str(x) for x in vacia)

print(f"""
      -------------------------------
      La contraseña generada es: {sv}
      -------------------------------""")






    
