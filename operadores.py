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
#los operadores de pertenencia in y not sirven para indicar que un elemento pertenece o no a un contenedor.
#operador       operacion
#   in          en (verifica si el operando de la izquierda esta contenido en el operando de la derecha)
#   not in      no en (verifica si el operando de la izquierda no esta contenido en el operando de la derecha)

#El operador in retorna un volor True si el elemento indicado a la izquierda del operador esta en el contenedor indicado a la derecha del operador. El operador not in hace lo contrario, y retorna True si el elemento no esta en el contenedor y False si no lo esta.

lista = ["silla", "mesa", "armario", "taburete"]
print("silla" in lista) #Mostrara True, porque "silla" esta en la lista

print("sofa" in lista) #Mostrara False, porque "sofa" no esta en la lista

print("mesa" not in lista) #Mostrara False, porque "mesa" esta en la lista

print(4 in lista) #Mostrara False

print("hola" not in lista) #Mostrara True

print(3 in range(10)) #Mostrara True


print("----------------------------\n\n") #separador

#Los operadores in y not in se pueden usar tambien para comprobar la pertenencia a un diccionario. El operador in retornara True si el primer operando coincide con alguna clave del diccionario. El operador not in retornara True cuando el primer operando no coincida con ninguna clave

mar = {"a": "Almeja",
       "b" : "Bacalao",
       "c": "Cangrejo"}

print("a" in mar) #Mostrara "True"

print("Bacalao" in mar) #Mostrara "False"

#En el caso de cadenas, bytes y bytearrays, estos operadores pueden usarse para comprobar si una cadena esta contenida en otra. El operador in retornara True si la secuencia del primer operando esta incluida en la secuencia del segundo operando; y not in retornara True si la secuencia del primer operando no esta en el segundo.

musculo = "esternocleidomastoideo"

print("nocle" in musculo) #Retornara True

print(b"cada" in b"abracadabra") #Retornara True

#Si tratamos de comprobar, con estos operadores, subcadenas de tipos distintos (como una  bytes en una str) se lanzara una excepcion de la clase TypeError.


print("----------------------------\n\n") #separador


#       OPERADORES PARA CONJUNTOS

#Los siguientes operadores pueden usarse sobre conjuntos (objetos de las clases set y frozenset), y retornan un nuevo conjunto, resultado de la operacion correspondiente.

# Operador  Operacion
#   |           Union
#   &           Inserccion
#   -           Diferencia (es el mismo operador de resta)
#   ^           Diferendcia simetrica

#La union retorna el resultado de unir los dos sets o frozensets. El conjunto tendra los elementos de ambos conjuntosoriginales, excluyendo las repeticiones.

union = {0, 1, 2, 3} | {2, 3, 4, 5}
print(union) #Retorna {0, 1, 2, 3, 4, 5}


#La diferencia de dos sets retorna un tercero con los elementos del primero menos los elementos del segundo.

diferencia = {0, 1, 2, 3} - {2, 3, 4, 5}
print(diferencia) #Retorna {0, 1}


#La insercion de dos conjuntos retorna el conjunto que son ambos comunes

interseccion = {0, 1, 2, 3} & {2, 3, 4, 5}
print(interseccion) #Retorna {2, 3}


#La diferencia simetrica es la opuesta a la anterior, y retorna el conjunto de elementos de ambos, excluyendo los que tienen en comun.

dif_simetrica = {0, 1, 2, 3} ^ {2, 3, 4, 5}
print(dif_simetrica) #Retorna {0, 1, 4, 5}


print("----------------------------\n\n") #separador


#Para todos estos operadores existe una version con asignacion, que opera exactamente igual, pero asignando el resultado al primer operando, en lugar de retornarlo.

#Operador               Operacion
#   |=              Union con asignacion
#   &=              Inserccion con asignacion
#   -=              Diferencia con asignacion
#   ^=              Diferencia simetrica con asignacion


a = {0, 1, 2, 3}
b = {2, 3, 4, 5}
a |= b
print(a) #Retorna {0, 1, 2, 3, 4, 5}


a = {0, 1, 2, 3}
b = {2, 3, 4, 5}
a -= b
print(a) #Retorna {0, 1}


a = {0, 1, 2, 3}
b = {2, 3, 4, 5}
a &= b
print(a) #Retorna {2, 3}


a = {0, 1, 2, 3}
b = {2, 3, 4, 5}
a ^= b
print(a) #Retorna {0, 1, 4, 5}



print("----------------------------\n\n") #separador


#             OPERADORES BINARIOS

#Los operadores binarios son bastante poco usados en la practica,  sirven para operar sobre las representaciones de los valores numericos. Los operadores binarios de pthon son los siguientes:

#  Operador    Operacion
#      &         AND    
#      \         OR
#      ^         XOR
#      ~         NOT
#      <<        Desplazamiento logico a la izquierda
#      >>        Desplazam,iento logico a la derecha

#El operador AND binario (&) compara las representaciones de los numeros proporcionados y devuelve un numero que tiene unos en las posiciones donde ambos operadores tienen uno  un cero enlas posiciones donde alguno de ellos tiene un cero:

#Primer oprando      Segundo operando     Resultado
#      1                    1                    1
#      1                    0                    0
#      0                    1                    0
#      0                    0                    0

numero1 = 0b1011 
numero2 = 0b101

print(numero1) #11
print(numero2) #5

print(numero1 & numero2) #1


#El operador OR binario (|), retorna un numero tal que su representacion binaria contenga al menos uno de los operandos un uno en esa posicion,  un cero si ambos tienen un cero en ella.

#El operador binario XOR (^) retorna un numero tal que su representacion binaria contenga un uno si los operadorers tienen distinto numero en esa posicion  un cero si ambos compartenel mismo numero en ella,

#El desplazamiento logico a la dewrecha mueve los bits del operando de la izquierda tantos espacios como indique el operador de la derecha. Los bits menores que el primero son descartados.

#El desplazamiento a la izquierda desplaza los bits del operando de la izquierda a la derecha, el espacio que deja este desplazamiento se rellena con ceros.

#La operacion NOT binaria, tambien llamada complemento a uno, actua sobre la representacion binaria de un numero, y retorna otro numero en el que los unos del original han sido remplazados por ceros y los ceros por unos.