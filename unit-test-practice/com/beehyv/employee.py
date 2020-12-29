class Employee:
    
    increment = 1.5
    
    def __init__(self, fname, lname, age, salary):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.salary = salary
        
    def email(self):
        return f"{self.fname}.{self.lname}{self.age}@gmail.com"   
    
    def fullName(self):
        return f"{self.fname} {self.lname}"
    
    def raisedSalary(self):
        self.salary = self.salary * self.increment       