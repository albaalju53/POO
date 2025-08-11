#Ejemplo Crear un programa en Python que:

#Guarde un número secreto.
#Pida al usuario que adivine un número.
#Indique si el número ingresado es menor, mayor, o igual al número secreto.

num = int(input("Ingrese un entero: "))
secret = 8
if num > secret:
    print("El numero es mayor al número secreto")
elif num < secret:
    print("El numero es menor al número secreto")
else:
    print("Número correcto")


 