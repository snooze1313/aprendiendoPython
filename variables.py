#los comentarios se escriben con "#"
#los comentarios no se ejecutan
#se usan para hacer mas legible el codigo

#una linea de codigo tambien puede ser llamada sentencia

#primeras variables y uso de print
texto = "Hola mundo"
print(texto)
print("esto es un saludo")
texto = "adios mundo"
print(texto)

#altura en metros
altura = 100
#se imprime la altura
print(altura)

#aritmetica dentro de print
#suma de 4 + 5
print(4 + 5)

#suma dentro de una variable y print
suma = 5 + 25 + 12
print(suma)

#la sentencia que retornan un resultado se les llama expresiones
#una expresion es una combinacion de variables, operadores y valores que se evalua a un resultado

suma = 5 + 25 + 12
print(suma)

cadena_con_suma = "5 + 25 + 12"
print(cadena_con_suma)

suma_de_cadenas = "5" + "25" + "12"
print(suma_de_cadenas)

#la funcion print puede usarse con varios argumentos
print("hola mundo", "un texto", "otro texto", "y otro mas")

#la funcion print puede ser usada con diferentes tipos de datos
print("hola mundo", 5, 3.14, True)

 #hay argumentos con nombre que se pueden usar en print
 #sep separa los argmentos con el valor que asignas despues del =
print("hola mundo", "un texto", "otro texto", "y otro mas", sep="---")

#la funcion input permite recibir datos
nombre = input("¿Cual es tu nombre? ")
print("se ha escrito:", nombre)