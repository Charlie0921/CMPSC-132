class Account: 

    def __init__(self, acct_holder): 
        """Initial account balance is 0 and holder is acct_holder"""
        self._holder = acct_holder
        self._balance = 0

    def deposit(self, amount): 
        """Increment account balance by amount and return new balance"""
        self._balance += amount

    def withdraw(self, amount): 
        """Decrement account balance by amount and return amount withdrawn. Overdraft is not allowed"""
        if amount <= self._balance:
            self._balance -= amount

    @property
    def get_balance(self): 
        """Return account's balance"""
        return self._balance

class Real(Complex):

    def __init__(self, value):
        super().__init__(value, 0)
      
#>>> my_acct = Account('Jane Doe')
#>>> your_acct = Account('John Doe') 
#>>> my_acct.deposit(1000) 
#>>> your_acct.get_balance
#0
#>>> my_acct.get_balance                  
#1000
#>>> my_acct.withdraw(50)  
#>>> my_acct.get_balance   
#950
#>>> your_acct.get_balance
#0