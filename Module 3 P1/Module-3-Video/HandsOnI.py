import datetime
class Person:
  def __init__(self, name, birthdate):
    self.name = name
    self.birthdate = birthdate
  
  # @property -> "a.age","a.name"
  def age(self):
    today = datetime.date.today()
    month, day, year = self.birthdate.split('/')
    age = today.year - int(year)

    if today < datetime.date(today.year,int(month),int(day)):
      age -= 1

    return age