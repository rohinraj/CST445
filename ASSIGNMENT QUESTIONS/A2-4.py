class Student:
    def __init__(self, name, rno):
        self.name = name
        self.rno = rno
    def dataprint(self):
        print("Name=", self.name)
        print("Roll number=", self.rno)
S1 = Student("Alex", 58)
S1.dataprint()
S2 = Student("Ashok", 40)
S2.dataprint()