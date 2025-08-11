
#nombre="Alice"
#apellido = "Smith"
#print(nombre,apellido)

#input-> Entrada de datos por consola
#nombre = input("¿Como te llamas?")
#print("Hola",nombre)


#Ejemplo de estructra if: Comparar mayor de dos numeros

"""
num_1= int(input("Escoge un entero: "))
num_2= int(input("Escoge un entero: "))

if num_1 > num_2:
    print("Primero mayor que el segundo")
elif num_1 < num_2:
    print("Sengundo mayor que el primero")
else:
    print("numeros iguales")
"""
"""
an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1–10): "))

for c in word:
    if c in an_letters:
        print(f'Give me an {c}: {c}')
    else:
        print(f'Give me a {c}: {c}')

print("What's that spell?")
for i in range(times):
    print(word, '!!!')

"""


#Demostración de Suma de número flotante 
"""x= 0
for i in range(10):
    x += 0.1
print(x == 1)
print(x, "==", 10* 0.1)
"""

#Demostración: Conversión decimal a flotante
"""num = 1507
result = ''

if num == 0:
   result = '0'

while num > 0:
   result = str(num%2) + result
   num = num // 2"""


"""
x = 0.1

p = 0
while ((2**p)*x) % 1 != 0:
    print('Resto = ' + str((2**p)*x - int((2**p)*x)))
    p += 1

num = int(x * (2**p))

resultado = ''
if num == 0:
    resultado = '0'
while num > 0:
    resultado = str(num % 2) + resultado
    num = num // 2

for i in range(p - len(resultado)):
    resultado = '0' + resultado

resultado = resultado[0:-p] + '.' + resultado[-p:]

print('La representación binaria del decimal ' + str(x) + ' es ' + str(resultado))"""

#Busqueda aproximada raíz cuadrada
"""objetive = int(input('Introduce un número entero:'))
epsilon = 0.01 #0.0001
step = epsilon**2
solution = 0.0

while abs(solution**2 - objetive) >= epsilon and solution <= objetive:
   print(abs(solution**2 - objetive), objetive)
  solution += step

if abs(solution**2 - objetive) >= epsilon:
   print(f'No se encontro la raíz cuadrada de {objetive}')
else:
   print(f'La raíz cuadrada de {objetive} es ~ {solution}')
"""

#Busqueda binaria raíz cuadrada
objetive = int(input('Introducir un número entero:'))
epsilon = 0.001
lower_limit = 0.0 #limte inferior
upper_limit = max(1.0, objetive) #limite superior. 
step = epsilon**2
solution = (upper_limit + lower_limit) / 2
count = 0

while abs(solution**2 - objetive) >= epsilon:
    if solution**2 < objetive:
        lower_limit = solution
        count += 1
    else:
        upper_limit = solution
    
    solution = (upper_limit + lower_limit) / 2

print(f'La raíz cuadrada de {objetive} es ~ {solution}')
print(f"count {count}")