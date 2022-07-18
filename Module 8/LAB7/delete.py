# LAB7
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement


class MinBinaryHeap:
    '''
        >>> h = MinBinaryHeap()
        >>> h.insert(10)
        >>> h.insert(5)
        >>> h
        [5, 10]
        >>> h.insert(14)
        >>> h._heap
        [5, 10, 14]
        >>> h.insert(9)
        >>> h
        [5, 9, 14, 10]
        >>> h.insert(2)
        >>> h
        [2, 5, 14, 10, 9]
        >>> h.insert(11)
        >>> h
        [2, 5, 11, 10, 9, 14]
        >>> h.insert(14)
        >>> h
        [2, 5, 11, 10, 9, 14, 14]
        >>> h.insert(20)
        >>> h
        [2, 5, 11, 10, 9, 14, 14, 20]
        >>> h.insert(20)
        >>> h
        [2, 5, 11, 10, 9, 14, 14, 20, 20]
        >>> h.getMin
        2
        >>> h._leftChild(1)
        5
        >>> h._rightChild(1)
        11
        >>> h._parent(1)
        >>> h._parent(6)
        11
        >>> h._leftChild(6)
        >>> h._rightChild(9)
        >>> h.deleteMin()
        2
        >>> h._heap
        [5, 9, 11, 10, 20, 14, 14, 20]
        >>> h.deleteMin()
        5
        >>> h
        [9, 10, 11, 20, 20, 14, 14]
        >>> len(h)
        7
        >>> h.getMin
        9
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
        # YOUR CODE STARTS HERE
        if len(self._heap) == 0:
            return None
        else:
            return self._heap[0]

    def _parent(self, index):
        # YOUR CODE STARTS HERE
        parent = (index // 2) - 1
        if parent <= len(self._heap) - 1 and parent >= 1:
            return self._heap[parent]
        else:
            return None

    def _leftChild(self, index):
        # YOUR CODE STARTS HERE
        left = (index * 2) - 1
        if left <= len(self._heap) - 1:
            return self._heap[left]
        else:
            return None

    def _rightChild(self, index):
        # YOUR CODE STARTS HERE
        right = (index * 2)
        if right <= len(self._heap) - 1:
            return self._heap[right]

    def insert(self, item):
        # YOUR CODE STARTS HERE
        #insert item into first available space in heap
        #Begin percolation with 2 stopping conditions(1. if there isn't a parent node anymore, 2. comparing the parent node is smaller than children) use while loop

        #swap values while percolating and update current item pointer
        lst = self._heap
        lst.append(item)
        current = len(lst)
        while current >= 1:
            parent = (current // 2)

            if parent >= 1:
                if lst[current - 1] < lst[parent - 1]:
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
            # YOUR CODE STARTS HERE
            print(self._heap)
            lst = self._heap
            root = lst[0]
            rIndex = len(self._heap)-1
            rightm = lst[rIndex]
            lst[0] = rightm
            lst.pop(rIndex)
            print(self._heap)
            return self.deleteHelper(root, 1)


    def deleteHelper(self, root, current):
      lst = self._heap
      left = self._leftChild(current)
      right = self._rightChild(current)
      now = lst[current - 1]
      print("current",current)
      print("info",now,left,right)
      if left == None and right == None:
        print("c1")
        print("h",lst)
        return root

      elif left != None and right != None:
        if left > now and right > now:
          print("c2")
          print("h",lst)
          return root
        elif left <= right:
            lst[current - 1],lst[current * 2 - 1] = lst[current * 2 - 1], lst[current - 1]
            print("c5")
            print("h",lst)
            return self.deleteHelper(root, current * 2)
        elif left > right:
          lst[current - 1],lst[current * 2] = lst[current * 2], lst[current - 1]
          print("c6")
          print("h",lst)
          return self.deleteHelper(root, current * 2 + 1)
      else:
        if left == None and right < current:
          lst[current - 1],lst[current * 2] = lst[current * 2], lst[current - 1]
          print("c3")
          print("h",lst)
          return self.deleteHelper(root, current * 2 + 1)
        elif right == None and left > current:
          lst[current - 1],lst[current * 2 - 1] = lst[current * 2 - 1], lst[current - 1]
          print("c4")
          print("h",lst)
          return self.deleteHelper(root, current * 2)
        


            # Replace the value at the root with the value of the rightmost item in the lowest level
            # Delete the last item in our heap
            # Percolate down considering the 2 stopping conditions
            # 1. min heap propery is satisfied
            # 2. in order to make the list -> swap the values at the parent
            # Compare the values of the children, keeping in mind the possibility of only having 1 child
            # swap with the smaller child
            # Return the min we deleted
        

def heapSort(numList):
    '''
       >>> heapSort([9,1,7,4,1,2,4,8,7,0,-1,0])
       [-1, 0, 0, 1, 1, 2, 4, 4, 7, 7, 8, 9]
       >>> heapSort([-15, 1, 0, -15, -15, 8 , 4, 3.1, 2, 5])
       [-15, -15, -15, 0, 1, 2, 3.1, 4, 5, 8]
    '''
    # YOUR CODE STARTS HERE
    pass
    # create a heap and insert all items into heap
    # call deleteMin and store in a list until heap is empty
    # Can't use sorted method
