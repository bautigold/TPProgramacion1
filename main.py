from viajes import *
from pasajeros import *
from reservas import *
from auxiliar import *

def menu():
    viajes = {}
    pasajeros = {}
    reservas = []
    bandera = True

    while bandera:
        print("SISTEMA DE GESTIÓN DE VIAJES")
        print("1. Cargar Nuevo Viaje")
        print("2. Mostrar Todos los Viajes")
        print("3. Realizar una Reserva")
        print("4. Aplicar Hot Sale (10% OFF)")
        print("5. Ver Últimas 3 Reservas (Historial)")
        print("6. Calcular Recaudación Total")
        print("7. Ver Listado de Pasajeros")
        print("8. Salir")
        
        try:
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                cargar_viaje(viajes)
            
            elif opcion == "2":
                mostrar_viajes(viajes)
                obtener_destinos_unicos(viajes) 

            elif opcion == "3":
                dni = input("Ingrese DNI del pasajero: ")
                if validar_dni(dni):
                    pasajero = registrar_pasajero(pasajeros, dni)
                    
                    mostrar_viajes(viajes)
                    cod = input("Ingrese el código del viaje para reservar: ").upper()
                    
                    hacer_reserva(viajes, pasajeros, reservas, dni, cod)
                else:
                    print("Error: El DNI debe tener 7 u 8 dígitos numéricos.")
            
            elif opcion == "4":
                aplicar_descuento_masivo(viajes)
            
            elif opcion == "5":
                ultimas = reservas[-3:]
                if not ultimas:
                    print("No hay reservas registradas aún.")
                else:
                    print(f"ÚLTIMAS RESERVAS")
                    for r in ultimas:
                        print(f"Pasajero: {r['dni']} | Viaje: {r['viaje']} | Asiento: {r['asiento']}")
            
            elif opcion == "6":
                total = calcular_recaudacion_total(reservas)
                print(f"Recaudación Total Acumulada: ${total:.2f}")
            
            elif opcion == "7":
                mostrar_pasajeros(pasajeros)
                
            elif opcion == "8":
                print("Saliendo del sistema... ¡Buen viaje!")
                bandera = False
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
                
        except Exception as e:
            print(f"Ocurrió un error inesperado en el menú: {e}")

menu()