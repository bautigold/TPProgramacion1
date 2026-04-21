def registrar_pasajero(pasajeros):
    """
    Objetivo: Registrar un pasajero
    Entrada:
    Salida:
    """
    dni = input("Ingrese el DNI del pasajero: ")
    
    if dni in pasajeros:
        print("Ya existe un pasajero con ese DNI")
        return

    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    contacto = input("Ingrese Email o telefono: ")

    pasajeros[dni] = {
        "nombre": nombre,
        "apellido": apellido,
        "contacto": contacto
    }
    print(f"Pasajero {nombre} {apellido} registrado.")


def buscar_pasajero(pasajeros, dni):
    """
    Objetivo: Buscar un pasajero por su DNI
    Entrada: 
    Salida:
    """
    return pasajeros.get(dni)


def mostrar_pasajeros(pasajeros):
    """
    Objetivo: Mostrar todos los pasajeros
    Entrada:
    Salida:
    """
    if not pasajeros:
        print("No hay pasajeros aún")
        return
    print("\nListado de Pasajeros")
    for dni, datos in pasajeros.items():
        print(f"DNI: {dni}  Nombre: {datos['nombre']} {datos['apellido']}")