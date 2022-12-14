class Car:

    wheels = 4 # class variable

    def __init__(self, manufacturer, model, year, color):
        self.manufacturer = manufacturer # instance variable
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This "+self.model+ " is driving")

    def stop(self):
        print("This "+self.model+" has stopped!")
