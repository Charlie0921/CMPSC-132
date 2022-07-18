# LAB4
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement


class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
                          
class SortedLinkedList:
    '''
        >>> x=SortedLinkedList()
        >>> x.add(8.76)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(5)
        >>> x.add(3)
        >>> x.add(-7.5)
        >>> x.add(4)
        >>> x.add(9.78)
        >>> x.add(4)
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 1 -> 1 -> 3 -> 4 -> 4 -> 5 -> 8.76 -> 9.78
        >>> x.replicate()
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> -7.5 -> 1 -> 1 -> 1 -> 3 -> 3 -> 3 -> 4 -> 4 -> 4 -> 4 -> 4 -> 4 -> 4 -> 4 -> 5 -> 5 -> 5 -> 5 -> 5 -> 8.76 -> 8.76 -> 9.78 -> 9.78
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 1 -> 1 -> 3 -> 4 -> 4 -> 5 -> 8.76 -> 9.78
        >>> x.removeDuplicates()
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 3 -> 4 -> 5 -> 8.76 -> 9.78
    '''

    def __init__(self):   # You are not allowed to modify the constructor
        self.head=None
        self.tail=None

    def __str__(self):   # You are not allowed to modify this method
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' -> '.join(out) 
        return f'Head:{self.head}\nTail:{self.tail}\nList:{out}'

    __repr__=__str__


    if self.isEmpty():
        self.head=newNode
        self.tail=newNode
      else:
        current = self.head
        if value <= self.head.value:
            newNode.next=self.head
            self.head=newNode
            print("intro")

        else:
          while current.next is not None:
            print(current.value)
            if current.next.value >= value:
              newNode.next = current.next
              current.next = newNode
              print("middle")
              break
            current = current.next
            
          if current.value == self.tail.value:
              current.next = newNode
              self.tail = newNode
              print("outro")
        

  #>>> x=SortedLinkedList()
   #     >>> x.add(8.76)
    #    >>> x.add(1)
     #   >>> x.add(1)
      #  >>> x.add(1)
          

    def replicate(self):
        # --- YOUR CODE STARTS HERE
      hello = SortedLinkedList().head
      current = self.head
      
      while current is not None:
        if current.value < 0 or isinstance(current.value, float):
          new = Node(current.value)
          new.next = current.next
          current.next = new
          current = current.next
         
        elif current.value > 0:
          number = current.value
          for i in range(1,number):
            new = Node(number)
            new.next = current.next
            current.next = new
            current = current.next  

        current = current.next
        
      return hello



    def removeDuplicates(self):
        # --- YOUR CODE STARTS HERE
      hello = SortedLinkedList()
      current = self.head

      while current is not None:
        hello.add(current.value)
        current = current.next

      current = hello.head
      hello = hello.replicate()

      current = hello.head
      
      while current.next.next is not None:
  
        if hello.head.value == hello.head.next.value:
          hello.head = hello.head.next
         
          current = current.next
        elif current.next.value == current.next.next.value:
          current.next = current.next.next

        else:
          current = current.next
      self = hello
      return self 