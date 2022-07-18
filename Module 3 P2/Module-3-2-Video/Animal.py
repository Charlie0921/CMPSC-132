import random
from abc import *

class Animal(ABC):

    def __init__(self,name,age):
        self.name=name
        self.age=age

    @abstractmethod
    def eat(self):
        raise NotImplementedError('Subclass must implement abstract method')    

    @abstractmethod
    def sleep(self):
        raise NotImplementedError('Subclass must implement abstract method')   


class Dog(Animal):

    def __init__(self, name, age):
        self.name=name
        self.age=age
        if self.age==0:
            self.__id=self.__createID()
        else:
            self.__id=self.__createID()*age

    def eat(self):
        return '{} is eating...'.format(self.name)

    def sleep(self):
        return '{} is sleeping...'.format(self.name)

    def getID(self):
        return self.__id

    def setID(self, new_id):
        self.__id=new_id

    def __createID(self):
        return random.randint(100,999)

    def __str__(self):
        return 'Subject #{}: {}, {} year(s) old'.format(self.__id,self.name, self.age)

    __repr__=__str__