#Función para eliminar el caracter solicitado de una lista, además los demás valor
def eliminarCaracter(caracteres:list, s:str):
    lista = []
    for caracter in caracteres:
        if (not(S in caracter)):
            for letra in caracter:
                if(int(S)<int(letra)):
                    caracter = caracter.replace(letra,"")

            if (not(len(caracter)==0)):
                lista.append(caracter)
        else:
            caracter = caracter.replace(S, "")
            for letra in caracter:
                if(int(S)<int(letra)):
                    caracter = caracter.replace(letra,"")
            if (not(len(caracter)==0)):
                lista.append(caracter)

    return lista

#Funcion para reordenar
def reordenar (lista:list):
    lista2 = []
    if(len(lista)==0):
        return lista
        
    for i in range(len(lista)):
        lista2.append(lista[(i+1)*(-1)])

    return lista2


#Valor obtenido en el hash
S = "8"

#Variable para controlar el while(True)
aprovar = True
#while(True) para revisar que los datos sean correctos

#Aca intento interacruar con el usuario, y que los datos de la lista los ingrese desde la consola.
#En el problema no definia muy bien como iba a ingresar la lista, asi que tomé esta iniciativa

while(True):
    aprovar = True

    #Leemos la entrada, que son de 0 a 100 dígitos
    entrada = input("Ingresa los números separados por una coma (,):\n")

    #Lista de los datos obtenidos en la entrada sin espacios
    caracteres = list(map(str.strip, entrada.split(",")))

    for i in caracteres:
        if(i.isdigit()==False):
            print("Los datos deben ser numéricos. Vuelve a intentarlo\n")
            aprovar = False 

            
    if(aprovar==True):
        break

#Eliminamos las ocurrencias de S y los numeros mayores
digitos = eliminarCaracter(caracteres, S)

#Arreglo final ordenado
final = list(map(int, reordenar(digitos)))

#Imprimimos la respuesta
print(final)