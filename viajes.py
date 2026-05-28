from auxiliar import *
CATEGORIAS = ("Económico", "Business", "Primera Clase")

def cargar_viaje(viajes):
    """
    Objetivo: Registrar un nuevo viaje en la base de datos (Hito 40/100%).
    """
    try:
        print("\nREGISTRO DE NUEVO VIAJE")
        viajeCod = input("Ingrese el código del viaje (Ej: AR101): ").upper()
        
        if not validar_codigo_viaje(viajeCod):
            print("Error: Formato de código inválido (debe ser 2 letras y 3 números).")
            return
        
        if viajeCod in viajes:
            print("Error: El código de viaje ya existe.")
            return

        destino = normalizar_texto(input("Ingrese el destino: "))
        precio = float(input("Ingrese el precio del pasaje: "))
        
        print("Seleccione la categoría del transporte:")
        for i in range(len(CATEGORIAS)): 
            print(f"{i} {CATEGORIAS[i]}")
        
        opcion_cat = int(input("Opción: "))
        categoria = CATEGORIAS[opcion_cat]

        mapa_asientos = [[0 for columna in range(4)] for fila in range(5)]
        
        viajes[viajeCod] = {
            "destino": destino,
            "precio": precio,
            "categoria": categoria,
            "mapa": mapa_asientos,
            "asientos_libres": 20
        }
        print(f"¡Viaje a {destino} ({categoria}) cargado exitosamente!")
        
    except ValueError:
        print("Error: El precio y la opción deben ser valores numéricos.")
    except IndexError:
        print("Error: La opción de categoría seleccionada está fuera de rango.")

def mostrar_viajes(viajes):
    """
    Objetivo: Mostrar todos los viajes registrados con f-strings [15].
    """
    if not viajes:
        print("No hay viajes registrados en el sistema.")
        return
    else:    
        print("\nLISTADO DE VIAJES")
        for cod, datos in viajes.items():
            print(f"[{cod}] {datos['destino']} | Cat: {datos['categoria']} | Precio: ${datos['precio']:.2f} | Libres: {datos['asientos_libres']}")

def buscar_viaje(viajes, cod):
    """
    Objetivo: Buscar un viaje específico por su clave única.
    """
    return viajes.get(cod)

def obtener_destinos_unicos(viajes):
    """
    Objetivo: Obtener un reporte de ciudades sin repeticiones (Alcance 100%).
    """
    destinos = {datos['destino'] for datos in viajes.values()}
    print(f"Ciudades cubiertas actualmente: {destinos}")
    return destinos

def obtener_viajes_disponibles(viajes):
    """
    Objetivo: Filtrar viajes que aún no están completos.
    """
    viajes_con_cupo = list(filter(lambda item: item[21]['asientos_libres'] > 0, viajes.items()))
    return viajes_con_cupo