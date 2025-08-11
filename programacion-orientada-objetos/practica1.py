#Ejercicio de practica
#Escribir un programa, el cual pedirá un verbo, y se imprimirá "I can _  better than you", donde se reemplaza _ por el verbo. Además se imprimirá cinco veces el verbo en la siguiente línea separada por espacios.

verbo = input("Ingresa un verbo en ingles: ")
print("I can", verbo , "better than you" '\n' ,(verbo + "," )*5 )