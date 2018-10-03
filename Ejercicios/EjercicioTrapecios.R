contador=0
trapecios=10
amplitud=91/trapecios
arr=c()
sum=0
var=1

f3 <- function(x) {
  return(sin(x))
}
f4 <- function(x) {
  return(cos(x+pi/2))
}
x=seq(0 , 12, 0.1)
ysen=c()
for(i in 1:length(x)){
  ysen[i]=sin(x[i])
}

seg <- seq.int(0, 12, length.out = 12)
segcos <- seq.int(0, 12, length.out = 12)

fx <- vector(length = length(seg))
fxcos <- vector(length = length(segcos))

for (i in 1:length(seg)) {
  fx[i] <- f3(seg[i])
}
for (i in 1:length(segcos)) {
  fxcos[i] <- f4(segcos[i])
}

df <- data.frame(xend = seg, 
                 y = rep(0, 12), 
                 yend = fx, 
                 yend1 = c(fx[2:12], fx[12]), 
                 xend1 = c(seg[2:12], seg[12]),
                 xendcos = segcos, 
                 ycos = rep(0, 12), 
                 yendcos = fxcos, 
                 yend1cos = c(fxcos[2:12], fxcos[12]), 
                 xend1cos = c(segcos[2:12], segcos[12]))

ggplot(data = df,main="Suma de Trapecios") + 
  stat_function(fun = f3, size = 1.05, alpha = 0.75, color='black') + 
  stat_function(fun = f4, size = 1.05, alpha = 0.75, color='black') + 
  geom_segment(aes(x=xend, y=y, xend=xend, yend=yend)) + 
  geom_ribbon(aes(x=xend, ymin=y, ymax=yend), fill = 'black', alpha = 0.3) +
  geom_segment(aes(x=xendcos, y=ycos, xend=xendcos, yend=yendcos)) + 
  geom_ribbon(aes(x=xendcos, ymin=ycos, ymax=yendcos), fill = 'blue', alpha = 0.3) +
  xlim(c(0, 12))


# Se realiza una iteracion por cada trapecio que se desea generar en la funcion
for(i in 1:trapecios){
  if(i==trapecios){
    arr[i]=ysen[i*amplitud]
  }else{
    arr[i]=abs(ysen[i*amplitud])+abs(ysen[(i+1)*amplitud])
  }
  contador=((arr[i]/2)*amplitud)*0.07
  if(var==1) {
    print(" -----  TABLA DE AREAS  -----")
    var=var+1;
  }
  cat("     ","|       ",contador,"      "," |","\n\r")
  sum=(sum+contador)
}
cat("Suma de las areas del trapecio ",sum)