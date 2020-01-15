# Document at least 3 use cases of class methods

class Player:
  teamName = 'Liverpool'      # class variables   
  
  def __init__(self, name):
    self.name = name        # creating instance variables
  # update class variable
  @classmethod
  def getTeamName(cls):
    return cls.teamName

print(Player.getTeamName())

from datetime import date 
  
class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
      
    # a class method to create a Person object by birth year. 
    @classmethod
    def fromBirthYear(cls, name, year): 
        return cls(name, date.today().year - year)

person = Person.fromBirthYear('Sayo', 1888)
print(person.age)

