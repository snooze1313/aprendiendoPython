#en python los datos se representan como objetos, los objetos son abstracciones que podemos vizualizar como una estructura logica que puede almacenar unos datos (que dependeran del tipo de objeto) y unos metodos que nos permiten manipular esos datos (que dependeran del tipo de objeto).

#una clase es una especie de plantilla a partir de la cual definimos un objeto, todas las cadenas de texto son similares y tienen los mismos metodos y atributos, aunque el texto concreto de cada una de ellas sea distinto, porque todas pertenecen a la misma clase.

#cuando creamos un objeto a partir de una clase, decimos que estamos instanciando un objeto o creando una instancia de esa clase.


#por ejemplo: el texto "hola mundo" se representa en python mediante un objrto str(string), que es la clase que define las cadenas de texto, mientras que el numero 47 es un objeto int(integer), que es la clase que define los numeros enteros.

#para crear un objeto str a partir de un objeto int usamos la funcion str() pasandole un objeto int.
cadena = str(13)
print(cadena)  # Imprime: '13'

#estas son tres formas de mostrar un numero 13 en string
cadena1 = str(13)
cadena2 = "13"
cadena3 = '13'

