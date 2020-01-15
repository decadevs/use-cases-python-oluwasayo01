# Document at least 3 use cases of instance methods

class User():
  def __init__(self, username = None):
    self.__username = username

  def setUsername(self, x):
    self.__username = x
  
  def getUsername(self):
    return(self.__username)

Steve = User('steve1')
print('Before setting:', Steve.getUsername())
Steve.setUsername('steve2')
print('After setting:', Steve.getUsername())


class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance


class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = 0
        self.perimeter = 0

    def calc_area(self):
        pass

    def calc_perimeter(self):
        pass


class Rectangle(Shape):

    def calc_area(self):
        self.area = self.length * self.width

    def calc_perimeter(self):
        self.perimeter = 2(self.length + self.width)

    def get_area(self):
        return self.area

    def get_perimeter(self):
        return self.perimeter


shape = Rectangle(23, 12)
print(shape.get_area())
print(shape.calc_area())
print(shape.get_area())

