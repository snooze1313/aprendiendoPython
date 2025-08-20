#todos los lengiuajes de programacion siponen de tipos de datos basicos con los que operar, estos tipos nativos varian entre lenguajes, pero casi todos incluyen uno o mas tipos numericos y alguna forma de codificar cadenas de texto.

#python  es asi, pero cuenta cuenta con el matiz de que todos los datos son objetos y esos tipos basicos son clases.


#cadenas de texto
#en python cuna cadena de texto o tambien llamada string es  tecnicamente un objeto str, es una secuencia de caracteres que lo comprende letras, numeros, simbolos y espacios en blanco. las cadenas de texto se definen encerrando el texto entre comillas simples o dobles (teniendo en cuenta que pythom soporta UFT-8).
cadena1 = "Hola, mundo!"

#cuando hay dos o mas cadenas de texto separadas por espacios, python las interpreta como una sola cadena de texto.
cadena2 = "Hola," " mundo!" " python es genial!"
print(cadena2)


print("\n---------\n")#seperador

#disponer de ambos tipos de comillas permite incluir una dentro de la otra sin necesidad de usar el caracter de escape.
cadena3 = "Hola, 'mundo'!"
cadena4 = 'Hola, "mundo"!'
print(cadena3)
print(cadena4)

print("\n---------\n")#seperador

#podemos solatar de linea una cadena de texto con el caracter de escape \n, que indica un salto de linea.
print("Hola, mundo!\nPython es genial!")

#otros caractertes de escape son:
#\a #alerta ASCII Bell 
#\b #retroceso
#\f #salto de pagina
#\n #salto de linea
#\r #retorno de carro
#\t #tabulacion horizontal
#\v #tabulacion vertical

print("\n---------\n")#seperador

#podemos usar el prefijo f para crear cadenas de texto formateadas, que permiten incluir variables o expresiones dentro de la cadena. la f es de formatted string.
nombre = "juan"
edad = 30
print(f"Hola, {nombre}! Tienes {edad} años.")

print("\n---------\n")#seperador

#esto tambien pede ser usado con funciones, operaciones, metodos o con cualquier expresion que retorne un valor.
print (f"El resultado de 2 + 3 es {2 + 3}.")
print(f"hola soy {nombre.upper()} y tengo {edad} años.")
print(f"la variable nombre es de tipo: {type(nombre)})")

#las variables pueden ser declaradas como cadena de texto sin tener que meter texo.
cadena5 = str() #esto crea una cadena de texto vacia, que es un objeto str.

print("\n------\n")#separador

#independientemente de como hayamos declarado las variables podemos concatenarlas usando (+)
saludo = "hola"
nombre = "juan"
print(saludo + " " + nombre) #imprime la frase "hola juan"

#no se pueden concatenar strings y numeros por lo que se debera transformar los numeros en str.
print(nombre + " tiene " + str(edad) + " a;os") #se transformo en str la edad con el metodo str()


print("\n------\n") #separador

#podemos hacer multiplicaciones de string con el operador *
print("hola " *  3) #imprime hola 3 veces


print("\n------\n") #separador

#la clase string tiene varios metodos como: upper(), lower(), title(), capitalize().
frase_pablo = "hola, soy plablo y estoy de paso"
print(frase_pablo.upper()) #hace mayusculas toda la cadena
print(frase_pablo.lower()) #hace minuscula toda la cadena
print(frase_pablo.title()) #hace mayuscula la primera letra de cada palabra
print(frase_pablo.capitalize()) #hace mayuscula la primera letra de la cadena

print("\n------\n") #separador

#el metodo stripe regresa una copia de la cadena pero sin los espacios (los tabs cuentan como espacio, junto con los \n) de el principio y el final
cadena = "  hola  mundo- "
#tab aqui --
print(cadena.strip())

#se pueden pasar un argumento
print(cadena.strip(" hol"))

#puedes hacer que inicie al revez
print(cadena.rstrip("o- "))


print("\n------\n") #separador


#el metodo replace retorna una copia de una cedena de texto y reemplaza las coincidencias que fueron asignadas como argumento
cadena = "una rosa es una rosa"
print(cadena.replace("rosa", "margarita"))

#un metodo bastante util es format(), admite tantos argumentos como sean necesarios.
cadena = "Hola, soy {}".format("pablo")
print(cadena)

print("\n------\n") #separador

#al ser format un metodo y no una convencion de formato como f-string, no estas limitado cadenas de texto, sino que puedes usar variables.
nombre = "pablo"
cadena = "hola, soy {}".format(nombre)
print(cadena)

plantilla = "Hola, soy{}"
resultado = plantilla.format(nombre)

print("\n------\n") #separador

