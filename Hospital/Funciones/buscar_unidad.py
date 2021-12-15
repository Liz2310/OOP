
def buscar_unidad(hospital, lista):
    nombre_unidad = input("Ingrese el nombre de la unidad medica: ").capitalize()
    for unidad in hospital._unidades:
        if unidad.nombre == nombre_unidad:
            id_empleado = input(f"Ingrese el Id de empleado del empleado que desea agregar a la unidad {unidad.nombre}: ").upper()
            for empleado in lista:
                if empleado.id_empleado == id_empleado:
                    unidad.agregar_doctor(empleado)
                    return f"Empleado {empleado.nombre} {empleado.apellido} {empleado.id_empleado} agregado a Unidad Medica: {unidad.nombre}"
                else:
                    pass
            return f"Empleado con id {id_empleado} no encontrado"
        else:
            pass
    return f"Unidad Medica {nombre_unidad} no encontrada"