ecuacion= function(x){
  return(2+(exp(1)-2)*exp(-x^3))
}
h=0.001
x=seq(-0.1, 0.1, h)
m=c()
for(i in 0:length(x)){
    m[i]=abs((ecuacion(x[i]+h)-ecuacion(x[i]))/h)
}
plot(m, pch='O')
cat("cota= ",m[length(m)])
m