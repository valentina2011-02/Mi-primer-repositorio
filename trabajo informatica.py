# Esto es un comentario de una sola linea
"""esto es un comentario de 
varias lineas"""

#Inicializando variables
nombre=  "laura valenttina reyes zapata"
edad= 14
estado=True
nota=5.0

#Mostrar el contenido de  las variables()
print(nombre)
print(edad)
print(estado)
print(nota)

#Que tipo de dato contiene cada variable.
print(type(nombre))
print(type(edad))
print(type(estado))
print(type(nota))

#vamos a utilizar  la funcion input para recoger datos por medio del teclado
nombre= input("¿como te llamas?")
edad=input("¿que edad tines?")
estado=input("¿en que estado te encuentras?")
nota= input("¿cual es tu nota?")

#para visualizar que guardamos en las variables anteriores
print("Hola", nombre,"un gusto conocerte")
print(" tu edad es :", edad)
print(" tu estado es;:", estado)
print(" tu nota es:", nota)