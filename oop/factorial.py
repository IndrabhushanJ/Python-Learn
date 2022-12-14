
# using for loop
def factorial(number):
    fact = 1
    for x in range(number, 0, -1):
        fact = fact * x
    return fact

# using recursion

# def factorial(number):
#     if number == 0 or number == 1:
#         return 1
#     else:
#         return number * factorial(number-1)


print(factorial(10))

greetig = "hello my fellow people. hello to you all"

