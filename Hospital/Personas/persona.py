from datetime import datetime
from excepciones import FechaInvalida

class Persona:
    """Datos que conforman la clase persona."""

    def __init__(self, nombre : str, apellido : str, fecha_nacimiento : datetime, sexo : str):
        self.nombre = nombre.capitalize()
        self.apellido = apellido.capitalize()
        try:
            self.fecha_nacimiento = fecha_nacimiento
        except ValueError:
            raise FechaInvalida("Algunos de los valores ingresados para la fecha son incorrectos")
        self.sexo = sexo.capitalize()

    @property
    def edad(self):
        diferencia = datetime.now() - self.fecha_nacimiento
        return int(diferencia.days // 365.25)

    def __str__(self):
        return f"""
    Nombre: {self.nombre}
    Apellido : {self.apellido}
    Edad: {self.edad}"""