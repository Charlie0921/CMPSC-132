# LAB3
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement
# All functions should NOT contain any for/while loops or global variables. Use recursion, otherwise no credit will be given

def get_count(aList, item):
    '''
        >>> get_count([1,4,3.5,'1',3.5, 9, 1, 4, 2], 1)
        2
        >>> get_count([1,4,3.5,'1',3.5, 9, 4, 2], 3.5)  
        2
        >>> get_count([1,4,3.5,'1',3.5, 9, 4, 2], 9)   
        1
        >>> get_count([1,4,3.5,'1',3.5, 9, 4, 2], 'a') 
        0
    '''
    ## YOUR CODE STARTS HERE

    if len(aList) == 0 or item not in aList:
      return 0
      
    elif aList[0] == item:
      new = aList[1:]
      return 1 + get_count(new, item)
    else:
      new = aList[1:]
      return get_count(new, item)


def replace(numList, old, new):
    '''
        >>> input_list = [1, 7, 5.6, 3, 2, 4, 1, 9]
        >>> replace(input_list, 1, 99.9)
        [99.9, 7, 5.6, 3, 2, 4, 99.9, 9]
        >>> input_list
        [1, 7, 5.6, 3, 2, 4, 1, 9]
        >>> replace([1,7, 5.6, 3, 2, 4, 1, 9], 5.6, 777) 
        [1, 7, 777, 3, 2, 4, 1, 9]
        >>> replace([1,7, 5.6, 3, 2, 4, 1, 9], 8, 99)    
        [1, 7, 5.6, 3, 2, 4, 1, 9]
    '''
    ## YOUR CODE STARTS HERE
    pass
    if len(numList) == 0:
      return []

    elif numList[0] != old:
      lst = [numList[0]]
      numLst = numList[1:]
      now = replace(numLst, old, new)

      return lst + now
      
    elif numList[0] == old:
      old1 = new
      lst = [old1]
      numLst = numList[1:]
      now = replace(numLst, old, new)

      return lst + now


def cut(aList):
    '''
        >>> cut([7, 4, 0])
        [7, 4, 0]
        >>> myList=[7, 4, -2, 1, 9]
        >>> cut(myList)   # Found(-2) Delete -2 and 1
        [7, 4, 9]
        >>> myList
        [7, 4, -2, 1, 9]
        >>> cut([-4, -7, -2, 1, 9]) # Found(-4) Delete -4, -7, -2 and 1
        [9]
        >>> cut([-3, -4, 5, -4, 1])  # Found(-3) Delete -2, -4 and 5. Found(-4) Delete -4 and 1
        []
        >>> cut([5, 7, -1, 6, -3, 1, 8, 785, 5, -2, 1, 0, 42]) # Found(-1) Delete -1. Found(-3) Delete -3, 1 and 8. Found(-2) Delete -2 and 0
        [5, 7, 6, 785, 5, 0, 42]
    '''
    ## YOUR CODE STARTS HERE
    if len(aList) == 0:
      return []
      
    elif aList[0] >= 0:
      lst = [aList[0]]
      now = cut(aList[1:])
      return lst + now
      
    elif aList[0] < 0:
      abso = abs(aList[0])
      now = cut(aList[abso:])
      return now



def neighbor(n):
    '''
        >>> neighbor(24680)
        24680
        >>> neighbor(2222466666678)
        24678
        >>> neighbor(0)
        0
        >>> neighbor(22224666666782)
        246782
        >>> neighbor(2222466666625)
        24625
    '''
    ## YOUR CODE STARTS HERE
    if n == 0:
      return 0
  
    elif (n%100)//10 == n%10:
      return neighbor(n//10)
      
    elif (n%100)//10 != n%10:
      first = n % 10
      new = neighbor(n//10)*10
      return first + new

if __name__ == "__main__":
    import doctest
    doctest.testmod()

