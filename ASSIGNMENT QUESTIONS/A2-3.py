class Car:
    def __init__(self, model, year, prize):
        self.model = model
        self.year = year
        self.prize = prize
    def cost(self):
        print("prize of the car= ", self.prize)
C1 = Car("Maruthi", 2004, 200000)
C2 = Car("Ford", 2014, 500000)

C1.cost()
C2.cost()