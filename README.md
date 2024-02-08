# Sistema de Gestión de Citas Médicas

Este es un sistema de gestión de citas médicas que utiliza Python y una base de datos MySQL en un servidor XAMPP para almacenar información de pacientes, doctores y citas médicas.

## Estructura de Archivos

- `paciente.py`: Contiene la definición de la clase `Paciente`.
- `doctor.py`: Contiene la definición de la clase `Doctor`.
- `cita_medica.py`: Contiene la definición de la clase `CitaMedica`.
- `agenda.py`: Contiene la definición de la clase `Agenda` y la lógica principal del sistema.

## Configuración y Uso

1. **Instalación de Python**: Asegurese de tener Python instalado en tu sistema.
2. **Instalación de `mysql-connector-python`**: Instala el paquete `mysql-connector-python` utilizando pip: `pip install mysql-connector-python`.
3. **Configuración de XAMPP**: Asegúrate de tener un servidor MySQL configurado y ejecutándose en XAMPP.
4. **Configuración de la Base de Datos**: Crea una base de datos en MySQL llamada `citas_medicas` con las tablas correspondientes
5. **Configuración de la Conexión a la Base de Datos**: En el archivo `agenda.py`, configura la conexión a la base de datos con los detalles apropiados (host, usuario, contraseña, nombre de la base de datos).
6. **Ejecución del Sistema**: Ejecuta el archivo `agenda.py` para comenzar a utilizar el sistema de gestión de citas médicas.

## Funcionalidades Principales

- Registro de pacientes y doctores.
- Agendamiento y eliminación de citas médicas.
- Modificación de información de pacientes y doctores.
- Listado de citas médicas por doctor.

## Base de datos
-- Crear la base de datos
CREATE DATABASE cita_medica;

-- Usar la base de datos
USE cita_medica;

-- Crear la tabla para los pacientes
CREATE TABLE Pacientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    edad INT,
    telefono VARCHAR(15)
);

-- Crear la tabla para los doctores
CREATE TABLE Doctores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    especialidad VARCHAR(100)
);

-- Crear la tabla para las citas medicas
CREATE TABLE CitasMedicas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    paciente_id INT,
    doctor_id INT,
    fecha DATE,
    hora TIME,
    FOREIGN KEY (paciente_id) REFERENCES Pacientes(id),
    FOREIGN KEY (doctor_id) REFERENCES Doctores(id)
);
