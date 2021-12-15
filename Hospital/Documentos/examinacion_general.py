from excepciones import InputInvalido, NoEsObjetoSolicitado
from Personas.paciente import Paciente

class ExaminacionGeneral:
    """Define los datos necesarios de una Examinacion General.
       Revisa si el argumento de paciente es instancia de clase Paciente.
       Revisa que el peso, estatura y temperatura sean numeros."""

    def __init__(self, paciente, peso : float, estatura : float, temperatura : float, ritmo_cardiaco : str,
                 estado_reflejos : str, presion_sanguinea : str):

        try:
            assert isinstance(paciente, Paciente)
            self.paciente = f"{paciente.nombre} {paciente.apellido}"
        except AssertionError:
            raise NoEsObjetoSolicitado("Lo ingresado como paciente no es un objeto Paciente")

        try:
            assert (peso is int or float) and (estatura is int or float) and (temperatura is int or float)
            self.peso = peso #en kg
            self.estatura = estatura #en cm
            self.temperatura = temperatura #en Celsius
        except AssertionError:
            raise InputInvalido("Debe ingresarse solamente numeros enteros o decimales")

        self.ritmo_cardiaco = ritmo_cardiaco
        self.estado_reflejos = estado_reflejos
        self.presion_sanguinea = presion_sanguinea

    @property
    def indice_de_masa_corporal(self):
        """Formula para deducir el IMC de un paciente"""

        self.imc = self.peso / (self.estatura ** 2)
        return self.imc

    def __str__(self):
        return f"""EXAMINACION GENERAL:
        Paciente: {self.paciente}
        Peso: {self.peso} Kg
        Estatura: {self.estatura} m
        Temperatura: {self.temperatura} 
        Ritmo cardiaco: {self.ritmo_cardiaco}
        Estado de reflejos: {self.estado_reflejos}
        Presion sanguinea: {self.presion_sanguinea}
        Indice de Masa Corporal: {self.indice_de_masa_corporal}"""
