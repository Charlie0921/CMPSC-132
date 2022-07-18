class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def hell0(self):
      return self.x


class Line: 
    ''' 
            >>> p1 = Point2D(-7, -9)
            >>> p2 = Point2D(1, 5.6)
            >>> line1 = Line(p1, p2)
            >>> line1.getDistance
            16.648
            >>> line1.getSlope
            1.825
            >>> line1
            y = 1.825x + 3.775
            >>> line2 = line1*4
            >>> line2.getDistance
            66.592
            >>> line2.getSlope
            1.825
            >>> line2
            y = 1.825x + 15.1
            >>> line1
            y = 1.825x + 3.775
            >>> line3 = 4*line1
            >>> line3
            y = 1.825x + 15.1
            >>> line1==line2
            False
            >>> line3==line2
            True
            >>> line5=Line(Point2D(6,48),Point2D(9,21))
            >>> line5
            y = -9.0x + 102.0
            >>> line5==9
            False
            >>> line6=Line(Point2D(2,6), Point2D(2,3))
            >>> line6.getDistance
            3.0
            >>> line6.getSlope
            inf
            >>> isinstance(line6.getSlope, float)
            True
            >>> line6
            Undefined
            >>> line7=Line(Point2D(6,5), Point2D(9,5))
            >>> line7.getSlope
            0.0
            >>> line7
            y = 5.0
        '''
    def __init__(self, point1, point2):
        #--- YOUR CODE STARTS HERE
        self.p1x = point1.x 
        self.p1y = point1.y
        self.p2x = point2.x
        self.p2y = point2.y


    #--- YOUR CODE STARTS HERE
    @property
    def getDistance(self):
      deltax = self.p1x - self.p2x
      deltay = self.p1y - self.p2y

      distance = ((deltax)**2 + (deltay)**2)**(1/2)

      self.distance = round(distance,3)
      return self.distance

    #--- YOUR CODE STARTS HERE
    @property
    def getSlope(self):
      deltax = self.p1x - self.p2x
      deltay = self.p1y - self.p2y

      if deltax != 0:
        slope = deltay / deltax
        if deltay == 0:
          self.slope = abs(slope)
        else:
          self.slope = round(slope,3)

      else:
        self.slope = float("inf")

      return self.slope

    #--- YOUR CODE CONTINUES HERE
    def __str__(self):

      if self.getSlope != float("inf"):
        b = round(self.p1y - self.getSlope * self.p1x, 3)
        if self.getSlope == 0:
          return f"y = {b}"
        elif b == 0:
          return f"y = {self.getSlope}x"

        elif b > 0:
          return f"y = {self.getSlope}x + {b}"

        elif b < 0:
          return f"y = {self.getSlope}x - {abs(b)}"
      else:
        return 'Undefined'
      
    __repr__ = __str__

    def __mul__(self,num):
      new = Line(Point2D(self.p1x,self.p1y), Point2D(self.p2x,self.p2y))
      new.p1x = self.p1x * num
      new.p1y = self.p1y * num
      new.p2x = self.p2x * num
      new.p2y = self.p2y * num
      new = Line(Point2D(new.p1x,new.p1y), Point2D(new.p2x,new.p2y))
      
      return new
    
    def __rmul__(self,num):
      new = Line(Point2D(self.p1x,self.p1y), Point2D(self.p2x,self.p2y))
      new.p1x = self.p1x * num
      new.p1y = self.p1y * num
      new.p2x = self.p2x * num
      new.p2y = self.p2y * num
      new = Line(Point2D(new.p1x,new.p1y), Point2D(new.p2x,new.p2y))
      
      return new

    def __eq__(self,other):
      isEq = False
      if not isinstance(other,Line):
        return isEq
      else:
        if self.p1x == other.p1x and self.p1y == other.p1y :
          if self.p2x == other.p2x and self.p2y == other.p2y:
            isEq = True
            return isEq
          else:
            return isEq
        else:
          return isEq
  
#line1 = Line(Point2D(1,2),Point2D(2,3))

if __name__=='__main__':
    import doctest
    doctest.testmod()  

    