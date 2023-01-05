class Book:
    def get_details(self):
        self.title = input("Enter the title name: ")
        self.author = input("Entyer Author name: ")
        self.cost = int(input("Enter the cost: "))
    def print_details(self):
        print("Title is: ", self.title)
        print("Author is", self.author)
        print("Cost is: ", self.cost)
B = Book()
B.get_details()
B.print_details()