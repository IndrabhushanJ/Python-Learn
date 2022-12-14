class Animal:
    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is Sleeping")


class Rabbit(Animal):
    def run(self):
        print("This animal is running.")


class Fish(Animal):
    def swim(self):
        print("This animal is Swimming.")


class Hawk(Animal):
    def fly(self):
        print("This animal is flying.")


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

rabbit.run()
fish.swim()
hawk.fly()
