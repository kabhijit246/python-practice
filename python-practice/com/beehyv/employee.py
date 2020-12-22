class Employee:
    company = "Beehyv"
    #salary = input("Enter your salary: ")
    #bonus = input("Enter your bonus: ")
    @staticmethod
    def getSalary(salary, bonus):
        totalSalary = salary + bonus
        return totalSalary

abhijit = Employee()
sal = abhijit.getSalary(600000,30000)   
print(f"Your total salary is: { sal }")  