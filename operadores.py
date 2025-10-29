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
#Son aquellos que sirven para efectuar operaciones con valores logicos. Estos operadores retornan tambien valores logicos (True o False) dependiendo del resultado de la operacion.

#operador       operacion
#   and         y logico (retorna True si ambos operandos son True)
#   or          o logico (retorna True si al menos uno de los operandos es True)
#   not         negacion (invierte el valor logico del operando)

#El operador and equivale a la conjuncion logica "y logica", y retorna un valor cierto solo si ambos operando son tambien ciertos.

#tabla del operardor and
#operando1   operando2   resultado
#  True       True        True
#  True       False       False
#  False      True        False
#  False      False       False

#El operador logico or equivale a la conjuncion "o logica", y retorna un valor cierto siempre que no sean ambos operandos falsos.

#tabla del operardor or
#operando1   operando2   resultado
#  True       True        True
#  True       False       True
#  False      True        True
#  False      False       False

#Al contrario que los anteriores, el operador  not se aplica sobre un solo operando (se dice que es un operador unario). E invierte el valor logico de este. Si el operando es True, retorna False; y si es False, retorna True.

#tabla del operardor not
#operando    resultado
#  True       False
#  False      True

resultado = 3 == 2
print(resultado)  # False
#3 no es igual a 2, por lo que la expresion retorna False

print(True and True)  # True
#ambos operandos son True, por lo que la expresion retorna True

print(True and False)  # False
#uno de los operandos es False, por lo que la expresion retorna False

print(False or True)  # True
#uno de los operandos es True, por lo que la expresion retorna True

print(False or False)  # False
#ambos operandos son False, por lo que la expresion retorna False

print(not True)  # False
#el operando es True, por lo que la expresion retorna False

print(not False)  # True
#el operando es False, por lo que la expresion retorna True

print("----------------------------\n\n") #separador

#Aunque todo lo anterior es correcto, los operadores and y or tienen algunas pecuiliaridaes encaminadas a mejorar su eficiencia.
 
#Dado a que and solo se cumple si ambos operardores son evaluados como True, en los casos en el que el primer operando resulta ser False resulta redundante comprobar el segundo operando.

# Del mismo modo, dado a que or se cumple si al menos uno de los operandos es True, en los casos en los que el primer operando resulta ser True resulta redundante comprobar el segundo operando.

lista=[]
print(lista or "lista vacia") # Retorna "lista vacia"
#la lista esta vacia, por lo que el primer operando es False, y se retorna el segundo operando

print(lista and "lista vacia") # Retorna []
#la lista esta vacia, por lo que el primer operando es False, y se retorna el primer operando


print("----------------------------\n\n") #separador


#    OPERADORES DE IDENTIDAD
#Un caso especial son los operadores de identidad is e is not,.

#operador       operacion
#   is          es identico a (verifica si ambos operandos son el mismo objeto en memoria)
#   is not      no es identico a (verifica si ambos operandos no son el mismo objeto en memoria)

#Abos operadores sirven para comparar objetos. El operador is devuelve  True si ambos elementos comparados son el mismo objeto (poseen el mismo id en memoria), y False si no lo son. El operador is not hace lo contrario: devuelve True si ambos elementos comparados no son el mismo objeto, y False si lo son.

a = [1, 2, 3]
b = a  # b referencia al mismo objeto que a

print(a is b)      # True
print(a is not b)  # False


print("----------------------------\n\n") #separador

#    OPERADORES DE PERTENENCIA