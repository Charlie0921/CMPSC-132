            current = 1
            while current < len(lst):
              print(current)
              left = self._leftChild(current)
              right = self._rightChild(current)
              now = lst[current - 1]
              if left == None and right == None: #left and right is none
                print(1)
                return root

              elif left != None or right != None:
                if left > now and right > now:
                  print(2)
                  return root
                elif left == None and right < current:
                  lst[current - 1],lst[current * 2] = lst[current * 2], lst[current - 1]
                  print(3)
                  current = current * 2
                elif right == None and left > current:
                  lst[current - 1],lst[current * 2 - 1] = lst[current * 2 - 1], lst[current - 1]
                  print(4)
                  current = current * 2 + 1