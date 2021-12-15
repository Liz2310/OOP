from datetime import datetime

class Membresia:
    def __init__(self, id_membresia : str, puntos : int):
        self.id_membresia = id_membresia
        self.puntos = puntos

class Venta:
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