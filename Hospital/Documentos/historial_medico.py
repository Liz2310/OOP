from Personas.paciente import Paciente
from excepciones import NoEsObjetoSolicitado, InputInvalido
import phonenumbers

class HistorialMedico:
    """Define los datos necesarios para llenar un Historial Medica.
       Revisa que paciente sea instancias de la clase Paciente.
       Usa la libreria externa phonenumbers para revisar que el telefono
       sea uno posiblemente valido."""

    def __init__(self, paciente, numero_telefono_paciente : str, estado_civil : str,
                 residencia_actual : str, ocupacion : str, nacionalidad : str, residencia_anterior : str,
                 grado_de_instruccion : str, religion : str = None, antecedentes_familiares : list = None,
                 antecedentes_personales : list = None):

        try:
            assert isinstance(paciente, Paciente)
            self.nombre_paciente = paciente.nombre + " " + paciente.apellido
            self.fecha_nacimiento_paciente = paciente.fecha_nacimiento.strftime("%Y-%m-%d")
            self.edad_paciente = paciente.edad
            self.fecha_de_visita = paciente.fecha_visita
            self.motivo_de_consulta = paciente.razon_visita
        except AssertionError:
            raise NoEsObjetoSolicitado("Lo ingresado como paciente no es objeto Paciente")

        try:
            assert phonenumbers.is_possible_number(numero_telefono_paciente)
            self.numero_telefono_paciente = numero_telefono_paciente
        except AssertionError:
            raise InputInvalido("Lo ingresado como telefono no aparenta ser un numero valido")


        self.sexo = paciente.sexo
        self.estado_civil = estado_civil
        self.residencia_actual = residencia_actual
        self.residencia_anterior = residencia_anterior
        self.ocupacion = ocupacion
        self.nacionalidad = nacionalidad
        self.religion = religion
        self.grado_de_instruccion = grado_de_instruccion

        self.antecedentes_familiares = antecedentes_familiares
        self.antecedentes_personales = antecedentes_personales


    def __str__(self):
        return f"""HISTORIAL MEDICO:
        Nombre y apellido: {self.nombre_paciente}
        Edad: {self.edad_paciente}
        Sexo: {self.sexo}
        Ocupacion: {self.ocupacion}
        Fecha de nacimiento: {self.fecha_nacimiento_paciente}
        Estado Civil: {self.estado_civil}
        Nacionalidad: {self.nacionalidad}
        Residencia Actual: {self.residencia_actual}
        Residencia Anterior: {self.residencia_anterior}
        Grado de instruccion: {self.grado_de_instruccion}
        Religion: {self.religion}
        Fecha de visita: {self.fecha_de_visita}
        Motivo de consulta: {self.motivo_de_consulta}
        Antecedentes Familiares: {self.antecedentes_familiares}
        Antecedentes Personales: {self.antecedentes_personales}"""

