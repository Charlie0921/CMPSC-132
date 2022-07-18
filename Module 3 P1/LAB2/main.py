# LAB2
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement
#########################Section 1###########################
import random


class Fibonacci:
    """
        >>> fib_seq = Fibonacci()
        >>> fib_seq
        <Fibonacci object>, value = 0
        >>> fib_seq.next()
        <Fibonacci object>, value = 1
        >>> fib_seq.next().next()
        <Fibonacci object>, value = 1
        >>> fib_seq.next().next().next()
        <Fibonacci object>, value = 2
        >>> fib_seq.next().next().next()
        <Fibonacci object>, value = 2
        >>> fib_seq.next().next().next().next()
        <Fibonacci object>, value = 3
        >>> fib_seq.next().next().next().next().next()
        <Fibonacci object>, value = 5
        >>> fib_seq.next().next().next().next().next().next()
        <Fibonacci object>, value = 8
        >>> other_fib_seq = Fibonacci()
        >>> other_fib_seq
        <Fibonacci object>, value = 0
        >>> other_fib_seq.next().next().next().next().next()
        <Fibonacci object>, value = 5
        >>> fib_seq.next().next().next().next().next().next()
        <Fibonacci object>, value = 8
    """
    def __init__(self):
        self.start = 0

    def next(self):

        #--- YOUR CODE STARTS HERE
        new = Fibonacci()

        previous = self.start

        if previous == 0:
            present = 1
        else:
            present = self.present

        result = previous + present
        #print(previous,present, result)

        new.present = result
        new.start = present
        
        return new

    def __repr__(self):
        return f"<Fibonacci object>, value = {self.start}"



########################Section 2#########################

class Vendor:
    '''
        In this class, self refers to VendingMachine objects

        >>> john_vendor = Vendor('John Doe')
        >>> west_machine = john_vendor.install()
        >>> west_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> john_vendor.restock(west_machine, 215, 9)
        'Invalid item'
        >>> west_machine.isStocked
        True
        >>> john_vendor.restock(west_machine,156, 1)
        'Current item stock: 4'
        >>> west_machine.getStock
        {156: [1.5, 4], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> west_machine.purchase(156)
        'Please deposit $1.5'
        >>> west_machine.purchase(156,2)
        'Please deposit $3.0'
        >>> west_machine.purchase(156,23)
        'Current 156 stock: 4, try again'
        >>> west_machine.deposit(3)
        'Balance: $3'
        >>> west_machine.purchase(156,3)
        'Please deposit $1.5'
        >>> west_machine.purchase(156)
        'Item dispensed, take your $1.5 back'
        >>> west_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> west_machine.deposit(300)
        'Balance: $300'
        >>> west_machine.purchase(876)
        'Invalid item'
        >>> west_machine.purchase(384,3)
        'Item dispensed, take your $292.5 back'
        >>> west_machine.purchase(156,10)
        'Current 156 stock: 3, try again'
        >>> west_machine.purchase(156,3)
        'Please deposit $4.5'
        >>> west_machine.deposit(4.5)
        'Balance: $4.5'
        >>> west_machine.purchase(156,3)
        'Item dispensed'
        >>> west_machine.getStock
        {156: [1.5, 0], 254: [2.0, 3], 384: [2.5, 0], 879: [3.0, 3]}
        >>> west_machine.purchase(156)
        'Item out of stock'
        >>> west_machine.deposit(6)
        'Balance: $6'
        >>> west_machine.purchase(254,3)
        'Item dispensed'
        >>> west_machine.deposit(9)
        'Balance: $9'
        >>> west_machine.purchase(879,3)
        'Item dispensed'
        >>> west_machine.isStocked
        False
        >>> west_machine.deposit(5)
        'Machine out of stock. Take your $5 back'
        >>> west_machine.purchase(156,2)
        'Machine out of stock'
        >>> west_machine.purchase(665,2)
        'Invalid item'
        >>> east_machine = john_vendor.install()
        >>> west_machine.getStock
        {156: [1.5, 0], 254: [2.0, 0], 384: [2.5, 0], 879: [3.0, 0]}
        >>> east_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> east_machine.deposit(10)
        'Balance: $10'
        >>> east_machine.cancelTransaction()
        'Take your $10 back'
        >>> east_machine.purchase(156)
        'Please deposit $1.5'
        >>> east_machine.cancelTransaction()
    '''

    def __init__(self, name):
        '''
            In this class, self refers to Vendor objects
            
            name: str
            vendor_id: random int in the range (999, 999999)
        '''
        self.name = name
        self.vendor_id = random.randint(999, 999999)
    
    def install(self):
        '''
            Creates and initializes (instantiate) an instance of VendingMachine 
        '''
        return VendingMachine()
    
    def restock(self, machine, item, amount):
        '''
            machine: VendingMachine
            item: int
            amount : int/float

            Call _restock for the given VendingMachine object
        '''
        return machine._restock(item, amount)
        


