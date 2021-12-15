
def buscar_dict_en_lista(elemento_a_buscar, lista):
    """Funcion utilizada en clase Calendario.
       Busca en una lista todos los elementos que hagan match con el elemento a buscar
       y los imprime en un diccionario."""

    elementos = {}
    enum = 1
    print(f"Eventos con {elemento_a_buscar} \n")

    for i in lista:
        for k,v in i.items():
            if elemento_a_buscar.upper() in v:
                elementos[str(enum)] = i
                enum += 1

    desplegar_diccionario(elementos)
    print("\n")

    return elementos

def desplegar_diccionario(diccionario):
    """Funcion utilizada en la clase Calendario.
       Imprime los key-value pairs dentro del diccionario."""

    print("\n")
    for k,v in diccionario.items():
        print(str(k)+ " : " + str(v))