#se puede usar varios espacios marcado con {} las cuales seran llenadas con los argumentos que se les pase, si se les pasa mas argumentos de los especificados dara error.
nombre = "plablo"
masacota = "un gato"
cadena = "hola soy {} y mi masacota es {}".format(nombre, masacota)
print(cadena)

print("\n------\n") #separador

#se puede identar las llaves de este modo iniciando por cero: {0}, {1}, etc.
cadena = "hola soy {1} y mi masacota es {0}".format(nombre, masacota)
print(cadena) #las variables se invierten e imprime la variable masacota primero y nombre despues

print("\n------\n") #separador

#de mismo modo puede usar argumentos como:
cadena = "hola soy {a} y mi masacota es {b}".format(a = nombre, b = masacota)
print(cadena)

print("\n------\n") #separador

#bytes
#otro prefijo que podemos usar es "b" o "B", que indica que lo que estamos definiendo no es una cadena de texto normal (un objeto str), sino una cadena de bytes (un objeto de la clse bytes).
#las cadenas de bytes solo admiten caracteres ASCII
b"Esto es una cadena de bytes"

#en ese sentido las cadena de bytes son una secuencia de numero enteros que van del 0 al 256 no caracteres. El que los bytes se pueden representar como una literalnos facilita su uso.

#al igual que con string tenemos el metodo str(), en bytes tenemos el metodo bytes(), con la salvedad de que no todos los objetos tienen una representacion en bytes.

print(bytes()) #imprime una cadena de bytes de longitud cero, literalmente b''.

#si se le pasa com argumento un numero entero como 3, retornara un objeto de tipo byte con tantos ceros como indique ese numero.
print(bytes(3)) #imprime: b'\x00\x00\x00'

#se puede pasar como argumento una cadena de texto, cuyo caso necesitara el argumento "utf-8" o "ascii"
print(bytes("hola mundo", "utf-8")) #imprime: b'hola mundo'

print("\n------\n") #separador


#cadena y bytes como secuencia
#los objetos de tiipo str son secuencias de caracteres unicode, mientras que los de tipo bytes son secuencias de bytes. 
#para leer un caracter individual de una cadena de caracteres, ponemos unos corchetes ([]), por ejemplo:
print("hola"[0]) #imprime la primera letra de la cadena

saludo = "hola"
print(saludo[2]) #imprime la tercera letra
print(saludo[3]) #imprime la cuarta letra
#el indice comienza desde 0, y no se puede poner un indice mayor a la cantidad de los caracteres menos 1.

print("\n------\n") #separador

#En el caso de los bytes se puede hacer lo mismo.
print(b"hola"[1]) #imprime la primera letra de la cadena
saludo = b"hola mundo"[8]
print(saludo)

print("\n------\n") #separador

#numeros enteros
#en python, el formato numerico elemental es el numero entero (clase int), los numeros enteros son aquellos que tienen parte entera y se pueden representar simplemente escribiendo el numero, sin comillas ni ningun tipo de marcador.
4
75
1000

#no se pueden usar comas, puntos o espacios para separar las distintas magnitudes (miles, millones, etc), pero python permite usar el signo (_) para agrupar cifras:
1_000_000
25_32_12_86
1_2_3
#los guiones bajos son solo para que el codigo resulte mas legible, el interprete de python simplemente lo ignorara, por lo que estos numeros son identicos para python:
1000000
1_000_000
10_00_00_0
1_0_0_0_0_0_0

print("\n------\n") #separador

#cuando representamos un literal numerico en el formato decimal el primer digito no puede ser un cero osaltara un error.
#ademas del sistema decimal, podemos usar otras bases para escribir nuestros nuimero.
#El formato binario es aquel que emplea 1 y 0. Se indica que un numero esta representado precediendo de un cero y una "b" mayuscula o minuscula.
0b111110
0B10000
0b1_0_0

#el formato octal, que usa los digitos del 0 al 8, se representa poniendo un cero y una "o" mayuscula o minuscula:
0o547
0O5320
0o3_64

#El formato hexadecimal usa los dieciseis digitos. Para representar los digitos por encima del 9 se usa las letras "a" a la "F" (en mayusculas o minusculas, aunque es preferible usar las mayusculas). Para indicar que el numero esta en base hexadesimal, se antepone el cero seguido de la letra "x", en mayusculas o minusculas.
0X17B5
0xF0B6
0xA9_01_4B

#Es importante tener en cuenta que, aunque representemos una literal numerico en formato binario, octal, hexadesimal, python almacena los numeros enteros como el mismo tipo de objeto numerico, por lo que estas cuatro expresiones mostraran lo mismo.
print(42)
print(0B101010)
print(0O052)
print(0X2A)