class VendingMachine:

    def __init__(self):
        #--- YOUR CODE STARTS HERE
        self.qty = 1
        self.balance = 0
        self.dic = {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        pass

        #vendor1 = Vendor('John Doe')
        #x = vendor1.install()


    def purchase(self, item, qty=1):
        #--- YOUR CODE STARTS HERE
        #input: item, gty
        dic = self.getStock
        values = list(self.getStock.values())
        lst = dic.keys()
       

        isZero = True
        i = 0
        while i < len(values):
          if values[i][1] != 0:
            isZero = False
            break
          i += 1

        if item not in lst:
          return "Invalid item"
        else:
    
          if isZero == True:
            return "Machine out of stock"
          elif dic[item][1] == 0:
            return "Item out of stock"
          elif dic[item][1] < qty:
            return f"Current {item} stock: {dic[item][1]}, try again"
          elif dic[item][0]*qty > self.balance:
            remaining = ((dic[item][0])*qty)-(self.balance)
            return f'Please deposit ${remaining}'
          else:
            self.balance = self.balance - ((dic[item][0])*qty)
            if self.balance != 0:
              
              self.dic[item][1] = self.dic[item][1]-qty
              balance = self.balance
              self.balance = 0
              return f'Item dispensed, take your ${balance} back'
            else: 
          
              self.dic[item][1] = self.dic[item][1]-qty
              return f'Item dispensed'



        #output: invalid item, machine out of stock, item out of stock, Current item id stock, please dep

        pass
    
    #vendor1 = Vendor('John Doe')
        #x = vendor1.install()

    def deposit(self, amount):
        #--- YOUR CODE STARTS HERE
        self.balance = amount
        values = list(self.getStock.values())

        isZero = True
        i = 0
        while i < len(values):
          if values[i][1] != 0:
            isZero = False
            break
          i += 1
        if isZero == True:
          return f"Machine out of stock. Take your ${self.balance} back"
        else:
          return f"Balance: ${self.balance}"
#vendor1 = Vendor('John Doe')
        #x = vendor1.install()
# vendor1.restock(x,215,9)


    def _restock(self, item, stock):
        #--- YOUR CODE STARTS HERE
        self.dic = self.getStock
        lst = self.dic.keys()
        
        if item in lst: 
          self.amount = self.dic[item][1]
          self.amount += stock
          self.dic[item][1] = self.amount
    
          return f"Current item stock: {self.amount}"
        else: 
          return "Invalid item"


    #--- YOUR CODE STARTS HERE

    @property
    def isStocked(self):
      values = list(self.getStock.values())
      isNonzero = False
      i = 0
      while i < len(values):
        if values[i][1] != 0:
          isNonzero = True
          break
        i += 1
      return isNonzero
        
        

    #--- YOUR CODE STARTS HERE

    @property
    def getStock(self):
      return self.dic

    def cancelTransaction(self):
        #--- YOUR CODE STARTS HERE
        if self.balance == 0:
          return None
        else:
          balance = self.balance
          self.balance = 0
          return f'Take your ${balance} back'

          
################section3###############
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def hell0(self):
      return self.x


class Line: 
    ''' 
            >>> p1 = Point2D(-7, -9)
            >>> p2 = Point2D(1, 5.6)
            >>> line1 = Line(p1, p2)
            >>> line1.getDistance
            16.648
            >>> line1.getSlope
            1.825
            >>> line1
            y = 1.825x + 3.775
            >>> line2 = line1*4
            >>> line2.getDistance
            66.592
            >>> line2.getSlope
            1.825
            >>> line2
            y = 1.825x + 15.1
            >>> line1
            y = 1.825x + 3.775
            >>> line3 = 4*line1
            >>> line3
            y = 1.825x + 15.1
            >>> line1==line2
            False
            >>> line3==line2
            True
            >>> line5=Line(Point2D(6,48),Point2D(9,21))
            >>> line5
            y = -9.0x + 102.0
            >>> line5==9
            False
            >>> line6=Line(Point2D(2,6), Point2D(2,3))
            >>> line6.getDistance
            3.0
            >>> line6.getSlope
            inf
            >>> isinstance(line6.getSlope, float)
            True
            >>> line6
            Undefined
            >>> line7=Line(Point2D(6,5), Point2D(9,5))
            >>> line7.getSlope
            0.0
            >>> line7
            y = 5.0
        '''
    def __init__(self, point1, point2):
        #--- YOUR CODE STARTS HERE
        self.p1x = point1.x 
        self.p1y = point1.y
        self.p2x = point2.x
        self.p2y = point2.y


    #--- YOUR CODE STARTS HERE
    @property
    def getDistance(self):
      deltax = self.p1x - self.p2x
      deltay = self.p1y - self.p2y

      distance = ((deltax)**2 + (deltay)**2)**(1/2)

      self.distance = round(distance,3)
      return self.distance

    #--- YOUR CODE STARTS HERE
    @property
    def getSlope(self):
      deltax = self.p1x - self.p2x
      deltay = self.p1y - self.p2y

      if deltax != 0:
        slope = deltay / deltax
        if deltay == 0:
          self.slope = abs(slope)
        else:
          self.slope = round(slope,3)

      else:
        self.slope = float("inf")

      return self.slope

    #--- YOUR CODE CONTINUES HERE
    def __str__(self):

      if self.getSlope != float("inf"):
        b = round(self.p1y - self.getSlope * self.p1x, 3)
        if self.getSlope == 0:
          return f"y = {b}"
        elif b == 0:
          return f"y = {self.getSlope}x"

        elif b > 0:
          return f"y = {self.getSlope}x + {b}"

        elif b < 0:
          return f"y = {self.getSlope}x - {abs(b)}"
      else:
        return 'Undefined'
      
    __repr__ = __str__

    def __mul__(self,num):
      new = Line(Point2D(self.p1x,self.p1y), Point2D(self.p2x,self.p2y))
      new.p1x = self.p1x * num
      new.p1y = self.p1y * num
      new.p2x = self.p2x * num
      new.p2y = self.p2y * num
      new = Line(Point2D(new.p1x,new.p1y), Point2D(new.p2x,new.p2y))
      
      return new
    
    def __rmul__(self,num):
      new = Line(Point2D(self.p1x,self.p1y), Point2D(self.p2x,self.p2y))
      new.p1x = self.p1x * num
      new.p1y = self.p1y * num
      new.p2x = self.p2x * num
      new.p2y = self.p2y * num
      new = Line(Point2D(new.p1x,new.p1y), Point2D(new.p2x,new.p2y))
      
      return new

    def __eq__(self,other):
      isEq = False
      if not isinstance(other,Line):
        return isEq
      else:
        if self.p1x == other.p1x and self.p1y == other.p1y :
          if self.p2x == other.p2x and self.p2y == other.p2y:
            isEq = True
            return isEq
          else:
            return isEq
        else:
          return isEq
  
#line1 = Line(Point2D(1,2),Point2D(2,3))




if __name__=='__main__':
    import doctest
    doctest.testmod()  

    

    






if __name__=='__main__':
    import doctest
    doctest.testmod()  # OR
    #doctest.run_docstring_examples(Fibonacci, globals(), name='LAB2',verbose=True) # replace Fibonacci for the class name you want to test