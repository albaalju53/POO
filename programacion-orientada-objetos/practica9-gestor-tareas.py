#Función para imprmir menu
def menu():
    print("\nGestor de tareas\n")
    print("1. Agregar tarea")
    print("2. Insertar tarea")
    print("3. Eliminar por nombre")
    print("4. Eliminar por posición")
    print("5. Marcar omo realizado")
    print("6. Ver tareas")
    print("7. Ordenar tares")
    print("8. Revertir orden")
    print("9. Salir")

#Función main 
if __name__ == '__main__':
    continuar = True
    tareas = []
    posicion = 0
    
    menu()
    opcion = int(input("Ingresa el número de la opción a ejecutar"))
    if opcion == 1:
        tareas.append(input("Ingresa la nueva tarea"))

    elif opcion == 2:
        posicion = int(input("¿En que posición te gustaria agregar tu tarea?"))
        tareas.insert(posicion,input("Ingresa la tarea"))
    
    elif opcion == 3:
        posicion = input("Ingresa el nombre de la tarea a eliminar")
        tareas.remove(posicion)

    elif opcion == 4:
        


