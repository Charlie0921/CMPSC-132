#Iterative Function
def dibi(n):
  x, y = 0, 1
  for i in range(n):
    x, y = y, x + y
    return x

#Recursive Function
computed = {0:0, 1:1}
def fibmr(n):
  if not n in computed:
    computed[n] = fibmr(n-1) + fibmr(n-2)
  return computed[n]