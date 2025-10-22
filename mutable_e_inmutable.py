#En los len guajes de programacion las variables se pueden ver como "cajas" en las que se guarda un valor (una cadena, un numero o lo que sea), de hecho, normalmente hablamos asi de python.

#En python esta imagen tambien sirve como una primera aproximacion pero la cosa es un poco mas compleja. el funcionamiento interno de las variables es algo diferente.

#como ya hemmos visto, una variable en python es un nombre, una referencia a un objeto. Es decir; como si fuera una etiqueta que esta enlazada a este objeto. El objeto en si tiene su propio nombre interno asignado por python y que es accesible con la funcion id() pasandole como argumento el objeto.

#por ejemplo, cundo asignamos el valor de esa variable a otra (haciendo algo como "variable2 = variable1"), en python, un mismo objeto puede tener varias etiquetas (varibles) apuntando a el.


variable1 ="hola"
variable2 = variable1
variable3 = "adios"

print("variable1 = ", id(variable1)) #Imprime el id del objeto al que apunta variable1
print("variable2 = ", id(variable2)) #Imprime el id del objeto al que apunta variable2 (que es el mismo que el de variable1)
print("variable3 = ", id(variable3)) #Imprime el id del objeto al que apunta variable3 (que es diferente al de variable1 y variable2)


#python hace esto porque es muy eficiente en terminos de  memoria y velocidad: es mucho mas rapido y economico crear una nueva referencia que hacer una copia del objeto.
#si posteriormente modificamos el contenido de la variable, loque en realidad hace python internamente es crear otra nueva (con un nuevo id) y hacer que el nombre que habiamos asignado a la original apunte a este nuevo objeto.

#ADICIONALMENTE, CUANDO NO QUEDA NINGUN NOMBRE QUE APUNTE A UN OBJETO, PYTHON ESE OBJETO DE LA MEMORIA.

#Lo que hemos visto hasta ahora es valido para todos los tipos de datos en python, pero hay una distincion importante entre dos tipos de objetos: los mutables y los inmutables.

#Los objetos inmutables son aquellos cuyo contenido no puede cambiarse una vez que han sido creados. Ejemplos de tipos de datos inmutables en python son: int, float, str, tuple y frozenset.


print("\n\n----------------------------") #Separador


#Sin embargo, las listas, los diccionarios y los conjuntos son ejemplos de tipos de datos mutables, lo que significa que su contenido puede cambiarse sin necesidad de crear un nuevo objeto.

lista = ["hola", "mundo", "palabra"]
print("lista antes de modificar: ", id(lista)) #Imprime el id del objeto al que apunta lista

lista[2] = "cosa" #modificamos el tercer elemento de la lista "palabra" por "cosa"
print("lista despues de modificar: ", id(lista)) #Imprime el id del objeto al que apunta lista (que es el mismo que antes de modificarla)


print("\n\n----------------------------") #Separador


#Este comportamiento de los tipos mutables (que pueden ser modificados sin que se cambie su referencia) tiene una consecuencia inesperada.

#Ya hemos visto que si modificamos una copia de un objeto inmutable esto no afecta al original (y viseversa) porque, en realidad estamos creando un objeto nuevo.

#pero, si copiamos un objeto mutable (como por ejemplo, una lista) y modificamos el original, estas modificaciones se mostraran tambien en la copia, igualmente, si modificamos la copia, tambien cambiara el original.

#Esto ocurre porque, al ser mutable, no se crea uno nuevo como ocurre con los inmutables y, por tanto, no cambianlas referencias y ambos objetos siguen siendo el mismo.


lista = ["hola", "mundo", "palabra"]
copia_lista = lista  #Hacemos una "copia" de la lista (en realidad, ambas variables apuntan al mismo objeto)
lista[2] = "cosa"  #Modificamos el original
print("imprime copia lista: ", copia_lista[2])  #Imprime "cosa", porque la copia apunta al mismo objeto que el 


print("\n\n----------------------------") #Separador


#Si queremos copiar una variable que referencia a un objeto de tipo mutable (como una lista o un diccionario), debemos hacerlo de forma explicita usando la funcion correspondiente.

lista = ["hola", "mundo", "palabra"]
lista2 = list(lista)  #Hacemos una copia de la lista usando la funcion list()

print("id lista original: ", id(lista))  #Imprime el id del objeto al que apunta lista
print("id lista copia:    ", id(lista2))  #Imprime el id del objeto al que apunta lista2 (que es diferente al de lista)

print("contenido de lista:  ", lista)
print("contenido de lista2: ", lista2)

print("\n\n----------------------------") #Separador


#Pero esto tiene sus limitaciones. Un objeto contenedor es un objeto (el contenedor en si) que tiene referencias a otros objetos (el contenido). Al copiar el objeto de modo explicito estamos creando un nuevo contenedor, pero las referencias que contiene siguen apuntando a los mismos objetos del original (es decir el contenido no se copia y sigue siendo el mismo).

listas = [
    [1,2,3,4],
    ["a","b","c","d"]
]

copia_listas = list(listas)  #Hacemos una copia de la lista usando la funcion list()

print("id listas original: ", id(listas))  #Imprime el id del objeto al que apunta listas
print("id listas copia:    ", id(copia_listas))  #Imprime el id del objeto al que apunta copia_listas (que es diferente al de listas)

print("id listas[0] original: ", id(listas[0]))  #Imprime el id del objeto al que apunta listas[0]
print("id copia_listas[0]:    ", id(copia_listas[0]))  #Imprime el id del objeto al que apunta copia_listas[0] (que es el mismo que el de listas[0])


print("\n\n----------------------------") #Separador


#Estamos haciendo una copia superficial (shallow copy): copiamos solo el objeto contenedor y sus referencias a los mismos objetos contenidos.

#Esto quiere decir que, si copiamos un contenedor que contiene objetos mutables y, despues los modificamos alguno de los objetos contenidos, los cambias se aplicaranen tambien en la copia, porque son los mismos objetos.

original = [[1,2,3]]
copia = list(original)  #Hacemos una copia superficial de la lista original

print("original: " ,original[0][1]) #Imprime 2
print("copia:    " ,copia[0][1]) #Imprime 2

original[0][1] = "cambiado"  #Modificamos el objeto contenido en la lista original

print("original despues de modificar:          " ,original[0][1]) #Imprime "cambiado"
print("copia despues de modificar original:    " ,copia[0][1]) #Imprime "cambiado", porque el objeto contenido es el mismo en ambas listas


#Naturalmente, esto es aplicable a cualquier combinacion de contenedores dentro de contenedores, con cualquier nivel de profundidad, a menos que todos ellos sean inmutables. para estos objetos, una "copia superficial" puede ser suficiente.

#Cuando queremos crear copias de contenedores de varios niveles con objetos mutables (y crear copias de todos ellos, en lugar de simplemente referencias a los objetos originales; lo que se conoce como un "deep copy" o "copia profunda") debemos recurrir a formas de copiar mas sofisticadas, como bucles o funciones recursivas, o usar el modulo de python copy, que contiene una funcion llamada deepcopy() que esta dise;ada para este tipo de trabajo.