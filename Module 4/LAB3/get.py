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


if __name__ == "__main__":
    import doctest
    doctest.testmod()


