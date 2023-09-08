"""
calificaciones = list(input("Introduce las calificaciones: ").split(","))

rango = max(calificaciones) - min(calificaciones)
total = len(calificaciones)
promedio = sum(calificaciones) / total
maximo = max(calificaciones)
minimo = min(calificaciones)

print(f"El rango de las calificaciones es {rango}")

"""

resis = input("Introduce 10 valores para la resistencia (separados por ','): ")
volt = input("Introduce 10 valores para el voltaje (separados por ','): ")

resis_list = [int(x) for x in resis.split(',')]
volt_list = [int(x) for x in volt.split(',')]

pot = []
print(resis_list)
for x, y in zip(volt_list, resis_list):
    pot.append((x ** 2) / y)

print(f"""
                Tabla
--------------------------------------
    Volt.    Resis.    Pote.
    {volt_list[0]:>3}       {resis_list[0]:>3}       {pot[0]:.2f}
    {volt_list[1]:>3}       {resis_list[1]:>3}       {pot[1]:.2f} 
    {volt_list[2]:>3}       {resis_list[2]:>3}       {pot[2]:.2f}
    {volt_list[3]:>3}       {resis_list[3]:>3}       {pot[3]:.2f}
    {volt_list[4]:>3}       {resis_list[4]:>3}       {pot[4]:.2f}
    {volt_list[5]:>3}       {resis_list[5]:>3}       {pot[5]:.2f}
    {volt_list[6]:>3}       {resis_list[6]:>3}       {pot[6]:.2f}
    {volt_list[7]:>3}       {resis_list[7]:>3}       {pot[7]:.2f}
    {volt_list[8]:>3}       {resis_list[8]:>3}       {pot[8]:.2f}
    {volt_list[9]:>3}       {resis_list[9]:>3}       {pot[9]:.2f}
---------------------------------------
      """)
        
        
