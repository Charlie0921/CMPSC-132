    def next(self):

        #--- YOUR CODE STARTS HERE
        new = Fibonacci()

        previous = self.start

        if previous == 0:
            present = 1
        else:
            present = self.present

        self.result = previous + present

        self.present = self.result
        self.start = present

        return new
##################################

    def next(self):

        #--- YOUR CODE STARTS HERE
        new = Fibonacci()

        previous = new.start

        if previous == 0:
            present = 1
        else:
            present = new.present

        new.result = previous + present

        new.present = new.result
        new.start = present

        return new

##############normal#######################
    def next(self):
        #--- YOUR CODE STARTS HERE
        previous = self.start
     
        if previous == 0:
          present = 1
        else:
          present = self.present

        result = previous + present
        
        self.present = result
        self.start = present
        
        return self