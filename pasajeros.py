from auxiliar import *

def registrar_pasajero(pasajeros):
    print("\n REGISTRO DE PASAJERO ")
    dni = input("Ingrese el DNI (sin puntos): ")
    if not validar_dni(dni):
        print("Error: Formato de DNI incorrecto.")
        return
    if dni in pasajeros:
        print(f"El pasajero con DNI {dni} ya existe.")
        return
    nombre = normalizar_texto(input("Nombre: "))
    apellido = normalizar_texto(input("Apellido: "))
    identidad = (nombre, apellido)     
    edad = leer_entero("Edad: ")
    celular = input("Teléfono: ")
    pasajeros[dni] = {
        "identidad": identidad,
        "edad": edad,
        "contacto": celular
    }
    guardar_datos(pasajeros, "pasajeros.json")
    print(f"Pasajero {apellido} registrado con éxito.")

def mostrar_pasajeros(pasajeros):
    if not pasajeros:
        print("\nNo hay pasajeros registrados.")
        return
    print("\n LISTADO DE PASAJEROS ")
    for dni, info in pasajeros.items():
        nombre, apellido = info["identidad"]
        linea = f"DNI: {dni} - Pasajero: {apellido}, {nombre} - Edad: {info['edad']}"
        print(linea)

