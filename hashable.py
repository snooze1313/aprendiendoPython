#Muy relacionado con el concepto de mutabiliad, tenemos el de hasheabilidad.

#En general, un hash es el resultado de aplicar una funcion resumen (funcion hash) a una cantidad de informacion de tama;o arbitrario, para poder obtener otra de tama;o conocido de forma eficiente, repetible t unica, normalmente en la forma de un numero entero.

#En python, se usan funciones hash para implementar las claves de ciertos conjuntos, como diccionarios y sets, en lo que se conoce como tablas hash. La idea detras de estos es que es mas eficiente y rapido obtener hashses de las claves al crear el diccionario y luego usar esos hashes en lugar de las propias claves para acceder, ordenar, modificar, etc. Para todo esto es importante que el hash no cambie a lo largo de la vida del objeto. Otra propiedad que necesitan los hashes en python es poder usarse para comparar objetos: dos objetos que sean iguales deben tener el mismo hash.

#A un objeto hash de python del que se puede obtener un hash que cumpla esas condiciones se le llama hasheable, y esos objetos son precisamente, los que podemos usar como claves en diccionarios, sets y otros contenedores.

#LA FUNCION hash() RETORNA EL HASH DEL OBJETO QUE SE LE PASA COMO ARGUMENTO, SI ES QUE TIENE UNO.

#Son haheables todos lo tipos de datos inmutables, como los numeros, las cadenas, los bytes y las tuplas (si su contenido es hasheable); por eso, se pueden usar de claves en diccionarios o como miembros de un set. Los tipos mutables (como listas o diccionarios) no son hasheables y no pueden usarse como clave. Los objetos creados a partir de nuestras propias clases son tambien (en principio) hasheables.

#los slices (que son obhjetos de tipo slice) son hasheables a partit de la version 3.12 de python, pero no en versiones anteriores.

#ES IMPORTATNTE HACER NOPTAR QUE LOS CONTENEDORES DE TIPO MUTABLES NUNCA SON HASHEABLES, LOS CONTENEDORES DE TIPO INMUTABLES SON HASHEABLES SOLO SI TODOS SUS ELEMENTOS DE SU CONTENIDO SON HASHEABLES. POR EJEMPLO UNA TUPLA QUE CONTIENE ENTRE SUS ELEMENTOS UNA LISTA YA NO ES HASHEABLE Y POR TANTO NO SE PUEDE USAR DE CLAVE EN DICCIONARIOS O SETS.

#               TECNICAMENTE, PARA SEA HASHEABLE DEBE TENER DEFINIDO UN METODO __hash__() QUE CALCULESU VALOR HASH Y UN METODO __eq__() QUE PERMITA CONPARARLO.