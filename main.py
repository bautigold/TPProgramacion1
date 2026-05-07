from viajes import cargar_viaje, mostrar_viajes
from pasajeros import registrar_pasajero, mostrar_pasajeros
from reservas import hacer_reserva
import auxiliar

def menu():
    viajes = {}      
    pasajeros = {}   
    reservas = []    
    recorre = True
    
    while recorre:
        print(" SISTEMA DE GESTIÓN DE VIAJES ")
        print("1. Cargar viaje")
        print("2. Registrar pasajero")
        print("3. Hacer reserva")
        print("4. Mostrar viajes")
        print("5. Mostrar pasajeros")
        print("6. Salir")
        print("7. Ver últimas 3 reservas")
        
        opcion = input("Opción: ")
        
        if opcion == "1":
            cargar_viaje(viajes)
        elif opcion == "2":
            dni = input("DNI: ")
            if auxiliar.validar_dni(dni): 
                registrar_pasajero(pasajeros, dni)
            else:
                print("DNI inválido.")
        elif opcion == "3":
            hacer_reserva(viajes, pasajeros, reservas)
        elif opcion == "4":
            mostrar_viajes(viajes)
        elif opcion == "5":
            mostrar_pasajeros(pasajeros)
        elif opcion == "6":
            recorre = False  
        elif opcion == "7":
            ultimas = reservas[-3:] 
            print(f"Historial reciente: {ultimas}")
        else:
            print("Opción no válida.")


menu()