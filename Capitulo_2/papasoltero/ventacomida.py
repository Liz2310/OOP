from venta import Venta

class Venta_Comida(Venta):
    def __init__(self, orden_completa : dict, precio_orden: float, **kwargs):
        super().__init__(**kwargs)
        self.orden_completa = orden_completa
        self.precio_orden = precio_orden

    def Precio_Total(self):
        if self.descuento == None:
            return self.precio_orden
        else:
            return self.precio_orden - self.descuento

    def Imprimir_Orden(self):
        for k, v in self.orden_completa.items():
            print(k, v)


if __name__ == "__main__":
    venta = Venta_Comida({"nachos": 2, "soda": 1}, 178, sucursal="Rosarito", pago=200)
    print(venta.Precio_Total())
    print(venta.Imprimir_Orden())
    print(venta.Hacer_Venta())
