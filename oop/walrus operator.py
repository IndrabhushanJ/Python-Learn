# walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assign values to variable as part of a large expression

# happy = True
# print(happy)

# print(happy = True) # TypeError
# print(happy := True)

# num = int()
#
# print(type(num))

# foods = list()
# while True:
#     food = input("What food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)


foods = list()
while food := input("What food do you like? ") != "quit" :
    foods.append(food)
