class Paciente:
    def __init__(self, nombre, apellido, edad, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre} {self.apellido}"