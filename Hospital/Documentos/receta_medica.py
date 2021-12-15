from datetime import datetime
from Personas.doctor import Doctor
from Personas.paciente import Paciente
from Hospital.hospital import Hospital
from excepciones import NoEsObjetoSolicitado

class RecetaMedica:
    """Define los datos necesarios para llenar una receta medica.
       Revisa que doctor, hospital y paciente sean instancias de sus respectivas clases."""

    def __init__(self, doctor, hospital, paciente, nombre_medicamento : str,
                 diagnostico_paciente : str, dosis : str,
                 via_de_administracion : str, duracion_tratamiento : str, especificaciones : str = "Ninguna"):

        try:
            assert isinstance(doctor, Doctor)
            self.nombre_doctor = f"{doctor.nombre} {doctor.apellido}"
            self.cedula_docotor = doctor.cedula
        except AssertionError:
            raise NoEsObjetoSolicitado("Lo ingresado como doctor no es objeto Doctor")

        try:
            assert isinstance(hospital, Hospital)
            self.nombre_hospital = hospital.nombre
            self.direccion_hospital = hospital.direccion
        except AssertionError:
            raise NoEsObjetoSolicitado("Lo ingresado como hospital no es objeto Hospital")

        try:
            assert isinstance(paciente, Paciente)
            self.paciente = f"{paciente.nombre} {paciente.apellido}"
        except AssertionError:
            raise NoEsObjetoSolicitado("Lo ingresado como paciente no es objeto Paciente")

        self.fecha_emision = datetime.now().strftime("%Y-%m-%d")
        self.nombre_medicamento = nombre_medicamento
        self.diagnostico_paciente = diagnostico_paciente
        self.dosis = dosis
        self.via_de_administracion = via_de_administracion
        self.duracion_tratamiento = duracion_tratamiento
        self.especificaciones = especificaciones

    def __str__(self):
        return f"""RECETA MEDICA:
        Doctor: {self.nombre_doctor}
        Cedula Doctor: {self.cedula_docotor}
        Hospital: {self.nombre_hospital}
        Direccion: {self.direccion_hospital}
        Fecha de emision: {self.fecha_emision}
        Paciente: {self.paciente}
        Diagnostico: {self.diagnostico_paciente}
        Medicamento: {self.nombre_medicamento}
        Dosis: {self.dosis}
        Via de administracion: {self.via_de_administracion}
        Duracion tratamiento: {self.duracion_tratamiento}
        Especificaciones: {self.especificaciones}"""





