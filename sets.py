#un set o cunjunto es una coleccion no ordenada de objetos. No posee un indice como las listas o diccionarios, y no se puede contener objetos repetidos.
#se clara usando llaves {} como un diccionario, pero, dado que no tiene pares clave-valor,sus elementos se separan simplemente poir comas.

cubiertos = {"cuchara", "tenedor", "cuchillo"}
print(cubiertos)


print("\n------------\n") #serparador


#si se incluyen elementos repetidos, las repeticiones seran ignoradas.
servilletas = {"servilleta", "servilleta", "servilleta"}
print(servilletas)
#dada esta propiedad de los sets, se pueden usar para eliminar elementos repetidos de una lista.


print("\n------------\n") #serparador


#un set tambien puede ser declarado usando la funcion set(), que puede recibir un iterable como argumento.
frutas = set(["naranja", "platano", "manzana"])
print(frutas) #los corchetes indican que se esta pasando una lista como argumento.


print("\n------------\n") #serparador


#al igual que las secuencias, las colecciones se pueden obtener su longitud con len()
mi_set = set("123456789")
print(len(mi_set)) #9


print("\n------------\n") #serparador


#los set aceptan varias operaciones matematicas como la union, interseccion y diferencia.
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a | b, "union") #union
print(a & b, "interseccion") #interseccion
print(a - b, "diferencia") #diferencia de a con b (que elementos de a no estan en b)
print(b - a, "diferencia") #diferencia de b con a (que elementos de b no estan en a)
print(a ^ b, "diferencia simetrica") #diferencia simetrica (elementos que estan en a o en b pero no en ambos)


print("\n------------\n") #serparador


#para cada uno de estos operadores, tambien existen metodos equivalentes:
print(a.union(b), "union") #union
print(a.intersection(b), "interseccion") #interseccion 
print(a.difference(b), "diferencia") #diferencia de a con b (que elementos de a no estan en b)
print(b.difference(a), "diferencia") #diferencia de b con a (que elementos de b no estan en a)
print(a.symmetric_difference(b), "diferencia simetrica") #diferencia simetrica (elementos que estan en a o en b pero no en ambos)


print("\n------------\n") #serparador


#los sets tambien tienen metodos para modificar su contenido, como add() para agregar un elemento, y remove() o discard() para eliminar un elemento.
planetas = {"Marte", "Jupiter", "Venus"}
print(planetas)
planetas.add("Tierra")
print(planetas)
planetas.remove("Jupiter") #genera un error si el elemento no existe
print(planetas)
planetas.discard("Pluton") #no genera error si el elemento no existe
print(planetas)
planetas.clear() #elimina todos los elementos del set
print(planetas)
print(len(planetas)) #0
print(type(planetas)) #<class 'set'>


print("\n------------\n") #serparador

print("Frozenset\n") #separador
#Frozenset
#un frozenset es una version inmutable de un set. Una vez creado, no se pueden agregar ni eliminar elementos.
#se crea usando la funcion frozenset(), que recibe un iterable como argumento.
dias = frozenset(["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"])
print(dias)
print(type(dias)) #<class 'frozenset'>
#los frozensets soportan las mismas operaciones matematicas que los sets, pero no tienen metodos para modificar su contenido.
print(dias | frozenset(["Sabado", "Domingo"]), "union") #union
print(dias & frozenset(["Lunes", "Sabado"]), "interseccion") #interseccion
print(dias - frozenset(["Lunes", "Sabado"]), "diferencia") #diferencia
print(dias ^ frozenset(["Lunes", "Sabado"]), "diferencia simetrica") #diferencia simetrica
