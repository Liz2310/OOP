from ventacomida import Venta_Comida
from ventaboleto import Venta_Boleto


boleto1 = Venta_Boleto(3,50,sucursal="Rosarito",pago=500)
print(boleto1.Precio_Total())
print(boleto1.Hacer_Venta())
print(boleto1.Regresar_Cambio())

orden_comida1 = Venta_Comida({"Palomitas":3 ,"soda":1},275,sucursal="Rosarito", pago=500)
print(orden_comida1.Imprimir_Orden())
print(orden_comida1.Regresar_Cambio())
print(orden_comida1.Hacer_Venta())