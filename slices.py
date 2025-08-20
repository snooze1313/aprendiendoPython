#podemos acceder a cada uno de los elementos de una secuencia por medio de su indice. mas interesante es que tambien podemos usar numeros negativos como indice, lo que retornara el elemento que ocupe la pocision indicada desde atras. de este modo, para obtener el ultimo y penultimo elemento de una lista hariamos esto:

lista = ["primero", "segundo", "tercero", "cuarto", "quinto", "sexto"]

print(lista[-1])  # ultimo elemento
print(lista[-2])  # penultimo elemento


print("\n\n-----------------\n\n") #separador

#contamos con una notacion especial, llamada slices, que permite extraer secciones de la lista de forma sencilla.
#los slices usan indices separados por el signo dos puntos (:) para indicar que parte de la lista queremos obtener, segun el siguiente formato: [inicio:parada]; donde iincio es el indice del primer elemento que queremos obtener y parada es el elemento donde se detendra nuestra seleccion (no incluido).

#por ejemplo: para mostrar los cuatro primeros elementos dentro de la lista que hemos definido, podriamos hacer lo siguiente:

alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
            "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
            "u", "v", "w", "x", "y", "z"]

print(alfabeto[0:3])  # ["a", "b", "c"]
#el elemento del indice 3 no se incluye en el resultado, por lo que el slice devuelve los elementos del 0 al 2.

#podemos omitir el indice de inicio o el de parada. si omitimos el indice de inicio, python asumira que queremos empezar desde el principio de la lista. si omitimos el indice de parada, python asumira que queremos llegar hasta el final de la lista.
print(alfabeto[:3])  # ["a", "b", "c"]
print(alfabeto[23:])  # ["x", "y", "z"]
print(alfabeto[:])  # toda la lista

#tambien podemos usar indices negativos en los slices. por ejemplo, para obtener los tres ultimos elementos de la lista, podriamos hacer lo siguiente:
print(alfabeto[-3:])  # ["x", "y", "z"]
print(alfabeto[:-3])  # todos menos los tres ultimos elementos
print(alfabeto[-6:-3])  # ["u", "v", "w"]
print(alfabeto[-3:-1])  # ["x", "y"]

#ademas, los slices pueden tener un tercer parametro, llamado step (paso), que indica el intervalo entre los indices seleccionados. el formato seria: [inicio:parada:step]. por defecto, el valor de step es 1, lo que significa que se seleccionan todos los elementos entre inicio y parada. si step es 2, se seleccionan todos los segundos elementos, si es 3, todos los terceros elementos, y asi sucesivamente.


print(alfabeto[::2])  # ["a", "c", "e", "g", "i", "k", "m", "o", "q", "s", "u", "w", "y"]
print(alfabeto[1::2])  # ["b", "d", "f", "h", "j", "l", "n", "p", "r", "t", "v", "x", "z"]
print(alfabeto[1:10:3])  # ["b", "e", "h"]
print(alfabeto[::-1])  # toda la lista en orden inverso
print(alfabeto[10:1:-1])  # ["k", "j", "i", "h", "g", "f", "e", "d", "c", "b"]
print(alfabeto[10:1:-2])  # ["k", "i", "g", "e", "c"]

texto = "Hola, mundo!"
print(texto[0:4])  # "Hola"
print(texto[5:])  # "mundo!"
print(texto[:5])  # "Hola,"
print(texto[::2])  # "Hl, mn!"
print(texto[::-1])  # "!odnum ,aloH"
print(texto[1:10:3])  # "o, u"
