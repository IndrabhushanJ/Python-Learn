from car import Car

car1 = Car("Tata", "Nexa", 2021, "Silver")
car2 = Car("MG", "Hector", 2022, "Red")

# print(car1.manufacturer)
# print(car1.model)
# print(car1.year)
# print(car1.color)

# car1.drive()
# car1.stop()

car1.wheels = 2
print(car1.wheels)
print(car2.wheels)
print(Car.wheels)
