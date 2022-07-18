
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
     
          if item not in oper:
            newItem = str(float(item))
            prefix.append(newItem)
          
          else:
            if item == "(": #if operator is ( push operator into stack
              newStack.push(item)
              
            elif item == ")": #if operator is ), pop items until top is ( and discard ()
              for i in range(len(newStack)):
                if newStack.top.value != "(":
                  prefix.append(newStack.pop())
                else:
                  newStack.pop()

              #while current.next != None and current.value != "(":
              #  prefix.append(newStack.pop())
          
            elif item in oper: #if operator is +-*/^. -> if item is lower priority,-> pop

              if newStack.isEmpty():
                newStack.push(item)
              else:
                itemStack = newStack.top.value

                for i in range(len(newStack)):
          
                  if level[itemStack] >= level[item]:
                    prefix.append(newStack.pop())
                
                    
                newStack.push(item)
        
        while len(newStack) != 0: #add remaining items in the stack
          prefix.append(newStack.top.value)
          newStack.pop()

        prefix = " ".join(prefix)
        return prefix

