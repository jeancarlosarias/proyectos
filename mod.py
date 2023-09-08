class Empleado():
    def __init__(self, id, name, salary, work_hours):
        self.id = id
        self.name = name
        self.salary = salary
        self.work_hours = work_hours
        
    def View(self):
        print(f"ID: {self.id}")
        print(f"Nombre: {self.name}")
        print(f"Tasa Salarial: {self.salary}")
        print(f"Horas: {self.work_hours}")   

usuarios = []
       
def Create():
    id_usuario = int(input("Introduce el ID del empleado: "))
    name_usuario = str(input("Introduce el nombre del empleado: "))
    salario_usuario = float(input("Introduce el salario del empleado: "))
    horas_usuario = float(input("Introduce las horas del empleado: "))
    print("\n")
    
    for usuario in usuarios:
        if usuario["ID"] == id_usuario:
            print("¡Error! La ID ya está en uso. \n")
            return
    
    usuario = {
        "ID": id_usuario,
        "Nombre": name_usuario,
        "Salario": salario_usuario,
        "Horas": horas_usuario
    }
    usuarios.append(usuario)
    print(f"Se ha creado exitosamente el empleado {name_usuario} \n")
    
    
def See():
    if usuarios == [None]:
        for usuario in usuarios:
            print("Empleado: ")
            for key, values in usuario.items():
                print(f"{key}: {values}")
            print()
    else:
        print("No hay Empleados \n")
    
        
def Update():
    id_usuario = int(input("Ingrese el ID del empleado a modificar: "))
    for usuario in usuarios:
        if usuario["ID"] == id_usuario:
            nuevo_tasa_salarial = float(input("Ingrese la nueva tasa salarial: "))
            nuevas_horas_semana = int(input("Ingrese el nuevo máximo de horas por semana:"))
            print("\n")
            usuario["Salario"] = nuevo_tasa_salarial
            usuario["Horas"] = nuevas_horas_semana
            print("Datos del empleado modificados exitosamente.\n")
            return
    print("Empleado no encontrado. \n")
   
def Delete():
    id_usuario = int(input("Ingrese el ID del empleado a eliminar: "))
    for usuario in usuarios:
        if usuario["ID"] == id_usuario:
            usuarios.remove(usuario)
            print("Empleado eliminado exitosamente.\n")
            return
    print("Empleado no encontrado. \n")
    
