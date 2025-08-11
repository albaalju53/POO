numero_secreto =  8

print("Adivina el número secreto")
numero = int(input("Ingres un número entre el 1 y e 10"))

while numero != numero_secreto:
    numero = int(input("Ingres un número entre el 1 y e 10"))

print("felicidades has adivinado el número")