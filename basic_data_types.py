#todos los lengiuajes de programacion siponen de tipos de datos basicos con los que operar, estos tipos nativos varian entre lenguajes, pero casi todos incluyen uno o mas tipos numericos y alguna forma de codificar cadenas de texto.

#python  es asi, pero cuenta cuenta con el matiz de que todos los datos son objetos y esos tipos basicos son clases.


#cadenas de texto
#en python cuna cadena de texto o tambien llamada string es  tecnicamente un objeto str, es una secuencia de caracteres que lo comprende letras, numeros, simbolos y espacios en blanco. las cadenas de texto se definen encerrando el texto entre comillas simples o dobles (teniendo en cuenta que pythom soporta UFT-8).
cadena1 = "Hola, mundo!"

#cuando hay dos o mas cadenas de texto separadas por espacios, python las interpreta como una sola cadena de texto.
cadena2 = "Hola," " mundo!" " python es genial!"
print(cadena2)


print("\n---------\n")#seperador

#disponer de ambos tipos de comillas permite incluir una dentro de la otra sin necesidad de usar el caracter de escape.
cadena3 = "Hola, 'mundo'!"
cadena4 = 'Hola, "mundo"!'
print(cadena3)
print(cadena4)
