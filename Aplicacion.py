import datetime

def ingresar_registro():
    nombre = input("Nombre: ")
    dni = input("Número de RUN: ")
    patente = input("Patente de vehículo: ").upper()
    
    nombre_formateado = ' '.join(word.capitalize() for word in nombre.split())
    hora_ingreso = datetime.datetime.now()
    hora_salida = None

    registro = f"{nombre_formateado},{nombre},{dni},{patente},{hora_ingreso},{hora_salida}\n"
    with open("registros.txt", "a") as archivo:
        archivo.write(registro)

    print("Registro de ingreso creado.")

def salir_registro_dni():
    dni = input("Número de RUN: ")

    with open("registros.txt", "r") as archivo:
        lineas = archivo.readlines()

    encontrado = False
    for i, linea in enumerate(lineas):
        datos = linea.strip().split(",")
        if datos[1] == dni and datos[4] == "":
            hora_salida = datetime.datetime.now()
            lineas[i] = f"{datos[0]},{datos[1]},{datos[2]},{datos[3]},{hora_salida}\n"
            encontrado = True
            break

    if encontrado:
        with open("registros.txt", "w") as archivo:
            archivo.writelines(lineas)
        print("Registro de salida registrado.")
    else:
        print("No se encontró un registro de ingreso para el DNI proporcionado.")


def salir_registro_patente():
    dni = input("Patente del Vehiculo: ")

    with open("registros.txt", "r") as archivo:
        lineas = archivo.readlines()

    encontrado = False
    for i, linea in enumerate(lineas):
        datos = linea.strip().split(",")
        if datos[1] == dni and datos[4] == "":
            hora_salida = datetime.datetime.now()
            lineas[i] = f"{datos[0]},{datos[1]},{datos[2]},{datos[3]},{hora_salida}\n"
            encontrado = True
            break
    if encontrado:
        with open("registros.txt", "w") as archivo:
            archivo.writelines(lineas)
        print("Registro de salida registrado.")
    else:
        print("No se encontró un registro de ingreso para la patente proporcionada.")
        
def eliminar_registro():
    indentificador = input("Ingrese el numero de RUN o la patente del registro a eliminar: ")
    
    with open("registros.txt", "r") as archivo:
        lineas = archivo.readlines()
        
    encontrado = False
    for i, linea in enumerate(lineas):
        datos = linea.strip().split(",")
        if datos[1] == indentificador or datos[2] == indentificador:
            del lineas[i]
            encontrado = True
            break
    if encontrado:
        with open("registro.txt", "w") as archivo:
            archivo.writelines(lineas)
        print("Registro eliminado.")
    else:
        print("No se encontró un registro para el numero de RUN o patente proporcionada.")
        

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