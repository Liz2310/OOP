from Personas.empleado_hospital import EmpleadoHospital
from datetime import datetime
from excepciones import NoEsObjetoSolicitado

class Enfermero(EmpleadoHospital):

    """Datos que conforman a un Enfermero.
       Hace los imports adecuados dentro de las funciones para evitar circular imports."""

    def __init__(self, cedula : str, **kwargs):
        super().__init__(**kwargs)
        self.cedula = cedula


    def crear_examinacion_general_paciente(self, paciente, peso : float, estatura : float, temperatura : float, ritmo_cardiaco : str,
                                           estado_reflejos : str, presion_sanguinea : str):
        """Crear una examinacion general a un paciente con los datos necesarios.
           Revisa que lo ingresado como paciente sea instancia de Paciente."""

        try:
            from Personas.paciente import Paciente
            from Documentos.examinacion_general import ExaminacionGeneral

            assert isinstance(paciente, Paciente)
            paciente._examinacion_general = ExaminacionGeneral(paciente, peso, estatura, temperatura, ritmo_cardiaco, estado_reflejos, presion_sanguinea)
        except AssertionError:
            raise NoEsObjetoSolicitado("Lo ingresado como paciente no es objeto Paciente")

    def crear_historial_medico_paciente(self, paciente, numero_telefono_paciente : str, estado_civil : str,
                                        residencia_actual : str, ocupacion : str, nacionalidad : str, residencia_anterior : str,
                                        religion : str, grado_de_instruccion : str, antecedentes_familiares : list,
                                        antecedentes_personales : list):
        """Crear un historial medico a un paciente con los datos necesarios.
           Revisa que lo ingresado como paciente sea instancia de Paciente."""

        try:
            from Personas.paciente import Paciente
            from Documentos.historial_medico import HistorialMedico

            assert isinstance(paciente, Paciente)
            paciente._historial_medico = HistorialMedico(paciente, numero_telefono_paciente, estado_civil, residencia_actual, ocupacion,
                                                     nacionalidad, residencia_anterior, grado_de_instruccion, religion,
                                                     antecedentes_familiares, antecedentes_personales)
        except AssertionError:
            raise NoEsObjetoSolicitado("Lo ingresado como paciente no es objeto Paciente")


    def crear_hospitalizacion_paciente(self, paciente, numero_cuarto : int, enfermeros : list, doctores : list,
                                       diagnostico : str, procedimientos : list, Departamento,
                                       fecha_de_internacion : datetime, fecha_de_alta : datetime, especificaciones : str):
        """Crear una hospitalizacion de un paciente con los datos necesarios.
           Revisa que lo ingresado como paciente sea instancia de Paciente."""

        try:
            from Personas.paciente import Paciente
            from Documentos.hospitalizacion import Hospitalizacion

            assert isinstance(paciente, Paciente)
            paciente._hospitalizacion = Hospitalizacion(paciente, numero_cuarto, enfermeros, doctores, diagnostico,
                                                    procedimientos, Departamento.nombre,
                                                    fecha_de_internacion, fecha_de_alta, especificaciones)
        except AssertionError:
            raise NoEsObjetoSolicitado("Lo ingresado como paciente no es objeto Paciente")

    def __str__(self):
        super_texto = super().__str__()
        adicional = f"Cedula: {self.cedula}"
        return super_texto + adicional


