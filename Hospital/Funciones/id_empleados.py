
def int32_to_id(n):
    """Funcion utilizada en clase EmpleadoHospital.
       Toma un numero y lo convierte a un id alfanumerico."""

    if n == 0:
        return "0"

    caracteres = "0123456789ACEFHJKLMNPRTUVWXY"
    longitud = len(caracteres)
    resultado = ""
    sobra = n

    while sobra > 0:
        pos = sobra % longitud
        sobra = sobra // longitud
        resultado = caracteres[pos] + resultado

    return resultado