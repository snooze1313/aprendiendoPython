#El flujo de un programa es, en principio, linea a linea. Primero se ejecuta la primera sentencia y despues las siguientes, una a una, hasta terminar el programa.

print("Esto se ejecuta primero")
print("y esto despues")
print("Y esto al final")

#Se puede poner mas de una instruccion por linea, separadas por el signo de punto y coma (;)
print("esto va primero"); print("segundo"); print("y al final")

#Pero lo mejor es no hacer eso, a menos que contribuya a la legibilidad del codigo, por la misma razon y como ya vimos las lineas en blanco son ignoradas por python, pero se deben usar para hacer el programa mas facil de leer.

#python esta dise;ado para ser legible y hace esto de forma mas inteligente, en python, el anidamiento de sentenciasno se hace con llaves ni con otros simbolos contenedores, sino por medio de la propia identacion. Las sentencias con un nivel de tabulacion estan contenidas en las que no estan identadas que le preceden, las sentencias con dos tabuladores estan incluidas en las anteriores.

'''
instruccion_principal
    una_instruccion_anidada
    otra_instruccion_anidada

instuccion_independiente
'''

#Se recomienda encarecidamente que no se use el caracter de tabulador (\t) para identar, sino que se usen espacios (pipipi me gusta usar el tabulador). La mayoria de los editores de texto especificamente aquellos que estan orientados a la programacion general, se pueden configurar para que inserten espacios en con la tecla tabulador.
#En cualquiera de los casos no se recomienda mezclar identados por espacios y por tabulador.

print("\n---------------\n")

#SALTO CONDICIONAL
#El salto condicional permite alterar el flujo de ejecucion de un programa dependiendo del valor de una condicion. En python, la instruccion para hacer saltos condicionales es "if" (si).

'''
if condicion:
    instruccion_a_ejecutar_si_se_cumple_la_condicion
'''

#si la wxpresion que sigue al if devuelve un valor False, ese bloque no se ejecutara y el flujo de ejecucion continuara con la siguiente instruccion despues del bloque if.

valor = 10
if valor > 5:
    print("El valor es mayor que 5")

print("Esta instruccion se ejecuta siempre")

#La condici0n de un if puede ser tan compleja como sea necesaria:

texto_1 = "hola"
texto_2 = "holo"

if len(texto_1) == len(texto_2) and texto_1[0] == texto_2[0] or texto_1[-1] == texto_2[-1]:
    print("Las condiciones se cumplen")
else:
    print("Las condiciones no se cumplen")


print("\n---------------\n")


#EXPRESIONES CONDICIONALES
#una forma especial de estructura condicional es la expresion condicional, tambien llamada operador ternario.
#Una ecpresion condicional tiene la siguiente sintaxis:
'''
RETORNAR_SI_CIERTO_ IF CONDICION ELSE RETORNAR_SI_FALSO
'''
#Ejemplo:
altura = 1.60
variable = "Alto" if altura > 1.70 else "Bajo"
print("juanito es:", variable)

print("\n---------------\n")


#AJUSTE DE PATRONES
#La novedad de python 3.10 fue el ajuste de patrones (pattern matching), que permite comparar un valor con varios patrones posibles y ejecutar el bloque de codigo correspondiente al primer patron que coincida.
#La sintaxis basica del ajuste de patrones es la siguiente:
'''
match valor_a_comparar:
    case patron_1:
        bloque_de_codigo_1
    case patron_2:
        bloque_de_codigo_2
    case _:
        bloque_de_codigo_por_defecto
'''

#Por ejemplo vamos como se puede resolver los codigos de un aeropuerto:

iata = "GRX"

match iata:
    case "MAD":
        print("Aeropuerto de MADRID")
    case "AEP":
        print("Aeropuerto de BUENOS AIRES")
    case "EPA":
        print("Aeropuerto de BUENOS AIRES")
    case "EZE":
        print("Aeropuerto de BUENOS AIRES")
    case "GRX":
        print("Aeropuerto de GRANDA")   #AEROPUERTO SELECCIONADO
    case "LHR":
        print("Aeropuerto de LONDRES")
    case _:
        print("Codigo de aeropuerto desconocido")
#El guion bajo (_) en el ultimo caso actua como un comodin que coincide con cualquier valor no contemplado en los casos anteriores. Es opcional pero recomendable incluirlo para manejar los casos no previstos.

print("\n---------------\n")

#Podemos indicar varios patrones alternativos en una sola clausula case separandolos por la barra vertical (|):

iata = "EPA"
match iata:
    case "MAD":
        print("Aeropuerto de MADRID")
    case "AEP" | "EPA" | "EZE":
        print("Aeropuerto de BUENOS AIRES")  #AEROPUERTO SELECCIONADO
    case "GRX":
        print("Aeropuerto de GRANDA")
    case "LHR":
        print("Aeropuerto de LONDRES")
    case _:
        print("Codigo de aeropuerto desconocido")


#BUCLE WHILE