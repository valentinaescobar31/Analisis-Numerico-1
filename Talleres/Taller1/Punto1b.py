def funcion(polinomio, valor, operaciones):
    poli= polinomio[:]
    return funcion1(poli, valor, operaciones)
    
    
def funcion1(polinomio, valor, operaciones):
    if(len(polinomio)==0):
        return 0;
    value = polinomio.pop(0)
    if(value!=0):
        operaciones[0]=operaciones[0]+2
    return round(value+funcion1(polinomio, valor, operaciones)*valor,4)
    
def derivar(polinomio):
    for i in range(0, len(polinomio)):
        polinomio[i]=polinomio[i]*i;
    
    polinomio.pop(0)
    return polinomio
polinomio = [-4,3,0,-6,6,7]
operaciones=[0]
valor=int(input("Ingrese el valor de X:"))
print("cuando x vale ",valor, ", el resultado es ",funcion(polinomio, valor, operaciones))
print("Numero de operaciones: ", operaciones)
polinomio=derivar(polinomio)
print("Derivada: ", polinomio)

