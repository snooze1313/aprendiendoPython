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


print("----------") #separador


#LISTAS
#Las listas son secuencias ordenas de elementos a los que se puede acceder por su posicion, exactamente igual que las tuplas, con la diferencia que se pueden modificar. Una lista es un objeto mutable, por lo que, al contrario visto con las tuplas.

#Las listas se declaran entre corchetes y separando los elementos con comas.

lista = ["primero", "segundo", "tercero", "cuarto"]

print(lista)


#si es necesario, se puede crear una lista vacia solo usando corchetes.
lista = []

#una lista puede tambien ser creada con la funcion list():
lista = list(("hola","mundo"))

print(lista)

#usada la funcion list() sin argumentos retornara una lista vacia. si sele pasa una tupla, creara la lista con los elementos iterables.

#Al igual que las secuencias las listas son accesibles mediante indices y ademas poder modificarlas.


print("----------") #separador


lista = ["primero", "segundo", "tercero", "cuarto"]

print(lista[2]) #mostrara el tercer elemento

lista[2] = "elemento modificado"

print(lista)

#Si llegaramos a usar un indice fuera del alcance de la lista dara error
#emplo: lista[10]

#Al igual que las tuplas se puede fotmastear las listas anidadas

lista_letras = [
    "a", "b", "c", "d",
    "e", "f", "g", "h",
    "i", "j",
]


print("----------") #separador


#es posible eliminar un elementos de estas listas pero esto hara que el indice de los demas elementos se vea afectado

#Las listas cuentan con metodos propios que permiten modificar de estas.

#el primero de estos es append(), que anade un nuevo elemento al final de la lista.

lista = ["cero", "uno", "dos"]

print(lista)

lista.append("tres") #Se anadio el elemento tres al final de la lsita

print(lista)


#el metodo insert permite indicar como primer argumento la posicion en la que se introducira el elemento indicado como segundo argumento. Los elementos posteriores a esa posicion se desplazaran un indice.

lista.insert(2, "uno y medio") #Se anade un elemento entre el indice [2] y [3]

print(lista)


print("----------") #separador


#El opuesto es remove(), que eliminar la primera aparicion del elemento que se le pasa que se le pasa como argumento. Si no existe el elemento que se quiere borrar, lanzara un error.

lista.remove("uno y medio")

print(lista) #Se eleimino el elemento "uno y medio"

#un metodo mas drastico es clear(), que se usa sin argumento y este elimina todos los elementos de la lista.


print("----------") #separador


numeros = [1, 2, 3, 4, 5]

print(numeros)

numeros.clear() #vaciar la lista

print(numeros) #imprime la lista vacia


#elmetodo reverse() invierte el orden de la lista:

numeros = [1, 2, 3, 4, 5]

print(numeros)

numeros.reverse()

print(numeros)


print("----------") #separador


#el metodo pop() elimina el ultimo elemento de una lista y lo retorna. Si la lista esta vacia saltara un error

numeros = ["cero", "uno", "dos"]

print(numeros)

print("numero popeado: ", numeros.pop())

print("numeros restantes: ", numeros)


#El metodo copy() retorna una copia de una lista "superficial", lo que implica que, si la lista contiene a objetos mutables, modificar esos objetos en la lista original tambien modificara la copia y viceversa.

vocales = ["aeiou"]

copia_vocales = vocales.copy()

print(vocales)
print(copia_vocales)


print("----------") #separador


#El metodo sort() reordena los elemenmtos en la lista. Si se ejecuta sin argumentos, ordenara la lista normalmente: numeros en orden ascendente, las cadenas por orden alfabetico, etc. Para poder ordenar los elementos, debe ser pociblecompararlos usando el operador "menor que" (<). Si sele pasa el argumento con nombre reverse con valor True (por defecto False), el orden de los elementos se invertira.

ciudades = ["Granada", "Boston", "Anara", "Beijin"]

print(ciudades)

ciudades.sort()

print(ciudades)

ciudades.sort(reverse = True)

print(ciudades)