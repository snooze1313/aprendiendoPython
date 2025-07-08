#primera incursion a los metodos de python

#variable que guarda un terxto y lo convierte en mayusculas con el metodo upper
mayusculas = "cadena de texto".upper()
print(mayusculas)

#otras formas de usar el metodo upper
print("otra cadena de texto".upper())

texto = "cadena de texto en variable"
print(texto.upper())

mayusculas = texto.upper()
print(mayusculas)

#usando metodo open, read, y close para leer un archivo de texto
f = open("archivo.txt")
texto = f.read()
f.close()
print(texto)

