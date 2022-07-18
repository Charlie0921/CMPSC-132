class Complex:
    """ Complex number of the form a + bi, where a and b are real numbers, and i is an indeterminate satisfying i2 = −1 """

    def __init__(self,r,i):
        self._real = r
        self._imag = i
        self._ans = 0
        
      
    def __str__(self):
        """Display complex number"""
        if self._imag>=0:
           return f"{self._real} + {self._imag}i"
        else:
           return f"{self._real} - {abs(self._imag)}i"
    
    def conjugate(self):
        """Returns a Complex object that represents the complex conjugate"""
        return Complex(self._real, -self._image)
    
    def __mul__(self,other):
        """Multiply two Complex numbers"""

        if isinstance(other, Complex):
          ans = Complex(self._real * other._real - self._imag * other._imag, self._real * other._imag + self._imag * other._real)
        else:
          ans = Complex(self._real * other,self._imag*other)
        return ans

    def __rmul__(self, other):
      return self*other


    __repr__ = __str__

class Real(Complex):

    def __init__(self, value):
      super().__init__(value, 0)
       

    def __mul__(self,other):
      result = Complex.__mul__(self, other)
      return result

    def __eq__(self,other):
      if self._real == other._real:
        return True
      else:
        return False

