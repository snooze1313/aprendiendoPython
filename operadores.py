#Un operardor es un elemento del lenguaje que representa una accion sobre datos, como una suma o una concatenacion. A los elementos sobre los que se aplica el operador (como los numeros de una suma, por ejemplo) se les llama operando. La mayoria de los operardores actuan sobre dos operandos, aunque hay algunos, llamados unarios, que afectan a uno solo.

#Las operaciones son expresiones. Cada vez que python se encuentra un conjunto de operaciones y operadores, evalua la sentencia que forman y retornan un resultado.

#Los operadores pueden encadenarse, de forma que la siguiente expresion es valida, y retornaria el resultado de la operacion completa:

total = 33 + 51 + 63 + 40 + 21 # Retorna 208
print("El total es:", total)

print("----------------------------\n\n") #separador


#   OPERADORES MATEMATICOS
#los operadores matematicos se aplican a valores numericos; consignan las siguietnes operaciones matematicas basicas:

#operador   operacion
#   +       suma
#   -       resta
#   *       multiplicacion
#   /       division
#   %       modulo (resto de una division)
#   **      exponenciacion (potencia)
#   //      division entera (redondea el resultado hacia abajo al entero mas cercano)

primer_numero = 10
segundo_numero = 5

suma = primer_numero + segundo_numero # Suma: 10 + 5 = 15
resta = primer_numero - segundo_numero # Resta: 10 - 5 = 5
multiplicacion = primer_numero * segundo_numero # Multiplicacion: 10 * 5 = 50
division = primer_numero / segundo_numero # Division: 10 / 5 = 2.0
modulo = primer_numero % segundo_numero # Modulo: 10 % 5 = 0
exponenciacion = primer_numero ** segundo_numero # Exponenciacion: 10 ** 5 = 100000
division_entera = primer_numero // segundo_numero # Division entera: 10 // 5 = 2
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicacion:", multiplicacion)
print("Division:", division)
print("Modulo:", modulo)
print("Exponenciacion:", exponenciacion)
print("Division entera:", division_entera)

#para estos operadores existe una version con asignacion cuyo simbolo es el mismo pero segiuido del signo igual (=).

primer_numero += segundo_numero  # Equivalente a primer_numero = primer_numero + segundo_numero
print("Nuevo valor de primer_numero despues de += :", primer_numero)

primer_numero -= segundo_numero  # Equivalente a primer_numero = primer_numero - segundo_numero
print("Nuevo valor de primer_numero despues de -= :", primer_numero)

primer_numero *= segundo_numero  # Equivalente a primer_numero = primer_numero * segundo_numero
print("Nuevo valor de primer_numero despues de *= :", primer_numero)

print("----------------------------\n\n") #separador


#   OPERADORES DE COMPARACION
#los operadores de comparacion comparan dos valores y retornan un valor booleano (True o False) dependiendo del resultado de la comparacion.

#operador       operacion
#   ==          igual a
#   !=          diferente de
#   >           mayor que
#   <           menor que
#   >=          mayor o igual que
#   <=          menor o igual que

numero = 7
texto = "hola mundo"

print("Es igual a 7?:", numero == 7)          # True
print("Es diferente de 5?:", numero != 5)     # True
print("Es mayor que 3?:", numero > 3)         # True
print("Es menor que 10?:", numero < 10)       # True
print("Es mayor o igual que 7?:", numero >= 7) # True
print("Es menor o igual que 6?:", numero <= 6)  # False
print("Es igual a 'hola mundo'?:", texto == "hola mundo") # True
print("Es diferente de 'adios mundo'?:", texto != "adios mundo") # True


print("----------------------------\n\n") #separador

#   OPERADORES DE CADENA
#los operadores de cadena permiten realizar operaciones con cadenas de texto.

#operador       operacion
#   +           concatenacion (unir dos cadenas)
#   *           repeticion (repetir una cadena un numero determinado de veces)

cadena1 = "Hola, "
cadena2 = "mundo!"
concatenacion = cadena1 + cadena2  # Concatenacion: "Hola, " + "mundo!" = "Hola, mundo!"
repeticion = cadena1 * 3            # Repeticion: "Hola, " * 3 = "Hola, Hola, Hola, "
print("Concatenacion:", concatenacion)
print("Repeticion:", repeticion)


print("----------------------------\n\n") #separador


#   OPERADORES LOGICOS