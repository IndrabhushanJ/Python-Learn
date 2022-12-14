# passing objects as argument

class Car:
    color = None


class Bike:
    color = None


def change_color(vehicle, color):
    vehicle.color = color


car1 = Car()
car2 = Car()
bike1 = Bike()
bike2 = Bike()

change_color(car1, "RED")
change_color(car2, "BLACK")
change_color(bike1, "BLUE")
change_color(bike2, "PINK")

print(car1.color)
print(car2.color)
print(bike1.color)
print(bike2.color)
