import re 

def validar_dni(dni):
    """
    Objetivo: Validar que el DNI tenga 7 u 8 dígitos numéricos
    """
    patron = r"^\d{7,8}$" 
    return bool(re.match(patron, dni))