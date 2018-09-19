'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def funcion1(valor, polinomio):
    if(len(polinomio)==0):
        return 0;
    value = polinomio.pop()
    return round(value+funcion1(valor, polinomio)*valor,4)
    

def funcion(polinomio, precision, intervalo):
    resultados=[]
    primero= intervalo[0]
    print (primero)
    while(primero!=intervalo[1]):
        polinom=polinomio[:]
        retorno=funcion1(primero, polinom)
        primero=round(primero+precision,4)
        if((retorno<0.0001)and(retorno>-0.0001)):
            resultados.append(primero)
        
    return resultados
    

polinomio = [4,4,4,4,4,4,4,4,1]
precision = 0.0001
intervalo=[-2,2]

print(funcion(polinomio, precision, intervalo))
