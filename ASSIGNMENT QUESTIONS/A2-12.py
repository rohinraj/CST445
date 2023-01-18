class Student:
    def readData(self):
        self.rollno = int(input("Enter roll number: "))
        self.name = input("Enter name: ")
        self.mark = int(input("Enter mark: "))
    def printDetails(self):
        print("Roll number: ", self.rollno)
        print("Name: ", self.name)
        print("mark: ", self.mark)
class Percentage(Student):
    def printpercentage(self):
        a = self.mark
        self.percentage = (a/50)*100
        print("Percentage: ", self.percentage)
S = Percentage()
S.readData()
S.printDetails()
S.printpercentage()