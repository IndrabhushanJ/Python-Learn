# Higher order function = a. function that either:
#                         1. accepts a function as an argument
#                               or
#                         2. returns a function
#                         (In Python, function are also treated as object)

# accepts a function as an argument
def loud(text):
    return text.upper()

def quite(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(loud)
hello(quite)

# returns a function

def divisor(x) :
    def divident(y):
        return y / x
    return divident

divide = divisor(2)
print(divide(10))