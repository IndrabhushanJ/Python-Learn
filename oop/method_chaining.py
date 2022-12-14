# method chaining = calling multiple methods sequentially
#                   each call perform an action on the same object and return self


class Car:

    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("you drive the car")
        return self

    def brake(self):
        print("you stop the car")
        return self

    def turn_off(self):
        print("you turn off the car")
        return self


car = Car()

# car.turn_on().drive().brake().turn_off()

car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()