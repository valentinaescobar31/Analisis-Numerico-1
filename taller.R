#Taller Análisis Numérico
arreglo=c(1)
indices=c(0)
lx=c()
i=0.1
x=1
#Conseguir puntos entre 0 y 1 (10 puntos)
while(i<1){
  indices[x]=i
  arreglo[x]=exp(i)
  cat("a sub i", arreglo[i])
  i=i+0.1
  x=x+1
}

plot(indices,arreglo, pch=19, cex=1, col = "red", asp=1,xlab="X", ylab="Y", main="Diagrama ")
Ajuste_Polinomio = poly.calc(indices,arreglo)
curve(Ajuste_Polinomio,add=T, from =-1, to =20)



