import datetime

class Registro:

    def __init__(self, nombre, dni, patente, hora_ingreso, hora_salida=None):
        self.nombre = nombre 
        self.dni = dni
        self.patente = patente.upper()
        self.hora_ingreso = hora_ingreso
        self.hora_salida = hora_salida
    
    def marcar_salida(self):
        if not self.hora_salida:
            self.hora_salida = datetime.datetime.now()
        else:
            print("Este registro ya tiene una hora de salida registrada.")


def ingresar_registro():
    nombre = input("Nombre: ")
    dni = input("Número de RUN: ")
    patente = input("Patente de vehículo: ").upper()
    hora_ingreso = datetime.datetime.now() 

    return Registro(nombre, dni, patente, hora_ingreso)

def guardar_registros(registros):
    with open("registros.txt", "a") as archivo:
        for registro in registros:
            archivo.write(f"{registro.nombre},{registro.dni},{registro.patente},{registro.hora_ingreso},{registro.hora_salida}\n")

def cargar_registros():
    registros = []
    try:
        with open("registros.txt", "r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                datos = linea.strip().split(",")
                nombre, dni, patente, hora_ingreso_str, hora_salida_str, = datos
                hora_ingreso = datetime.datetime.strptime(hora_ingreso_str, "%Y-%m-%d %H:%M:%S.%f")
                if hora_salida_str:
                    hora_salida = datetime.datetime.strptime(hora_salida_str, "%Y-%m-%d %H:%M:%S.%f")
                else:
                    hora_salida = None
                registros.append(Registro(nombre, dni, patente, hora_ingreso, hora_salida))
    except FileNotFoundError:
        pass
    return registros   
    
def salir_registro(registros, identificador, por_dni=True):
    encontrado = False
    for registro in registros:
        if (por_dni and registro.dni == identificador) or (not por_dni and registro.patente == identificador):
            registro.marcar_salida()
            encontrado = True
            break
    
    if not encontrado:
        print("No se encontró un registro de ingreso para el identificador proporcionado.")
        
def eliminar_registro(registros, identificador):
    registros = [registro for registro in registros if registro.dni != identificador and registro.patente != identificador]
    return registros

    
def main():
    print("Bienvenido al sistema de control de acceso")
    print("1. Ingresar")
    print("2. Salida por RUN")
    print("3. Salida por patente")
    print("4. Eliminar un registro")
    opcion = input("Seleccione una opción: ")


    if opcion == "1":
        ingresar_registro()
    elif opcion == "2":
        salir_registro_dni()
    elif opcion == "3":
        salir_registro_patente()
    elif opcion == "4":
        eliminar_registro()
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
