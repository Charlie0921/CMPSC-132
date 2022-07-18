
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

