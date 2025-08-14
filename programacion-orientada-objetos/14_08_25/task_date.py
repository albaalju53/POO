from task import Task

class TaskDate(Task):
    date: str

    def __init__(self, descripcion: str, date: str) -> None:
        super().__init__(descripcion)
        self.date = date

    def mostrar_tarea (self) -> None:
        print(f"Descripción: {self.descripcion}")
        print(f"status: {self.status}")
        print(f"Priority: {self.priority}")
        print(f"Date: {self.date}")