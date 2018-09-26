x=c(1.8, 1.9, 2, 2.1, 2.2)
y=c()
b=2
a=2
for (i in 0:5)
  y[i]=x[i]*exp(x[i])
cat(x)
cat(y)


f= function(x) x*exp(x)
#derivar con 4.4
h=0.1                   
cuatro= function(x1,x2,x3,h){
  valor=1/(2*h)*(-3*f(x1)+4*f(x2)-f(x3))
  cat(valor)
  return valor
}
cinco= function(x1,x2,h){
  valor=1/(2*h)*(f(x1)-f(x2))
  cat(valor)
  return valor
}
derivar=function(x){
  return exp(x)*x*exp(x)
}
cuatro(x[3],x[4], x[5],h)
cuatro(x[3],x[2], x[1],h)
cinco(2.1,1.9,h)
h=0.2
cinco(2.2,1.8,h)
derivar(2)
error1=derivar(x[3])-cuatro(x[3],x[4], x[5],h)