#independiente mente del tipo de base se pueden indicar numeros negativos.
-42
-0B101010
-0O052
-0X2A


print("\n------\n") #separador

#se puede definir un numero intexplicitamente con la funcion int(), invocado sin ningun argumento retornara 0.
#cuando se le pasa como argumento un numero decimal, este redondeara hacia abajo. cuando se le pasa un numero binario, octal o hexadecimal lo retornara como entero.
print(int()) #imprime 0

print(int(3.1416)) #imprime 3
num = int(2 + 6)
print(num)
num = int("1000", 2)
print(num)
num = int("0O62", 0)
print(num)


print("\n------\n") #separador

#numero flotantes
#Para representar un numero de coma flotante (de la clase float), tenemos que agregar un punto (.) seguido de la parte de punto flotante.
4.5
-12.98
3.1416
1.0
0.0
#al igual que int podemos usar "_" para mejorar la legibilidad.
#al igual que la notacienon cientifica la podemos representar con una "e" minuscula o mayuscula, seguido del orden de magnitud.(es decir la potencia 10 por la que se multiplica).
1e1_000
3.14e-4
0E0
-1E1

#podemos obtener numeros float de forma explicita mediante la funcion float(). Si se ejecuta sin argumento, retornara un cero de tipo flotante. si le pasamos un numero lo retornara de tipo float. al igual si le pasamos numeros del tipo str o byte.
print(float())
print(float(1/2))
print(float('1983.4'))
print(float("1.4e3"))


print("\n------\n") #separador


#numeros complejos
#python tiene una tercera clase de numeros menos utilizada, se trata de los numeros completos de la clase complex, y se usa para representar aquellos numeros imaginiarios.
#serepresentan en la forma 4 + 5j, donde el numero anterior al signo + es la oparte real, y el numero posterior debe terminar en j mayusculas o minusculas, es la parte imaginaria. si la parte imaginario es negativa, el signo debe ser un -, como el siguiente ejemplo: 4 - 5j.
12 + 6j
3 + 4j
4.0 - 0j
0j
23.9j

#se pueden generar numeros complejos con la funcion complex(), sin argumentos esta retornara 0j, si se le retorna un argumento numerico retornara ese valor en el tipo complejo, como ocurre con todos los valores numericos se puede usar _ para mejorar la legibilidad.
print(complex(3.4))
print(complex(239))
print(complex(0))
print(complex(7e9))


print("\n------\n") #separador

#tambien funciona si se le pasa como argumento una cadena de texto numerica
print(complex("3.4"))
print(complex("239"))
print(complex("0"))
print(complex("7e9"))


print("\n------\n") #separador

#si se le pasa como argumento un numero, este sera usado como la parte imaginaria
print(complex(3, 7))
print(complex(0, 21))
print(complex(10, 3e7))

print("\n------\n") #separador


#valores logicos
#los valores de clase bool, tambien llamados valores logicos o "booleanos" son solo dos: "cierto" y "falso", que en python se representan mediante las palabras reservadas True y False, respectivamente.
True
False

#Se utilizan en muchos contextos en los que nuestros proogramas tengan que tomar desiciones en base a ciertas condiciones, y hay muchas funciones y operaciones que retornan valores logicos.

#Las listas, tuplas, diccionarios y otros contenedores retornaran True si contienen al menos un elemento y False si estan vacios.
print("retornaran false: ")
print(bool())
print(bool(0))
print(bool(""))
print(bool([]))
print(bool({}))
print(bool(None))


print("\n------\n") #separador

print("Retornaran True")
print(bool(5))
print(bool(1.4))
print(bool("lidia"))
print(bool([1, 2]))
print(bool(...))

print("\n------\n") #separador

#Clases especiales

#None
#el objeto none es lo que retornamos en las funciones que no retornan explicitamente ningun resultado. Se usa en muchas circunstancias, siempre que es necesario indicar la ausencia de una objeto. es un sigleton, un objeto del que solo hay una instancia. es dfecir: todos lo None son referenciasd al mismo None. En un contexto booleano, None retorna False.


#NotImplemented
#Al igual que none, notimplemented se usa como retorno en algunos metodos numericos y de comparacion especiales, para indicar que el metodo que lo retorna no esta implementado.
#En las operaciones logicas, notimplemented retorna True, pero esto es una caracteristica obsoleta, y notimplemented no deberia usarse en un contexto booleano.


#Eli[sis
#Elipsis es otro singleton. Se representa con un literal por medio de tres puntos seguidos (...) y tambien con la palabra reservada Elipsis. Actualmente no tiene ningun tipo de uso en python (salvo en algunos paquetes de terceros, como el paquete de calculo NumPy).
#En un contexto booleano, Elipsis retornara True.
