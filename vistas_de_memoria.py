#Vista de memoria
#Las vistas de memoria son un tipo de objeto enfocado a solucionar un aspecto muy concreto de python, y que lomas probable es que no usemos practicamente nunca.

#El protocolo buffer
#Algunos objetos de python implementan el protocolo buffer (buffer protocol) de bajo nivel que forma parte de la API-C de python. El protocolo buffer es importante cuando se quiere programar en lenguaje C bibliotecas que optimizen el acceso a flujos de datos, pero no suelen ser relevantes cuando trabajamos directaamente en python.

#los objetos que soportan el protocolo buffer pueden por medio de este exponer informacion de forma eficiente, en forma de un flujo de bits o grupo de bits; el protocolo buffer sacrifica potencia y flexibilidad por eficiencia, y es por eso que no es muy utilizado en python.

#Los objetos bytes o los objetos bytearray son ejemplos de objetos que implementan el protocolo buffer, y por lo tanto pueden ser utilizados como vistas de memoria.


#Los objetos memoryview
#Las vistas de memoria u objetos de memoryview son una forma de acceder, desde codigo escrito en python, al protocolo buffer de los objetos que lo implementen. Un objeto memoryview solo puede crearce con la funcion memoryview(), a partir de un objeto que soporte el protocolo buffer.

mis_bytes = b"123456789012345678901234567890"
mi_vista = memoryview(mis_bytes)
print(type(mi_vista))
print(mi_vista)

#si se le pasa un objeto que no soporte el protocolo buffer, se genera un TypeError


#Las vistas de memoria tienen metodos para extraer datos como tobytes() que retornan los datos del buffer en forma de cadena de bytes, o tolist() que retorna en forma de lista.

mi_sring = b"abcdefghijklmnopqrstuvwxyz"
vista = memoryview(mi_sring)
print(type(vista))
print(vista)
print("como bytes: ", vista.tobytes())  # Retorna los datos como bytes
print("como listya: ", vista.tolist())   # Retorna los datos como lista de enteros

#tambien algunos atributos iunteresantes como itemsize, que contienen el tamaño en bytes de cada elemento del buffer, o nbytes que contiene el tamaño total en bytes del buffer.
print("tamaño de cada elemento: ", vista.itemsize)

