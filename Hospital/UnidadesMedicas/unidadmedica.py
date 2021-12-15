from Personas.doctor import Doctor
from Personas.enfermero import Enfermero
from Personas.recepcionista import Recepcionista
from excepciones import NoEsObjetoSolicitado, InputInvalido

class UnidadMedica:
    """Datos que conforman una instancia de UnidadMedica."""

    def __init__(self, nombre : str, capacidad : int):
        self.nombre = nombre.capitalize()
        try:
            self.capacidad = int(capacidad)
        except ValueError:
            raise InputInvalido("La capacidad de la unidad medica debe ser un numero entero")
        self._doctores = []
        self._enfermeros = []
        self._recepcionistas = []

    def agregar_doctor(self, doctor):
        """Agrega un objeto doctor a la lista de doctores que estan relacionados con la unidad medica.
           Revisa que lo ingresado como doctor sea instancia de la clase Doctor."""

        try:
            assert isinstance(doctor, Doctor)
            self._doctores.append((doctor.nombre,doctor.apellido,doctor.id_empleado))
        except AssertionError:
            raise NoEsObjetoSolicitado("Lo ingresado como doctor no es objeto Doctor")

    def agregar_enfermero(self, enfermero):
        """Agrega un objeto enfermero a la lista de enfermeros que estan relacionados con la unidad medica.
           Revisa que lo ingresado como enfermero sea instancia de la clase Enfermero."""

        try:
            assert isinstance(enfermero, Enfermero)
            self._enfermeros.append((enfermero.nombre,enfermero.apellido,enfermero.id_empleado))
        except AssertionError:
            raise NoEsObjetoSolicitado("Lo ingresado como enfermero no es objeto Enfermero")

    def agregar_recepcionista(self, recepcionista):
        """Agrega un objeto recepcionista a la lista de recepcionistas que estan relacionados con la unidad medica.
           Revisa que lo ingresado como recepcionista sea instancia de la clase Recepcionista."""
        try:
            assert isinstance(recepcionista, Recepcionista)
            self._recepcionistas.append((recepcionista.nombre,recepcionista.apellido,recepcionista.id_empleado))
        except AssertionError:
            raise NoEsObjetoSolicitado("Lo ingresado como recepcionista no es objeto Recepcionista")

    def __str__(self):
        return f"""
    Nombre: {self.nombre}
    Capacidad: {self.capacidad}
    Doctores: {self._doctores}
    Enfermeros: {self._enfermeros}
    Recepcionistas: {self._recepcionistas}"""