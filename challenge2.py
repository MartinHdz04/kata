#Función que utiliza recursividad para ordenar una lista
def ascendente(lista):
    #Si la lista está vacia o solo tiene un elemento
    if len(lista) <= 1:
        return lista
    else:
        referencia = lista[0]
        menores = [i for i in lista[1:] if i <= referencia]
        mayores = [i for i in lista[1:] if i > referencia]
        return ascendente(menores) + [referencia] + ascendente(mayores)
    
#Función para calcular cuadrados
def cuadrados(lista):
    if(len(lista)==0):
        return lista
    else:
        cuadrado = lista[0]*lista[0]
        return [cuadrado] + cuadrados(lista[1:])
    
#Eliminar un cuddrado superior al de la referencia
def eliminarsuperior(lista, ref):
    if (len(lista)==0):
        return lista
    elif(lista[0]>ref):
        return eliminarsuperior(lista[1:], ref)
    else:
        return [lista[0]] + eliminarsuperior(lista[1:], ref)
    
#Valor obtenido en el hash
S = 8

#Cuadrado de referencia
ref = 8*8

#Lista de entrada
prueba = [1,2,3,4,5,6,7,11,22]

#Calculo de cuadrados de la lista
cuad = cuadrados(prueba)

#Eliminamos cuadrados superiores
cuad_final = eliminarsuperior(cuad, ref)

#Ordenamiento ascendente final
ord = ascendente(cuad_final)

print(ord)