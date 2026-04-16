from viajes import cargar_viaje, mostrar_viajes
from pasajeros import registrar_pasajero
from reservas import hacer_reserva

def menu():
    viajes = {}
    pasajeros = {}
    reservas = []
    recorre = True

    while recorre == True:
        print("\n1. Cargar viaje")
        print("2. Registrar pasajero")
        print("3. Hacer reserva")
        print("4. Mostrar viajes")
        print("5. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            cargar_viaje(viajes)
        elif opcion == "2":
            registrar_pasajero(pasajeros)
        elif opcion == "3":
            hacer_reserva(viajes, pasajeros, reservas)
        elif opcion == "4":
            mostrar_viajes(viajes)
        elif opcion == "5":
            recorre = False

menu()