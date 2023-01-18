class Rectangle:
    def __init__ (self, length = 0, breadth = 0):
        self.length = length
        self.breadth = breadth
    def area(self):
        print ("area=", self.length*self.breadth)
R1 = Rectangle(20,30)
R1.area()
R2 = Rectangle(23,34)
R2.area()