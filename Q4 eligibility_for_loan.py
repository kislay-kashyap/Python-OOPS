class EligibilityException(Exception):
    pass

class Person:
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary
    
    def check_eligibility(self):
        if(self.salary<10000):
            raise EligibilityException("Monthly salary must not be less than 10000")
        
name = input("Please enter your name: ")
age = int(input("Please enter your Salary(per month): "))

person1 = Person(name, age)
try:
    person1.check_eligibility()
    print("You are eligible for loan, contact customer service")
except EligibilityException as e:
    print(e)