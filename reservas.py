from viajes import buscar_viaje
from pasajeros import buscar_pasajero

def hacer_reserva(viajes, pasajeros, reservas):
    id_viaje = input("Ingrese el ID del viaje: ")
    viaje = buscar_viaje(viajes, id_viaje)
    
    if not viaje:
        print("Viaje no encontrado.")
        return
    
    id_pasajero = input("Ingrese el ID del pasajero: ")
    pasajero = buscar_pasajero(pasajeros, id_pasajero)
    
    if not pasajero:
        print("Pasajero no encontrado.")
        return
    
    reserva = {
        'id_viaje': id_viaje,
        'id_pasajero': id_pasajero
    }
    
    reservas.append(reserva)
    print("Reserva realizada con éxito.")