from Personas.doctor import Doctor
from Personas.paciente import Paciente
from Hospital.hospital import Hospital
from excepciones import NoEsObjetoSolicitado

class Diagnostico:
    """Define los datos necesarios para un Diagnostico.
        Revisa que los argumentos de doctor, hospital y paciente sean instancias
        de sus clases respectivas."""

    def __init__(self, doctor, hospital, paciente, diagnosis : str, sintomas : list, resultados_estudios : list,
                 tratamiento : str, especificaciones :str = None):

        try:
            assert isinstance(doctor,Doctor)
            self.doctor = f"{doctor.nombre} {doctor.apellido} {doctor.cedula} {doctor.departamento}"
        except AssertionError:
            raise NoEsObjetoSolicitado("Lo ingresado como doctor no es un objeto Doctor")

        try:
            assert isinstance(hospital,Hospital)
            self.hospital = f"{hospital.nombre}"
        except AssertionError:
            raise NoEsObjetoSolicitado("Lo ingresado como hospital no es un objeto Hospital")

        try:
            assert isinstance(paciente,Paciente)
            self.paciente = f"{paciente.nombre} + {paciente.apellido}"
        except AssertionError:
            raise NoEsObjetoSolicitado("Lo ingresado como paciente no es un objeto Paciente")

        self.diagnosis = diagnosis
        self.sintomas = sintomas
        self.resultados_estudios = resultados_estudios
        self.tratamiento = tratamiento

        if especificaciones == None:
            self.otras_especificaciones = "Ninguna"
        else:
            self.otras_especificaciones = especificaciones

    def __str__(self):
        return f"""DIAGNOSTICO:
        Doctor: {self.doctor}
        Hospital: {self.hospital}
        Paciente: {self.paciente}
        Diagnosis: {self.diagnosis}
        Sintomas: {self.sintomas}
        Resultados de estudios: {self.resultados_estudios}
        Tratamiento: {self.tratamiento}
        Especificaciones: {self.otras_especificaciones}"""
