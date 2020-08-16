# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 11:30:41 2020
@author: DiegoZ

hay que instalar éstas librerías...
pip install flask flask-restful

Como probarlo:
    ejecutar de la siguiente forma: py chalenge-restapi.py 
       
    usar curl, postman, etc para tirar éste ejemplo:
        http://127.0.0.1:5000/translate/from-morse/.----%20..---%20...--%20....-%20.....%20-....%20--...%20---..%20----.%20-----
        http://127.0.0.1:5000/translate/to-morse/1234567890

"""
import translate
from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
app.config["DEBUG"] = True
    
@app.route('/translate/from-morse/<codigo_morse>', methods=['GET'])
def translate_from_morse(codigo_morse):
    return jsonify(translate.translate_2_human( codigo_morse ))

@app.route('/translate/to-morse/<mensaje_de_texto>', methods=['GET'])
def translate_to_morse(mensaje_de_texto):
    return jsonify(translate.translate_2_morse( mensaje_de_texto ))   

if __name__ == '__main__':
     app.run(port='5000')