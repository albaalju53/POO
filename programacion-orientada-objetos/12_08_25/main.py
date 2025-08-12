from pendiente import Pendiente


list_task = []

for _ in range(3):
    pendiente = Pendiente()
    pendiente.crear_pendiente()
    pendiente.show_pendiente()
    list_task.append(pendiente)

print(len(list_task))