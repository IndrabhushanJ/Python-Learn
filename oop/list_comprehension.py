# list comprehension = a way to create a new list with less syntax
#                      can mimic certain lambda functions, easier to read
#
#                      list = [expression for item in iterable] --syntax
#                      list - [expression for item in iterable if condition]
#                      list - [expression if/else for item in iterable]


# square = []  # Create an empty list
# for i in range(1, 11):  # create a loop
#     square.append(i * i)  # define what each loop iteration should do
# print(square)
#
# square = [i * i for i in range(1, 11)] # list comprehension
# print(square)

students = [100, 90, 80, 70, 60, 50, 40, 30, 0]

# passed_students = list(filter(lambda x: x >= 60, students))
# print(passed_students)
#
# passed_students = [i for i in students if i >= 60]

passed_students = [i if i >= 60 else "Failed" for i in students]
print(passed_students)
