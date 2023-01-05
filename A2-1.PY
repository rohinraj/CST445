class Arith:
    def read(self):
        self.x = int(input("Enter first number: "))
        self.y = int(input("Enter second number: "))
    def add(self):
        print("sum=", self.x + self.y)
A = Arith()
A.read()
A.add()