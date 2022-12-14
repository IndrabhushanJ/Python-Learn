# duck typing = concept where the type or the class of an object is less important than the methods
#               it defines.

class Duck:

    def walk(self):
        print("Duck is walking!")

    def talk(self):
        print("Duck is quaking")


class Chicken:

    def walk(self):
        print("Chicken is walking")

    def talk(self):
        print("Chicken is clucking")


class Person:

    def catch(self, bird):
        bird.walk()
        bird.talk()
        print("You Caught a", bird.__class__.__name__)
        print()


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)
person.catch(chicken)
