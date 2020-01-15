# Document at least 3 use cases of static methods
class Dates:
    def __init__(self, date):
        self.date = date
        
    def getDate(self):
        return self.date
    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")
date = Dates("15-12-2016")
dateFromDB = "15/12/2016"
dateWithDash = Dates.toDashDate(dateFromDB)
if(date.getDate() == dateWithDash):
    print("Equal")
else:
    print("Unequal")

class Employee:
     
    def func_message(self):
        print('Welcome to Python Programming')
 
    @staticmethod
    def func_msg():
        print("Welcome to Tutorial Gateway")