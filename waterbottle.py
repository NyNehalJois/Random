class waterbottle:
    def __init__(self, capacity, size, colour, material,style,enerydrink,owner):
        self.capacity = capacity
        self.size = size
        self.colour = colour
        self.material = material
        self.style = style
        self.energydrink = enerydrink
        self.owner = owner

    def fill(self):
        print(f"the {self.colour} bottle is filled with liquid.")

    def drink(self):
        print(f"the {self.colour} bottle has {self.energydrink} and is being drunk, on a {self.style} day at the {self.material} bottle.")

    def user(self):
        print(f"the {self.colour} bottle is being used by the {self.owner}, on a {self.style} day at the {self.material} bottle.")
        
bottle1 = waterbottle("500ml","small", "blue", "plastic","gym", "Gatorade", "Alice")
print("this waterbottle has: \n", bottle1.capacity,"of capacity.\n",bottle1.size,"size. \n", bottle1.colour,"colour. \n", bottle1.material,"material. \n", bottle1.style,"style."," \n", bottle1.energydrink,"as energy drink.")
bottle1.fill()
bottle1.drink()
bottle1.user()
print("\n")
bottle2 = waterbottle("1000ml","large", "red", "metal","hiking", "Monster", "Bob")
print("this bottle has: \n", bottle2.capacity,"of capacity.\n",bottle2.size,"size. \n", bottle2.colour,"colour. \n", bottle2.material,"material. \n", bottle2.style,"style."," \n", bottle2.energydrink,"as energy drink.")
bottle2.fill()  
bottle2.drink()
bottle2.user()