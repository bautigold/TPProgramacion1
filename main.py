from auxiliar import *
from viajes import *
from pasajeros import *
from reservas import *

def main():
    dicViajes = cargar_datos("viajes.json", {})
    dicPasajeros = cargar_datos("pasajeros.json", {})
    dicReservas = cargar_datos("reservas.json", [])
    continuar = True
    while continuar:
        print("\n SISTEMA UADE VIAJES ")
        print("1. Viajes (Cargar / Mostrar)")
        print("2. Pasajeros (Registrar / Mostrar)")
        print("3. Reservas (Nueva / Mostrar)")
        print("4. Reporte de Recaudación")
        print("0. Salir y Guardar")
        opcion = leer_entero("Opción: ")
        if opcion == 1:
            segundaOpcion = input("a. Cargar / b. Mostrar: ").lower()
            if segundaOpcion == "a": cargar_viaje(dicViajes)
            elif segundaOpcion == "b": mostrar_viajes(dicViajes)
        elif opcion == 2:
            segundaOpcion = input("a. Registrar / b. Mostrar: ").lower()
            if segundaOpcion == "a": registrar_pasajero(dicPasajeros)
            elif segundaOpcion == "b": mostrar_pasajeros(dicPasajeros)
        elif opcion == 3:
            segundaOpcion = input("a. Nueva Reserva / b. Mostrar Historial: ").lower()
            if segundaOpcion == "a": realizar_reserva(dicViajes, dicPasajeros, dicReservas)
            elif segundaOpcion == "b": mostrar_reservas(dicReservas)
        elif opcion == 4:
            calcular_recaudacion_total(dicReservas)
        elif opcion == 0:
            print("Guardando y saliendo...")
            guardar_datos(dicViajes, "viajes.json")
            guardar_datos(dicPasajeros, "pasajeros.json")
            guardar_datos(dicReservas, "reservas.json")
            continuar = False
        else:
            print("Opción no válida.")

main()



