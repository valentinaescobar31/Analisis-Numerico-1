raizCuadrada<- function(n,p,x,y){
  
    y <- 1/2*(x+n/x)
    while (abs(x-y)>p){
     x<-y
     y<- 1/2*(x+n/x)
        
      }
    return(y)
}
round(raizCuadrada(7,0.001,1,1)

