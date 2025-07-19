#Secuencias
#Existe una serie de clases que pueden contener otros objetos y se conocen como contenedores.
##las secuencias son objetos que contienen conjuntos de elementos ordenados, como su propio nombre indica, secuencialmente. Estos nos poermiten acceder a esos elementos en funcion de su posicion en la secuencia., las secuencias tambien tienen la propiedad de ser iterables.

#Tuplas
#Al hablar de las cadenas de caracteres (objetos str) o bytes (objetos bytes), vimosque opueden ser tratados como secuencias usando los corchetes [], podemos acceder a sus elementos de forma individual.


print("hola mundo"[1]) #imprime: la segunda letra de la cadena

print("----------") #separador

#la generalizacion de esta idea son llamadas tuplas
#Una tupla es una sucesion de elementos de cualquier tipo (o de varios tipos) separados por coma:

vocales = "a", "e", "i", "o", "u"
nombres = "juguete", "libro", "gato", "caramelo"
numeros = 12, 35, 2002, 140, 197
de_todo = 45, 3.15, "laberinto", False

print(vocales)
print(nombres)
print(numeros)
print(de_todo)

#python nos muestra los elementos de la tupla separados por comas y dentro parentesis. Los parentesis en python para agrupar operaciones y, aunque no es necesario, las tuplas se suelen definir entre parentecis por claridad, (y, en ocaciones, para evitar ambiguedades), por lo que el siiguiente emeplo es en todo identico anterior:

#Se puede iniciar una tupla vacia
vacio =()
print(vacio)

print("----------") #separador

#para ecceder de forma individual a los elementos de una tupla debemos usar los corchetes[]
print(vocales[0])
print(vocales[4], vocales[3])

#los elementos seleccionados pueden ser usados para cualquier tipo de operacion, excepto modificarlos

palabras = "Hola", "mundo"

saludo = palabras[0] + " " + palabras[1]

print(saludo)

#tratar de modificar los elementos nos dara error
#ejemplo:
#   palabras[0] = "adios"

print("----------") #separador

#Tambien pueden contener tuplas dentro de otra tupla:
tupla = (32, (1, 2, 3), 21, 4)

print(tupla)

tupla_interna = tupla[1]

print(tupla_interna)
print(tupla_interna[2])


print("----------") #separador


#para acceder al contenido de una tupla dentro de otra tupla, se pone un indice a continuacion de otro; primero el de la lista inicial y el segundo de la lista contenida.

print(tupla[1][0])
print(tupla[1][1])
print(tupla[1][2])

print("----------") #separador


#esto no solo sirve para para tuplas anidadas, sino que tambien se puede usar con cualquier tipo de secuencia, como cadenas de texto, anidar y acceder a tantas tuplas como necesites.
anidadas = (((1, 2), (2, 6), (3, 1)), ((2, 8), (3, 2), (9, 0)))

print(anidadas[1][2][0])

#Cuando anidamos tuplas dentro de otras la linea de codigo comienza a hacerse menos legible. Lo mismo ocurre cuando no nidamos usamos lineas muy largas para definir tuplas.
#Los parentesis nos permite dividir su contenido en varias lineas de manera que nos paresca mas conveniente.

numeros = (
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10
)

letras = (
    "a", "b", "c", "d",
    "e", "f", "g", "h"
)

tuplas_con_tuplas = (
    (11, 12, 13),
    (21, 22, 23),
    (31, 32, 33)
)

nidadas = (
    (
        (1, 2),
        (2, 6),
        (3, 1)
    ),
    (
        (2, 8),
        (3, 2),
        (9,0)
    )
)

