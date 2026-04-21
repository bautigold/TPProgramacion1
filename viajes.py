def cargar_viaje(viajes):
    """
    Objetivo: Cargar datos de un nuevo viaje
    Entrada:
    Salida:
    """
    viajeCod = input("Ingrese el código del viaje: ")
    if viajeCod in viajes:
        print("Ese código ya fue cargado antes.")
        return

    destino = input("Ingrese el destino: ")
    fecha = input("Ingrese la fecha: ")
    precio = float(input("Ingrese el precio: "))
    asientos = int(input("Ingrese la cantidad de asientos: "))

    viajes[viajeCod] = {
        "destino": destino,
        "fecha": fecha,
        "precio": precio,
        "asientos": asientos 
    }
    print(f"Viaje a {destino} cargado")


def mostrar_viajes(viajes):
    """
    Objetivo: Mostrar los viajes cargados
    Entrada:
    Salida:
    """
    if not viajes:
        print("No hay viajes cargados")
    else:
        print("\nListado de Viajes")
        for codigo, datos in viajes.items():
            print(f"Código: {codigo}  Destino: {datos['destino']}  Asientos: {datos['asientos']}")



def buscar_viaje(viajes, viajeCod):
    """
    Objetivo: Busca un viaje por su código
    Entrada:
    Salida:
    """
    return viajes.get(viajeCod)