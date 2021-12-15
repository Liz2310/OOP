from Autenticador.autenticadoradminhospital import AutenticadorAdminHospital
from UnidadesMedicas.unidadmedica import UnidadMedica
from Personas.doctor import Doctor
from Personas.paciente import Paciente
from Personas.enfermero import Enfermero
from Personas.recepcionista import Recepcionista
from excepciones import NoEsObjetoSolicitado

class Hospital:
    """Datos que conforman un hospital"""

    def __init__(self, nombre : str, direccion : str, numero_telefono : str, cupo : int):
        self.nombre = nombre.capitalize()
        self.direccion = direccion
        self.numero_telefono = numero_telefono
        self.cupo = cupo
        self._pacientes = []
        self._doctores = []
        self._recepcionistas = []
        self._enfermeros = []
        self._unidades = []
        self._autenticador_admin = AutenticadorAdminHospital()

    def agregar_unidad_medica(self, unidad_medica):
        """Revisa que la unidad medica ingresada sea instancia de la clase UnidadMedica.
           Agrega objeto UnidadMedica a lista de unidades medicas del hospital"""

        try:
            assert isinstance(unidad_medica, UnidadMedica)
            self._unidades.append(unidad_medica)
        except AssertionError:
            raise NoEsObjetoSolicitado("Lo ingresado como unidad medica no es objeto UnidadMedica")

    def agregar_doctor(self, doctor):
        """Revisa que el doctor ingresado sea instancia de la clase Doctor.
           Agrega objeto Doctor a lista de doctores del hospital"""

        try:
            assert isinstance(doctor, Doctor)
            self._doctores.append(doctor)
        except AssertionError:
            raise NoEsObjetoSolicitado("Lo ingresado como doctor no es objeto Doctor")


    def agregar_enfermero(self, enfermero):
        """Revisa que el enfermero ingresado sea instancia de la clase Enfermero.
           Agrega objeto Enfermero a lista de enfermeros del hospital"""

        try:
            assert isinstance(enfermero, Enfermero)
            self._enfermeros.append(enfermero)
        except AssertionError:
            raise NoEsObjetoSolicitado("Lo ingresado como enfermero no es objeto Enfermero")

    def agregar_recepcionista(self, recepcionista):
        """Revisa que el recepcionista ingresado sea instancia de la clase Recepcionista.
           Agrega objeto de Recepcionista a lista de recepcionistas del hospital"""

        try:
            assert isinstance(recepcionista, Recepcionista)
            self._recepcionistas.append(recepcionista)
        except AssertionError:
            raise NoEsObjetoSolicitado("Lo ingresado como recepcionista no es objeto Recepcionista")

    def agregar_paciente(self, paciente):
        """Revisa que el paciente ingresado sea instancia de la clase Paciente.
           Agrega objeto de Paciente a lista de pacientes del hospital"""

        try:
            assert isinstance(paciente,Paciente)
            self._pacientes.append(paciente)
        except AssertionError:
            raise NoEsObjetoSolicitado("Lo ingresado como paciente no es objeto Paciente")

    def __str__(self):
        return f"""
    Nombre: {self.nombre}
    Direccion: {self.direccion}
    Telefono: {self.numero_telefono}
    Cupo: {self.cupo}"""

