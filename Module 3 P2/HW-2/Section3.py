
  
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

if __name__=='__main__':
    import doctest
    doctest.testmod()  # OR
    #doctest.run_docstring_examples(Course, globals(), name='HW22',verbose=True) # replace Course for the class name you want to test