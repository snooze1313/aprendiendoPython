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

#todos los objetos de clase str tienen metodos que nos permiten manipularlos, por ejemplo, el metodo upper() convierte una cadena de texto a mayusculas.
hola = "hola mundo"
print(hola.upper())  # Imprime: 'HOLA MUNDO'
hola = hola.upper()  # Asigna el resultado a la variable hola y la convierte a mayúsculas

#tambien hay un metodo llamado islower() que verifica si una cadena de texto esta en minusculas, y devuelve True o False.
es_minusculas = hola.islower()  # Verifica si la cadena está en minúsculas
print(es_minusculas)  # Imprime: false

#la forma de llamar a un metodo es similar a llamar una funcion, pero en este caso se usa el operador punto (.) para acceder al metodo del objeto. en estos casos especificos los metodos no requieren de argumentos.

#cuando escribimos en valor directamente en el codigo, como una cadena de texto o un numero, llamamos a eso una literal o simplemente un literal de ese tipo de dato. por ejemplo, "hola mundo" es un literal de tipo str y 13 es un literal de tipo int.


print("\n------\n")  # separador para mejor visualización
#algunos metodos metodos admiten argumentos al ser llamados, por ejempplo el metodo count() de la clase str, que cuenta el numero incidencias de un caracter o caracteres en una cadena de texto, por ejemplo:
texto = "dale la banana a la mona"
print(texto.count("na"))  # Imprime: cuenta cuántas veces aparece 'na' en la cadena

#tambien podemos hacerlo en una sola linea.
print("dale la banana a la mona".count("a"))  # Imprime: cantidad de veces que aparece 'a' en la cadena

print("\n------\n")  # separador para mejor visualización

#los objetos de la clase int no tienen metodos como upper() o islower() o count(), por lo que tratar de usar esos metodos con un objeto int generara un error.

#sin embargo los objetos de clase int tienen metodos propios, como por ejemplo el metodo bit_length() que devuelve la cantidad de bits necesarios para representar el numero en binario.
numero = 42
print(numero.bit_length())  # Imprime: 6 (porque 42 en binario es 101010, que requiere 6 bits)


print("\n------\n")  # separador para mejor visualización
#los metodos son como funciones ligadas a un tipo de objeto, los atributos son como variables que estan definidas dentro de un objeto. En python los numeros todos los numeros tienen una parte real y una parte imaginiaria, (aunque en la practica estos solo tienen sentido para los numeros complejos), se puede acceder a ambas partes a traves de los atributos real e imag de un objeto de la clase complex.
numero = 42 
print(numero.real)  # Imprime: 42 (parte real del número)
print(numero.imag)  # Imprime: 0 (parte imaginaria del número

#las cadenas de texto no tienen estos atributos y tratar de acceder a ellos generara un error.

#podemos sumar dos objetos de la clase int, y el resultado sera otro objeto de la clase int, por ejemplo:
numero1 = 10
numero2 = 20
suma = numero1 + numero2  # Suma de dos objetos int
print(suma)  # Imprime: 30

#tambien podemos sumar dos objetos de la clase str, y el resultado sera otro objeto de la clase str, por ejemplo:
cadena1 = "Hola "
cadena2 = "Mundo"
suma_cadenas = cadena1 + cadena2  # Concatenación de dos objetos str
print(suma_cadenas)  # Imprime: 'Hola Mundo'

#pero no podemos sumar un objeto de la clase str con un objeto de la clase int, porque son tipos de datos diferentes y no tienen sentido sumar un texto con un numero, esto nos generara un error.

#si queremos sumar un objeto de la clase str con un objeto de la clase int, debemos convertir el objeto int a str primero, por ejemplo:
numero = 42
cadena_numero = str(numero)  # Convertimos el número a cadena

#si queremos sumar un objeto de la clase int con un objeto de la clase str, debemos convertir el objeto str a int primero, por ejemplo:
cadena = "42"
numero_cadena = int(cadena)  # Convertimos la cadena a número

#es importante recordar que los objetos de diferentes clases no se pueden sumar directamente, y debemos convertirlos al mismo tipo de dato antes de realizar la operacion.

#python dispone de una funcion llamada type() que nos permite saber el tipo de dato de un objeto.

#este tipo de clases predefinidas son a las que llamamos clases nativas, y son las que vienen incluidas en el lenguaje por defecto. ademas de estas clases nativas, podemos crear nuestras propias clases, que son plantillas para crear objetos personalizados.