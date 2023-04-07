"""
This script shutdowns the PC in the hour and minutes specified via hora_apagado and minutos_apagado
"""

import time
import os

hora = list(time.gmtime())[3] - 3
minutos = list(time.gmtime())[4]

def shut(hora_apagado, minutos_apagado=0):
    while (hora < hora_apagado & minutos < minutos_apagado):
        hora = list(time.gmtime())[3] - 3
        minutos = list(time.gmtime())[4]
        time.sleep(55)
    os.system("shutdown /s /t 1")
