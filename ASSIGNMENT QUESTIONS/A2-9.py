class Rectangle:
    def read(self):
        self.height = int(input("Enter the height of rectangle:"))
        self.width = int(input("Enter the width of rectangle:"))
        self.corner_x = int(input("Enter right corner x:"))
        self.corner_y = int(input("Enter right corner y:"))
    def center(self):
        self.corner_x1 = self.corner_x-self.width
        self.corner_y1 = self.corner_y+self.height
        print("Center={}, {}".format((self.corner_x+self.corner_x1)/2,(self.corner_y+self.corner_y1)/2))
    def area(self):
        print("Area=", self.height*self.width)
    def perimeter(self):
        print("Perimeter=", 2*(self.height+self.width))
R = Rectangle()
R.read()
R.center()
R.area()
R.perimeter()