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
    """
    Objetivo: Mostrar por pantalla los viajes cargados.
    Entrada:
    Salida:
    """
    if not viajes:
        print("No hay viajes cargados.")
    else:
        print("\n--- Listado de Viajes ---")
        for viajeCod, datos in viajes.items():
            print(f"Codigo: {viajeCod} | Destino: {datos['destino']} | Fecha: {datos['fecha']} | "
                f"Precio: ${datos['precio']} | Plazas: {datos['plazas']}")

def buscar_viaje(viajes, id_busqueda):
    """
    Objetivo: Busca un viaje por su codigo y lo devuelve.
    """
    return viajes.get(id_busqueda) 


