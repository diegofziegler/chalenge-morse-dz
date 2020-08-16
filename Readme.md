#Ejemplo código morse

##Importante

Voy a asumir lo siguiente como base para el análisis de los bits que lleguen:
    
    1. La duración del punto es la mínima posible.
    
    2. Una raya tiene una duración de aproximadamente tres veces la del punto.
    
    3. Entre cada par de símbolos de una misma letra existe una ausencia de 
       señal con duración aproximada a la de un punto. 
       
    4. Entre las letras de una misma palabra, la ausencia es de aproximadamente
       tres puntos. 
       
    5. Para la separación de palabras transmitidas el tiempo es de 
       aproximadamente tres veces el de la raya.
 
Al traducir hacia o desde código morse, convierto en mayúsculas y solamente estamos soportando las siguientes letras y números:
A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,0,1,2,3,4,5,6,7,8,9

##Cosas para mejorar

Algunos nombres están escritos mezclando inglés y español. Los endpoints podrían tener un nmbre mejor, pero los armé de forma que fueran más claros.
      

##chalenge-funciones-meli.py

Contiene la primera parte del ejercicio con las 2 funciones solicitadas. Para probarlo manualmente se pueden ejecutar éstos ejemplos:

    py chalenge-funciones-meli.py 000000001101101100111000001111110001111110011111100000001110111111110111011100000001100011111100000111111001111110000000110000110111111110111011100000011011100000000000
    py chalenge-funciones-meli.py 101010001110111011100010101
    py chalenge-funciones-meli.py 11110110110000110110000110000111101111001000011110111101111000000
    py chalenge-funciones-meli.py 0000001011101110111011100001010111011101110000010101011101110000001010101011100000101010101000000111010101010000011101110101010000111011101110101000011101110111011101000001110111011101110111000000000
    py chalenge-funciones-meli.py 000000101110111011101110000010010011100111001110000010101011101110000010101010111000001101101010110000011101010101000001110111010101000001110111011101010000011101110111011101000001110111011101110111000000000

Una manera de armar el "string de bits" que puede resultar útil es desde ésta página: 
    https://onlinetexttools.com/join-text
tipear las palabras binarias que representan al código morse, luego unir (join) las líneas sin separador, y de esa forma podes armar la línea de comandos para pruebas.

##chalenge-restapi.py

Contiene la segunda parte, es decir los dos endpoints solicitados

Para ejecutar localmente, hayque hacer lo siguiente:

    py chalenge-restapi.py 
       
... luego se puede usar curl, postman, etc para tirar éste ejemplo:

    http://127.0.0.1:5000/translate/from-morse/.----%20..---%20...--%20....-%20.....%20-....%20--...%20---..%20----.%20-----
    http://127.0.0.1:5000/translate/to-morse/1234567890

##analize.py

No fueron pedidas en el chalenge,yo las hice para entender como trabajar cuando los puntos, rayas y separadores van teniendo distintas longitudes

