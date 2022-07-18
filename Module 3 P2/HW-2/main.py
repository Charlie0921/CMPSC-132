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
        self.cid = cid
        self.cname = cname
        self.credits = credits
        


    def __str__(self): #print formated course name with course id, credits, and course name
        return f"{self.cid}({self.credits}): {self.cname}"

    __repr__ = __str__

    def __eq__(self, other):
        isEq = True
        if isinstance(other, Course): #check if other is Course object
          if self.cid != other.cid: #if self and other has same course id, they are the same
            isEq = False
        else:
          isEq = False
        
        return isEq

  
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
        self.courseOfferings = {}


    def addCourse(self, cid, cname, credits, capacity):
       
        if cid not in self.courseOfferings.keys(): #check if the course is already in the dictionary
          course = Course(cid, cname, credits)
          self.courseOfferings[cid] = (course, capacity) #input key(course id) and values(course, capacity) inside of the dictionary
          return "Course added successfully"
        
        else: #output this statement if course already exists
          return "Course already added"

    def removeCourse(self, cid):
      del self.courseOfferings[cid] #deletes the course
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
      
      if len(self.courses) == 0: #check if there is courses inside of the dictionary
        return "No courses"
      else: #output the course ids
        keys = self.courses.keys()
        keys = list(keys)
        keys = ", ".join(keys)
        return keys

    __repr__ = __str__

    def addCourse(self, course): #adds courses to the self.courses dictionary
      cid = course.cid
      if cid not in self.courses.keys():
        self.courses[cid] = course
      else:
        return 'Course already added'
  

    def dropCourse(self, course):
     
      cid = course.cid
      if cid in self.courses.keys(): #checks if the course exists in the dictionary and then removes it
        self.courses.pop(cid)
      else:
        return "No such course"



    @property
    def totalCredits(self):
      crd = 0
      for cid in self.courses: #calculate total credits with the courses inside of self.courses
        cred = self.courses[cid].credits
        crd += cred
      return crd
       
    @property
    def isFullTime(self):
       
      credit = self.totalCredits #call totla credits and decide if it;s fulltime or not

      isFullTime = False
      if credit >= 12:
        isFullTime = True
      
      return isFullTime
    
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
      self.loan_id = random.randint(10000,99999) #set loand Id with a random number between 10000 and 99999
      self.amount = amount
        


    def __str__(self):
      return f'Balance: ${self.amount}' #outputs string that shows the amount

    __repr__ = __str__


    @property
    def __getloanID(self):
      return f'{self.loan_id}' #outputs loan_id



class Person:
    '''
        >>> p1 = Person('Jason Lee', '204-99-2890')
        >>> p2 = Person('Karen Lee', '247-01-2670')
        >>> p1
        Person(Jason Lee, ***-**-2890)
        >>> p2
        Person(Karen Lee, ***-**-2670)
        >>> p3 = Person('Karen Smith', '247-01-2670')
        >>> p3
        Person(Karen Smith, ***-**-2670)
        >>> p2 == p3
        True
        >>> p1 == p2
        False
    '''

    def __init__(self, name, ssn):
      self.name = name
      self.ssn = ssn
      

    #*****create a private attribute - SSN(put at the beginning of the name)
    


    def __str__(self):

      last = str(self.ssn)
      last = last[-4:] #access last for digits
      self.ssn = f'***-**-{last}'
      return f'Person({self.name}, {self.ssn})' #leaves the last for digits and make all other numbers *
        

    __repr__ = __str__

    def get_ssn(self):
      return self.ssn #return social security number


    def __eq__(self, other): #see if ssn of self and other is equal
      isEq = True
      if self.ssn != other.ssn:
        isEq = False
      return isEq


