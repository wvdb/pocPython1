from paps.OO1.Worker import Worker

__author__ = 'admin'

class Employee(Worker):
    def __init__(self, fname, lname, age, birthDate):
        super().__init__()
        self.fname = fname
        self.lname = lname
        self.age = age
        self.birthDate = birthDate

    def printName(self):
        print("Hello my name is " + self.fname + " " + self.lname)

    def getName(self):
        return self.fname + " " + self.lname

    def __str__(self, *args, **kwargs):
        return "Employee{" + "fname='" + self.fname + '\'' + ", lname='" + self.lname + '\'' + "}"

