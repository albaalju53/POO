class Pendiente: 
    def __init__(self) -> None:
        self.estado = False
        self.prioridad = 0

    def crear_pendiente(self) -> None:
        self.descripcion= input("Ingresa tu pendiente: ")
        self.fecha_vencimiento = input("Fecha de vencimiento: ")

    def show_pendiente(self) -> None:
        print(f"Descripción: {self.descripcion} Estado: {self.estado}")
        print(f"Prioridad: {self.prioridad} Vencimiento {self.fecha_vencimiento}")

    def set_estado(self) -> None:
        if(self.estado == False):
            self.estado = True
        else:
            self.estado = False
