"""
Escriba un programa que pida al usuario una entrada de texto de cualqier longitud, y muestre cada palabra, la cantidad de veces 
que se repite y la cantidad total de palabras unicas. Utilice un diccionario para procesar la informacion
"""



def contado(entrada):
    
    texto = entrada.split()
    palabras = {}
    for palabra in entrada:
        if palabra in palabras:
            palabras[palabra] += 1
        else:
            palabras[palabra] = 1
    return palabra
        
entrada = input("Introduzca cualquier texto: ")

final = contado(entrada)

print("Las palabras y su frecuencia: ")

for palabra, frecuencia in str(final.items()):
    print(f"{palabra}: {frecuencia}")

total_de_las_palabras = len(final)
print(f"Total de palabras únicas: {total_de_las_palabras}")