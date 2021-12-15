from venta import Venta

class Venta_Boleto(Venta):
    """Subclase que se enfoca en la venta de boletos, donde la funcion de Precio_Total cambia de acuerdo
       con la cantidad de boletos vendidos y el precio de un solo boleto."""


    def __init__(self,cantidad_boletos : int, precio_boleto: float, **kwargs):
        super().__init__(**kwargs)
        self.cantidad_boletos = cantidad_boletos
        self.precio_boleto = precio_boleto

    def Precio_Total(self):
        if self.descuento == None:
            return (self.cantidad_boletos * self.precio_boleto)
        else:
            return (self.cantidad_boletos * self.precio_boleto)-self.descuento


if __name__ == "__main__":
    boleto = Venta_Boleto(2,50, sucursal="Rosarito",pago=200)
    print(boleto.Precio_Total())
    print(boleto.Hacer_Venta())