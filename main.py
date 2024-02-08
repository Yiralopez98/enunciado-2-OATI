from agenda import Agenda
from paciente import Paciente
from doctor import Doctor

def main():
    # Crear una instancia de Agenda
    agenda = Agenda()

    # Agregar pacientes
    paciente1 = Paciente("Yira", "Lopez", 35, "123456789")
    paciente2 = Paciente("Pedro", "García", 25, "987654321")
    agenda.agregar_paciente(paciente1)
    agenda.agregar_paciente(paciente2)

    # Agregar doctores
    doctor1 = Doctor("Dr. Carlos", "Gómez", "Pediatra")
    doctor2 = Doctor("Dra. Ana", "López", "Dermatóloga")
    agenda.agregar_doctor(doctor1)
    agenda.agregar_doctor(doctor2)

    # Agregar citas médicas
    agenda.agregar_cita(paciente1, doctor1, "2024-02-10", "10:00")
    agenda.agregar_cita(paciente2, doctor2, "2024-02-12", "11:00")

    # Listar doctores y sus citas
    agenda.listar_doctores_citas()

    # Modificar información de un paciente
    nuevo_paciente1 = Paciente("Yira", "Lopez", 32, "123456789")
    agenda.modificar_info_paciente(paciente1, nuevo_paciente1)

    # Eliminar una cita médica
    agenda.eliminar_cita(paciente1, doctor1)

    # Listar doctores y sus citas después de las modificaciones
    agenda.listar_doctores_citas()

if __name__ == "__main__":
    main()
