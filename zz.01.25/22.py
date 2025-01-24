class Car:
    def __init__(self, name:str, brand:str, max_speed:int, color:str):
        self.name = name
        self.brand = brand
        self.max_speed = max_speed
        self.color = color
        self.star_speed = 0
    def drive(self):
        print(f' машина {self.name} {self.brand} може їхати зі скоростю от {self.star_speed} до {self.max_speed}')

car1 = Car("M5", "BMW", 150, "black")
car2 = Car('C class', "Mercedes", 180, 'red')

car1.drive()
car2.drive()
# car1.change_color("orange")