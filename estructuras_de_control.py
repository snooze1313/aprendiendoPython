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
