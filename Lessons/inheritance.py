#inheritance.py

class Pet:
    def __init__(self, name:str, price:int, type:str):
        self.name = name
        self.price = price
        self.type = type
        print("Created a pet")

    def get_price_tax(self):
        # assume 10%
        return self.price*1.1

class Goldfish(Pet):
    def __init__(self, brain:bool, name:str, price:int):
        super().__init__(name=name, price=price, type="fish")
        self.brain = brain
        print("Created a goldfish")


    def swim(self):
        return "Swimming straight" if self.brain else "swimming upside down"

# Create a new pet
bob = Pet(name="bob", price=3, type="dog")
print(bob.get_price_tax())
carl = Goldfish(name="carl", price=5, brain=False)
print(carl.get_price_tax())
print(carl.swim())
