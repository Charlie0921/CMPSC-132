"""
def squareFunction(n):
  i = 1
  while n >= i:
    print(i*i)
    i+=1

def doubleFunction(n):
  i = 1
  while n >= i:
    print(2*i)
    i+=1
"""
def squareFunction(n):
  operation(square,n)

def doubleFunction(n):
  operation(double,n)

def cubeFunction(n):
  operation(cube,n)

def square(x):
  return x*x

def double(x):
  return 2*x

def cube(x):
  return x*x*x

def operation(f,n):
  i = 1
  while n >= i:
    print(f(i)) #print(double(i))
    i += 1

"""
def f1(arg):
  def f2(arg2):
    return f2
"""
def addFunction(f,n): #outer function
  def newFunction(x): #inner function
    return f(x)+n
  return newFunction