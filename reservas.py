from viajes import buscar_viaje
from pasajeros import buscar_pasajero

def hacer_reserva(viajes, pasajeros, reservas):
    """
    Objetivo: Realizar la reserva 
    Entrada:
    Salida:
    """
    viajeCod = input("Ingrese el código del viaje: ")
    viaje = buscar_viaje(viajes, viajeCod)

    if not viaje:
        print("Viaje no encontrado.")
        return

    
    if viaje['asientos'] <= 0:
        print("No hay asientos libres para este viaje.")
        return

    dni = input("Ingrese el DNI del pasajero: ")
    pasajero = buscar_pasajero(pasajeros, dni)

    if not pasajero:
        print("Pasajero no encontrado")
        return

    reserva = {
        'viajeCod': viajeCod,
        'dni': dni
    }
    
    reservas.append(reserva)
    
    viaje['asientos'] -= 1
    print(f"Reserva realizada. Asientos libres: {viaje['asientos']}")