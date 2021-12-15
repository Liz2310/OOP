from passlib.context import CryptContext

class Admin():
    """Crea un admin con un ususario y una contraseña que usa la libreria passlib
       para encriptarla."""

    algoritmo_para_hashing = CryptContext(
        schemes = ["pbkdf2_sha256"],
        default = "pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
    )

    def __init__(self, usuario : str, contraseña : str):
        self.usuario  = usuario
        self.contraseña = self._encripta_contra(contraseña)

    def _encripta_contra(self, contra):
        """Encripta la contraseña usando el metodo hash que viene con la libreria passlib"""
        return self.algoritmo_para_hashing.hash(contra)

    def verifica_contra(self, contra):
        """Verifica que la contraseña ingresada haga match con la asociada con el usuario usando el metodo
           verify que viene con la libreria passlib"""
        return self.algoritmo_para_hashing.verify(contra, self.contraseña)



if __name__ == "__main__":
    a = Admin("lol", "pass1234")
    print(a.verifica_contra("pass1234"))