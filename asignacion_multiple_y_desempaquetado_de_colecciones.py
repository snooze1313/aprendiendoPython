#       ASIGNACION MULPTIPLE Y DESEMPAQUETADO DE COLECCIONES

#Cuiando hablamos de la asignacion de valores a variables, vimos que podiamos asignar varios valores a varias variables en una sola linea, de este modo:

a, b, c = "valor de a", "valor de b", "valor de c"
print(a, b, c)

#Tras haber visto las tuplas y como se definen, ahora podemos darnos cuenta de que lo que hemos hecho en el ejemplo anterior no es mas que asignar una tupla de cadenas de texto a una tupla de variables (pero no olvidemos que en python asignar un valor a una variable solo es ponerle el nombre de la variable a ese valor).

#En general, podemos hacer algo similar para asignar el contenido de una coleccion a una serie de varibles, de modo que cada variable designe a uno de los elementos de la coleccion, de este modo:

a, b, c, d = 1, 2, 3, 4
print(a, b, c, d)


tupla = 1, 2, 3, 4
a, b, c, d = tupla
print(a, b, c, d)


lista = [1, 2, 3, 4]
a, b, c, d = lista
print(a, b, c, d)


set = (1, 2, 3, 4)
a, b, c, d = set
print(a, b, c, d)


diccionario = {"a" : 1,
               "b" : 2,
               "c" : 3,
               "d" : 4}
a, b, c, d = diccionario #Solo desempaqueta los id
print(a, b, c, d)


diccionario = {"a" : 1,
               "b" : 2,
               "c" : 3,
               "d" : 4}
a, b, c, d = diccionario.values() #Metodo para acceder a los valores
print(a, b, c, d)


diccionario = {"a" : 1,
               "b" : 2,
               "c" : 3,
               "d" : 4}
a, b, c, d = diccionario.items() #Metodo para acceder a los items en forma de tupla
print(a, b, c, d)


#Un problema que presenta esta forma de desempaquetar los valores de una coleccion es que el numero de variables y el numero de elementos debe ser el mismo. Si el numero de variables es mayor o menor al de valores, obtendremos una excepcion del tipo ValueError.

#Podemos hacer que, si en la collecion hay mas elementos que variables, los elementos sobrantes se asignen a una sola variable, para ello la marcamos con un asterisco (*) seguida de su nombre:

lista = [1, 2, 3, 4, 5, 6]
a, b, *c = lista
print(a, b, c)

#Python repartira los elementos secuencialmente, de modo que los valores se acumulen en forma de lista en una variable indicada con con el asterisco; Esta variable, aunque en el ejemplo anterior es la ultima, puede ser cualquiera de ellas:

lista = [1, 2, 3, 4, 5, 6]
a, *b, c = lista
print(a, b, c)

#Si en la coleccion hubiera valores para ocupar todas las variables menos la marcada con un asterisco esta ultima apuntaria a una lista vacia.

#No es posible marcar con un asterisco mas de unua variable, ya que python no sobria como repartir los valores; lo que nos haria obtener una excepcion SyntaxError.

print("\n-----------\n") #separador

#La funcion print nos permite un numero indeterminado de argumentos separados por comas, los cuales se imprimiran uno detras de otro.

print("hola", "esto", "es", "una", "prueba")

#Tambien sabemos que, si print() le pasamos como argumento una lista, imprimira esa lista en el formato usual (elementos separados por comas dentro de corchetes).

lista = ["hola", "esto", "es", "una", "prueba"]
print(lista)

#De modo que si queremos imprimir todos los elementos de una lista sin saber la longitud de esta podemos usar el asterisco de la siguiente manera:

print(*lista)

#Es importante notar, que aunque es muy parecido al desempaquetado en las asignaciones que hemos visto antes, es un caso muy distiunto.


print("\n-----------\n") #separador


#Para empezar, aqui anteponemos al asterisco al nombre de la coleccion, no a la variable que recibira los elementos, pero, sobre todo, es el resultado lo que es diferente. En la practica, es como si extrajeramos los elementos de una lista y los pusieramos, separados por comas, en lugar de esta, por lo que estos ejemplos son equivalentes:

lista = ["hola", "esto", "es", "una", "prueba"]
print(*lista)
print("hola", "esto", "es", "una", "prueba")


lista1 = [1, 2, 3]
lista2 = [10, 20, 30]
tupla = *lista1, *lista2
print(tupla)


#Si intentamos usar este modo de desempaquetado con diccionarios, podemos comprobar que, como nos pasaba con las asignaciones anteriores, lo que se nos muestra son las claves y no los valores.

diccionario = {
    "a" : "hola",
    "b" : "esto",
    "c" : "es",
    "d" : "una",
    "e" : "prueba"
}
print(*diccionario) #imprime los id
print(*diccionario.values()) #imprime los valores
print(*diccionario.items()) #imprime los items en forma de tupla

#Pero los diccionarios tienen su propio desempaquetado que nos permite hacer cosas mucho mas interesantes.

#Los diccionarios pueden ser desempaquetados usando dos asteriscos (**), de modo que se expanden en pares clave-valor que podemos usar en la funcion como argumento con nombre, como ejemplo:

diccionario = {
    "sep" : "--",
    "end" : "-FIN\n\n"
    }
print("Hola", "Mundo", **diccionario) #EL argumento **diccionario desempaqueta el valor (diccionario.values)

#COMO RESULTADO, LA FUNCION PRINT(), ADEMAS ACEPTAR UN NUMERO INDETERMINADO DE ARGUMENTOS ANONIMOS, TAMBIEN ADMITE ALGUNOS ARGUMENTOS CON NOMBRE COMO, POR EJEMPLO, SEP (CON EL QUE INDICAMOS EL SEPARADOR ENTRE PALABRAS, QUE ES"" POR DEFECTO) O END(QUE USAMOS PARA DEFINIR EL FINALDE LA LINEA -- "" POR DEFECTO). CUANDO TRATEMOS LAS FUNCIONES ALGO MAS EN PROFUNDIDAD, VEREMOS MAS DETALLES, PERO POR AHORA, BASTA DECIR QUE ESTOS ARGUMENTOS SE IMPLEMENTAN INTERNAMENTE COMO DICCIONARIO.

#Podemos desempaquetar listas conjuntamente con diccionarios en una misma funcion:

lista = ["Esto", "es", "una", "prueba"]
diccionario = {
    "sep" : "---",
    "end" : "XX\n\n"
}
print(*lista, **diccionario)


letras = {
    "a" : "Letra a",
    "b" : "Letra b",
    "c" : "Letra c",
    "d" : "Letra d"

}

numeros = {
    "1" : "el 1",
    "2" : "el 2",
    "3" : "el 3",
    "4" : "el 4"
}

union = {**letras, **numeros}
print(union)