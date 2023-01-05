class Student:
    def readData(self):
        self.rno = int(input("Enter roll number:"))
        self.mark1 = int(input("Enter mark1:"))
        self.mark2 = int(input("Enter mark2:"))
    def computeTotal(self):
        self.total = self.mark1+self.mark2
    def display_details(self):
        print("Roll Number=", self.rno)
        print("Mark1=", self.mark1)
        print("Mark2=", self.mark2)
        print("Total Mark=", self.total)
S = Student()
S.readData()
S.computeTotal()
S.display_details()