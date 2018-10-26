#install.packages("phaseR")
install.packages("pracma")
#library(phaseR)
library(pracma)

metodoEuler <- function(f, h, xi, yi, xf)
{
  N = (xf - xi) / h
  x = y = numeric(N+1)
  x[1] = xi; 
  y[1] = yi;
  i = 1
  while (i <= N)
  {
    x[i+1] = x[i]+h
    y[i+1] = y[i]+(h*f(x[i],y[i]))
    i = i+1
  }
  return (data.frame(X = x, Y = y))
}

f <- function(x, y) {x-y}

e1 = metodoEuler(f, 1e-6, 0, -1, 4)

e1[nrow(e1),]

xx <- c(-3, 3); yy <- c(-1, 1)
vectorfield(f, xx, yy, scale = 0.1)
for (xs in seq(-1, 1, by = 0.25)) 
{
  sol <- rk4(f, -1, 1, xs, 100)
  lines(sol$x, sol$y, col="purple")
}

#primero


