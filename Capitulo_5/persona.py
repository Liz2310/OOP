from datetime import datetime

class Persona:

    def __init__(self, nombre: str, apellido: str, fecha_de_nacimiento: datetime):
        self.nombre = nombre
        self.apellido = apellido
        self._fecha_de_nacimiento = fecha_de_nacimiento

    @property
    def edad(self):
        "Propiedad para calcular la edad"
        delta = datetime.now() - self._fecha_de_nacimiento
        return int(delta.days // 365.25)

    @property
    def fecha_de_nacimiento(self):
        "Propiedad que representa la fecha de nacimiento"
        return self._fecha_de_nacimiento.strftime("%d/%m/%Y")

    @fecha_de_nacimiento.setter
    def fecha_de_nacimiento(self, fecha_de_nacimiento_nueva):
        if datetime.now() < fecha_de_nacimiento_nueva:
            raise Exception("Fecha en el futuro")
        self._fecha_de_nacimiento = fecha_de_nacimiento_nueva


if __name__ == "__main__":
    p = Persona("Ximena","Glez", datetime(2002,10,23))
    print(p.edad)
    print(p.fecha_de_nacimiento)
    p.fecha_de_nacimiento = datetime(2002,1,27)
    print(p.fecha_de_nacimiento)
    print(p.edad)

