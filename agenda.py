from cita_medica import CitaMedica
import mysql.connector

class Agenda:
    def __init__(self):
        self.pacientes = []
        self.doctores = []
        self.citas = []
        #Configurar la conexión a la base de datos MySQL
        self.conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=" ",
        database="cita_medica"
        )
        self.cursor = self.conn.cursor()

    # Métodos de la clase Agenda
    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)
        # Insertar el paciente en la base de datos
        sql = "INSERT INTO Pacientes (nombre, apellido, edad, telefono) VALUES (%s, %s, %s, %s)"
        values = (paciente.nombre, paciente.apellido, paciente.edad, paciente.telefono)
        self.cursor.execute(sql, values)
        self.conn.commit()

    def agregar_doctor(self, doctor):
        self.doctores.append(doctor)
        #Insertar doctor en la base de datos
        sql = "INSERT INTO Pacientes (nombre, apellido, especialidad) VALUES (%s, %s, %s, %s)"
        values = (doctor.nombre, doctor.apellido, doctor.especialidad)
        self.cursor.execute(sql, values)
        self.conn.commit()

    def eliminar_cita(self, paciente, doctor):
        for cita in self.citas:
            if cita.paciente == paciente and cita.doctor == doctor:
                self.citas.remove(cita)
                doctor.eliminar_cita(paciente)
                # Eliminar la cita médica de la base de datos
                sql = "DELETE FROM CitasMedicas WHERE paciente_id = %s AND doctor_id = %s"
                values = (paciente.id, doctor.id)
                self.cursor.execute(sql, values)
                self.conn.commit()
                break

    def listar_doctores_citas(self):
        for doctor in self.doctores:
            print(f"{doctor}:")
            for paciente in doctor.citas:
                 print(f"  {paciente}")

    def modificar_info_paciente(self, paciente, nueva_info):
        index = self.pacientes.index(paciente)
        self.pacientes[index] = nueva_info
        # Modificar la información del paciente en la base de datos
        sql = "UPDATE Pacientes SET nombre = %s, apellido = %s, edad = %s, telefono = %s WHERE id = %s"
        values = (nueva_info.nombre, nueva_info.apellido, nueva_info.edad, nueva_info.telefono, paciente.id)
        self.cursor.execute(sql, values)
        self.conn.commit()

    def modificar_info_doctor(self, doctor, nueva_info):
        index = self.doctores.index(doctor)
        self.doctores[index] = nueva_info
        # Modificar la información del doctor en la base de datos
        sql = "UPDATE Doctores SET nombre = %s, apellido = %s, especialidad = %s WHERE id = %s"
        values = (nueva_info.nombre, nueva_info.apellido, nueva_info.especialidad, doctor.id)
        self.cursor.execute(sql, values)
        self.conn.commit()