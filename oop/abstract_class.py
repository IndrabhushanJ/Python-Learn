# abstract class = class which contains one or more abstract methods
# abstract method = method that has declaration but does not have implementation

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("This car stopped")

class Bike (Vehicle):

    def go(self):
        print("you drive the bike")

    def stop(self):
        print("This bike stopped")


car = Car()
bike = Bike()


car.go()
bike.go()
car.stop()
bike.stop()