class Staff(Person):
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3, 400)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3, 200)
        'Course added successfully'
        >>> s1 = Staff('Jane Doe', '214-49-2890')
        >>> s1.getSupervisor
        >>> s2 = Staff('John Doe', '614-49-6590', s1)
        >>> s2.getSupervisor
        Staff(Jane Doe, 905jd2890)
        >>> s1 == s2
        False
        >>> s2.id
        '905jd6590'
        >>> p = Person('Jason Smith', '221-11-2629')
        >>> st1 = s1.createStudent(p)
        >>> isinstance(st1, Student)
        True
        >>> s2.applyHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        'Unsuccessful operation'
        >>> s2.removeHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        >>> st1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> st1.semesters
        {1: CMPSC132}
        >>> s1.applyHold(st1)
        'Completed!'
        >>> st1.enrollCourse('CMPSC360', C, 1)
        'Unsuccessful operation'
        >>> st1.semesters
        {1: CMPSC132}
    '''
    def __init__(self, name, ssn, supervisor=None):
      self.supervisor = supervisor
      self.name = name
      self.ssn = ssn



    def __str__(self):
        return f'Staff({self.name}, {self.id})' #print staff information with names and ids

    __repr__ = __str__


    @property
    def id(self):
        
      upper = []
      for item in self.name: #collect the uppercase letters to make initials
        for i in range(60,91):
          if item == chr(i):
            upper.append(item)

      upper = "".join(upper)
      upper = upper.lower()

      ssn= str(self.ssn)
      ssn = ssn[-4:]
      self.ID = f'905{upper}{ssn}' #finalize the id by adding initiials, ssn and 905 together
      return self.ID
  
    @property  
  
    def getSupervisor(self):
      return self.supervisor #return supervisor
   

    def setSupervisor(self, new_supervisor):
      if isinstance(new_supervisor, Staff):
        self.supervisor = new_supervisor #set new_supervisor as supervisor
        return "Completed!"



    def applyHold(self, student): #check if student is Student object and then make student.hold true
    
      if isinstance(student,Student):
        student.hold = True 
        return "Completed!" 

    def removeHold(self, student): #check if student is Student object and then make student.hold false
      if isinstance(student,Student):
        student.hold = False
        return "Completed!"
      

    def unenrollStudent(self, student): #check if student is Student object and then make student.active false
      if isinstance(student,Student):
        student.active = False
        return "Completed!"


    def createStudent(self, person): #create a student object
        # YOUR CODE STARTS HERE
      return(Student(person,person.ssn,'Freshman'))


class Student(Person):
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3, 400)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3, 200)
        'Course added successfully'
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1
        Student(Jason Lee, jl2890, Freshman)
        >>> s2 = Student('Karen Lee', '247-01-2670', 'Freshman')
        >>> s2
        Student(Karen Lee, kl2670, Freshman)
        >>> s1 == s2
        False
        >>> s1.id
        'jl2890'
        >>> s2.id
        'kl2670'
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC132}
        >>> s1.enrollCourse('CMPSC360', C, 1)
        'Course added successfully'
        >>> s1.enrollCourse('CMPSC311', C, 1)
        'Course not found'
        >>> s1.semesters
        {1: CMPSC132, CMPSC360}
        >>> s2.semesters
        {}
        >>> s1.enrollCourse('CMPSC132', C, 1)
        'Course already enrolled'
        >>> s1.dropCourse('CMPSC360')
        'Course dropped successfully'
        >>> s1.dropCourse('CMPSC360')
        'Course not found'
        >>> s1.semesters
        {1: CMPSC132}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC132, 2: No courses}
        >>> s1.enrollCourse('CMPSC360', C, 2)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC132, 2: CMPSC360}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC132, 2: CMPSC360, 3: No courses}
        >>> s1
        Student(Jason Lee, jl2890, Sophomore)
    '''
    def __init__(self, name, ssn, year):
      random.seed(1)
      self.year = year
      self.name = name
      self.ssn = ssn
      self.hold = False
      self.active = True
      self.semesters= {}
      self.account = self.__createStudentAccount()
      
        # YOUR CODE STARTS HERE


    def __str__(self): #output student inforamtion
        
      return f"Student({self.name}, {self.id}, {self.year})"
   

    __repr__ = __str__

    def __createStudentAccount(self): #check if self.active is true and then creates StudentAccount object
        # YOUR CODE STARTS HERE
      if self.active == True:
        return StudentAccount(self)


    @property
    def id(self): #get initials with Uppercased alphabets and combine it with last 4 digits of ssn
      upper = []
      for item in self.name:
        for i in range(60,91):
          if item == chr(i):
            upper.append(item)

      upper = "".join(upper)
      upper = upper.lower()

      ssn= str(self.ssn)
      ssn = ssn[-4:]
      ID = f'{upper}{ssn}'
      return ID

    def registerSemester(self):
      if self.active == False or self.hold == True: #check if student is active or at hold
          return "Unsuccessful operation"
      else:
        sem = len(self.semesters.keys())+1 #adds a nuw semester and update year

        object = Semester(sem)
        self.semesters[sem] = object
      
        if sem == 1 or sem == 2:
          self.year = "Freshman"
        elif sem == 3 or sem == 4:
          self.year = "Sophomore"
        elif sem == 5 or sem == 6:
          self.year = "Junior"
        elif sem > 6:
          self.year = "Senior"
      
        

    def enrollCourse(self, cid, catalog, semester): 
      if self.active == False or self.hold == True: #check if student is active or at hold
        return "Unsuccessful operation"
      elif cid not in catalog.courseOfferings.keys(): #check if course is supported
        return "Course not found"
      elif cid in self.semesters[semester].courses.keys() : #check if course is already enrolled
        return "Course already enrolled"
      else:
        object = self.semesters.get(semester) #adds course and updates student's account
        course = catalog.courseOfferings[cid][0]
        object.addCourse(course)
        self.account.chargeAccount(StudentAccount.CREDIT_PRICE*course.credits)
        return "Course added successfully"
  

    def dropCourse(self, cid):
      if self.active == False or self.hold == True: #check if student is active or at hold
        return "Unsuccessful operation"
      elif cid not in self.semesters[len(self.semesters.keys())].courses.keys(): #check if course is in the self.semester
        return "Course not found"
      else:
        course = self.semesters[len(self.semesters.keys())].courses.pop(cid) #drop the course and updates student's account
        self.account.makePayment(StudentAccount.CREDIT_PRICE*course.credits*1/2)
        return "Course dropped successfully"


    def getLoan(self, amount):
        # YOUR CODE STARTS HERE
      last = self.semesters[len(self.semesters.keys())]
      if self.active == False:  #check if the student is active
        return "Unsuccessful operation"
      elif last.isFullTime == False: #check if the student is in FullTime 
        return "Not full-time"
      else:
        object = Loan(amount) #update student's account
        self.account.makePayment(amount)
        self.account.loans[object.loan_id] = object



