class Doctor:
    def __init__(self, nombre, apellido, especialidad):
        self.nombre = nombre
        self.apellido = apellido
        self.especialidad = especialidad
        self.citas = []

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.especialidad}"

    def agregar_cita(self, paciente):
        self.citas.append(paciente)

    def eliminar_cita(self, paciente):
        self.citas.remove(paciente)