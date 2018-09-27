x=seq(-3,3,0.1)
y=dnorm(x)
suma=0
for(i in 1:length(x)){
  suma=abs(y[i])+suma
}
barplot(y, main= "Distribucion normal", xlab="x", ylab="y", col=c("gold","red"))
cat("resultado de la suma: ",suma)


