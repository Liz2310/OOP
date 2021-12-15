from datetime import datetime
from Personas.persona import Persona
from Calendario.calendario import Calendario
from Funciones.id_empleados import int32_to_id
from excepciones import FechaEnElFuturo

class EmpleadoHospital(Persona):

    cuenta_para_id = 100000000 #con la funcion int32_to_id se convierte a alfanumerico

    def __init__(self, posicion : str, fecha_de_empleo : datetime ,  departamento : str,
                 horario : dict, telefono : str, correo : str,  **kwargs):

        """Datos que conforman a un empleado del hospital.
           Levanta una excepcion si la fecha de empleo esta en el futuro."""

        super().__init__(**kwargs)
        self.id_empleado = int32_to_id(EmpleadoHospital.cuenta_para_id)
        self.calendario = Calendario()

        if fecha_de_empleo > datetime.now():
            raise FechaEnElFuturo("Fecha de empleo en el futuro invalida")
        else:
            # El error se corrigio aqui, estaba como fecha_de_empleo.strftime(), pero mejor decidimos ponerselo en __str__
            self.fecha_de_empleo = fecha_de_empleo

        self.estatus_empleo = "Empleado Actualmente"
        self.departamento = departamento.capitalize()
        self.horario = horario
        self.telefono = telefono
        self.correo = correo
        self.posicion = posicion

        EmpleadoHospital.cuenta_para_id += 1

    def agregar_evento_calendario(self, evento : str, fecha_evento : datetime, hora : str, detalles : str = "Ninguno"):
        """Agrega una cita o evento al calendario del empleado"""
        self.calendario.agregar_evento(evento, fecha_evento, hora, detalles)

    def eliminar_evento_calendario(self, evento : str):
        """Elimina una cita o evento del calendario del empleado"""
        self.calendario.eliminar_evento(evento)

    def ver_calendario(self):
        """Imprime los contenidos del calendario del empleado"""
        self.calendario.ver_calendario()


    def __str__ (self):
        super_texto = super().__str__()
        adicional = f"""
    Id Empleado: {self.id_empleado}
    Fecha de empleo: {self.fecha_de_empleo.strftime("%Y-%m-%d")}
    Departamento : {self.departamento}
    Estatus Empleo: {self.estatus_empleo}
    Info contacto: 
        Tel: {self.telefono}
        Correo: {self.correo}
    Posicion : {self.posicion}
    Horario: {self.horario}"""
        return super_texto + adicional
