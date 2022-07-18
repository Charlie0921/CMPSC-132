import random


class Fibonacci:
    """
        >>> fib_seq = Fibonacci()
        >>> fib_seq
        <Fibonacci object>, value = 0
        >>> fib_seq.next()
        <Fibonacci object>, value = 1
        >>> fib_seq.next().next()
        <Fibonacci object>, value = 1
        >>> fib_seq.next().next().next()
        <Fibonacci object>, value = 2
        >>> fib_seq.next().next().next()
        <Fibonacci object>, value = 2
        >>> fib_seq.next().next().next().next()
        <Fibonacci object>, value = 3
        >>> fib_seq.next().next().next().next().next()
        <Fibonacci object>, value = 5
        >>> fib_seq.next().next().next().next().next().next()
        <Fibonacci object>, value = 8
        >>> other_fib_seq = Fibonacci()
        >>> other_fib_seq
        <Fibonacci object>, value = 0
        >>> other_fib_seq.next().next().next().next().next()
        <Fibonacci object>, value = 5
        >>> fib_seq.next().next().next().next().next().next()
        <Fibonacci object>, value = 8
    """
    def __init__(self):
        self.start = 0

    def next(self):

        #--- YOUR CODE STARTS HERE
        new = Fibonacci()
  

        previous = self.start

        if previous == 0:
            present = 1
        else:
            present = self.present

        result = previous + present
        #print(previous,present, result)

        new.present = result
        new.start = present
        

        return new

    def __repr__(self):
        return f"<Fibonacci object>, value = {self.start}"



if __name__=='__main__':
    import doctest
    doctest.testmod()  # OR
    #doctest.run_docstring_examples(Fibonacci, globals(), name='LAB2',verbose=True) # replace Fibonacci for the class name you want to test

