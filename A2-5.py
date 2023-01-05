class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def dataprint(self):
        print("Name=", self.name)
        print("Age=", self.age)
        print("salary=", self.salary)
S1 = Person("Alex", 23, 12387847384000)
S1.dataprint()
S2 = Person("Ashok", 40, 123000)
S2.dataprint()