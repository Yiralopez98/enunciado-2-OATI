class CitaMedica:
    def __init__(self, paciente, doctor, fecha, hora):
        self.paciente = paciente
        self.doctor = doctor
        self.fecha = fecha
        self.hora = hora

    def __str__(self):
        return f"{self.paciente} - {self.doctor} - {self.fecha} - {self.hora}"
