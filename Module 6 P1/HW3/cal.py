
class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

#=============================================== Part I ==============================================

class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        self.top = None
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__


    def isEmpty(self):
        # YOUR CODE STARTS HERE
      if self.top == None:
        return True
      else:
        return False
      

    def __len__(self): 
        # YOUR CODE STARTS HERE
      current = self.top
      count = 0
      while current is not None:
        count += 1
        current = current.next

      return count
        
    
      #traverse stack similarly to linkedlist traversal (make sure stopping conditions correct)

    def push(self,value):
        # YOUR CODE STARTS HERE
      new = Node(value)
      if self.isEmpty():
        self.top = new
      else:
        new.next = self.top
        self.top = new
  
      #check if the stack is empty

     
    def pop(self):
        # YOUR CODE STARTS HERE

      if self.isEmpty():
        return None
      else:
        remove = self.top
        self.top = self.top.next
        return remove.value
      #update top attribute and unlink old top, return value

    def peek(self):
        # YOUR CODE STARTS HERE
      if self.isEmpty():
        return None
      else:
        return self.top.value

#=============================================== Part II ==============================================

class Calculator:
    def __init__(self):
        self.__expr = None


    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str):
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None

    def _isNumber(self, txt):
        '''
            >>> x=Calculator()
            >>> x._isNumber(' 2.560 ')
            True
            >>> x._isNumber('7 56')
            False
            >>> x._isNumber('2.56p')
            False
            >>> x._isNumber('2.56')
            True

        '''
        txt = txt.strip()
        try:
            float(txt)
            return True
        except:
            return False
      

      
      #CHECKING VALIDITY ->  IF IT IS AN NUMBER -> IS IT A VALID OPERATOR
      #valid operator -> create an object in python {} that contains valid operators, compare with the characters in the string



    def _getPostfix(self, txt):
        '''
            Required: _getPostfix must create and use a Stack for expression processing
            >>> x=Calculator()
            >>> x._getPostfix('2 ^ 4')
            '2.0 4.0 ^'
            >>> x._getPostfix('2')
            '2.0'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x._getPostfix('2 * 5.34 + 3 ^ 2 + 1 + 4')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('( 2.5 )')
            '2.5'
            >>> x._getPostfix ('( ( 2 ) )')
            '2.0'
            >>> x._getPostfix ('2 * ( ( 5 + -3 ) ^ 2 + ( 1 + 4 ) )')
            '2.0 5.0 -3.0 + 2.0 ^ 1.0 4.0 + + *'
      
        '''

        # YOUR CODE STARTS HERE
        newStack = Stack()
        oper = ["+","-","*","%","/","^","(",")"]
        prefix = []
        level = {")":1,"(":1,"+":2,"-":2,"/":3,"*":3,"^":4}

        txt = txt.split()

      
        for item in txt:
          print("item",item)
          if item not in oper:
            newItem = str(float(item))
            prefix.append(newItem)
          
          else:
            if item == "(":
              newStack.push(item)
              
              
            elif item == ")":

              current = newStack.top
              while current is not None and current.value != "(":
                prefix.append(newStack.pop())
          
            elif item in oper:
              if newStack.isEmpty():
                newStack.push(item)
              else:
                itemStack = newStack.top.value
                current = newStack.top
                while current is not None and newStack.top.value != "(":
                  if level[itemStack] >= level[item]:
                    prefix.append(newStack.pop())
                    
                
                newStack.push(item)

          print("hihihih",newStack)

            
        
        while len(newStack) != 0:
          prefix.append(newStack.top.value)
          newStack.pop()

        prefix = " ".join(prefix)
        return prefix

      # method must use postfixStack to compute the postfix expression

      # to make validity checks, either perform them here before creating postfix, or call a method before Postfix

    #method1: def validtitycheck(self,check)
   
      #follow PEMDAS
      #to create PEMDAS precedence, use a data structure that can map an operator (i,e, *, +) with a priority number (1,2,3)
      #'-','+' = 1
      #'*','/' = 2
      #run the algorithm discussed i

      #wath video STACK Applications

      

      

    @property
    def calculate(self):
        '''
            calculate must call _getPostfix
            calculate must create and use a Stack to compute the final result as shown in the video lecture
            
            >>> x=Calculator()
            >>> x.setExpr('4 + 3 - 2')
            >>> x.calculate
            5.0
            >>> x.setExpr('-2 + 3.5')
            >>> x.calculate
            1.5
            >>> x.setExpr('4 + 3.65 - 2 / 2')
            >>> x.calculate
            6.65
            >>> x.setExpr('23 / 12 - 223 + 5.25 * 4 * 3423')
            >>> x.calculate
            71661.91666666667
            >>> x.setExpr(' 2 - 3 * 4')
            >>> x.calculate
            -10.0
            >>> x.setExpr('7 ^ 2 ^ 3')
            >>> x.calculate
            5764801.0
            >>> x.setExpr(' 3 * ( ( ( 10 - 2 * 3 ) ) )')
            >>> x.calculate
            12.0
            >>> x.setExpr('8 / 4 * ( 3 - 2.45 * ( 4 - 2 ^ 3 ) ) + 3')
            >>> x.calculate
            28.6
            >>> x.setExpr('2 * ( 4 + 2 * ( 5 - 3 ^ 2 ) + 1 ) + 4')
            >>> x.calculate
            -2.0
            >>> x.setExpr(' 2.5 + 3 * ( 2 + ( 3.0 ) * ( 5 ^ 2 - 2 * 3 ^ ( 2 ) ) * ( 4 ) ) * ( 2 / 8 + 2 * ( 3 - 1 / 3 ) ) - 2 / 3 ^ 2')
            >>> x.calculate
            1442.7777777777778
            

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            >>> x.setExpr(" 4 + + 3 + 2") 
            >>> x.calculate
            >>> x.setExpr("4  3 + 2")
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * ( 2 - 3 * 2 ) )')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * / ( 2 - 3 * 2 )')
            >>> x.calculate
            >>> x.setExpr(' ) 2 ( * 10 - 3 * ( 2 - 3 * 2 ) ')
            >>> x.calculate
            >>> x.setExpr('( 3.5 ) ( 15 )') 
            >>> x.calculate
            >>> x.setExpr('3 ( 5 ) - 15 + 85 ( 12 )') 
            >>> x.calculate
            >>> x.setExpr("( -2 / 6 ) + ( 5 ( ( 9.4 ) ) )") 
            >>> x.calculate
        '''

        if not isinstance(self.__expr,str) or len(self.__expr)<=0:
            print("Argument error in calculate")
            return None

        calcStack = Stack()   # method must use calcStack to compute the  expression
        
          
        # YOUR CODE STARTS HERE
        pass
      #implement the algorithm discussed in the video lectures
