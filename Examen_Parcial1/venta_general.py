from datetime import datetime

class Membresia:
    """Clase que mantiene registro de los puntos dentro de la membresia de un cliente"""

    def __init__(self, id_membresia : str, puntos : int):
        self.id_membresia = id_membresia
        self.puntos = puntos

class Venta:
    """Superclase que define los básicos de una venta, como hora, fecha y lugar de venta.

       Se observa el pilar de herencia ya que Venta_Comida y Venta_Boleto heredan de Venta.

       Otro pilar que se observa es el polimorfismo ya que se puede interactuar con la clase Venta, Venta_Boleto
       y Venta_Comida de la misma forma ya que comparten la mayoría de los métodos, a excepción de un método
       diferente en Venta_Comida y cambios en la funcion de Precio_Total en cada respectiva clase.

       En esto último se observa la abstracción. Para el Precio_Total en Venta_Boleto no es lo mismo que
       el Precio_Total en Venta_Comida ya que depende de distintas cosas. En Venta_Boleto se modifica para que
       tome en cuenta la cantidad de boletos y en Venta_Comida se modifica para que se tome en cuenta las
       especificaciones de la orden. También en Venta_Comida se agrega una nueva función que imprime los
       datos de la orden.

       Se hace uso de parametros opcionales: pueda que el cliente tenga una membresia o no y pueda que
       aplique un descuento o no"""

    def __init__(self, sucursal : str, pago : float, descuento : float = None, membresia : Membresia = None):
        self.sucursal = sucursal
        self.fecha_hora = datetime.now()
        self.descuento = descuento
        self.pago = pago
        self.membresia = membresia

    def Precio_Total(self):
        if self.descuento == None:
            return self.pago
        else:
            return self.pago - self.descuento

    def Hacer_Venta(self):
        return (f"""Fecha y hora de venta: {self.fecha_hora}\nMonto de Venta: {self.Precio_Total()} pesos""")

    def Agregar_Puntos_Membresia(self):
        if self.membresia != None:
            self.membresia.puntos += 10
            return "Los puntos han sido agregados"
        else:
            pass

    def Cancelar_Venta(self):
        return "Venta cancelada"

    def Regresar_Cambio(self):
        self.cambio = self.pago - self.Precio_Total()
        return f"El cambio es {self.cambio}"

if __name__ == "__main__":
    venta = Venta("Rosarito", 150)
    print(venta.Hacer_Venta())
    print(venta.Precio_Total())