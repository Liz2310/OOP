from datetime import datetime
from Personas.paciente import Paciente
from excepciones import NoEsObjetoSolicitado, FechaInvalida
from UnidadesMedicas.unidadmedica import UnidadMedica

class Hospitalizacion:
    """Define los datos necesarios para los detalles de una Hospitalizacion.
       Revisa que paciente y unidad medica sean instancias de sus respectivasb clases."""

    def __init__(self, paciente, numero_cuarto : int, enfermeros : list, doctores : list,
                 diagnostico : str, procedimientos : list, unidad_medica,
                 fecha_de_internacion : datetime, fecha_de_alta : datetime, especificaciones : str = "Ninguna"):

        try:
            assert isinstance(paciente, Paciente)
            self.paciente = f"{paciente.nombre} {paciente.apellido}"
        except AssertionError:
            raise NoEsObjetoSolicitado("Lo ingresado como paciente no es objeto Paciente")

        self.numero_cuarto = numero_cuarto
        self.enfermeros = enfermeros
        self.doctores = doctores
        self.diagnostico = diagnostico
        self.procedimientos = procedimientos
        self.especificaciones = especificaciones

        try:
            assert isinstance(unidad_medica, UnidadMedica)
            self.unidad_medica = unidad_medica.nombre
        except AssertionError:
            raise NoEsObjetoSolicitado("Lo ingresado como unidad medica no es objeto UnidadMedica")

        try:
            assert fecha_de_internacion and fecha_de_alta is datetime
            self.fecha_de_internacion = fecha_de_internacion
            self.fecha_de_alta = fecha_de_alta
        except AssertionError:
            raise FechaInvalida("Lo ingresado como fecha de internacion o fecha de alta no es una fecha en formato valido")


    def __str__(self):
        return f"""HOSPITALIZACION:
        Paciente: {self.paciente}
        Cuarto: {self.numero_cuarto}
        Departamento: {self.unidad_medica}
        Diagnostico: {self.diagnostico}
        Procedimiento(s): {self.procedimientos}
        Doctor(es): {self.doctores}
        Enfermero(s): {self.enfermeros}
        Fecha internacion: {self.fecha_de_internacion}
        Fecha de alta: {self.fecha_de_alta}
        Especificaciones: {self.especificaciones}"""