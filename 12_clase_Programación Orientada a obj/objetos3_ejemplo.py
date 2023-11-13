class Alumno:
    def __init__(self, nombre: str, nota: float) -> None:
        self.nombre= nombre
        self.nota = nota

    def imprimir(self):
        print(f"La nota del estudiante {self.nombre} es {self.nota}")

    def resultado(self):
        if self.nota < 3.5:
            print(f"El resultado es: desaprobado")
        else:
            print(f"El resultado es: aprobado")


alu1 = Alumno("Luis", 3.2)
alu1.imprimir()
alu1.resultado()
