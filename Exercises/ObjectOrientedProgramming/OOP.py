class Person(object):

    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

    def details(self):
        print('My name is {}'.format(self.name))
        print('My ID number is {}'.format(self.idnumber))


print("-- Name & ID test --")
p1 = Person("Ayaan", 1234)
p1.display()
p1.details()


class Employee(Person):
    def __init__(self, name, idNumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking init of first class
        Person.__init__(self, name, idNumber)

    def details(self):
        print('My name is {}'.format(self.name))
        print('My ID number is {}'.format(self.idNumber))
        print('My post is {}'.format(self.post))


print("")
print("-- Employee info --")
employeeJohn = Employee('John', 123456, 200000, "Intern")
employeeJohn.display()
employeeJohn.details()


class Salary(Person):
    def __init__(self, name, idNumber, post, salary, commission, finalSalary):
        self.name = name
        self.idNumber = idNumber
        self.post = post
        self.salary = salary
        self.commission = commission
        self.finalSalary = finalSalary

        Person.__init__(self, name, idNumber)

    def details(self):
        print("-- Salary + Employee info --")

        # Basic info
        print("My name is {}" + self.name)
        print("My ID number is {}" +self.idNumber)
        print("My post is {}" +self.post)

        # Salary calculations
        self.commission = self.salary * 0.055
        self.finalSalary = self.salary + self.commission

        # Display
        print("My salary is {}" + self.salary)
        print("My commission payments are {}" + self.commission)
        print("My final salary is {}" + self.finalSalary)
