
def buscar_detalles_empleado(id_empleado, lista):
    for empleado in lista:
        if empleado.id_empleado == id_empleado:
            print(empleado)
            empleado.calendario.ver_calendario()
            return True

