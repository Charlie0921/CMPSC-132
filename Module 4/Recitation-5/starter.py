# Recitation Activity 5

def hailstone(num):
    '''
        >>> hailstone(10)
        [10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(1)
        [1]
        >>> hailstone(27)
        [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(7)
        [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(19)
        [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    '''
    # -- YOUR CODE STARTS HERE  
    if num == 1: #if the input number is 1, it outputs [1]
      return [1]
    elif num % 2 == 0: #if the input number is even, then it divides num by 2. And then, adds number in the list and sets the number as input
      current = [num]
      num /= 2
      rest = hailstone(int(num))
      return current + rest
      
    elif num % 2 == 1: #if the input number is odd, then it multiplies num by 3 and adds 1. And then, it adds number in the list and sets the number as input
      current = [num]
      num = 3*num + 1
      rest = hailstone(int(num))
      return current + rest
      


if __name__ == "__main__":
    import doctest
    doctest.testmod()



