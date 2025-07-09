#para importar un modulo se usa la palabra clave import

import time #modulo de tiempo

#uso de la funcion asctime del modulo time
fecha = time.asctime() #funcion del modulo time
print(fecha)

#a veces el nombre del modulo es muy largo, por lo que se puede usar la palabra clave as para renombrarlo
import time as ti #ahora se puede usar ti en lugar de time
fecha = ti.asctime() #funcion del modulo time
print(fecha)

#tambien se pueden importar funciones especificas de un modulo
from time import asctime #importa solo la funcion asctime del modulo time
fecha = asctime() #ahora se puede usar asctime directamente
print(fecha)

#tambien se pueden importar varias funciones especificas de un modulo
#from nombreDelModulo import funcion1, funcion2 //importa las funciones funcion1 y funcion2 del modulo NombreDelModulo

#tambien se pueden importar todas las funciones de un modulo
#from nombreDelModulo import * //importa todas las funciones del modulo NombreDelModulo
from time import * #importa todas las funciones del modulo time
#python no importa modulos que inician con guion(_) bajo cuando se usa el asterisco(*)
#algunos modulos de python estan diseñados para ser utilisadps directamente y no a traves de otros scrips

