"""
Práctica: Caracteres únicos

Objetivo Aplicar bucle for y operaciones básicas de cadenas en Python para identificar y contar caracteres únicos dentro de una cadena de texto.

Instrucciones:

Escribe un programa en Python que realice lo siguiente:

Pide al usuario que ingrese una cadena de texto compuesta solo por letras minúsculas, sin espacios ni caracteres especiales.
El programa debe contar cuántas letras diferentes (únicas) contiene la cadena.
Imprime el resultado como un número entero.
"""

cadena = input("Ingresa una caden de texto compuesta solo por letras nimusculas,si espacios ni caractereas especiales")

unique = ""
count = 0
for c in cadena:
    if c not in unique:
        count = unique+c

print ("La cadena tiene")