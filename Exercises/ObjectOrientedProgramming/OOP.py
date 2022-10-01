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

p1 = Person("Ayaan", 1234)
p1.display()
p1.details()

class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking init of first class
        Person.__init__(self, name, idnumber)
