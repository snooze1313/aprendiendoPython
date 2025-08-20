#Casi todas las secuencias admiten una serie de operaciones comunes:

#a excepcion de los rangos, dos secuencias del mismo tipo se pueden conectar a continuacion de la otra usando el operador +. Esto retorna una tercera secuencia de ese tipo.

print("hola" + "mundo") # Concatena dos cadenas
print([1, 2, 3] + [4, 5]) # Concatena dos listas
print((1, 2) + (3, 4)) # Concatena dos tuplas


print("\n\n------------------------\n\n") #separador

#Una secuencia se puede repetir un numero indeterminado de veces usando el operador *. Esto retorna una tercera secuencia del mismo tipo.
print("hola" * 3) # Repite la cadena 3 veces
print([1, 2] * 3) # Repite la lista 3 veces
print((1, 2) * 3) # Repite la tupla 3 veces


print("\n\n------------------------\n\n") #separador


#El operador in se puede usar para verificar si un elemento esta contenido en una secuencia. Retorna True o False.
print("a" in "hola") # Verifica si 'a' esta en la cadena
print(1 in [1, 2, 3]) # Verifica si 1 esta en la lista
print(2 in (1, 2, 3)) # Verifica si 2 esta en la tupla
print(4 in range(10)) # Verifica si 4 esta en el rango de 0 a 9


print("\n\n------------------------\n\n") #separador


#En el caso de las cadenas de bytes y bytearray, este operador tiene un comportamiento especial, podemos usarlo para localizar subcadenas completas de caracteres o bytes respectivamente, y no solo caracteres o bytes individuales.
print(b"abc" in b"abcdef") # Verifica si la subcadena b'abc' esta en la cadena de bytes
print(bytearray(b"abc") in bytearray(b"abcdef")) # Verifica si la subcadena bytearray(b'abc') esta en el bytearray
print("pablo" in "hola soy pablo") # Verifica si la subcadena 'pablo' esta en la cadena


print("\n\n------------------------\n\n") #separador


#Al contrario el operador not in retorna True si el elemento no esta contenido en la secuencia.
print("x" not in "hola") # Verifica si 'x' no esta en la cadena
print(5 not in [1, 2, 3]) # Verifica si 5 no esta en la lista
print(6 not in (1, 2, 3)) # Verifica si 6 no esta en la tupla
print(10 not in range(10)) # Verifica si 10 no esta en el rango de 0 a 9


print("\n\n------------------------\n\n") #separador


#O tambien se puede usar el operador not in para verificar si una subcadena no esta contenida en una cadena de bytes o bytearray.
print(b"xyz" not in b"abcdef") # Verifica si la subcadena b'xyz' no esta en la cadena de bytes
print(bytearray(b"xyz") not in bytearray(b"abcdef")) # Verifica si la subcadena bytearray(b'xyz') no esta en el bytearray


print("\n\n--------------------------\n\n") #separador


#las secuencias disponen de un metodo llamado count() que retorna el numero de veces que un elemento aparece en la secuencia.
mi_tupla = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
print(mi_tupla.count(3)) # Cuenta cuantas veces aparece el 3 en la tupla


#tambien se puede usar el metodo count() en cadenas, listas y bytearrays.
mi_cadena = "hola mundo"
print(mi_cadena.count("o")) # Cuenta cuantas veces aparece la letra 'o'
mi_lista = [1, 2, 3, 1, 2, 3]
print(mi_lista.count(2)) # Cuenta cuantas veces aparece el 2 en la lista
mi_bytearray = bytearray(b"hola mundo")
print(mi_bytearray.count(b"o")) # Cuenta cuantas veces aparece el byte b'o


print("\n\n--------------------------\n\n") #separador


#otro metodo que tienen las secuencias es index(), que retorna el indice de la primera ocurrencia de un elemento en la secuencia. Si el elemento no se encuentra, se lanza una excepcion ValueError.
mi_lista = [1, 2, 3, 4, 5]
print(mi_lista.index(3)) # Retorna el indice del primer 3 en la lista

abecedario = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
print(abecedario.index("d")) # Retorna el indice de la letra 'd' en la tupla

mi_cadena = "hola mundo"
print(mi_cadena.index("m")) # Retorna el indice de la letra 'm'


print("\n\n--------------------------\n\n") #separador

#A index() se le pueden pasar dos argumentos opcionales, el inicio y el final del rango en el que buscar. Si no se especifican, se busca en toda la secuencia.
mi_lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(mi_lista.index(3, 4)) # Busca el primer 3 a partir del indice 4
print(mi_lista.index(1, 5)) # Busca el primer 1 a partir del indice 5

tupla = ("casa", "perro", "gato", "pez", "pajaro", "gato")
print(tupla.index("gato", 2)) # Busca el primer 'gato' a partir del indice 2
print(tupla.index("gato", 0, 4)) # Busca el primer 'gato' entre los indices 0 y 4 (sin incluir el 4)


print("\n\n--------------------------\n\n") #separador

#El operador len() retorna el numero de elementos en una secuencia.
print(len("hola")) # Retorna 4, la longitud de la cadena
print(len([1, 2, 3, 4, 5])) # Retorna 5, la longitud de la lista
print(len((1, 2, 3))) # Retorna 3, la longitud de la tupla
print(len(b"hola")) # Retorna 4, la longitud de la cadena de bytes
print(len(bytearray(b"hola"))) # Retorna 4, la longitud del bytearray

print("\n\n--------------------------\n\n") #separador

#la funcion max() retorna el elemento mayor de una secuencia, mientras que min() retorna el elemento menor. Si la secuencia esta vacia, se lanza una excepcion ValueError.
rango = range(10)
print(max(rango)) # Retorna 9, el mayor elemento del rango
print(min(rango)) # Retorna 0, el menor elemento del rango
print(max("hola")) # Retorna 'o', el mayor caracter de la cadena segun el orden lexicografico (alfabético)
print(min("hola")) # Retorna 'a', el menor caracter de la cadena segun el orden lexicografico (alfabético)