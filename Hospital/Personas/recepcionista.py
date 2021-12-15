from Personas.empleado_hospital import EmpleadoHospital
from excepciones import NoHayCupo, HoraOcupada, NoEsObjetoSolicitado
from datetime import datetime


class Recepcionista(EmpleadoHospital):
    """Datos que conforman una recepcionista"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def registrar_paciente_en_hospital(self, paciente, hospital):
        """Mete al registro de pacientes de un hospital una instancia de Paciente.
           Revisa que lo ingresado como paciente y hospital sean instancias de sus respectivas clases.
           Levanta una excepcion si el hospital ya no tiene cupo."""

        try:
            from Personas.paciente import Paciente
            from Hospital.hospital import Hospital

            assert isinstance(hospital, Hospital) and isinstance(paciente, Paciente)
            if hospital.cupo == 0:
                raise NoHayCupo(f"Ya no hay cupo en el hospital {hospital.nombre}")

            hospital.agregar_paciente(paciente)
            hospital.cupo -= 1
        except AssertionError:
            raise NoEsObjetoSolicitado("Lo ingresado como hospital y/o paciente no es objeto Hospital y/o Paciente")

    def agendar_cita(self, doctor, paciente, evento : str, fecha : datetime, hora : str):
        """Agrega una cita en el calendario del doctor especificado y como detalles incluye al Paciente de la cita.
           Revisa que lo ingresado como paciente y doctor sean instancias de sus respectivas clases."""

        try:
            from Personas.paciente import Paciente
            from Personas.doctor import Doctor

            assert isinstance(doctor, Doctor) and isinstance(paciente, Paciente)
            for i in doctor.calendario.calendario:
                for j in i:
                    if j == hora:
                        raise HoraOcupada("Hora no disponible")
            doctor.calendario.agregar_evento(evento, fecha, hora, detalles_evento=f"Paciente {paciente.nombre} {paciente.apellido}")
        except AssertionError:
            raise NoEsObjetoSolicitado("Lo ingresado como doctor y/o paciente no es objeto Doctor y/o Paciente")












