"""
CONSTRUYA UNA DEFINICION DE CLASE QUE PUEDA UTILIZARSE PARA REPRESENTAR A UN EMPLEADO DE UNA COMPAÑIA. CADA EMPLEADO ES DEFINIDO POR
UN NUMERO ENTERO DE IDENTIFICACION, UNA TASA SALARIAL EN PUNTO FLOTANTE Y UN NUMERO MAXIMO DE HORAS QUE EL EMPLEADO DEBERIA TRABAJAR
CADA SEMANA. LOS SERVICIOS DE LA CLASE DEBERAN PROPORCIONAR LA CAPACIDAD PARA INTRODUCIR DATOS, DESPLEGANDO DATOS EXISTENTES DE UN EMPLEADO

INCLUIR UN MENU QUE OFREZCA LAS SIGUIENTES OPCIONES:
1.- AGREGAR UN EMPLEADO
2.- VER EMPLEADOS
3.- MODIFICAR LOS DATOS DE UN EMPLEADO
4.- ELIMINAR UN EMPLEADO
5.- SALIR DEL PROGRAMA 
"""
from mod import Empleado, Create, See, Update, Delete

empleados = []

while True:
    print("OPCIONES (INTRODUZCA EL NUMERO): \n")
    print("1. Agregar un empleado")
    print("2. Ver empleados")
    print("3. Modificar los datos de un empleado")
    print("4. Eliminar un empleado")
    print("5. Salir del programa \n")
    
    opcion = int(input("Ingrese la opcion deseada: "))
    
    if opcion == 1:
        Create()
    elif opcion == 2:
        See()
    elif opcion == 3:
        Update()
    elif opcion == 4:
        Delete()
    elif opcion == 5:
        print("Saliendo del programa.")
        break
    else:
        print("La opcion no es valida, ingresa el numero correcto. \n")

