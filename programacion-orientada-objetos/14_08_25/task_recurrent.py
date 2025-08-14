from task import Task

class TaskRecurrent(Task):
    frecuencia: int

    def __init__(self, descripcion: str, frecuencia: int) -> None:
        super().__init__(descripcion)
        self.frecuencia = frecuencia

    def mostrar_tarea (self) -> None:
        print(f"Descripción: {self.descripcion}")
        print(f"status: {self.status}")
        print(f"Priority: {self.priority}")
        print(f"Frecuencia: {self.frecuencia}")