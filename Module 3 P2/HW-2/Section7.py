
class Person:
    '''
        >>> p1 = Person('Jason Lee', '204-99-2890')
        >>> p2 = Person('Karen Lee', '247-01-2670')
        >>> p1
        Person(Jason Lee, ***-**-2890)
        >>> p2
        Person(Karen Lee, ***-**-2670)
        >>> p3 = Person('Karen Smith', '247-01-2670')
        >>> p3
        Person(Karen Smith, ***-**-2670)
        >>> p2 == p3
        True
        >>> p1 == p2
        False
    '''

    def __init__(self, name, ssn):
      self.name = name
      self.ssn = ssn


    #*****create a private attribute - SSN(put at the beginning of the name)
    


    def __str__(self):
        # YOUR CODE STARTS HERE
        # access last for digits -> think about what method we've that can split with a character
        # Think of how we can isolate the last 4 digits of ssn
      last = str(self.ssn)
      last = last[-4:]
      self.ssn = f'***-**-{last}'
      return Person({self.name}, {self.ssn})
        

    __repr__ = __str__

    def get_ssn(self):
        # YOUR CODE STARTS HERE
        # return the social security number
      return self.ssn


    def __eq__(self, other):
      isEq = True
      if self.ssn != other.ssn:
        isEq = False
      return isEq


if __name__=='__main__':
    import doctest
    doctest.testmod()  # OR
    #doctest.run_docstring_examples(Course, globals(), name='HW22',verbose=True) # replace Course for the class name you want to test