from excepciones import UsuarioYaExistente, ContraseñaMuyCorta, UsuarioInvalido, ContraseñaInvalida
from Personas.admin import Admin

class AutenticadorAdminHospital:
    """Autenticador que permite agregar y dar acceso a un admin al sistema de un hospital."""

    def __init__(self):
        self.usuarios = {}

    def agregar_usuario(self, usuario, contra):
        """Agrega usuario como key y objeto Admin como value al diccionario de usuarios.
           Regresa excepciones en vez de levantarlas con el fin de que el menu del hospital no deje de correr."""

        if usuario in self.usuarios:
            raise UsuarioYaExistente(f"Usuario {usuario} ya existe")

        if len(contra) < 8:
            raise ContraseñaMuyCorta("La contraseña ingresada es muy corta, debe ser minimo 8 caracteres")

        self.usuarios[usuario] = Admin(usuario, contra)
        return f"Admin {usuario} agregado"

    def login(self, usuario, contra):
        """Permite hacer login si el usuario y la contraseña ingresadas hacen match"""

        try:
            admin = self.usuarios[usuario]
            if not admin.verifica_contra(contra):
                raise ContraseñaInvalida(f"Contraseña para usuario {usuario} es incorrecta")
            else:
                return True

        except KeyError:
            raise UsuarioInvalido(f"Usuario {usuario} invalido")




