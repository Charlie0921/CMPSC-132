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
  

if __name__ == "__main__":
    import doctest
    doctest.testmod()

