#con el operador = asignamos el valor "hola mundo" a la variable saludo
saludo = "Hola mundo"

#cuando asignamos un valor a una variable, se crea una referencia a ese valor
#por lo cual podemos usar la variable saludo para acceder al valor "hola mundo"
print(saludo)

#en vez de usar la cadena "hola mundo" directamente
print("hola mundo")

#usar las variables tiene como ventaja que si queremos cambiar el valor de la variable
#no tenemos que cambiarlo en todos los lugares donde lo usamos, solo en la asignación
#por ejemplo:
saludo = "Hola Python"
print(saludo)
print(saludo)
print(saludo)

#con una line podemos cambiar el valor de los 3 saludos
print("hola gente")
print("hola gente")
print("hola gente")


#podemos realizar operaciones con las variables
pi = 3.1416 #valor aproximado de pi
radio = 5   #valor del radio de un círculo
area_circulo = pi * radio ** 2  #multiplicamos pi con el operador * y elevamos el radio al cuadrado con el operador **
print(area_circulo) #imprimimos el área del círculo


#podemos hacer referencia a un valor con dos variables diferentes
valor = 10 #asignamos el valor 10 a la variable valor
mismo_valor = valor #asignamos el mismo valor a la variable mismo_valor
print(valor)    #imprimimos el valor de la variable valor
print(mismo_valor) #imprimimos el valor de la variable valor referenciada a la variable mismo_valor


#con la funcion id podemos ver la dirección de memoria donde se almacena el valor de una variable
print(id(valor))    #imprimimos el valor de la variable valor
print(id(mismo_valor)) #imprimimos el valor de la variable mismo_valor
#basicamente las vos variables tienen el mismo valor y por lo tanto la misma dirección de memoria

#hay que tener cuidado con las variables mutables, ya que si cambiamos el valor de una variable que hace referencia a otra variable, ambas variables cambiarán su valor

#python tiene recursos de memoria para optimizar el uso de memoria, por lo cual si asignamos el mismo valor a dos variables diferentes, ambas variables apuntarán al mismo valor en memoria
#por ejemplo:
a = 1  #asignamos el valor 10 a la variable a
b = 1  #asignamos el mismo valor a la variable b
print("------") #separador
print("id a:", id(a))  #imprimimos la dirección de memoria de la variable a
print("id b:", id(b))  #imprimimos la dirección de memoria de la variable b

#otro ejemplo con cadenas de texto
cadena1 = "Hola"  #asignamos el valor "Hola" a la variable
cadena2 = "Hola"  #asignamos el mismo valor a la variable cadena2
print("------")  #separador 
print("id cadena1: ", id(cadena1))  #imprimimos la dirección de memoria de la variable cadena1
print("id cadena2: ", id(cadena2))  #imprimimos la dirección de memoria de la variable cadena



#   ***error puesto a proposito por motivos didacticos***

#hay una palabra reservada en python que hace que la variable sea inalcanzable, es decir, que no se pueda acceder a su valor
#del es una palabra reservada que elimina la referencia a una variable
del cadena1  #eliminamos la referencia a la variable cadena1
print(cadena1)
#si intentamos acceder a la variable cadena1, nos dará un error porque ya no existe
#del no elimina el valor de la variable, solo elimina la referencia a ese valor

#python cuenta con muvhas palabras reservadas que no se pueden usar como nombres de variables
#por ejemplo:
#and, as, assert, break, class, continue, def, del, elif, else, except, False, finally, for, from, global, if, import, in, is, lambda, None, nonlocal, not, or, pass, raise, return, True, try, while, with, yield,

#las palabras match y case son palabras reservadas blandas, es decir, que se pueden usar como nombres de variables, pero no se recomienda porque pueden causar confusión

#las variables deben de tener un nombre descrptivo y seguir las convenciones de nombres de python, tabien llamado snake_case
#por ejemplo:
precio_sin_iva = 100  #perfecto: letras en minusculas, guiones bajos para separar palabras
PrecioConIva = 120 #correcto: pero solo se recomienda usar mayusculas al inicio de cada palabra para clases
numero_1 = 1  #correcto: se pueden usar numeros al final del nombre de la variable, pero no al inicio
ESTADO = "activo"  #correcto: se pueden usar mayusculas, pero se recomienda usar solo para constantes (valores que no cambian)
_contenido = "valor"  #correcto: se pueden usar guiones bajos al inicio del nombre de la variable, pero se recomienda solo para variables privadas (que no se deben usar fuera de la clase o modulo donde se definen)

#los siguientes nombres de variables son validos pero no se recomiendan
español = "Hola"  #correcto: pero no se recomienda usar caracteres especiales como la ñ
número = 1  #correcto: pero no se recomienda usar caracteres especiales como la tilde
fasdsf = "valor"  #correcto: pero no se recomienda usar nombres de variables que no tengan sentido



#   ***error puesto a proposito por motivos didacticos***

#los siguientes ejemplos no son validos y darán un error
2version = "1.0"  #incorrecto: no se puede iniciar el nombre de una variable con un numero
precio con iva = 100  #incorrecto: no se pueden usar espacios en el nombre de una variable
precio-sin-iva = 100  #incorrecto: no se pueden usar guiones en el nombre de una variable

#adicionalmente se recomienda que las variables sean los mas coratas psosible y que usen nombres en ingles, ya que es el idioma estandar de programacion


#se pueden declarar varias variables en una sola linea, separando los nombres de las variables con comas
a, b, c = 1, 2, 3  #asignamos los valores 1, 2 y 3 a las variables a, b y c respectivamente
print(a, b, c)  #imprimimos los valores de las variables a,

#pero no se recomienda hacer esto porque puede hacer que el codigo sea menos legible
#es mejor declarar cada variable en una linea diferente
a = 1  #asignamos el valor 1 a la variable a
b = 2  #asignamos el valor 2 a la variable b
c = 3  #asignamos el valor 3 a la variable c
print(a, b, c)  #imprimimos los valores de las variables a, b y c



#las constantes en python se declaran con mayusculas y se utilisan para valores que no cambian a lo largo del programa, estas no son una caracteristica del lenguaje, sino una convension
#por ejemplo:
PI = 3.1416  #valor aproximado de pi, se declara en mayusculas para indicar que es una constante
GRAVEDAD = 9.81  #valor de la gravedad en m/s^2
RADIO_TIERRA = 6371  #radio de la tierra en kmu
RUTA_DE_ARCHIVOS = "/ruta/al/archivo.txt"  #ruta al archivo

#supongamos que la socedad de pizzeros matematicos quiere asignar el precio de las pizzas segun su superficie en 0.25 por cm^2 mas impuesto del 21%
PRECIO_POR_CM2 = 0.25  #precio por cm^2 de la pizza
PI = 3.1416  #valor aproximado de pi
IMPUESTO = 0.21  #impuesto del 21% sobre el precio de la pizza

radio = float(input("Ingrese el radio de la pizza en cm: "))  #pedimos al usuario que ingrese el radio de la pizza
superficie = PI * radio ** 2  #calculamos la superficie de la pizza
precio_final = (PRECIO_POR_CM2 * superficie) * (1 + IMPUESTO)  #calculamos el precio final de la pizza con el impuesto
print(f"El precio final de la pizza es:", precio_final, "$")  #imprimimos el precio final de la pizza
