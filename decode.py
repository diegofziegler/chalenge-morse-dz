# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 13:27:26 2020
@author: DiegoZ

Decodificar un conjunto de bits y pasarlos a código morse.

Voy a asumir lo siguiente como base para el análisis de los bits que lleguen:
    
    1. La duración del punto es la mínima posible.
    
    2. Una raya tiene una duración de aproximadamente tres veces la del punto.
    
    3. Entre cada par de símbolos de una misma letra existe una ausencia de 
       señal con duración aproximada a la de un punto. 
       
    4. Entre las letras de una misma palabra, la ausencia es de aproximadamente
       tres puntos. 
       
    5. Para la separación de palabras transmitidas el tiempo es de 
       aproximadamente tres veces el de la raya.

"""
from bitstring import BitArray
import re

def descomponer_mensaje(mensaje : BitArray) -> []:
    mensaje_interno = []
    patron = re.findall(r'[1]{1,}|[0]{1,}', str(mensaje.bin))
    for simbolo in patron:
        mensaje_interno.append( 
                (simbolo, len(simbolo), None) #tupla: simbolo, longitud, tipo
        )
    return mensaje_interno

def detectar_simbolos(mensaje_interno : [], tolerancia_punto) -> ():
    punto_min=0
    for s in mensaje_interno:
        if s[0][0] == '1':
            punto_min = s[1] if punto_min==0 or punto_min > s[1] else punto_min
    return (punto_min, punto_min+tolerancia_punto)

def armar_mensaje_morse(mensaje_interno : [], 
                        punto: (), raya : (), 
                        separador_simbolo :(), separador_letra : (), separador_palabra : ()
                        ) -> []:
    nuevo_mensaje_interno = []
        
    for s in mensaje_interno:
        final_mensaje = False
        descartar = False
        
        #el simbolo asterisco, no existe para representa gráficamente el código
        #Morse, solo deberíamos usar punto, raya y espacio. ¿Porque agrego un 
        #asterisco? para tener en cuenta que hay algo que no pude reconocer según
        #lo que las reglas morfológicas del código Morse.
        simbolo_morse = '*'
        
        if s[0][0] == '1':
            if s[1] >= punto[0] and s[1] <= punto[1]:
                simbolo_morse = '.' 
            elif s[1] >= raya[0] and s[1] <= raya[1]:
                simbolo_morse = '-' 
                
        elif s[0][0] == '0':
            if s[1] <= separador_simbolo[1]:
                simbolo_morse = '' #separador de símbolo, no imprimo nada
            elif s[1] >= separador_letra[0] and s[1] <= separador_letra[1]:
                simbolo_morse = ' '
            elif s[1] >= separador_palabra[0] and s[1] <= separador_palabra[1]:
                simbolo_morse = '  '
            elif s[1] > separador_palabra[1]:
                final_mensaje = True
                simbolo_morse= '.-.-.-'
            else:
                simbolo_morse= ' ' #separador fuera de largo
            
            #esto lo hice porque no se menciona nada acerca del inicio del mensaje
            if len(nuevo_mensaje_interno) == 0:
                descartar = True
                 
                
        if (not descartar) :
            if( final_mensaje ) :
                nuevo_mensaje_interno.append( ('0', 1, ' ') )
            nuevo_s=(s[0], s[1], simbolo_morse)
            #print(nuevo_s)
            nuevo_mensaje_interno.append( nuevo_s )
        
    return nuevo_mensaje_interno
 
def imprimir_mensaje_morse( mensaje_interno : []) -> str:
    mensaje_morse=''
    for s in mensaje_interno:
        mensaje_morse = mensaje_morse + s[2]
    return mensaje_morse

def decode_bits_2_morse(bit_array : BitArray ) -> str:
    mensaje_interno = descomponer_mensaje(bit_array)
    
    tolerancia_punto = 1
 
    punto = detectar_simbolos( mensaje_interno, tolerancia_punto )
    
    raya = ( punto[0]*3, punto[1]*3 )
    
    separador_simbolo = (
            punto[0]-tolerancia_punto, 
            punto[1])
    
    separador_letra_std =punto[0]*3
    separador_letra = (
            separador_letra_std - tolerancia_punto, 
            separador_letra_std + tolerancia_punto)
    
    separador_palabra = (
            separador_letra[1] + tolerancia_punto, 
            separador_letra[1] + tolerancia_punto)
    
    #print(punto, raya, separador_simbolo, separador_letra, separador_palabra)
    
    mensaje_parseado = armar_mensaje_morse( mensaje_interno, punto, raya, separador_simbolo, separador_letra, separador_palabra ) 
    return imprimir_mensaje_morse(mensaje_parseado)


