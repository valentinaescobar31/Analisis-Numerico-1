# Remueve todos los objetos creados
rm(list=ls())
# Halla la raiz de Fx
Fx <- function(x,y) 2*cos(x)+sin(y)
F1x <- function(x,y) -2*sin(x)+cos(y)
newton <- function(x,y) {
  for(i in 1:10) {
    x<-0-Fx(x,y)/F1x(x,y)
    if (Fx(x,y) == 0) break
    error<-abs(Fx(x,y)/F1x(x,y))
    cat("X=",x,"\t","E=",error,"\n")
  }
}
newton(1,1)
