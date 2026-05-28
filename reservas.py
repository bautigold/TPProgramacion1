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


def aplicar_descuento_masivo(viajes):
    for cod in viajes:
        viajes[cod]['precio'] = (lambda p: p * 0.9)(viajes[cod]['precio'])
    print("Se aplicó un 10% de descuento a todos los viajes.")

def calcular_recaudacion_total(reservas):
    if not reservas: return 0
    total = reduce(lambda acumulado, res: acumulado + res['monto'], reservas, 0)
    return total

