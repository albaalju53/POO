guess = 0
cube = int(input("Ingresa un número entero: "))

while (guess**3 >= cube ) and (guess**3 != cube ):
    guess += 1

if ( guess**3 == cube):
    print("Raiz es ", cube)
else:
    print("No hay", guess)