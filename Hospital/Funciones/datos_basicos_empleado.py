from datetime import datetime
from excepciones import FechaInvalida, FechaEnElFuturo, InputInvalido
from Personas.empleado_hospital import EmpleadoHospital

def pedir_datos_basicos_empleado():
    """Funcion utilizada en el archivo menu_hospital.
       Toma inputs necesarios para crear una instancia de un empleado de hospital."""

    nombre = input("Nombre(s): ").capitalize()
    apellido= input("Apellido(s): ").capitalize()

    try:
        año_nacimiento = int(input("Año de nacimiento en formato AAAA: "))
        mes_nacimiento = int(input("Mes de nacimiento en formato M: "))
        dia_nacimiento = int(input("Dia de nacimiento en formato D: "))
        fecha_nacimiento = datetime(año_nacimiento, mes_nacimiento,dia_nacimiento)
    except ValueError:
        raise FechaInvalida("Algunos de los valores ingresados para la fecha son incorrectos")

    sexo = input("Sexo: ").capitalize()
    departamento = input("Departamento: ").capitalize()
    posicion = input("Posicion: ").capitalize()

    try:
        horario = crear_horario()
    except InputInvalido:
        raise

    telefono = input("Telefono: ")
    correo = input("Correo: ")

    try:
        año_empleo = int(input("Año de empleo en formato AAAA: "))
        mes_empleo = int(input("Mes de empleo en formato M: "))
        dia_empleo = int(input("Dia de empleo en formato D: "))
        fecha_empleo = datetime(año_empleo, mes_empleo, dia_empleo)
    except ValueError:
        raise FechaInvalida("Algunos de los valores ingresados para la fecha son incorrectos")

    try:
        return EmpleadoHospital(nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, sexo=sexo,
                     posicion=posicion, fecha_de_empleo=fecha_empleo, departamento=departamento,
                     horario=horario, telefono=telefono, correo=correo)

    except FechaEnElFuturo:
        raise

def crear_horario():
    """Toma input sobre que cantidad de dias se va a agregar al horario y que horas, y los agrega a un diccionario"""

    try:
        num_dias = int(input("Ingrese la cantidad de dias del horario: "))
        if num_dias == 0:
            raise InputInvalido("Debe ingresar por lo menos un dia al horario")
        if num_dias > 7:
            raise InputInvalido("No debe ingresar mas de 7 dias al horario")
    except ValueError:
        raise InputInvalido("Dato ingresado es invalido, solo agregar numeros enteros al horario")

    horario = {}
    for i in range(num_dias):
        dias = input("Ingrese el dia de la semana: ").capitalize()
        horas = input("Ingrese las horas del turno en formato Xam - Xpm: ")
        horario[dias] = horas

    return horario

if __name__ == "__main__":
    e = pedir_datos_basicos_empleado()
    print(type(e.fecha_nacimiento))
    print(type(e.fecha_de_empleo))
