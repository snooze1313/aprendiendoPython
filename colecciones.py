#colecciones
#Las colecciones son una serie de clase de contenedores cuyos elementos no estan ordenados por su posicion, las colecciones, igual que las secuencias, son objetos iterables.

#Diccionarios
#un diccionario es un conjunto de valores emparejados, en cierto modo, un diccionario es parecido a una lista, con la diferencia de que los indices no tienen porque ser numericos, sino que ademas pueden ser cadenas de texto, tuplas, o en general, objetos hasheables. No todas las claves de un diccionario tienen porque ser del mismo tipo, sino que pueden ser una mezlca de ellos.

#Al definir un diccionario, los valores de cada par se separan entre ellos por dos puntos (:) (y, de los otros por comas (,). El conjunto debe estar acotado por llaves ({}).

diccionario = {
    "clave1": "valor",
    "clave2": "otro valor"}

#para acceder a un valor concreto se usa el nombre del diccionario seguido del indice entre corchetes ({}), con la salvedad de  que aqui ese indice no tiene por que ser un numero. Los diccionarios son objetos mutables, por lo que se pueden modificar sus valores, pero no se pueden modificar las claves.

print(diccionario["clave1"])  # Imprime: valor
diccionario["clave1"] = "nuevo valor"
print(diccionario["clave1"])  # Imprime: nuevo valor


#Para añadir un nuevo par clave-valor, se usa la sintaxis del nombre del diccionario seguido de la nueva clave entre corchetes y el valor que se le quiere asignar.
diccionario["clave3"] = "tercer valor"
print(diccionario)  # Imprime: {'clave1': 'nuevo valor', 'clave2': 'otro valor', 'clave3': 'tercer valor'}


 #para crear un diccionario vacio, se usa la sintaxis de llaves sin nada dentro o la funcion dict()
diccionario_vacio = {}
diccionario_vacio2 = dict()

