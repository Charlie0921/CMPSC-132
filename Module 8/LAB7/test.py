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
          
            lst = self._heap
            root = lst[0]
            rIndex = len(self._heap)-1
            rightm = lst[rIndex]
            lst[0] = rightm
            lst.pop(rIndex)
            
            return self.deleteHelper(root, 1)


    def deleteHelper(self, root, current):
      lst = self._heap
      left = self._leftChild(current)
      right = self._rightChild(current)
      now = lst[current - 1]
      
      if left == None and right == None:
        
        return root

      elif left != None and right != None:
        if left > now and right > now:
          
          return root
        elif left <= right:
            lst[current - 1],lst[current * 2 - 1] = lst[current * 2 - 1], lst[current - 1]
            
            return self.deleteHelper(root, current * 2)
        elif left > right:
          lst[current - 1],lst[current * 2] = lst[current * 2], lst[current - 1]
          
          return self.deleteHelper(root, current * 2 - 1)
      else:
        if left == None and right < current:
          lst[current - 1],lst[current * 2] = lst[current * 2], lst[current - 1]
          
          return self.deleteHelper(root, current * 2 - 1)
        elif right == None and left > current:
          lst[current - 1],lst[current * 2 - 1] = lst[current * 2 - 1], lst[current - 1]
         
          return self.deleteHelper(root, current * 2)