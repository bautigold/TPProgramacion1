from functools import reduce

def hacer_reserva(viajes, pasajeros, reservas, dni, cod_viaje):
    viaje = viajes.get(cod_viaje)
    if not viaje or viaje['asientos_libres'] == 0:
        print("Viaje no disponible o completo.")
        return

    print("Mapa de asientos (0:Libre, 1:Ocupado):")
    for i, fila in range(len((viaje['mapa']))):
        fila = viaje["mapa"][i]
        print(f"Fila {i}: {fila}")
    
    try:
        fila = int(input("Elija fila (0-4): "))
        columna = int(input("Elija columna (0-3): "))
        
        if viaje['mapa'][fila][columna] == 0:
            viaje['mapa'][fila][columna] = 1 
            viaje['asientos_libres'] -= 1
            reserva = {"dni": dni, "viaje": cod_viaje, "asiento": (fila, columna), "monto": viaje['precio']}
            reservas.append(reserva)
            print("¡Reserva confirmada!")
        else:
            print("Asiento ya ocupado.")
    except:
        print("Error: Selección de asiento inválida.")



def aplicar10off(viajes):
    """
    Objetivo: Aplicar 10% de descuento a todos los viajes 
    """
    for cod in viajes:
        viajes[cod]['precio'] *= 0.9
    print("¡Descuento aplicado con éxito!")