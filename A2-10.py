class Complex:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
    def display(self):
        if self.b>0:
            print("complex number is :", self.a, " + ", self.b, "j")
        else:
            print("complex number is :", self.a, self.b, "j")
    def __add__(self, other):
        r = self.a+other.a
        i = self.b+other.b
        return Complex(r, i)
c1 = Complex(2,-3)
c2 = Complex(3,4)
c3 = c1 + c2
c1.display()
c2.display()
c3.display()