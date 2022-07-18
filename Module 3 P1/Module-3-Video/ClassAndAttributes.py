class Account:
    def __init__(self, name):
        self.holder = name
        self.balance = 0

    #x = Account('Alan')
  
#######################################
class MyClass:
    def method(self,arg1, arg2):
        <statements>
    #my_object = MyClass()
  
###########object Identity#############
x = Account('Alan')
y = Account('Liz')
x.holder -> Alan
y.holder -> Liz

#########Attributes####################
class Dog:
    index = 0.04
    def __init__(self, name, breed):
      self.name = name
      self.breed = breed
      self.vaccines = 0
        
    def getVaccine(self):
      self.vaccines += 1
      return self.vaccines

    #harry = Dog('Harry','Chihuahua')
    #harry.vaccines -> 0
    #getattr(harry,'vaccines') -> 0
    #harry.vaccines -> 1

######Looking up attribtues with dot(.)###########
class Dog:
    index = 0.04 #class attributes
    def __init__(self, name, breed):
      self.name = name
      self.breed = breed
      self.vaccines = 0 #instance attributes
        
    def getVaccine(self):
      self.vaccines += 1
      return self.vaccines

    #harry=Dog('Harry','Chihuahua')
    #sandy=Dog('sandy','Bulldog')
    #harry.index -> 0.04
    #sandy.index -> 0.04

###########Attribute Assignment####################
class Dog:
  index = 0.04
  def __init__(self,name,breed):
    self.name = name
    self.breed = breed
    self.vaccines = 0

  def getVaccine(self):
    self.vaccines += 1
    return self.vaccines
    
    #harry=Dog('Harry','Chihuahua')
    #harry.breed -> 'Chihuahua'
    #harry.breed = 'Poodle'
    #harry.breed -> 'Poodle'
    #harry.index = 0.09
    #harry.index -> 0.09

##############Methods###################
class Dog:
  index = 0.04
  def __init__(self,name,breed):
    self.name = name
    self.breed = breed
    self.vaccines = 0

  def getVaccine(self):
    self.vaccines += 1 #Methods
    return self.vaccines

  def changeName(self,new_name):
    self.name = new_name #Methods
    return self.name

#######Invoking Methods##################
class Dog:
  index = 0.04
  def __init__(self,name,breed):
    self.name = name
    self.breed = breed
    self.vaccines = 0

  def getVaccine(self):
    self.vaccines += 1 #Methods
    return self.vaccines

  def changeName(self,new_name):
    self.name = new_name #Methods
    return self.name

#harry = Dog('Harry','Chihuahua')
#harry.getVaccine() -> 1 -> Dog.getVaccine(harry)
#harry.name -> harry
#harry.changeName('Lupin') -> Lupin
#harry.name -> Lupin

#####Special Methods and Operator Overloading#####
class Dog:
  index = 0.04
  def __init__(self,name,breed):
    self.name = name
    self.breed = breed
    self.vaccines = 0

  def getVaccine(self):
    self.vaccines += 1 #Methods
    return self.vaccines

  def changeName(self,new_name):
    self.name = new_name #Methods
    return self.name
  
  def __str__(self):
    return 'My name is {}'.format(self.name)