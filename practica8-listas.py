food = []
num = 0

num = int (input("Ingresa e número de comidas para tu fiesta: "))

for i in range(0, num):
    food.append(input(f"Ingresa la comida numero {i+1} "))

print(food)
