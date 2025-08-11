import aritmetica
from multiplicacion_division import multiplicar
import multiplicacion_division as md


num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

print(multiplicar(num1,num2))
print(md.division(num1, num2))
print(aritmetica.restar(num1, num2))
print(aritmetica.sumar(num1, num2))
