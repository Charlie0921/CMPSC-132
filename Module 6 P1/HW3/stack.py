# HW3
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement


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

