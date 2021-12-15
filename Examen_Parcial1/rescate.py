# Los alumnos del CESYTs van mucho al bar Moreno’s.
# Saben que alguna botella está adulterada,y causara al que la beba quedarse dormido 5 minutos después de probarla.
# Cuántos alumnos son el mínimo de alumnos que deben probar para identificar la botella adulterada entre n botellas.
# Cada alumno puede mezclar bebidas de n botellas.
# Crea la función para resolver esteproblema.

def binary_search(botellas):
    alumnos = 0
    while botellas > 0:
        alumnos += 1
        botellas //= 2
    return alumnos


