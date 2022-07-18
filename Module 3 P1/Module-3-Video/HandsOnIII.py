class Fraction:

  def __new__(self, numerator, denominator):
    if denominator == 0:
      raise ZeroDivisionError('Denominator cannot be zero')
    instance = super(Fraction, self).__new__(self)
    return instance


  def __init__(self, numerator, denominator):
    self.n = numerator
    self.d = denominator

  def __str__(self):
    return f'{self.n}/{self.d}'

  __repr__ = __str__ #don't have to use print()
  
  def __add__(self, other):
    n = self.n * other.d + self.d * other.n
    d = self.d * other.d
    return Fraction(n,d)

  def __sub__(self, other):
    n = self.n * other.d - self.d * other.n
    d = self.d * other.d
    return Fraction(n,d)
  
  def __mul__(self, other):
    n = self.n * other.n
    d = self.d * other.d
    return Fraction(n,d)
  
  def __truediv__(self,other):
    n = self.n * other.d
    d = self.d * other.n
    return Fraction(n,d)
  
  #x and y memory location is different!

  def __eq__(self,other):
    return self.n==other and self.d == other.d

