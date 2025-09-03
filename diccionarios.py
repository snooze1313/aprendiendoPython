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


print("\n------------\n") #separador

#se puede usar dict() para crear un diccionario a partir de una lista de tuplas, donde cada tupla contiene un par clave-valor.
lista_tuplas = [("clave1", "valor1"), ("clave2", "valor2")]
diccionario_desde_tuplas = dict(lista_tuplas)
print(diccionario_desde_tuplas)  # Imprime: {'clave1': 'valor1', 'clave2': 'valor2'}

print("\n------------\n") #separador

#se puede usar len() para obtener el numero de pares clave-valor en un diccionario.
print(len(diccionario_desde_tuplas))  # Imprime: 2


print("\n------------\n") #separador


#la funcion zip() se puede usar para combinar dos listas en un diccionario. Una lista se usa para las claves y la otra para los valores.
claves = ["a", "b", "c"]
valores = [1, 2, 3]
diccionario_zip = dict(zip(claves, valores))
print(diccionario_zip)  # Imprime: {'a': 1, 'b': 2, 'c': 3}


print("\n------------\n") #separador

#se puede usar del para eliminar un par clave-valor de un diccionario.
numeros = {1: "uno",
           2: "dos",
           3: "tres"}
del numeros[2]
print(numeros)  # Imprime: {1: 'uno', 3: 'tres'}


print("\n------------\n") #separador

#la union de dos diccionario se hace con el operador | (disponible a partir de Python 3.9).
dic1 = {"a": 1,
        "b": 2}
dic2 = {"b": 3,
         "c": 4}

dic_union = dic1 | dic2
print(dic_union)  # Imprime: {'a': 1, 'b': 3, 'c': 4}
#en caso de que haya claves repetidas, el valor del segundo diccionario prevalece.

print("\n------------\n") #separador


#tambien se puede usar el operador |= para actualizar un diccionario con los pares clave-valor de otro diccionario.

diccionario_a = {"x": 10,
                 "y": 20}

diccionario_b = {"y": 30,
                 "z": 40}

diccionario_a |= diccionario_b
print(diccionario_a)  # Imprime: {'x': 10, 'y': 30, 'z': 40}
#en caso de que haya claves repetidas, el valor del segundo diccionario prevalece.

print("\n------------\n") #separador


#Tambien se puede usar el metodo update() para actualizar un diccionario con los pares clave-valor de otro diccionario.
dic1.update(dic2)
print(dic1)  # Imprime: {'a': 1, 'b': 3, 'c': 4}

print("\n------------\n") #separador

#si trtatamos de acceder a una clave que no existe en el diccionario, se genera un error KeyError. Para evitar esto, se puede usar el metodo get(), que devuelve None o un valor por defecto si la clave no existe.

dic1.get("d")  # Devuelve: None
print(dic1.get("d"))  # Imprime: None
print(dic1.get("a", "valor por defecto"))  # Imprime: 1

#si la clave no existe, se devuelve el valor por defecto
print(dic1.get("d", "valor por defecto"))  # Imprime: valor por defecto

print("\n------------\n") #separador

#los diccionarios tienen varios metodos utiles para trabajar con ellos:
#keys(): devuelve una vista de las claves del diccionario.
print(dic1.keys())  # Imprime: dict_keys(['a', 'b', 'c'])
#values(): devuelve una vista de los valores del diccionario.
print(dic1.values())  # Imprime: dict_values([1, 3, 4])
#items(): devuelve una vista de los pares clave-valor del diccionario.
print(dic1.items())  # Imprime: dict_items([('a', 1), ('b', 3), ('c', 4)])
#clear(): elimina todos los pares clave-valor del diccionario.
dic1.clear()
print(dic1)  # Imprime: {}
#copy(): devuelve una copia superficial del diccionario.
dic_copia = dic2.copy()
print(dic_copia)  # Imprime: {'b': 3, 'c': 4}
#pop(): elimina y devuelve el valor asociado a una clave especifica. Si la clave no existe, se puede proporcionar un valor por defecto.
valor_b = dic2.pop("b", "clave no encontrada")
print(valor_b)  # Imprime: 3
print(dic2)  # Imprime: {'c': 4}
#popitem(): elimina y devuelve un par clave-valor aleatorio del diccionario. Si el diccionario esta vacio, genera un error KeyError.
par_aleatorio = dic2.popitem()
print(par_aleatorio)  # Imprime: ('c', 4)
print(dic2)  # Imprime: {}
#update(): actualiza el diccionario con los pares clave-valor de otro diccionario o de un iterable de pares clave-valor.
dic1.update({"d": 5, "e": 6})
print(dic1)  # Imprime: {'d': 5, 'e': 6}
