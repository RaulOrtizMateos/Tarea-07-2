#Encoding:UTF-8
#RAul Ortiz Mateos
#Listas

#En esta funcion lo que se va a realizar es poner los numeros al azar y solo te regresa los numeros pares, mientras que los numeros impares no los regresa.

def calcularNumerosPares(lista):
    pares=[]
    for i in lista:
        if i %2==0:
            pares.append(i)
    return pares


#Recibe como parámetro una lista y regresa una nueva lista, con los valores que son mayores a un elemento previo.
def calcularParametro(lista):
    Parametro = []
    for i in range (0,len(lista)-1):
        if lista[i]<lista[i+1]:
            Parametro.append(lista[i+1])
    return Parametro


#recibe una lista de valores y regresa una nueva lista con cada pareja de datos intercambiados.

def calcularParejaDeDatos(lista):
    intercambiados = []
    if len(lista) % 2 == 0:
        for i in range(0, len(lista),2):
            intercambiados.append(lista[i+1])
            intercambiados.append(lista[i])
        return intercambiados
    else:
        for i in range(0, len(lista)-1,2):
            intercambiados.append(lista[i+1])
            intercambiados.append(lista[i])
        intercambiados.append(lista[len(lista)-1])
        return intercambiados

#recibe una lista de valores y regresa una nueva lista con el valor menor y mayor intercambiados.
def calcularMayorYMenor(lista):
    if len(lista) >= 1:
        listaN = lista[:]
        mayor = max(lista)
        menor = min(lista)
        ubicacionmayor = listaN.index(mayor)
        ubicacionmenor = listaN.index(menor)
        listaN.remove(mayor)
        listaN.remove(menor)
        listaN.insert(ubicacionmenor, mayor)
        listaN.insert(ubicacionmayor, menor)
    else:
        listaN = []
    return (listaN)

def calcularPromedio(lista):
    promedio=sum(lista)/len(lista)
    n=0
    for i in lista:
        if i>=promedio:
            n+=1
    return n

def calcularDesviacion(lista):
    promedio = sum(lista) / len(lista)

    n=0
    for i in lista:
        suma=(i-promedio)**2
        n=suma+n
        v=n/len(lista)
        d=(v)**0.5

    return d


def calcularPromedio1(lista):
    promedio = sum(lista) / len(lista)

    return promedio





def main():#esta es la funcion principal aqui se controla con el menu
    print ("TAREA 7-2")
    print ("--------------------------")
    print ("Autor:Raul Ortiz Mateos, A01375407")
    print ("---------------------------")
    print ("LISTAS")
    print("---------------------------")
    print ("0. salir del menu")
    print ("1. regresar numeros pares")
    print ("2. Recibe como parámetro una lista y regresa una nueva lista")
    print ("3.recibe una lista de valores y regresa una nueva lista con cada pareja de datos intercambiados.")
    print("4.recibe una lista de valores y regresa una nueva lista con el valor menor y mayor intercambiados.")
    print ("5.calcular Promedio")
    print ("6.")
    print ("----------------------------")
    numero=int(input("que numero deseas elegir en el menu para poder obtener las listas: "))
    while not numero==0:
        if numero==1:
            print ("problema 1")
            lista = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
            lista2 = [5, 7, 3]
            print("la lista que tienes es:", lista, "regresa", calcularNumerosPares(lista))
            print("la lista que tienes es:", lista2, "regresa", calcularNumerosPares(lista2))

        elif numero==2:
            print ("problema 2")
            lista = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
            lista2 = [5, 4, 3, 2]
            print("la lista que tienes es:", lista, "regresa", calcularParametro(lista))

            print("la lista que tienes es:", lista2, "regresa", calcularParametro(lista2))

        elif numero==3:
            print ("problema 3")
            lista = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
            lista2 = [1, 2, 3]
            lista3 = [7]
            print("la lista que tienes es:", lista, "regresa", calcularParejaDeDatos(lista))
            print("la lista que tienes es:", lista2, "regresa", calcularParejaDeDatos(lista2))
            print("la lista que tienes es:", lista3, "regresa", calcularParejaDeDatos(lista3))

        elif numero==4:
            print ("problema 4")
            lista1 = [5, 9, 3, 22, 19, 31, 10, 7]
            lista2 = [1, 2, 3]
            print("la lista que tienes es:", lista1, "regresa", calcularMayorYMenor(lista1))
            print("la lista que tienes es:", lista2, "regresa", calcularMayorYMenor(lista2))

        elif numero==5:
            print ("problema 5")
            lista1 = [70, 80, 90]
            lista2 = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
            print("la lista que tienes es:", lista1, "regresa", calcularPromedio(lista1))
            print("la lista que tienes es:", lista2, "regresa", calcularPromedio(lista2))

        elif numero==6:
            print ("problema 6.")
            lista=[1,2,3,4,5,6]
            lista2=[95,21,73,24,15,69,71,80,49,100,85]
            lista3=[3]
            print ("la lista es:",lista,"regresa ",calcularPromedio(lista),calcularDesviacion(lista))
            print ("la lista es:", lista2, "regresa ", calcularPromedio1(lista2), calcularDesviacion(lista2),)
            print ("la lista es:", lista3, "regresa ", calcularPromedio1(lista3), calcularDesviacion(lista3),)


        else:
            numero!=0 and numero!=1 and numero!=2 and numero!=3 and numero!=4 and numero!=5 and numero!=6
            print ("---------------------------------------------")
            print ("Error,solo se puede elegir numeros del 0-6.")
            print ("---------------------------------------------")

        print("-------------------------------------------------------------------------------------------------------")
        print ("0. salir del menu")
        print ("1. regresar numeros pares")
        print ("2. Recibe como parámetro una lista y regresa una nueva lista")
        print ("3.recibe una lista de valores y regresa una nueva lista con cada pareja de datos intercambiados.")
        print("4.recibe una lista de valores y regresa una nueva lista con el valor menor y mayor intercambiados.")
        print ("5.calcular Promedio")
        print ("6.")
        print ("------------------------------------------------------------------------------------------------------")

        numero = int(input("que numero deseas elegir en el menu para poder obtener las listas: "))

    print ("Nos vemos, regresa pronto ten un buen dia, ten un buen dia")

main()