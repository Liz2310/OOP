
def buscar_id_y_cambiar_estatus(id_empleado, lista):
    """Funcion utilizada en el archivo menu_hospital.
       Busca en la lista de empleados y cambia el atributo de estado de empleo a caso contrario."""

    for i in lista:

        if i.id_empleado == id_empleado:
            print(f"Cambiando estatus de {i.nombre} {i.apellido} {i.id_empleado} {i.departamento}")

            if i.estatus_empleo == "Empleado Actualmente":
                i.estatus_empleo = "Ex-Empleado"
                print("Estatus cambiado a Ex-Empleado")

            else:
                i.estatus_empleo = "Empleado Actualmente"
                print("Estatus cambiado a Empleado Actualmente")

            return True








