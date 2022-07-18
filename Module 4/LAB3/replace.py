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


if __name__ == "__main__":
    import doctest
    doctest.testmod()


