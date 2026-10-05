class WaterBottle:
    def __init__(self, color, capacity):
        self.color = color
        self.capacity = capacityF
        self.current_water = 0
    def fill(self, amount):
        if self.current_water + amount <= self.capacity:
            self.current_water += amount
            print(f"Filled {amount}ml. Current water: {self.current_water}ml")
        else:
            print(f"Cannot fill! Bottle capacity is {self.capacity}ml, only {self.capacity - self.current_water}ml available.")
    def drink(self, amount):
        if self.current_water >= amount:
            self.current_water -= amount
            print(f"Drank {amount}ml. Remaining water: {self.current_water}ml")
        else:
            print(f"Not enough water! Only {self.current_water}ml available.")
    def is_empty(self):
        return self.current_water == 0
    def display(self):
        print(f"Color: {self.color}")
        print(f"Capacity: {self.capacity}ml")
        print(f"Current water: {self.current_water}ml")
        print(f"Empty: {self.is_empty()}\n")
bottle1 = WaterBottle("blue", 500)
bottle1.fill(300)
bottle1.drink(100)
bottle1.display()
bottle2 = WaterBottle("red", 750)
bottle2.fill(750)
bottle2.drink(200)
bottle2.display()
