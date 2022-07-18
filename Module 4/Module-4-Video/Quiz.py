#power

def power(x, n):
  if n == 0:
    return 1
  else:
    return x * power(x,n-1)

#repeat digits
def repeatDigits(n):
  last, rest = n % 10, n//10
  if n == 0:
    return 0
  return repeatDigits(rest) * 100 + last * 10 + last
  
