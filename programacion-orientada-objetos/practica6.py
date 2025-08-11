secret = 8
flag = False

for i in range(11):
    if(i == secret):
        print("Se encontro")
    
if secret not in range(11):
    print("No se encontro en el rango")
