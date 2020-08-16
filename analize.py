# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 13:27:26 2020
@author: DiegoZ

Analiza lo que viene como array de bits. 
No fue pedido en el chalenge, lo use yo para entender como venía el input de 
ejemplo.

"""
from bitstring import BitArray
import re

def detectar_largo_simbolos(mensaje : BitArray, expresion : str) -> {}:
    frecuencia = {}
    patron = re.findall(expresion, str(mensaje.bin))
    for simbolo in patron:
        count = frecuencia.get(simbolo,0)
        frecuencia[simbolo] = count + 1
    return frecuencia

def detectar_largo_uno(mensaje : BitArray) -> {}:
    return detectar_largo_simbolos(mensaje, r'[1]{1,}')

def detectar_largo_cero(mensaje : BitArray) -> {}:
    return detectar_largo_simbolos(mensaje, r'[0]{1,}')

def mostrar_frecuencias(mensaje : BitArray):
    frecuencia_uno = detectar_largo_uno(mensaje)
    frecuencia_list = frecuencia_uno.keys()
    for simbolo in frecuencia_list:
        print( simbolo, frecuencia_uno[simbolo], len(simbolo))

    frecuencia_cero = detectar_largo_cero(mensaje)
    frecuencia_list = frecuencia_cero.keys()
    for simbolo in frecuencia_list:
        print( simbolo, frecuencia_cero[simbolo], len(simbolo))    

