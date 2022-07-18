from math import pi, sqrt

def areaSquare(r):
    return r * r

def areaCircle(r):
    return r * r * pi

def areaHexagon(r):
    return r * r * 3 * sqrt(3) / 2

################
def area(r, shape_constant):
    if r<0:
       return 'Length must be positive'
    return r * r * shape_constant

def areaSquare(r):
    return area(r, 1)

def areaCircle(r):
    return area(r, pi)

def areaHexagon(r):
    return area(r, 3 * sqrt(3) / 2)