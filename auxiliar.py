import re
import json
import os

def validar_dni(dni):
    patron = r"^\d{7,8}$"
    return bool(re.match(patron, dni))

def validar_codigo_viaje(codigo):
    patron = r"^[A-Z]{2}\d{3}$"
    return bool(re.match(patron, codigo))

def normalizar_texto(texto):
    return texto.strip().title()

def obtener_ruta(nombre_archivo):
    ruta_actual = os.path.dirname(__file__)
    return os.path.join(ruta_actual, nombre_archivo)

def guardar_datos(datos, nombre_archivo):
    ruta = obtener_ruta(nombre_archivo)
    try:
        with open(ruta, "w") as archivo:
            json.dump(datos, archivo, indent=4)
    except Exception as e:
        print(f"Ocurrió un error al guardar: {e}")

def cargar_datos(nombre_archivo):
    ruta = obtener_ruta(nombre_archivo)
    try:
        with open(ruta, "r") as archivo:
            return json.load(archivo)
    except Exception as e:
        print(f"Ocurrió un error al cargar: {e}")

def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except Exception as e:
            print(f"Entrada inválida ({e}). Intente de nuevo.")

def leer_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except Exception as e:
            print(f"Entrada inválida ({e}). Ingrese un número decimal.")

