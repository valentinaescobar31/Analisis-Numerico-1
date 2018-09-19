import math                                                             #para la función math.exp

    

def seccionar (intervalo, nsecciones):

    secciones= []                                                       #guarda las secciones encontradas según el número de particiones

    interval = round(abs((intervalo[0])-(intervalo[1]))/nsecciones,8)   #cada intervalo se separa por este valor, menos el primero

    secciones.append(intervalo[0])                                      #ingresa el primer intervalo sin ser alterado

    print (secciones)

    for i in range(0,nsecciones-1):                                     #insertar en el arreglo los intervalos intermedios, menos el primero, y el último, que no necesitan que se les sume ningún valor

        secciones.append(round(secciones[i]+interval,8))

    secciones.append(round(intervalo[1],8))

    return secciones                                                    #se retorna el arreglo para ser verificado recursivamente en la funcion "Reducir Intervalo"





def funcion(coeficiente):

    return round((((9.8*68.1)/coeficiente)*(1-math.exp(-(coeficiente/68.1)*10))-40),8)
    
def funcion2(coeficiente):

    return round((((9.8*68.1)/coeficiente)*(1-math.exp(-(coeficiente/68.1)*10))),8)

def reducirIntervalo (intervalo, nsecciones, precision, convergencia):

    secciones = seccionar(intervalo, nsecciones)                       #recibe las secciones halladas en la función "seccionar"

    for i in range (0,len(secciones)):

        resultado=abs(funcion(secciones[i]))

        if(resultado<=precision):

            return secciones[i]
    primero = funcion(secciones[0])

    for i in range(1, len(secciones)):                                  #se inicia desde el segundo elemento porque el primero se guarda

        intermedio = funcion (secciones[i])

        intermedio = round(intermedio,8)

        if((primero*intermedio)>0): #revisa si los valores estan positivos o negativos, si es así, continúa buscando
            convergencia=intermedio/primero
            print("la convergencia es: ",convergencia)
            primero=intermedio

        else:                                                           #si hay dos valores en ambos subintervalos se reduce el intervalo a los dos coeficientes intermedios

            interval = []

            interval.append(secciones[i-1])

            interval.append(secciones[i])

            return reducirIntervalo(interval,nsecciones,precision, convergencia)   #se inicia recursivamente la función con el intervalo reducido

#------------------------------------------------main------------------------------------------------------
intervalos = [14, 16]
precision = 0.00000001
convergencia=0
print ("Intervalo de 11 a 18")
nsecciones=3
solucion=round(reducirIntervalo(intervalos, nsecciones,precision, convergencia),8)
print ("Resultado con triseccion:", solucion,"+ -", precision)
print(funcion2(solucion))
nsecciones=4
solucion=round(reducirIntervalo(intervalos, nsecciones,precision, convergencia),8)
print ("Resultado con cuadriseccion:", solucion,"+ -", precision)
print(funcion2(solucion))
