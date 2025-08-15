#la clase range son una forma especial de secuencias inmutables de numeros enteros. Su principal particularidad es la forma de contruirlo con la funcion range()

#La funcion range() admite hasta tres argumentos: start, stop y steps. Si no se le pasan lanzara un typeError.

#si se le pasa un solo argumento, este retornara una secuencia de numeros enteros desde 0 hasta el numero pasado como argumento, sin incluirlo.

rango = range(12)
print(rango)
print(rango[0])
print(rango[12-1]) # Acceso al último elemento o tambien puede ser escrito como print(rango[11])

#el objeto range no contiene la sucecion de numeros enteros, sino que es un objeto iterable que genera los numeros, algo asi como una "receta" para crear estos numeros.


print("\n-----------------\n") #separador

#si se le pasan dos argumentos, este indicara el numero de inicio y el segundo el nuemro del final
rango = range(6, 12) 
print(rango)
print(rango[0]) # Acceso al primer elemento
print(rango[12-6-1]) # Acceso al último elemento 0 tambien puede ser escrito como print(rango[6-1]) o print(rango[5])


print("\n-----------------\n") #separador

#Si se le pasan tres argumentos, el primero sera el numero de inicio, el segundo el numero del final y el tercero seran los pasos.

rango = range(6, 12, 2)
print(rango)
print(rango[0]) # Acceso al primer elemento 
print(rango[12-6-1]) # Acceso al último elemento 0 tambien puede ser escrito como print(rango[6-1]) o print(rango[5])
