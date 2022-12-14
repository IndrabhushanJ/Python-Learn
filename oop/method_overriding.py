# method overring

class Animal:

    def eat(self):
        print("This animal is eating")


class Rabbit(Animal):
    def eat(self):
        print("Rabbit is eating")


animal = Animal()
rabbit = Rabbit()

animal.eat()
rabbit.eat()
