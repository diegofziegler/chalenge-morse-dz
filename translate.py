# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 13:27:26 2020
@author: DiegoZ

Traducir un mensaje en código Morse a letras del alfabeto segpun la tabla de 
traducción.

"""

#este diccionario lo utilizo para traducir de morse a letras delalfabeto.
diccionario_morse = {
     '.-':'A',
     '-...':'B',
     '-.-.':'C',
     '-..':'D',
     '.':'E',
     '..-.':'F',
     '--.':'G',
     '....':'H',
     '..':'I',
     '.---':'J',
     '-.-':'K',
     '.-..':'L',
     '--':'M',
     '-.':'N',
     '---':'O',
     '.--.':'P',
     '--.-':'Q',
     '.-.':'R',
     '...':'S',
     '-':'T',
     '..-':'U',
     '...-':'V',
     '.--':'W',
     '-..-':'X',
     '-.--':'Y',
     '--..':'Z',
     '-----':'0',
     '.----':'1',
     '..---':'2',
     '...--':'3',
     '....-':'4',
     '.....':'5',
     '-....':'6',
     '--...':'7',
     '---..':'8',
     '----.':'9',
     '.-.-.-':''  #'<fin>'
     }

#este diccionario lo utilizo para transformar de letras a morse
diccionario_letras_a_morse = {}

def armar_diccionario_letras() -> {}:
    """
    Doy vuelta el diccionario Morse para que sea más facil traducir de letras 
    a morse.
    Lo único que hay que hacer es llamar a la función,y si nunca cargó el 
    diccionario inverso, lo va a hacer.
    """
    if len(diccionario_letras_a_morse) == 0:
        claves = diccionario_morse.keys()
        for k in claves:
            diccionario_letras_a_morse[ diccionario_morse[k] ] = k
    return diccionario_letras_a_morse
        


def translate_2_human(morse_str : str) -> str:
    """ Traducir un string que contien simbolos en código morse.
    Parametros:
        morse_str : string para taducir
    Retorna:
        un string que se puede leer fácilmente.
    """
    traduccion = []
    morse_array = morse_str.split(' ')
    for m in morse_array:
        if m in diccionario_morse:
            x = diccionario_morse[m]
        else :
            x = ' '
        traduccion.append(x)
    return ''.join(traduccion)


def translate_2_morse(human_readable_str : str, incluir_fullstop : bool = True) -> str:
    """ Traducir un mensaje de texto a a código morse. Solo soporta las letras
    que actualmente tenemos en la tabla y las palabras van separadas por 
    espacios.
    
    Parametros:
        human_readable_str : string para convertir en codigo morse
    Retorna:
        un string en codigo morse.
    """
    diccionario = armar_diccionario_letras()
    lista_codigo_morse=[]
    palabras = human_readable_str.split(' ')
    for palabra in palabras:
        for letra in palabra:
            if (not (letra == None)) and letra.upper() in diccionario:
                lista_codigo_morse.append( diccionario[ letra.upper() ] )
            else:
                lista_codigo_morse.append( letra )
    
    if incluir_fullstop:
        lista_codigo_morse.append( diccionario[''] )
        
    return ' '.join( lista_codigo_morse )

