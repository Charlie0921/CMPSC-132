# HW4
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement
# You might add additional methods to encapsulate and simplify the operations, but they must be
# thoroughly documented


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
        >>> x.insert('mom')  
        >>> x.insert('omm') 
        >>> x.insert('mmo') 
        >>> x.root          
        Node({'mmo': ['mom', 'omm', 'mmo']})
        >>> x.insert('sat')
        >>> x.insert('kind')
        >>> x.insert('ats') 
        >>> x.root.left
        Node({'ast': ['sat', 'ats']})
        >>> x.root.right is None
        True
        >>> x.root.left.right
        Node({'dikn': ['kind']})
    '''

    def __init__(self):
        self.root = None


    # Modify the insert and _insert methods to allow the operations given in the PDF
    # Document all the modifications done
    #***********test this code with the text files Make sure section1 is working correctly before working on section2
    def insert(self, value): 
        if self.root is None:
          #Create a Node whose value is a dict where key is sorted string, value is list that contains string
            dic = {}
            key = sorted(value)
            key = "".join(key)
            dic[key] = [value]
            self.root=Node(dic)
        else:
            self._insert(self.root, value)


    def _insert(self, node, value):
      #sort our string and compare with the key of node.value
      #add a condition for equality where we add this word to the end of the node's list
        #word is less than
        #greater
        #equal 
      
        sortStr = sorted(value)
        sortStr = "".join(sortStr)
        dicKey = list(node.value.keys())[0]
      
        if sortStr < dicKey:
          if node.left == None:
            dic1 = {}
            dic1[sortStr] = [value]
            node.left = Node(dic1)
          else:
            self._insert(node.left,value)

        elif sortStr > dicKey:
          if node.right == None:
            dic2 = {}
            dic2[sortStr] = [value]
            node.right = Node(dic2)
          else:
            self._insert(node.right, value)

        else:
          node.value[dicKey].append(value)

    def isEmpty(self):
        return self.root == None

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

    