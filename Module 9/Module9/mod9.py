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
    return x**3

def operation(f,n):
    i=1
    while n>=i:
        print(f(i)) #print(double(i))
        i+=1

def addFunction(f,n):
    def newFunction(x):
        return f(x)+n
    return newFunction