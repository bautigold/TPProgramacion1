import re

def validar_dni(dni):
    patron = r"^\d{7,8}$"
    return bool(re.match(patron, dni))

def validar_codigo_viaje(codigo):
    patron = r"^[A-Z]{2}\d{3}$"
    return bool(re.match(patron, codigo))

def normalizar_texto(texto):
    return texto.strip().title()