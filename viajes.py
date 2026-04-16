def cargar_viaje(viajes):
    """
    Objetivo: Cargar datos de un nuevo viaje y agregarlo 
    Entrada: 
    Salida: 
    """
    viajeCod = input("Ingrese el codigo del viaje: ")
    
    if viajeCod in viajes:
        print("El codigo ya fue cargado antes.")
        return

    destino = input("Ingrese el destino: ")
    fecha = input("Ingrese la fecha: ")
    precio = float(input("Ingrese el precio: "))
    asientos = int(input("Ingrese la cantidad de asientos: "))

    viajes[viajeCod] = {
        "destino": destino,
        "fecha": fecha,
        "precio": precio,
        "plazas": asientos
    }
    print(f"Viaje a {destino} cargado con éxito.")
    

def mostrar_viajes(viajes):
    return

def buscar_viaje(viajes, id_busqueda):
    return 


