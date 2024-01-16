#Employee class 
#scripted by:
#Eng/Kirollos Gerges

class Employee:
    def __init__(self,name,age,depertment,is_manager):
        self.name=name
        self.age=age
        self.depertment=depertment
        self.is_manager=is_manager

class student:
    def __init__(self,name,age,gpa):
        self.name=name
        self.age=age
        self.gpa=gpa

def is_excellent(self):
    if self.is_manager:
        return True
    else:
        return False
