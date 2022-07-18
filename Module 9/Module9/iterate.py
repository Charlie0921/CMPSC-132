#iterator
class fib:
  def __init__(self,n):
    self.n = n
    self.a = 0
    self.b = 1
    self.count = 0

  def __iter__(self):
    return self

  def __next__(self):
    if self.count >= self.n:
      raise StopIteration
    output=self.a
    self.count += 1
    self.a, self.b = self.b, self.a+self.b
    return output

def double(x):
  print('##',x,'=>',2*x,'##')
  return 2 * x

#generator

def fib2(n):
  a, b = 0, 1
  count = 0
  while count < n:
    yield a
    a, b = b, a+b
    count += 1


def fib3():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a+b
