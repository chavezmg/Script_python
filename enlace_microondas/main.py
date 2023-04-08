"""
Script para cálculos básicos para enlaces de microondas
"""

import math

K = 1.38e-23

def conversor_w_dbm(value, dB=False):
    """Convierte entre watts y dB y viceversa, utilizar el segundo argumento para elegir
    """
    if not dB:
        return (10**(value/10)/1000)
    else:
        return 10*math.log10((value)/0.001)
        
def umbral_ruido(B, db=False):
    """
    Funcion para calcular el umbral de ruido a Temperatura estandar (17 grados), B=ancho de banda en MHz
    El segundo parametro determina el resultado en Watts o dB
    """
    if not db:
        return f"{290 * K * (B*1e6)} Watts"
    else:
        return f"{10*math.log10((290 * K * (B*1e6))/0.001)} dB"

def sensibilidad(SNRi, Pni):
    """
    Pni y SNRi deben estar en dB
    resultado en dB
    """
    return SNRi+Pni


