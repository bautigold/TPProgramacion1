from auxiliar import *
from reservas import *
from viajes import *

def test_validar_dni():
    assert validar_dni("12345678") == True
    assert validar_dni("9512345") == True
    assert validar_dni("123") == False 
    assert validar_dni("123456789") == False 
    assert validar_dni("letras12") == False 

def test_validar_codigo_viaje():
    assert validar_codigo_viaje("AR101") == True
    assert validar_codigo_viaje("ar101") == False 
    assert validar_codigo_viaje("A101") == False 
    assert validar_codigo_viaje("ARG10") == False

def test_normalizar_texto():
    assert normalizar_texto("  bariloche  ") == "Bariloche"
    assert normalizar_texto("SALTA") == "Salta"
    assert normalizar_texto("mendoza") == "Mendoza"

def test_calcular_recaudacion_total():
    reservas_prueba = [
        {"monto": 100.0},
        {"monto": 250.0},
        {"monto": 50.0}
    ]
    total = calcular_recaudacion_total(reservas_prueba)
    assert total == 400.0
    assert calcular_recaudacion_total([]) == 0

def test_inicializacion_matriz_asientos():
    filas = 5
    columnas = 4
    matriz = [[0 for columna in range(columnas)] for fila in range(filas)]
    assert len(matriz) == 5                    
    matriz = 1

def test_acceso_diccionario_viajes():
    dicViajes_prueba = {
        "AR101": {"destino": "Bariloche", "precio": 5000.0}
    }
    
    viaje = dicViajes_prueba.get("AR101")
    assert viaje["destino"] == "Bariloche"
    assert dicViajes_prueba.get("ERROR") == None

