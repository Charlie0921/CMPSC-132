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
        if self.root is None: #Creates a Node whose value is a dictionary where key is sorted string, value is list that contains string
            dic = {}
            key = sorted(value)
            key = "".join(key)
            dic[key] = [value]
            self.root=Node(dic)
        else:
            self._insert(self.root, value)


    def _insert(self, node, value):
      
        sortStr = sorted(value) #sort string
        sortStr = "".join(sortStr)
        dicKey = list(node.value.keys())[0]
      
        if sortStr < dicKey: #when the sorted word is less than dictionary key
          if node.left == None:
            dic1 = {}
            dic1[sortStr] = [value]
            node.left = Node(dic1)
          else:
            self._insert(node.left,value)

        elif sortStr > dicKey: #when the sorted word is greater than dictionary key
          if node.right == None:
            dic2 = {}
            dic2[sortStr] = [value]
            node.right = Node(dic2)
          else: 
            self._insert(node.right, value)

        else: #when the sorted word is equal to dictionary key
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

class Anagrams:
    '''
       - # Verify class has _bst attribute  
        >>> x = Anagrams(5)
        >>> '_bst' in x.__dict__    
        True
        >>> isinstance(x.__dict__.get('_bst'), BinarySearchTree)
        True
        >>> x = Anagrams(6)
        >>> x.create('words_medium.txt')
        >>> x.getAnagrams('tap')
        'No match'
        >>> x.getAnagrams('arm')
        'No match'
        >>> x.getAnagrams('whiter')
        ['whiter', 'wither', 'writhe']
    '''
    
    def __init__(self, word_size):
        # -YOUR CODE STARTS HERE
        self._bst = BinarySearchTree()
        self.word_size = word_size

    def create(self, file_name):
        # -YOUR CODE STARTS HERE
        with open(file_name) as f: #reads the contents of give files
          contents = f.read()
          lst = contents.split() #puts all the words into a list
        
      
        for item in lst:
          if len(item) <= self.word_size: #check if the lenght of word is too big
            self._bst.insert(item) #if not, insert word into BST

  
    def getAnagrams(self, word):
        # -YOUR CODE STARTS HERE
        if self._bst.isEmpty():
          return None
        else:
          return self._getHelper(self._bst.root, word)
          
    def _getHelper(self, node, word): #helper method for getAnagrams
      word = sorted(word)
      word = "".join(word)
      if node is not None:
        if list(node.value.keys())[0] == word: #if the are equal, return the list
          return node.value[word]
        elif list(node.value.keys())[0] > word: #if the key is greater than sorted word, traverse left
          return self._getHelper(node.left, word)
        elif list(node.value.keys())[0] < word:
          return self._getHelper(node.right, word) #if the key is smaller than sorted word, traverse right
      else: #if the sorted word is not found, return "No match"
        return "No match"

        
