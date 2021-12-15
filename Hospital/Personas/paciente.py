from Personas.persona import Persona
from datetime import datetime

class Paciente(Persona):

    """Datos necesarios de un Paciente."""

    cuenta_id = 100

    def __init__(self, razon_visita : str, seguro_medico : str = "Sin Seguro Medico", guardian : str = "Sin Guardian", **kwargs):
        super().__init__(**kwargs)
        self.id_paciente = str(Paciente.cuenta_id)
        self.razon_visita = razon_visita
        self.seguro_medico = seguro_medico
        self.guardian = guardian
        self.fecha_visita = datetime.now().strftime("%Y-%m-%d")
        self._receta = "No Cuenta Con Receta Medica"
        self._historial_medico = "No Cuenta Con Historial Medico"
        self._hospitalizacion = "No Cuenta Con Detalles de Hospitalizacion"
        self._diagnostico = "No Cuenta Con Diagnostico"
        self._examinacion_general = "No Cuenta Con Examinacion General"

        Paciente.cuenta_id += 1 #cada vez que se crea un paciente se suma uno a la variable cuenta_id (compartida por todas las instancias)

    def __str__(self):
        super_texto = super().__str__()
        adicional = f"""
    Id Paciente: {self.id_paciente}
    Razon Visita: {self.razon_visita}
    Seguro Medico: {self.seguro_medico}
    Guardian: {self.guardian}
    Fecha Visita: {self.fecha_visita}
    {self._receta}
    {self._historial_medico}
    {self._hospitalizacion}
    {self._diagnostico}
    {self._examinacion_general}"""
        return super_texto + adicional



