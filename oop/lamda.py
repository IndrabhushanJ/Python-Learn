# lambda function = function written in one line using lamda keyword
#                  accepts any number of arguments, but only has one expression
#                  (think it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)

#  syntax - lambda parameters:expression

# def double(x):
#     return x * 2
#
# print(double(5))

double = lambda x: x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name: first_name + " " + last_name
age_check = lambda age: True if age >= 18 else False
print(double(10))
print(multiply(2, 4))
print(add(10, 2, 40))
print(full_name("Indrabhushan", "Jaiswar"))
print(age_check(18))
