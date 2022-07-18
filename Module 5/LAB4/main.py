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


    def isEmpty(self):
        return self.head == None

    def __len__(self):
        count=0
        current=self.head
        while current:
            current=current.next
            count+=1
        return count

                
    def add(self, value):
      newNode=Node(value)
      
      if self.isEmpty(): #set head and tail when the list is empty
        self.head=newNode
        self.tail=newNode
      else: 
        current = self.head
        if value <= self.head.value: #check if the number is less or equal to head
            newNode.next=self.head
            self.head=newNode

        else:
          while current.next is not None:
           
            if current.next.value >= value: #Compare "value" and number in the middle of the list
              newNode.next = current.next
              current.next = newNode
              
              return None
            current = current.next
            
          if current.value == self.tail.value: #If the number is the largest
              current.next = newNode
              self.tail = newNode
              

    def replicate(self):
      hello = SortedLinkedList() #create new object to duplicate list
      current = self.head

      while current is not None: #put the numbers in the new list
        hello.add(current.value)
        current = current.next

      current = hello.head
      
          
      while current is not None:
        if current.value < 0 or isinstance(current.value, float): #if the number is negative or float, repeat once
          new = Node(current.value)
          new.next = current.next
          current.next = new
          current = current.next
         
        elif current.value > 0: #if the number is positive, repeats value number of times
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
    
      current = self.head

      
      while current.next.next is not None:
  
        if self.head.value == self.head.next.value: #head changes if the values of head and head.next is equal
          self.head = self.head.next
         
          current = current.next
        elif current.next.value == current.next.next.value: #if the values in the middle are equal, the number is removed
          current.next = current.next.next

        else: #if anything else, change current
          current = current.next
      