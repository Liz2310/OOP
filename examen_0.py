def rectangulo(palabra):
    palabra = palabra.upper()
    longitud = len(palabra)
    palabra_mocha = palabra[1:(longitud-1)]
    espacios = " " * (longitud-2)

    print(palabra[::-1])#imprime palabra al reves
    for i in range(len(palabra_mocha)):
        if i == 0:
            #imprime ultima letra de palabra_mocha + espacios + primera letra de palabra_mocha
            print(palabra_mocha[(len(palabra_mocha)-1)] + espacios + palabra_mocha[i])
        else:
            #imprime las siguientes letra de reversa + espacios + letras en orden normal, el i + 1 va aumentando el indice de reversa
            print(palabra_mocha[len(palabra_mocha)-(i+1)] + espacios + palabra_mocha[i])
    print(palabra)#imprime palabra normal

rectangulo("Pinguino")

def printRectangle(h, w) : 
    for i in range(0, h) : 
        print ("") 
        for j in range(0, w) :
            # Print @ if this is first row 
            # or last row. Or this column 
            # is first or last. 
            if (i == 0 or i == h-1 or j== 0 or j == w-1) : 
                print("@",end="") 
            else : 
                print(" ",end="") 

h = 4
w = 5
#printRectangle(h, w)  


def consonantes_vocales(palabra):
    palabra = palabra.lower()
    palabra_nueva = ""
    cont_V = 0
    cont_C = 0
    vocales = "aeiou"
    for letra in palabra:
        if letra in vocales:
            palabra_nueva += "V"
        else:
            palabra_nueva += "C"

    for i in palabra_nueva:
        if i == "C":
            cont_V += 1
        else:
            cont_C += 1

    if cont_V > cont_C:
        print(palabra_nueva + " V")
    elif cont_C > cont_V:
        print(palabra_nueva + " C")
    else:
        print(palabra_nueva + " E")

#consonantes_vocales("RSTAEU")

def temperatura(string):
    
    if string[0] == "F" and string[1] == "K":
        temp = float(string[2::])
        conversion = round((temp + 459.67) * (5/9))
        return ("K" + str(conversion))
    
    elif string[0] == "F" and string[1] == "C":
        temp = float(string[2::])
        conversion = round((temp - 32) * (5/9))
        return ("C" + str(conversion))
    
    elif string[0] == "K" and string[1] == "F":
        temp = float(string[2::])
        conversion = round((temp * (9/5)) - 459.67)
        return ("F" + str(conversion))
    
    elif string[0] == "K" and string[1] == "C":
        temp = float(string[2::])
        conversion = round((temp - 273.15))
        return ("C" + str(conversion))
    
    elif string[0] == "C" and string[1] == "F":
        temp = float(string[2::])
        conversion = round((temp * (9/5) + 32))
        return ("F" + str(conversion))
    
    elif string[0] == "C" and string[1] == "K":
        temp = float(string[2::])
        conversion = round((temp + 273.15))
        return ("K" + str(conversion))
    else:
        return(f"{string} es una entrada invalida")

#print(temperatura("XL20"))


def sumar_digitos(numero):
    numero_nuevo = ""
    for digito in str(numero):
        if digito == "9":
            numero_nuevo += "10"
            continue
        numero_nuevo += str(int(digito) + 1)
        
        
    print(numero_nuevo)

#sumar_digitos(99)

def valles(arreglo):
    arreglo_nuevo = []
    
    for i in range(len(arreglo)):
        
        if i == 0:
            continue
        
        elif arreglo[i-1] > arreglo[i] and arreglo[i+1] > arreglo[i]:
            arreglo_nuevo.append(arreglo[i])
            
        elif i == len(arreglo):
            break

    print(arreglo_nuevo)
    
#valles([5,2,10,8,9,11,9,12])













    
