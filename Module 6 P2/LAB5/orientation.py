# LAB 5
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return ("Node({})".format(self.value)) 

    __repr__ = __str__


class BinarySearchTree:
    '''
        >>> x=BinarySearchTree()
        >>> x.isEmpty()
        True
        >>> x.insert(9)
        >>> x.insert(4)
        >>> x.insert(11)
        >>> x.insert(2)
        >>> x.insert(5)
        >>> x.insert(10)
        >>> x.insert(9.5)
        >>> x.insert(7)
        >>> x.getMin
        Node(2)
        >>> x.getMax
        Node(11)
        >>> 67 in x
        False
        >>> 9.5 in x
        True
        >>> x.isEmpty()
        False
        >>> x.getHeight(x.root)   # Height of the tree
        3
        >>> x.getHeight(x.root.left.right)
        1
        >>> x.getHeight(x.root.right)
        2
        >>> x.getHeight(x.root.right.left)
        1
        >>> x.printInorder
        2 : 4 : 5 : 7 : 9 : 9.5 : 10 : 11 : 
        >>> new_tree = x.mirror()
        11 : 10 : 9.5 : 9 : 7 : 5 : 4 : 2 : 
        >>> new_tree.root.right
        Node(4)
        >>> x.printInorder
        2 : 4 : 5 : 7 : 9 : 9.5 : 10 : 11 : 
    '''
    def __init__(self):
        self.root = None


    def insert(self, value):
        if self.root is None:
            self.root=Node(value)
        else:
            self._insert(self.root, value)


    def _insert(self, node, value):
        if(value<node.value):
            if(node.left==None):
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:   
            if(node.right==None):
                node.right = Node(value)
            else:
                self._insert(node.right, value)
    
    @property
    def printInorder(self):
        if self.isEmpty(): 
            return None
        else:
            self._inorderHelper(self.root)
        
    def _inorderHelper(self, node):
        if node is not None:
            self._inorderHelper(node.left) 
            print(node.value, end=' : ') 
            self._inorderHelper(node.right)         


    def mirror(self):
        # Creates a new BST that is a mirror of self: 
        #    Elements greater than the root are on the left side, and smaller values on the right side
        # Do NOT modify any given code
        if self.root is None:
            return None
        else:
            newTree = BinarySearchTree()
            newTree.root = self._mirrorHelper(self.root)
            newTree.printInorder
            return newTree
        




    def isEmpty(self):
        # YOUR CODE STARTS HERE, check the init method
      if self.root == None:
        return True
      else:
        return False
      

    def _mirrorHelper(self, node):
        # YOUR CODE STARTS HERE
        #using the mirror method, make new left and right(recursively traversing)
        #1. we need a base case to tell when to stop, Initialize a base case(None)
        #*****we are not modifying the old tree
        #2. create a new Node with the same value of old Node
        #3. Recusively call, new left attribute = old right attribute, new right attribute = old left attribute
        #*****Set left and right attributes to the recursive calls of old right and left attributes
        
        pass



    @property
    def getMin(self): 
        # YOUR CODE STARTS HERE
        #minimum, left most node
        #maximum, right most node
        #start at the root and continously iterate to the left until we cannot continue.
        #return the value of this leftmost Node 
      pass



    @property
    def getMax(self): 
      #start at the root and continously iterate to the right until we cannot continue.
      #return the value of this rightmost Node 
        pass
      



    def __contains__(self,value):
        # YOUR CODE STARTS HERE
        pass

    #def containshelper -> dont' necessary
    #recursion over complicates it -> use iteration
    #check base case (if doing recursion) or create stopping condition (if using iteration)
    #start iteration/recursion at the root
    #compare value with current Node's value (if they are equal, return True)
    #Iterate or make a recursive call to left or right subtree depending on the value



    def getHeight(self, node):
        # YOUR CODE STARTS HERE
      #return maximum between left and right heights
      # can do the recursion directly
      # create a counter to count how many edges
      leftCount = 1
      while node != None:
        leftCount += 1
        node = node.left
      print("l",leftCount)
      rightCount = 1
      while node != None:
        rightCount += 1
        node = node.right
      print("r",rightCount)

      



