calificacion = float(input("Introduce la primera calificacion: "))
calificacion_2 = float(input("Introduce la segunda calificacion: "))
calificacion_3 = float(input("Introduce la tercera calificacion: "))

promedio = (calificacion + calificacion_2 + calificacion_3)/3
print(f"{promedio:.2f}")

if promedio >= 90:
    print("Su promedio es A")
elif promedio >= 80:
    print("Su promedio es B")
elif promedio >= 70:
    print("Su promedio es C")
else:
    print("Su promedio es F")


