#esto es un comentario de una sola linea
"""Esto es un comentario de varias lineas"""

#Inicializando variables
nombre="Nombre del estudiante"
edad=45
estado=True
nota=5.0

#Mostrar el contemido de las variables print()
print(nombre)
print(edad)
print(estado)
print(nota)

#Que tipo de dato contiene cada variable.
print(type(nombre))
print(type(edad))
print(type(estado))
print(type(nota))

#Utilizando la funcion imput para recogger datos por medio del teclado
nombre=input("¿Como te llamas? ")
edad=input("¿Que edad tienes? ")
estado=input("¿Enque estado te encuentras? ")
nota=input("¿Cual es tu nota?")

#Para visualizar guardamos las variables anteriores
print("Hola,",nombre, "un gusto conocerte")
print("Tu edad es:",edad)
print("Tu estado es:",estado)
print("Tu nota es:",nota)