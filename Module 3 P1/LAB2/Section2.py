########################Section 2#########################
import random

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
        #create instance variable for balance and dictionary 
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


if __name__=='__main__':
    import doctest
    doctest.testmod()  
