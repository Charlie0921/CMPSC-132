def sumSquares(numList):
    """
        >>> sumSquares([2, 4, 5, 6, 7, 8, 10, -4])
        96
        >>> sumSquares([0, 89, -4, -62, -36, 12, 5])
        1456
    """
    if len(numList)==0:
        return 0
    else:
        if numList[0]%4==0:
            return numList[0]**2 + sumSquares(numList[1:])
        else:
            return sumSquares(numList[1:])


def isPrime(num, i = 2):
    '''
        >>> isPrime(5)
        True
        >>> isPrime(1)
        False
        >>> isPrime(0)
        False
        >>> isPrime(85)
        False
    '''     
    if num<=1:
        return False
    if num==i:
        return True
    if num%i==0:
        return False
    return isPrime(num, i+1)



def isPrime(num):
    '''
        >>> isPrime(5)
        True
        >>> isPrime(1)
        False
        >>> isPrime(0)
        False
        >>> isPrime(85)
        False
    '''     
    if num<=1:
        return False
    return helper_isPrime(num,2)


def helper_isPrime(num, i):
    if num==i:
        return True
    if num%i==0:
        return False
    return helper_isPrime(num, i+1)



def hasNumbers(num1, num2):
    """
        >>> hasNumbers(357, 12345678)
        True
        >>> hasNumbers(753, 12345678)
        False
        >>> hasNumbers(357, 37)
        False
    """
    if num1 == num2:
        return True
    if num1 > num2:
        return False
    if num1 % 10 == num2 % 10:
        return hasNumbers(num1 // 10, num2 // 10)
    else:
        return hasNumbers(num1, num2 // 10)


def getVowels(txt):
    """
        >>> getVowels('Hello there!')
        'eoee'
        >>> getVowels('7 days until breAk')
        'auiea'
    """
    if len(txt)==0:
        return ''
    else:
        if txt[0] in 'aeiouAEIOU':
            return txt[0].lower() + getVowels(txt[1:])
        else:
            return getVowels(txt[1:])
