class drink:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        print(f"{self.name}, {self.price}")
        
class order:
        def