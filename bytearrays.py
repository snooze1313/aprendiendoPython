#los objetos bytearray son la version mutable de los objetos de la clase bytes, es decir, secuencias mutables de enteros entre 0 y 256.

#se definnen por medio de la funcion bytearray() que, ejecutada sin argumentos, crea un objeto bytearray vacio, y si se le pasa un numero entero, retornara un objeto bytearray que contendra todos los ceros como indique ese numero.

#se le pueden pasar como argumento un objeto bytes, con lo que retornnaremos un objeto bytearray con sus elementos.

#se le puede pasar un objeto string, en cuyo caso se requiere un segundo argumento para indicar la codificacion que debe usar la cadena y, opcionalmente, un tercer argumento que indique que hacer ante un error de codificacion y que, al igual que en la funcion bytes(), puede ser ignore, replace o strict.

#strict: Es la opcion por defecto que lanza una excepcion unicodeerror
#ignore: Ignora los caracteres que han producido el error de codificacion
#replace: reemplaza el caracter que ha producido el error con un signo de interrogacion

numeros = bytearray([68, 69, 70, 71])
print(numeros) #bytearray(b'DEFG')

numeros[2] = 77 #cambianos el valor del tercer elemento 
print(numeros) #bytearray(b'DEMG')
