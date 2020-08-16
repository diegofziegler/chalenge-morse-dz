# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 13:27:26 2020
@author: DiegoZ

Funciones para obtener el código Morse a partir de un conjunto de bits. Y para
mostrar la traducción de un mensaje en código morse.

Insrucciones:
hay que tener python,yo tengo éste: Python 3.6.4 :: Anaconda custom (64-bit)

hay que instalar éstas librerías... 
    pip install argparse    
    pip install bitstring

para que funcione, deben estar en el msmo directorio 
    translate.py, decode.py, analize.py y chalenge-funciones-meli.py
    
para armar los input de prueba:
    https://onlinetexttools.com/join-text

Ejemplos de ejecución:
    py chalenge-funciones-meli.py 000000001101101100111000001111110001111110011111100000001110111111110111011100000001100011111100000111111001111110000000110000110111111110111011100000011011100000000000
    py chalenge-funciones-meli.py 101010001110111011100010101
    py chalenge-funciones-meli.py 11110110110000110110000110000111101111001000011110111101111000000
    py chalenge-funciones-meli.py 0000001011101110111011100001010111011101110000010101011101110000001010101011100000101010101000000111010101010000011101110101010000111011101110101000011101110111011101000001110111011101110111000000000
    py chalenge-funciones-meli.py 000000101110111011101110000010010011100111001110000010101011101110000010101010111000001101101010110000011101010101000001110111010101000001110111011101010000011101110111011101000001110111011101110111000000000
"""
import sys
from bitstring import BitArray, BitStream
import decode
import translate
import analize
import argparse



def main() -> None :
    cmd_parser = argparse.ArgumentParser(
            description='recibir un array de bits e interpretarlo como un mensaje en código morse'
            )
    
    cmd_parser.add_argument('bits',
                           metavar='bits',
                           type=str,
                           help='el conjunto de bits a traducir')

    args = cmd_parser.parse_args()
    
    bits_linea_de_comandos = args.bits
    
    #no es muy amigable, podría indicar como utilizar el programa manualmente
    if len(bits_linea_de_comandos) <= 0:
        sys.exit()
    
    try:
        
        mensaje_en_bits = BitArray('0b' + bits_linea_de_comandos)
        print( analize.mostrar_frecuencias(mensaje_en_bits) )
        
        codigo_morse = decode.decode_bits_2_morse( mensaje_en_bits )
        print( codigo_morse )         
         
        traduccion = translate.translate_2_human( codigo_morse )
        print( traduccion )
        
        mensaje_original = translate.translate_2_morse( traduccion, True )
        print( mensaje_original )
        
    except:
        print(f"Ocurrió un error iterpretando la cadena de bits proporcionada.", file=sys.stderr)


    
if __name__ == "__main__":
    main()
    
    