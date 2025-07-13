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
