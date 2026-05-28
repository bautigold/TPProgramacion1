from auxiliar import *

def registrar_pasajero(pasajeros, dni):
    """
    Objetivo: Registrar un nuevo pasajero en el sistema
    """
    if dni in pasajeros:
        print("El pasajero ya está registrado.")
        return pasajeros[dni]
    
    nombre = normalizar_texto(input("Ingrese nombre: "))
    apellido = normalizar_texto(input("Ingrese apellido: "))
    contacto = input("Ingrese medio de contacto (Email/Tel): ")
    identidad = (nombre, apellido) 
    
    pasajeros[dni] = {
        "identidad": identidad,
        "contacto": contacto
    }
    
    print(f"Pasajero {nombre} {apellido} registrado con éxito.")
    return pasajeros[dni]

def buscar_pasajero(pasajeros, dni):
    """
    Objetivo: Buscar un pasajero específico por su DNI.
    """
    return pasajeros.get(dni)

def mostrar_pasajeros(pasajeros):
    """
    Objetivo: Mostrar el listado completo de pasajeros
    """
    if not pasajeros:
        print("No hay pasajeros registrados.")
        return
    
    print("\nLISTADO DE PASAJEROS REGISTRADOS")
    for dni, datos in pasajeros.items():
        nombre, apellido = datos['identidad'] 
        print(f"DNI: {dni} | Pasajero: {apellido}, {nombre} | Contacto: {datos['contacto']}")