class StudentAccount:
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3, 400)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3, 200)
        'Course added successfully'
        >>> C.addCourse('MATH 230', 'Calculus', 4, 600)
        'Course added successfully'
        >>> C.addCourse('PHYS 213', 'General Physics', 2, 500)
        'Course added successfully'
        >>> C.addCourse('CMPEN270', 'Digital Design', 4, 300)
        'Course added successfully'
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.account.balance
        3000
        >>> s1.enrollCourse('CMPSC360', C, 1)
        'Course added successfully'
        >>> s1.account.balance
        6000
        >>> s1.enrollCourse('MATH 230', C,1)
        'Course added successfully'
        >>> s1.enrollCourse('PHYS 213', C,1)
        'Course added successfully'
        >>> print(s1.account)
        Name: Jason Lee
        ID: jl2890
        Balance: $12000
        >>> s1.account.chargeAccount(100)
        12100
        >>> s1.account.balance
        12100
        >>> s1.account.makePayment(200)
        11900
        >>> s1.getLoan(4000)
        >>> s1.account.balance
        7900
        >>> s1.getLoan(8000)
        >>> s1.account.balance
        -100
        >>> s1.enrollCourse('CMPEN270', C,1)
        'Course added successfully'
        >>> s1.account.balance
        3900
        >>> s1.dropCourse('CMPEN270')
        'Course dropped successfully'
        >>> s1.account.balance
        1900.0
        >>> s1.account.loans
        {27611: Balance: $4000, 84606: Balance: $8000}
        >>> StudentAccount.CREDIT_PRICE = 1500
        >>> s2 = Student('Thomas Wang', '123-45-6789', 'Freshman')
        >>> s2.registerSemester()
        >>> s2.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s2.account.balance
        4500
        >>> s1.enrollCourse('CMPEN270', C,1)
        'Course added successfully'
        >>> s1.account.balance
        7900.0
    '''
    CREDIT_PRICE = 1000 #price per credit

    def __init__(self, student):
        # YOUR CODE STARTS HERE
      self.student = student
      self.balance = 0
      self.loans = {}


    def __str__(self): #output's student's account info
      return f'Name: {self.student.name}\nID: {self.student.id}\nBalance: ${self.balance}' 
  

    __repr__ = __str__


    def makePayment(self, amount): #subtract amount from the balance
      self.balance -= amount
      return self.balance


    def chargeAccount(self, amount): #adds amount from the balance
      self.balance += amount

      return self.balance


if __name__=='__main__':
    import doctest
    doctest.testmod()  # OR
    #doctest.run_docstring_examples(StudentAccount, globals(), name='HW22',verbose=True) # replace Course for the class name you want to test
    