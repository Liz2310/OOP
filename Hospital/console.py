from menu_hospital import MenuHospital
import sys

class Console:

    """Consola principal para que el admin haga login."""

    def __init__(self, Hospital):
        self.hospital = Hospital
        self.opciones = {
            "1": self.login,
            "2": self.quit
        }

        print(f"""
    Bienvenido al sistema de {self.hospital.nombre}.
        
    Menu 
    1: Login.
    2: Salir
    """)

        while True:
            resp = input("Ingrese una opcion: ")
            accion = self.opciones.get(resp)
            if accion:
                accion()
            else:
                print(f"{resp} no es una opcion valida")

    def login(self):
        """Llama a la funcion del autenticador que permite hacer login al admin autorizado."""

        usuario = input("Ingrese el usuario: ")
        contra = input("Ingrese la contraseña: ")

        if self.hospital._autenticador_admin.login(usuario, contra):
            MenuHospital(self.hospital).correr()

    def quit(self):
        sys.exit()


