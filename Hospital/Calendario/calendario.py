from datetime import datetime
from excepciones import FechaInvalida, InputInvalido
from Funciones.imprimir_lista import buscar_dict_en_lista, desplegar_diccionario
#Flask
class Calendario:
    def __init__(self):
        self.calendario = []

    def agregar_evento(self, evento : str, fecha_evento : datetime, hora_evento : str, detalles_evento : str = "Ninguno"):
        """Agrega un evento a la lista calendario.
           Si la fecha ingresada esta en el pasado o se ingresan valores invalidos, se levanta una excepcion"""

        self.evento = evento.upper() #en mayusculas para facilitar la busqueda de eventos en el calendario
        self.hora_evento = hora_evento
        self.detalles_evento = detalles_evento

        try:
            if fecha_evento < datetime.today():
                raise FechaInvalida("Fecha en el pasado no es valida")
        except ValueError:
            raise FechaInvalida("Valores de fecha ingresada son incorrectos")
        self.fecha_evento = fecha_evento.strftime("%Y-%m-%d")

        self.calendario.append({"Evento" : self.evento, "Fecha" : self.fecha_evento,"Hora" : self.hora_evento, "Detalles" : self.detalles_evento})

    def eliminar_evento(self, evento_a_eliminar: str):
        """Buscar en el calendario busquedas que hagan match con el evento
           y dar al usuario a elegir cual de los resultados desea eliminar"""

        buscar_dict_en_lista(evento_a_eliminar,self.calendario)
        op = int(input("Ingrese el numero de la cita que desea eliminar: "))
        self.calendario.pop(op-1)

    def modificar_evento(self, evento_a_modificar : str):
        """Buscar en el calendario busquedas que hagan match con el evento
          y dar al usuario a elegir cual de los resultados desea cambiar y
          a que lo quiere cambiar"""

        diccionario = buscar_dict_en_lista(evento_a_modificar,self.calendario)
        try:
            respuesta_1 = input("Ingrese el numero del evento que desea modificar: ")
            desplegar_diccionario(diccionario[respuesta_1])

        except KeyError:
            raise InputInvalido("Input invalido")

        else:

            try:
                respuesta_2 = input("Ingrese el detalle del evento que desea modificar: ").capitalize()
                modificacion = input("Ingrese la nueva modificacion: ")

            except KeyError:
                raise InputInvalido("Input invalido")

            else:
                index_diccionario_en_calendario = self.calendario.index(diccionario[respuesta_1])
                self.calendario[index_diccionario_en_calendario][respuesta_2] = modificacion


    def ver_calendario(self):
        """Imprime los contenidos de un calendario"""

        print("Calendario:")
        for i in self.calendario:
            desplegar_diccionario(i)



if __name__ == "__main__":
    c = Calendario()
    c.agregar_evento("Cita Mensual", datetime(2021, 4, 30), "7pm")
    c.agregar_evento("Cita Anual", datetime(2021, 4, 30), "6pm")
    c.agregar_evento("Cita Mensual", datetime(2021, 4, 30), "5pm")
    c.ver_calendario()
    # c.eliminar_evento("Cita Mensual")
    # c.ver_calendario()




