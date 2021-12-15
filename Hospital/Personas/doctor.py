from Personas.empleado_hospital import EmpleadoHospital
from excepciones import PacienteNoReconocido, NoEsObjetoSolicitado, PacienteDuplicado

class Doctor(EmpleadoHospital):
    """Datos que conforman a un doctor.
       Hace los imports adecuados dentro de las funciones para evitar circular imports."""

    def __init__(self, especialidad : str, cedula : str, **kwargs):
        super().__init__(**kwargs)
        self.especialidad = especialidad
        self.cedula = cedula
        self.lista_pacientes = []

    def agregar_paciente_a_lista_de_pacientes(self, paciente):
        """Agrega un paciente a lista de pacientes que atiende un doctor.
           Revisa que lo ingresado como paciente sea instancia de Paciente."""
        try:
            from Personas.paciente import Paciente
            assert isinstance(paciente, Paciente)
            if (paciente.nombre, paciente.apellido, paciente.id_paciente) in self.lista_pacientes:
                raise PacienteDuplicado(f"El paciente ingresado ya se encuentra en la lista del doctor {self.nombre} {self.apellido}")
            self.lista_pacientes.append((paciente.nombre, paciente.apellido, paciente.id_paciente))
        except AssertionError:
            raise NoEsObjetoSolicitado("Lo ingresado como paciente no es objeto Paciente")

    def eliminar_paciente_de_lista_de_pacientes(self, paciente):
        """Elimina un paciente de lista de pacientes que atiende un doctor.
           Revisa que lo ingresado como paciente sea instancia de Paciente."""
        try:
            from Personas.paciente import Paciente
            assert isinstance(paciente, Paciente)
            self.lista_pacientes.remove((paciente.nombre, paciente.apellido, paciente.id_paciente))
        except AssertionError:
            raise NoEsObjetoSolicitado("Lo ingresado como paciente no es objeto Paciente")

    def crear_receta_para_paciente(self, hospital, paciente, nombre_medicamento : str,
                                   diagnostico_paciente : str, dosis : str, via_de_administracion : str,
                                   duracion_tratamiento : str):
        """Crea un receta medica a un paciente
           Levanta una excepcion si el paciente proporcionado no esta en
           la lista de pacientes del doctor"""

        try:
            from Personas.paciente import Paciente
            from Hospital.hospital import Hospital
            from Documentos.receta_medica import RecetaMedica

            assert isinstance(paciente, Paciente) and isinstance(hospital, Hospital)
            if (paciente.nombre, paciente.apellido, paciente.id_paciente) not in self.lista_pacientes:
                raise PacienteNoReconocido(f"Paciente {paciente.nombre} {paciente.apellido} {paciente.id_paciente} no se encuentra en la lista de pacientes")

            paciente._receta = RecetaMedica(self, hospital, paciente, nombre_medicamento,
                                                diagnostico_paciente, dosis, via_de_administracion,
                                                duracion_tratamiento)
        except AssertionError:
            raise NoEsObjetoSolicitado("Lo ingresado como paciente y/u hospital no es objeto Paciente y/u Hospital")

    def crear_diagnostico_de_paciente(self, hospital, paciente, diagnosis : str, sintomas : list, resultados_estudios : list,
                                      tratamiento : str, especificaciones : str = None):
        """Crea un diagnostico a un paciente.
           Levanta una excepcion si el paciente proporcioHnado no esta en
           la lista de pacientes del doctor"""

        try:
            from Personas.paciente import Paciente
            from Hospital.hospital import Hospital
            from Documentos.diagnostico import Diagnostico

            assert isinstance(paciente, Paciente) and isinstance(hospital, Hospital)
            if (paciente.nombre, paciente.apellido, paciente.id_paciente) not in self.lista_pacientes:
                raise PacienteNoReconocido(f"Paciente {paciente.nombre} {paciente.apellido} {paciente.id_paciente} no se encuentra en la lista de pacientes")

            paciente._diagnostico = Diagnostico(self, hospital, paciente, diagnosis, sintomas, resultados_estudios,
                                                    tratamiento, especificaciones)
        except AssertionError:
            raise NoEsObjetoSolicitado("Lo ingresado como paciente y/u hospital no es objeto Paciente y/u Hospital")


    def __str__(self):
        super_texto = super().__str__()
        adicional = f"""
    Cedula: {self.cedula}
    Especialidad: {self.especialidad}"""

        return super_texto + adicional












