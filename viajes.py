from auxiliar import *
CATEGORIAS = ("Económico", "Business", "Primera Clase")

def cargar_viaje(viajes):
    print("\n REGISTRO DE NUEVO VIAJE ")    
    try:
        codigo = input("Ingrese el código del viaje (Ej: AR101): ").upper()        
        if not validar_codigo_viaje(codigo):
            print("Error: Formato de código inválido.")
            return
        if codigo in viajes:
            print(f"El código {codigo} ya existe.")
            return
        destino = normalizar_texto(input("Ingrese Ciudad de Destino: "))
        precio = leer_float("Ingrese el precio del pasaje: ")
        print("Categorías disponibles:")
        for i in range(len(CATEGORIAS)):
            print(f"{i} - {CATEGORIAS[i]}")        
        idCat = leer_entero("Seleccione el número de categoría: ")
        if idCat < 0 or idCat >= len(CATEGORIAS):
            print("Categoría inexistente. Se asignará 'Económico' por defecto.")
            cat_seleccionada = CATEGORIAS[0]
        else:
            cat_seleccionada = CATEGORIAS[idCat]
        asientos = [[0 for columna in range(4)] for fila in range(5)]        
        viajes[codigo] = {
            "destino": destino,
            "precio": precio,
            "categoria": cat_seleccionada,
            "matriz_asientos": asientos,
            "libres": 20
        }
        guardar_datos(viajes, "viajes.json")
        print(f"Viaje a {destino} cargado con éxito.")
    except Exception as e:
        print(f"Error al cargar el viaje: {e}")



def mostrar_viajes(viajes):
    if not viajes:
        print("\nNo hay viajes registrados.")
        return
    print("\n LISTADO DE VIAJES ")
    for cod, datos in viajes.items():
        linea = f"CÓDIGO: {cod} - DESTINO: {datos['destino']} - PRECIO: ${datos['precio']:.2f} - LIBRES: {datos['libres']}"
        print(linea)
    


def mostrar_mapa_asientos(viaje):
    print(f"\nMapa de asientos para: {viaje['destino']}")
    matriz = viaje["matriz_asientos"]
    
    for fila in range(len(matriz)):
        print(f"Fila {fila}: {matriz[fila]}")
    print("(0 = Libre, 1 = Ocupado)")

def obtener_destinos_unicos(viajes):
    destinos = {datos['destino'] for datos in viajes.values()}
    print(f"\nDestinos cubiertos: {destinos}")
    return destinos


def obtener_viajes_disponibles(viajes):
    viajes_con_cupo = list(filter(lambda item: item[1]["libres"] > 0, viajes.items()))
    
    if not viajes_con_cupo:
        print("No hay viajes con asientos disponibles.")
    return viajes_con_cupo


