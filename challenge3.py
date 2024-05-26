#Utilizo función del challenge2 para ordenar
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


#funcion del cambio, siempre devuelve una tupla con el dinero y el valor del cambio mínimo
def cambio(money, cambio_minimo, reunido):
    #Ordeno el dinero
    money = ascendente(money)

    #Cuando la lista esté vacia me devolverá el cambio mínimo
    if(len(money)==0):
        return [], cambio_minimo + 1
    #Es una pequeña excepción que encontré en mi código, cuando solo hay una moneda y es de valor 1
    #lo mínimo que no puede cambiar es 2
    elif(len(money)==1 and money[0] == 1):
        return [], 2
    #Si el cambio es menor a la moneda de menor valor, y al dinero acumulado se encuentra el cambio mínimo
    elif(cambio_minimo+1<money[0] and cambio_minimo>=reunido):
        return [], cambio_minimo+1
    #En cualquier otro caso
    else:
        #Reunido es el valor que se acumula mediante se descartan las monedas de menor valor
        reunido = reunido + money[0]
        #Cambio mínimo aumenta conforme se descartan monedas
        cambio_minimo = cambio_minimo + money[0]
        #Volvemos a calcular el ínimo sin tener en cuenta la moneda de menor valor
        return cambio(money[1:], cambio_minimo, reunido)



dinero = [1, 1,2,1,1,1,1,1,1,6,1,17]

#Es una tupla
cambiomin = cambio(dinero, 0, 0)

#Posisión 1 de la tupla que es donde esta el valor buscado
print(cambiomin[1])

