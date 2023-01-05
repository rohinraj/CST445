class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        area = 3.14*self.r**2
        print("Area of circle", area)
    def perimeter(self):
        perimeter = 2*3.14*self.r
        print ("Perimeter of the circle", perimeter)
C = Circle(7)
C.area()
C.perimeter()