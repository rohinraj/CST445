class Mobile:
    def set_details(self):
        self.company = input("Enter company name:")
        self.model = input("Enter model name:")
        self.price = input("Enter price:")
    def display_details(self):
        print("company name=", self.company)
        print("model name=", self.model)
        print("price=", self.price)
M = Mobile()
M.set_details()
M.display_details()