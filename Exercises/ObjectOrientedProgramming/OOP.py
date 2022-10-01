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

p1 = Person("Ayaan", "123456")
p1.display()
p1.details()
