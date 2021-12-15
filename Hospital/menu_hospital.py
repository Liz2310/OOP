from Personas.enfermero import Enfermero
from Personas.recepcionista import Recepcionista
from Funciones.datos_basicos_empleado import pedir_datos_basicos_empleado
from Personas.doctor import Doctor
from Funciones.buscar_unidad import buscar_unidad
from Funciones.buscar_detalles_empleado import buscar_detalles_empleado
from Funciones.estatus_empleado import buscar_id_y_cambiar_estatus
from UnidadesMedicas.unidadmedica import UnidadMedica
from excepciones import FechaInvalida, FechaEnElFuturo, InputInvalido, UsuarioYaExistente, ContraseñaMuyCorta
import sys

class MenuHospital:

    def __init__(self, Hospital):
        self.hospital = Hospital

        self.opciones = {
            "1": self.ver_staff_doctores,
            "2": self.ver_staff_enfermeros,
            "3": self.ver_staff_recepcionistas,
            "4": self.ver_unidades_medicas,
            "5": self.modificar_estatus_empleo_empleado,
            "6": self.agregar_empleado_a_staff,
            "7": self.ver_registro_pacientes,
            "8": self.agregar_empleado_a_unidad_medica,
            "9": self.agregar_admin,
            "10": self.agregar_unidad_medica,
            "11": self.ver_detalles_empleado,
            "12": self.ver_detalles_paciente,
            "13": self.ver_detalles_admin,
            "14": self.eliminar_admin,
            "15": self.salir
        }

    def mostrar_menu(self):
        """Imprime las opciones del menu."""

        print(
        """
        Menu

        1. Ver Staff de Doctores
        2. Ver Staff de Enfermeros
        3. Ver Staff de Recepcionistas
        4. Ver Unidades Medicas
        5. Modificar Estatus de Empleo de Empleado
        6. Agregar Empleado a Staff
        7. Ver Registro de Pacientes
        8. Agregar Empleado a Unidad Medica
        9. Agregar Admin
        10. Agregar Unidad Medica
        11. Ver Detalles de Empleado
        12. Ver Detalles de Paciente
        13. Ver ususarios de Admins
        14. Eliminar Admin
        15. Salir
        """
        )

    def correr(self):
        """Dependiendo de la opcion ingresada por el usuario, llama a esa funcion usando el input como llave para
           obtener el value correspondiente."""

        while True:
            self.mostrar_menu()
            resp = input("Ingrese una opcion: ")
            accion = self.opciones.get(resp)
            if accion:
                accion()
            else:
                print(f"{resp} no es una opcion valida")

    def ver_staff_doctores(self):
        """Imprime los doctores afiliados al hospital y que esten empleados actualmente."""

        print("STAFF DOCTORES: ")
        for doctor in self.hospital._doctores:
            if doctor.estatus_empleo != "Ex-Empleado":
                print(doctor)
        input("\nPresiona ENTER para continuar")

    def ver_staff_enfermeros(self):
        """Imprime los enfermeros afiliados al hospital y que esten empleados actualmente."""

        print("STAFF ENFERMEROS: ")
        for enfermero in self.hospital._enfermeros:
            if enfermero.estatus_empleo != "Ex-Empleado":
                print(enfermero)
        input("\nPresiona ENTER para continuar")

    def ver_staff_recepcionistas(self):
        """Imprime los recepcionistas afiliados al hospital y que esten empleados actualmente."""

        print("STAFF RECEPCIONISTAS: ")
        for recepcionista in self.hospital._recepcionistas:
            if recepcionista.estatus_empleo != "Ex-Empleado":
                print(recepcionista)
        input("\nPresiona ENTER para continuar")

    def ver_unidades_medicas(self):
        """Imprime las unidades medicas afiliadas al hospital."""

        print("UNIDADES MEDICAS: ")
        for unidad in self.hospital._unidades:
            print(unidad)
        input("\nPresiona ENTER para continuar")

    def modificar_estatus_empleo_empleado(self):
        """Dependiendo del tipo de empleado, pide el id del empleado a buscar, lo busca en
           la lista correspondiente y cambia el atributo estatus_empleo a lo opuesto."""

        while True:
            print("""
             1. Doctor
             2. Enfermero
             3. Recepcionista
             """)

            resp = input("Ingrese el tipo de empleado al cual desea cambiar el estatus: ")

            if resp == "1":
                id_empleado = input("Ingrese el Id de empleado del doctor: ").upper()
                if not buscar_id_y_cambiar_estatus(id_empleado, self.hospital._doctores):
                    print(f"Doctor con id {id_empleado} no encontrado")
                input("\nPresiona ENTER para continuar")
                break

            elif resp == "2":
                id_empleado = input("Ingrese el Id de empleado del enfermero: ").upper()
                if not buscar_id_y_cambiar_estatus(id_empleado, self.hospital._enfermeros):
                    print(f"Enfermero con id {id_empleado} no encontrado")
                input("\nPresiona ENTER para continuar")
                break

            elif resp == "3":
                id_empleado = input("Ingrese el Id de empleado del recepcionista: ").upper()
                if not buscar_id_y_cambiar_estatus(id_empleado, self.hospital._recepcionistas):
                    print(f"Recepcionista con id {id_empleado} no encontrado")
                input("\nPresiona ENTER para continuar")
                break

            else:
                print(f"{resp} no es una opcion valida")

    def agregar_empleado_a_staff(self):
        """Dependiendo del tipo de empleado, pide los datos basicos de un empleado mediante una funcion
           que regresa un objeto EmpleadoHospital, pide datos extras en caso de ser necesario, crea un objeto del tipo
           de empleado y lo agrega a la lista de esos empleados del hospital."""

        while True:
            print("""
            1. Doctor
            2. Enfermero
            3. Recepcionista
            """)
            resp = input("Ingrese el tipo de empleado que desea registrar: ")

            if resp == "1":
                print("Ingrese los datos necesarios para agregar un doctor")
                try:
                    args = pedir_datos_basicos_empleado()
                except FechaInvalida as e:
                    print(e)
                except FechaEnElFuturo as e:
                    print(e)
                except InputInvalido as e:
                    print(e)
                else:
                    especialidad = input("Especialidad: ")
                    cedula = input("Cedula: ")
                    empleado = Doctor(especialidad, cedula, nombre=args.nombre, apellido=args.apellido,
                                      fecha_nacimiento=args.fecha_nacimiento, sexo=args.sexo,
                                      fecha_de_empleo=args.fecha_de_empleo, departamento=args.departamento,
                                      posicion=args.posicion, horario=args.horario, telefono=args.telefono,
                                      correo=args.correo)
                    self.hospital.agregar_doctor(empleado)
                    print("Doctor agregado")
                    input("\nPresiona ENTER para continuar")
                    break

            elif resp == "2":
                print("Ingrese los datos necesarios para agregar un enfermero")
                try:
                    args = pedir_datos_basicos_empleado()
                except FechaInvalida as e:
                    print(e)
                except FechaEnElFuturo as e:
                    print(e)
                except InputInvalido as e:
                    print(e)
                else:
                    cedula = input("Cedula: ")
                    empleado = Enfermero(cedula, nombre=args.nombre, apellido=args.apellido,
                                fecha_nacimiento=args.fecha_nacimiento, sexo=args.sexo,
                                fecha_de_empleo=args.fecha_de_empleo, departamento=args.departamento,
                                posicion=args.posicion, horario=args.horario, telefono=args.telefono,
                                correo=args.correo)

                    self.hospital.agregar_enfermero(empleado)
                    print("Enfermero agregado")
                    input("\nPresiona ENTER para continuar")
                    break

            elif resp == "3":
                print("Ingrese los datos necesarios para agregar un recepcionista")
                try:
                    args = pedir_datos_basicos_empleado()
                except FechaInvalida as e:
                    print(e)
                except FechaEnElFuturo as e:
                    print(e)
                except InputInvalido as e:
                    print(e)
                else:
                    empleado = Recepcionista(nombre=args.nombre, apellido=args.apellido,
                                fecha_nacimiento=args.fecha_nacimiento, sexo=args.sexo,
                                fecha_de_empleo=args.fecha_de_empleo, departamento=args.departamento,
                                posicion=args.posicion, horario=args.horario, telefono=args.telefono,
                                correo=args.correo)

                    self.hospital.agregar_recepcionista(empleado)
                    print("Recepcionista agregado")
                    input("\nPresiona ENTER para continuar")
                    break

            else:
                print(f"{resp} no es una opcion valida")

    def ver_registro_pacientes(self):
        """Imprime los datos de los pacientes registrados en la lista de pacientes del hospital."""

        print("REGISTRO PACIENTES")
        for paciente in self.hospital._pacientes:
            print(paciente)
        input("\nPresiona ENTER para continuar")

    def agregar_empleado_a_unidad_medica(self):
        """Dependiendo del tipo de empleado, llama la funcion buscar_unidad para pedir el nombre de la unidad
           y el id del empleado. Si amabos son encontrados, agrega el empleado a la lista correspondiente de
           empleados de la unidad."""

        while True:

            print("""
            1. Doctor
            2. Enfermero
            3. Recepcionista
            """)

            resp = input("Ingrese el tipo de empleado al cual desea agregar a una unidad medica: ")

            if resp == "1":
                print(buscar_unidad(self.hospital,self.hospital._doctores))
                input("\nPresiona ENTER para continuar")
                break

            elif resp == "2":
                print(buscar_unidad(self.hospital, self.hospital._enfermeros))
                input("\nPresiona ENTER para continuar")
                break

            elif resp == "3":
                print(buscar_unidad(self.hospital, self.hospital._recepcionistas))
                input("\nPresiona ENTER para continuar")
                break

            else:
                print(f"{resp} no es una opcion valida")

    def agregar_admin(self):
        """Pide usuario y contraseña del nuevo usuario, y llama la funcion de agregar_usuario del autenticador."""

        try:
            usuario = input("Ingrese el usuario: ")
            contra = input("Ingrese la contraseña: ")
            self.hospital._autenticador_admin.agregar_usuario(usuario, contra)
            input("\nPresiona ENTER para continuar")
        except UsuarioYaExistente as e:
            print(e)
            input("\nPresiona ENTER para continuar")
        except ContraseñaMuyCorta as e:
            print(e)
            input("\nPresiona ENTER para continuar")

    def agregar_unidad_medica(self):
        """Pide el nombre y la capacidad de la nueva unidad medica."""

        nombre = input("Ingrese el nombre de la nueva unidad: ")
        try:
            capacidad = int(input("Ingrese la capacidad de la nueva unidad: "))
        except ValueError:
            print("La capacidad debe ser un numero entero")
            input("\nPresiona ENTER para continuar")
        else:
            unidad = UnidadMedica(nombre, capacidad)
            self.hospital.agregar_unidad_medica(unidad)
            print(f"Unidad Medica {nombre} agregada")
            input("\nPresiona ENTER para continuar")

    def ver_detalles_empleado(self):
        """Dependiendo del tipo de empleado, llama a la funcion buscar_detalles_empleado donde pide el id
           para buscarlo en la lista correspondiente e imprimir los detalles del empleado con ese id."""

        while True:
            print("""
            1. Doctor
            2. Enfermero
            3. Recepcionista
            """)

            resp = input("Ingrese el tipo de empleado del cual desea ver los detalles: ")

            if resp == "1":
                id_empleado = input(f"Ingrese el Id de empleado del doctor que desea buscar: ").upper()
                if not buscar_detalles_empleado(id_empleado, self.hospital._doctores):
                    print(f"Doctor con id {id_empleado} no encontrado")
                    input("\nPresiona ENTER para continuar")
                    break
                else:
                    input("\nPresiona ENTER para continuar")
                    break

            elif resp == "2":
                id_empleado = input(f"Ingrese el Id de empleado del enfermero que desea buscar: ").upper()
                if not buscar_detalles_empleado(id_empleado, self.hospital._enfermeros):
                    print(f"Enfermero con id {id_empleado} no encontrado")
                    input("\nPresiona ENTER para continuar")
                    break
                else:
                    input("\nPresiona ENTER para continuar")
                    break

            elif resp == "3":
                id_empleado = input(f"Ingrese el Id de empleado del recepcionista que desea buscar: ").upper()
                if not buscar_detalles_empleado(id_empleado, self.hospital._recepcionistas):
                    print(f"Recepcionista con id {id_empleado} no encontrado")
                    input("\nPresiona ENTER para continuar")
                    break
                else:
                    input("\nPresiona ENTER para continuar")
                    break

    def ver_detalles_paciente(self):
        """Pide el id de paciente para buscarlo en la lista de pacientes del hospital y una vez encontrados
           imprime los detalles del paciente."""

        id_de_paciente = input("Ingrese el numero de Id del paciente a buscar: ")
        for paciente in self.hospital._pacientes:
            if paciente.id_paciente == id_de_paciente:
                print(paciente)
                input("\nPresiona ENTER para continuar")
                break
            else:
                pass
        print(f"Paciente con id {id_de_paciente} no encontrado")
        input("\nPresiona ENTER para continuar")

    def ver_detalles_admin(self):
        """Imprime los usuarios de los admins autorizados del hospital"""

        print("USUARIOS ADMIN")
        for usuario in self.hospital._autenticador_admin.usuarios.keys():
            print(usuario)
        input("\nPresiona ENTER para continuar")

    def eliminar_admin(self):
        """Pide el usuario del admin a eliminar, busca por la lista de admins, confirma que si se quiere eliminar al admin y
           despues de recibir una s, lo elimina. Si recibe una n, cancela la accion y regresa al menu principal. De otra manera
           espera hasta recibir un input valido"""

        admin = input("Ingrese el usuario del Admin a eliminar: ")
        for usuario in self.hospital._autenticador_admin.usuarios.keys():
            if usuario == admin:
                print(f"¿Seguro que quiere eliminar el usuario {usuario}?")
                while True:
                    resp = input("Ingrese S para si o N para no: ").upper()
                    if resp == "S":
                        print(f"Eliminando usuario {admin}")
                        del self.hospital._autenticador_admin.usuarios[usuario]
                        input("\nPresiona ENTER para continuar")
                        return True
                    elif resp == "N":
                        input("\nAccion cancelada, presiona ENTER para continuar")
                        return True
                    else:
                        print(f"{resp} no es una respuesta valida")
            else:
                pass

        print(f"Admin con usuario {admin} no encontrado")
        input("\nPresiona ENTER para continuar")

    def salir(self):
        """Deja de correr el programa"""

        print("SALIENDO DEL SISTEMA")
        sys.exit()

