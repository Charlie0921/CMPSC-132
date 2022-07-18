import random 

class Course:
    '''
        >>> c1 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c2 = Course('CMPSC360', 'Discrete Mathematics', 3)
        >>> c1 == c2
        False
        >>> c3 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c1 == c3
        True
        >>> c1
        CMPSC132(3): Programming in Python II
        >>> c2
        CMPSC360(3): Discrete Mathematics
        >>> c3
        CMPSC132(3): Programming in Python II
        >>> c1 == None
        False
        >>> print(c1)
        CMPSC132(3): Programming in Python II
    '''
    def __init__(self, cid, cname, credits):
        # YOUR CODE STARTS HERE
        self.cid = cid
        self.cname = cname
        self.credits = credits
        


    def __str__(self):
        # YOUR CODE STARTS HERE
        return f"{self.cid}({self.credits}): {self.cname}"

    __repr__ = __str__

    def __eq__(self, other):
        # YOUR CODE STARTS HERE
        isEq = True
        if isinstance(other, Course):
          if self.cid != other.cid:
            isEq = False
        else:
          isEq = False
        
        return isEq

if __name__=='__main__':
    import doctest
    doctest.testmod()  # OR
    #doctest.run_docstring_examples(Course, globals(), name='HW22',verbose=True) # replace Course for the class name you want to test
  
class Catalog:
    ''' 
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3, 400)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3, 200)
        'Course added successfully'
        >>> C.courseOfferings
        {'CMPSC132': (CMPSC132(3): Programming in Python II, 400), 'CMPSC360': (CMPSC360(3): Discrete Mathematics, 200)}
        >>> C.removeCourse('CMPSC360')
        'Course removed successfully'
        >>> C.courseOfferings
        {'CMPSC132': (CMPSC132(3): Programming in Python II, 400)}
        >>> isinstance(C.courseOfferings['CMPSC132'][0], Course)
        True
    '''

    def __init__(self):
        # YOUR CODE STARTS HERE
        self.courseOfferings = {}

    #{'CMPSC132': (CMPSC132(3): Programming in Python II, 400), 'CMPSC360': (CMPSC360(3): Discrete Mathematics, 200)}
      
    def addCourse(self, cid, cname, credits, capacity):
        # YOUR CODE STARTS HERE
        #Check if the course is already in our dict
        #Create a course object using the inputs
        #Add new course to the dictionary with ID as a key and value as tuple of the course and capacity
        #x = d.pop("key") -> has to save it in a variable, it has to be a key not value
        if cid not in self.courseOfferings.keys(): 

          course = Course(cid, cname, credits)
          self.courseOfferings[cid] = (course, capacity)
          return "Course added successfully"
        
        else:
          return "Course already added"

    def removeCourse(self, cid):
      del self.courseOfferings[cid]
      return "Course removed successfully"


class Semester:
    '''
        >>> cmpsc131 = Course('CMPSC131', 'Programming in Python I', 3)
        >>> cmpsc132 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> math230 = Course("MATH 230", 'Calculus', 4)
        >>> phys213 = Course("PHYS 213", 'General Physics', 2)
        >>> econ102 = Course("ECON 102", 'Intro to Economics', 3)
        >>> phil119 = Course("PHIL 119", 'Ethical Leadership', 3)
        >>> semester = Semester(1)
        >>> semester
        No courses
        >>> semester.addCourse(cmpsc132)
        >>> isinstance(semester.courses['CMPSC132'], Course)
        True
        >>> semester.addCourse(math230)
        >>> semester
        CMPSC132, MATH 230
        >>> semester.isFullTime
        False
        >>> semester.totalCredits
        7
        >>> semester.addCourse(phys213)
        >>> semester.addCourse(econ102)
        >>> semester.addCourse(econ102)
        'Course already added'
        >>> semester.addCourse(phil119)
        >>> semester.isFullTime
        True
        >>> semester.dropCourse(phil119)
        >>> semester.addCourse(Course("JAPNS 001", 'Japanese I', 4))
        >>> semester.totalCredits
        16
        >>> semester.dropCourse(cmpsc131)
        'No such course'
        >>> semester.courses
        {'CMPSC132': CMPSC132(3): Programming in Python II, 'MATH 230': MATH 230(4): Calculus, 'PHYS 213': PHYS 213(2): General Physics, 'ECON 102': ECON 102(3): Intro to Economics, 'JAPNS 001': JAPNS 001(4): Japanese I}
    '''

    def __init__(self, sem_num):
      self.sem_num = sem_num
      self.courses = {}
      pass

    def __str__(self):
        # YOUR CODE STARTS HERE
        # combine all the cid with commas -> .join methods 
        #HINT: Think about the . join methods
      if len(self.courses) == 0:
        return "No courses"
      else:
        keys = self.courses.keys()
        keys = list(keys)
        keys = ", ".join(keys)
        return keys

    __repr__ = __str__

    def addCourse(self, course):
      cid = course.cid
      if cid not in self.courses.keys():
        self.courses[cid] = course
      else:
        return 'Course already added'
      

    def dropCourse(self, course):
        # YOUR CODE STARTS HERE
        #same as other dropcourse
      cid = course.cid
      if cid in self.courses.keys():
        self.courses.pop(cid)
      else:
        return "No such course"



    @property
    def totalCredits(self):
      #'CMPSC132': CMPSC132(3): Programming in Python II
      crd = 0
      for cid in self.courses:
        cred = self.courses[cid].credits
        crd += cred
      return crd
        
      
      
      
      pass
        # YOUR CODE STARTS HERE
        #iterate through out dictionary and at each step, access the course object's credits attribute and add it to a counting sum


    @property
    def isFullTime(self):
        # YOUR CODE STARTS HERE
        # call total credits
      credit = self.totalCredits

      isFullTime = False
      if credit >= 12:
        isFullTime = True
      
      return isFullTime
      
      print(credit)


class Loan:
    '''
        >>> import random
        >>> random.seed(2)  # Setting seed to a fixed value, so you can predict what numbers the random module will generate
        >>> first_loan = Loan(4000)
        >>> first_loan
        Balance: $4000
        >>> first_loan.loan_id
        17412
        >>> second_loan = Loan(6000)
        >>> second_loan.amount
        6000
        >>> second_loan.loan_id
        22004
        >>> third_loan = Loan(1000)
        >>> third_loan.loan_id
        21124
    '''
    

    def __init__(self, amount):
        # YOUR CODE STARTS HERE
        #call the method get Loan ID no defining as instance variable
      self.loan_id = random.randint(10000,99999)
      self.amount = amount
        


    def __str__(self):
        # YOUR CODE STARTS HERE
      return f'Balance: ${self.amount}'

    __repr__ = __str__


    @property
    def __getloanID(self):
        # YOUR CODE STARTS HERE
        # randint, randrange
        #when you are using a module in python -> doesn't work as functions
      return f'{self.loan_id}'

if __name__=='__main__':
    import doctest
    doctest.testmod()  # OR
    #doctest.run_docstring_examples(Course, globals(), name='HW22',verbose=True) # replace Course for the class name you want to test