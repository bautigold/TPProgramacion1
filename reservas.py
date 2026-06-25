from functools import reduce
from auxiliar import *
from viajes import mostrar_mapa_asientos


def realizar_reserva(viajes, pasajeros, reservas):
    print("\n NUEVA RESERVA ")    
    dni = input("Ingrese el DNI del pasajero: ")
    if dni not in pasajeros:
        print("Error: El pasajero no está registrado. Debe cargarlo primero.")
        return
    codigo = input("Ingrese el código del viaje: ").upper()
    if codigo not in viajes:
        print("Error: El viaje ingresado no existe.")
        return
    viaje = viajes[codigo]
    if viaje["libres"] == 0:
        print(f"Lo sentimos, el viaje a {viaje['destino']} está completo.")
        return
    mostrar_mapa_asientos(viaje)    
    print("\nSeleccione su asiento:")
    fila = leer_entero("Ingrese numero de fila (0-4): ")
    columna = leer_entero("Ingrese numero de columna (0-3): ")
    if (fila < 0 or fila > 4) or (columna < 0 or columna > 3):
        print("Error: Coordenadas de asiento fuera de rango.")
        return
    if viaje["matriz_asientos"][fila][columna] == 1:
        print("Error: Ese asiento ya se encuentra ocupado.")
        return
    try:
        viaje["matriz_asientos"][fila][columna] = 1
        viaje["libres"] -= 1
        nombre, apellido = pasajeros[dni]["identidad"]
        nueva_reserva = {
            "dni": dni,
            "pasajero": f"{apellido}, {nombre}",
            "viaje": codigo,
            "destino": viaje["destino"],
            "asiento": (fila, columna), 
            "monto": viaje["precio"]
        }
        reservas.append(nueva_reserva)
        guardar_datos(viajes, "viajes.json")
        guardar_datos(reservas, "reservas.json")        
        print(f"Reserva confirmada para {nombre} {apellido} en el asiento ({fila},{columna}).")
        
        with open("pasaje.txt", "w") as pasaje:
            pasaje.write(f"Pasajero: {nueva_reserva['pasajero']}\n")
            pasaje.write(f"Destino: {nueva_reserva['destino']}\n")
            pasaje.write(f"Asiento: Fila {fila} - Columna {columna}\n")
            pasaje.write(f"Monto: ${nueva_reserva['monto']}\n")

        print("Archivo de pasaje generado exitosamente.")

    except Exception as e:
        print(f"Error al procesar la reserva: {e}")

    
##Añade función de archivos para generar un pasaje

def mostrar_reservas(reservas):
    if not reservas:
        print("\nNo hay reservas registradas en el sistema.")
        return
    print("\n LISTADO DE RESERVAS ")
    for res in reservas:
        f, c = res["asiento"]
        linea = f"Pasajero: {res['pasajero']} - Destino: {res['destino']} - Asiento: F{f}-C{c} - Monto: ${res['monto']:.2f}"
        print(linea)


def calcular_recaudacion_total(reservas):
    if not reservas:
        return 0.0
    montos = [res["monto"] for res in reservas]
    total = reduce(lambda acumulado, actual: acumulado + actual, montos)    
    print(f"\nRecaudación total del sistema: ${total:.2f}")
    return total


##Añade función para calcular la recaudación total del sistema usando funciones lambda y reduce.

