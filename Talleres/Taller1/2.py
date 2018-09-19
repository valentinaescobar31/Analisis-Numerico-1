import math                                                             #para la función math.exp

def seccionar (intervalo, nsecciones,redondeo):
    secciones= []                                                       #guarda las secciones encontradas según el número de particiones
    interval = round(abs((intervalo[0])-(intervalo[1]))/nsecciones,redondeo)   #cada intervalo se separa por este valor, menos el primero
    secciones.append(intervalo[0])                                      #ingresa el primer intervalo sin ser alterado
    for i in range(0,nsecciones-1):                                     #insertar en el arreglo los intervalos intermedios, menos el primero, y el último, que no necesitan que se les sume ningún valor
        secciones.append(round(secciones[i]+interval,redondeo))
    secciones.append(round(intervalo[1],redondeo))
    return secciones                                                    #se retorna el arreglo para ser verificado recursivamente en la funcion "Reducir Intervalo"
def funcion(coeficiente, redondeo):
    return round(((largo-coeficiente-coeficiente)*(ancho-coeficiente-coeficiente)*coeficiente)-1000, redondeo)
def reducirIntervalo (intervalo, nsecciones, precision, convergencia, redondeo, largo, ancho):
    secciones = seccionar(intervalo, nsecciones ,redondeo)   #recibe las secciones halladas en la función "seccionar"
    for i in range (0,len(secciones)):
        resultado=funcion(secciones[i], redondeo)
        if(i!=0):
            resultadoanterior = funcion(secciones[i-1], redondeo)
            if(resultadoanterior==resultado):
                return secciones[i]
        if(abs(resultado)<precision):
            return secciones[i]
    primero= funcion(secciones[0], redondeo)
    for i in range (0, len(secciones)):
        intermedio=funcion(secciones[i], redondeo)
        if(primero*intermedio>0):
            primero=intermedio
        else:                                                           #si hay dos valores en ambos subintervalos se reduce el intervalo a los dos coeficientes intermedios
            interval = []
            interval.append(secciones[i-1])
            interval.append(secciones[i])
            return reducirIntervalo(interval,nsecciones,precision, convergencia, redondeo, largo, ancho)   #se inicia recursivamente la función con el intervalo reducido
#------------------------------------------------main------------------------------------------------------
intervalos = [0.1,10]
redondeo= 7
precision = 1*(10**-redondeo)
convergencia=0
largo=float(input("Ingrese el largo de la caja"))
ancho=float(input("Ingrese el largo de la caja"))
print ("Intervalo de ",intervalos)
nsecciones=2
solucion=round(reducirIntervalo(intervalos, nsecciones,precision, convergencia, redondeo, largo, ancho),redondeo)
print ("Resultado con biseccion:", solucion,"+ -", precision)

#Incisos
#a.La etapa donde se calcula el nuevo intervalo reducido, ya que si se excede el valor del volumen el algoritmo entra en proceso de ciclo infinito, por tanto las condiciones y los nuevos valores del intervalo, siempre deben estar por debajo del valor que se busca, y al final la diferencia debe ser muy pequeña, con un muy pequeño error de truncamiento.
#b. Conocer sobre el cálculo de volúmenes, saber construir la ecuación que resuelve el problema, la cual se usa como fórmula para hallar el volumen en cada iteración, y conocimientos de programacion
#c. La prueba y error tiene varias desventajas: 1.Tiempo, a menudo no se llega a la solución más aproximada, 2. No es util en cuanto al aprendizaje, y tampoco es óptimo en cuanto a consumo de recursos, menos iteraciones es mejor
#d. El error de redondeo es más crítico, porque el de truncamiento a medida pasan las iteraciones éste disminuye, el de redondeo funciona durante todas la iteraciones reduciendo la exactitud de acuerdo a la precisión que se asigne
#e. El aprovechamiento de una máquina para trabajar, y las pruebas de escritorio ayudan a entender mejor el problema
#f. 1. Para hallar el error de truncamiento, 2. Para conocer cuán preciso fue el algoritmo, 3. Para tener un punto de referencia con respecto al resultado ideal
