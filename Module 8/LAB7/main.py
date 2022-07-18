# LAB7
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement


class MinBinaryHeap:
    '''
        >>> h = MinBinaryHeap()
        >>> h.insert(10)
        >>> h.insert(5)
        >>> h.insert(14)
        >>> h.insert(9)
        >>> h.insert(2)
        >>> h.insert(11)
        >>> h.insert(14)
        >>> h.insert(20)
        >>> h.insert(20)
        >>> h._parent(6)
        11
        >>> h._leftChild(2)
        10
        >>> h._rightChild(2)
        9
        >>> h._heap
        [2, 5, 11, 10, 9, 14, 14, 20, 20]
        >>> h.deleteMin()
        2
        >>> h.getMin
        5
        >>> h._heap
        [5, 9, 11, 10, 20, 14, 14, 20]
        >>> len(h)
        8
    '''
    def __init__(self):  # YOU ARE NOT ALLOWED TO MODIFY THE CONSTRUCTOR
        self._heap = []

    def __str__(self):
        return f'{self._heap}'

    __repr__ = __str__

    def __len__(self):
        return len(self._heap)

    @property
    def getMin(self):
        # get value in index 0 of heap
        if len(self._heap) == 0:
            return None
        else:
            return self._heap[0]

    def _parent(self, index):
        # calculate to get the heap index of parent with the index of current
        parent = (index // 2) - 1
        if parent <= len(self._heap) - 1 and parent >= 1: # 
            return self._heap[parent]
        else:
            return None

    def _leftChild(self, index):
        # calculate to get the heap index of left child with the index of current
        left = (index * 2) - 1
        if left <= len(self._heap) - 1:
            return self._heap[left]
        else:
            return None

    def _rightChild(self, index):
        # calculate to get the heap index of right child with the index of current
        right = (index * 2)
        if right <= len(self._heap) - 1:
            return self._heap[right]

    def insert(self, item):
        lst = self._heap
        lst.append(item) #insert item to the heap
        current = len(lst)
        while current >= 1: 
            parent = (current // 2)

            if parent >= 1: #if there parent node exists
                if lst[current - 1] < lst[parent - 1]: #if there is a parent node greater than children, swap values
                    p1 = lst[parent - 1]
                    c1 = lst[current - 1]

                    lst[current - 1] = p1
                    lst[parent - 1] = c1
            current -= 1

    def deleteMin(self):
        # Remove from an empty heap or a heap of size 1

        if len(self) == 0: 
            return None
        elif len(self) == 1: 
            deleted = self._heap[0]
            self._heap = []
            return deleted
        else:
            # Replace the value at the root with the value of the rightmost item in the lowest level
            lst = self._heap
            root = lst[0]
            rIndex = len(self._heap)-1
            rightm = lst[rIndex]
            lst[0] = rightm
            lst.pop(rIndex)
            return self.deleteHelper(root, 1) #calls the helper for updating heap



    def deleteHelper(self, root, current):
      lst = self._heap
      left = self._leftChild(current)
      right = self._rightChild(current)
      now = lst[current - 1]
    
      if left == None and right == None: #if there are no children, stop recursion by returning root
        return root

      elif left != None and right != None: #if both children exists
        if left > now and right > now: #if parent and children meets min heap property, stop recursion by returning root
          return root
        elif left <= right:
            lst[current - 1],lst[current * 2 - 1] = lst[current * 2 - 1], lst[current - 1]
            return self.deleteHelper(root, current * 2)
        elif left > right:
          lst[current - 1],lst[current * 2] = lst[current * 2], lst[current - 1]
          return self.deleteHelper(root, current * 2 + 1)
      else: #if only one child exists
        if left == None and right < now:
          lst[current - 1],lst[current * 2] = lst[current * 2], lst[current - 1]
          return self.deleteHelper(root, current * 2 + 1)
        elif right == None and left < now:
          lst[current - 1],lst[current * 2 - 1] = lst[current * 2 - 1], lst[current - 1]
          return self.deleteHelper(root, current * 2)
      return root
        
        

def heapSort(numList):
    '''
       >>> heapSort([9,1,7,4,1,2,4,8,7,0,-1,0])
       [-1, 0, 0, 1, 1, 2, 4, 4, 7, 7, 8, 9]
       >>> heapSort([-15, 1, 0, -15, -15, 8 , 4, 3.1, 2, 5])
       [-15, -15, -15, 0, 1, 2, 3.1, 4, 5, 8]
    '''

    new = MinBinaryHeap() #creates a new MinBinaryHeap object
    for item in numList: #insert items in numList into the min binary heap
      new.insert(item)
    
    lst = new._heap
    
    sortLst = []
    while len(lst) > 1: #call deleteMin and store in a list during length of the heap is greater than 1
      a = new.deleteMin()
      sortLst.append(a)
   
    sortLst.append(lst[0]) #add the last number of the heap list into sortLst
     
    return sortLst
