objetive = int(input('Introduce un número entero:'))
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