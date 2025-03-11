# first_name = "Indrabhushan"
# last_name = "Jaiswar"
# full_name = first_name + " " + last_name
# print("Hello " + full_name)
#
# age = 25
# age += 1
# # print("Your age is: "+str(age))
# # print(type(age))
# print("age: ", age)
#
# # float
# height = 166.78
# print("Height: ", height, "cm")
# print("Height: " + str(height) + "cm")
# print("Height: {}".format(height))
# print(f"Height: {height} cm")
#
# isMarried = False
# if isMarried:
#     print(full_name + "is Married")
# else:
#     print(full_name + " is Not Married")
#
# # Multiple Assignment
#
# name, age, attractive = "indra", 26, "yes"
#
# print("name: " + name)
# print("age: " + str(age))
# print("attractive: " + str(attractive))
import math

# # String Methods
#
# name = "indrabhushan"
#
# print(len(name))
# print(name.find("bhushan"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("a"))
# print(name.replace("a", "i"))
# print(name*3)

# # Type Casting
#
# x = 1
# y = 2.0
# z = "3"
#
# x = float(x)
# y = float(y)
# z = float(z)
#
# print("x is "+str(x))
# print("y is "+str(y))
# print(z*3)

# INPUT

# name = input("What's your name: ")
# age = int(input("How old are you?: "))
# height = float(input("How tall are you?: "))
# print("Hello " + name)
# print("You are "+str(age)+" years old.")
# print("You are "+str(height) + " cm tall.")

# Math function

# import math
#
# pi = 3.14
# x = 1
# y = 2
# z = 3
#
# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi)) #Tells how much far it is from 0
# print(pow(pi, 2))
# print(math.sqrt(pi))
# print(max(x, y, z))
# print(min(x, y, z))

# Slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:steps]

# name = "Indrabhushan Jaiswar"
#
# first_name = name[:12]
# last_name = name[13:]
# funky_name = name[::2]
# reversed_name = name[::-1]
# test_name = name[:-7]
#
# print(first_name)
# print(last_name)
# print(funky_name)
# print(reversed_name)
# print(test_name)
#
# website1 = "http://google.com"
# website2 = "http://wikipedia.com"
#
# slice = slice(7, -4)
#
# print(website1[slice])
# print(website2[slice])

# if statement

# age = int(input("How old are you?: "))
#
# if age >= 18:
#     print("You are an Adult!")
#     if age == 100:
#         print("& You are a century old!")
# elif age < 0:
#     print("You haven't been born yet!")
# else:
#     print("You are a child!")

# logical operators (and, or, not)

# temp = int(input("What's the temperature outside?: "))
#
# if temp >= 0 and temp <= 30:
#     print("The temperature is good today!")
#     print("Go outside!!")
# elif temp < 0 or temp > 30:
#     print("The temperature is bad today!")
#     print("Stay Inside")

# while loop

# name = None
#
# while not name:
#     name = input("Enter your name: ")
#
# print("Hello "+name)

# for loop
#       while loop : unlimited
#       for loop: limited

# for i in range(10+1):
#     print(i)

# for i in range(50, 100+1, 2): # range(start,stop,steps)
#     print(i)

# for i in "indrabhushan":
#     print(i)

# import time
#
# for seconds in range(10, 0, -1):
#     print(seconds)
#     time.sleep(1)
# print("Happy New Year!!")

# nested loops

# rows = int(input("How many rows?: "))
# columns = int(input("How many columns?: "))
# symbol = input("Enter your symbol: ")
#
# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()

#  loop control(break, continue, pass)
#         break - used to terminate a loop entirely
#         continue - skips to the next iteration of the loop
#         pass - does nothing, acts as a placeholder

# while True:
#         name = input("Enter your name: ")
#         if name != "":
#                 break

# phone_number = "123-456-7890"
#
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")

# for i in range(1,21):
#     if i == 13:
#         pass
#     else:
#         print(i)

# list = used to store multiple items in a single variable

# food = ["pizza", "burger", "butter chicken", "mutton masala"]
#
# food[0] = "sandwich"
#
# food.append("vada pav")
# food.remove("burger")
# food.pop()  # removes last element
# food.insert(0, "cake")
# food.sort()
# food.clear()
#
# # print(food[0])
#
# for i in food:
#     print(i)

# 2D list = a list of lists

# dinner = ["Butter Chicken", "Mutton Masala", "Garlic Naan"]
# drinks = ["Lime soda", "Masala Chai", "Coffee"]
# dessert = ["Cake", "Caramel Custard"]
#
# food = [dinner, drinks, dessert]
#
# print(food[2][1])
#
# user_detail = [1, "indra", 7.2]
# print(user_detail)

# Tuples = collection which is ordered and unchangeable
#          used to group related data

# student = ("indra", 26, "male")
#
# student.count("indra")
# student.index("male")
#
# for x in student:
#     print(x)
#
# if "indra" in student:
#     print("indra is here!")

# set = collection which is unordered, un-indexed. No duplicate value

# utensils = {"spoon", "fork", "knife"}
# dishes = {"bowl", "plate", "cup", "knife"}

# utensils.add("Steel glass")
# utensils.remove("plate")
# utensils.clear()
# utensils.update(dishes)
#
# dinner_table = utensils.union(dishes)

# print(utensils.difference(dishes))
# print(utensils.intersection(dishes))
# for x in dinner_table:
#     print(x)

# dictionary = A changable, unordered collection of unique key:value pairs
#              Fast because it uses hashing, allow us to access  a value quickly

# capitals = {'USA': 'Washington DC',
#             'India': 'New Delhi',
#             'China': 'Beijing',
#             'Russia': 'Moscow'}
#
# capitals.update({'Germany': "Berlin"})  # Add new Value
# capitals.update({'USA': 'Las Vagas'})  # Update existing data
# capitals.pop('China')
# capitals.clear()

# print(capitals['India'])
# print(capitals.get('China'))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())
#
#
# for key, value in capitals.items():
#     print(key, value)

# index operator [] = gives access to a sequence's of element (str, list, tuple, etc)

# name = "indrabhushan Jaiswar!"

# if name[0].islower():
#     name = name.capitalize()

# first_name = name[:12].upper()
# last_name = name[13:-1].lower()
# last_element = name[-1]
#
# print(name)
# print(first_name)
# print(last_name)
# print(last_element)

# function = a block of code which is executed only when it is called

# def hello(first_name, last_name, age):
#     print("hello " + first_name + " " + last_name)
#     print("You are " + str(age) + " years old")
#     print("Have nice day!")
#
#
# hello("Indrabhushan", "Jaiswar", 26)

# def multiply(number1, number2):
#     return number1 * number2
#
#
# print(multiply(3, 3))


# keyword argument = arguments preceded by an identifier when we pass them to a function
#                    The order of the arguments doesn't matter, unlike positional arguments
#                    Python knows the names of the arguments that our function receives

# def hello(first, middle, last):
#     print("Hello " + first + " " + middle + " " + last)


# hello(last="Jaiswar", first="Indrabhushan", middle="Dukhhran")

# Nested functions calls = function calls inside other function call
#                          innermost function calls are resolved first
#                          returned value is used as argument for the next outer function

# print(round(abs(float(input("Enter a Whole Positive Number: ")))))


# *args = parameter that will pack all elemets into tuple
#         useful so that a function can accept a varying amount of arguments

# def add(*stuff):
#     sum = 0
#     stuff = list(stuff)
#     stuff[0] = 0
#     for i in stuff:
#         sum += i
#     return sum
#
#
# print(add(3, 3, 4, 5, 6, 3, 4))

# **kwargs = parameter that will pack all arguments into dictionary
#         useful so that a function can accept a varying amount of keyword arguments


# def hello(**kwargs):
#     print("Hello", end=" ")
#     for key, value in kwargs.items():
#         print(value, end=" ")
#
#
# hello(title="Mr.", first="Indrabhushan", middle="Dukkhran", last="Jaiswar")

# str.format() = optional method that gives users more control when displaying output
# animal = "cow"
# item = "moon"

# print("The " + animal + " jumped over the " + item)
# print("The {} jumped over the {}".format(animal, item))
# print("The {1} jumped over the {0}".format(animal, item))  # positional argument
# print("The {animal} jumped over the {item}".format(animal="cow", item="moon"))  # keyword argument

# text = "The {} jumped over the {}"
# print(text.format(animal, item))

# name = "Indra"
# print("Hello my name is {}. Nice to meet you".format(name))
# print("Hello my name is {:10}. Nice to meet you".format(name))  # adds padding to the right  default
# print("Hello my name is {:<10}. Nice to meet you".format(name))  # left align it
# print("Hello my name is {:>10}. Nice to meet you".format(name))  # right align it
# print("Hello my name is {:^10}. Nice to meet you".format(name))  # center align it

# number = 3.14159;
# number1 = 1000
#
# print("The number pi is {:.3f}".format(number))
# print("The number is {:,}".format(number1))
# print("The number is {:_}".format(number1))
# print("The number is {:b}".format(number1))
# print("The number is {:o}".format(number1))
# print("The number is {:X}".format(number1))
# print("The number is {:E}".format(number1))

# random

# import random
#
# x = random.randint(1, 100)
# y = random.random()
#
# myList = ['rock', 'paper', 'scissor']
# z = random.choice(myList)
#
# cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'K', 'Q']
#
# random.shuffle(cards)
#
# print(cards)

# exception = events detected during execution that interupts the flow of a program

# try:
#     numerator = int(input("Enter a number to divide: "))
#     denominator = int(input("Enter a number to divide by: "))
#     result = numerator/denominator
# except ZeroDivisionError as e:
#     print(e)
#     print("You can't divide by Zero! Dummy! XD")
# except ValueError as e:
#     print(e)
#     print("Enter numbers only...")
# except Exception as e:
#     print(e)
#     print("Someting went wrong :(")
# else:
#     print(result)
# finally:
#     print("This always executes")

# file handling

# import os
#
# path = "C:\\Users\\indra\\Desktop\\test.txt"
#
# if os.path.exists(path):
#     print("This path exists!")
#     if os.path.isfile(path):
#         print("This is a file.")
#     elif os.path.isdir(path):
#         print("This is a folder.")
# else:
#     print("This path doesn't exists!")

# read a file

# try:
#     with open('test.txt') as file:
#         print(file.read())
# except FileNotFoundError:
#     print("That file not find :(")

# write a file

# text = "Have a nice day!"
#
# with open('test2.txt', 'a') as file:
#     file.write(text)

# copyfile() - copies contents of a filec
# copy() - copyfile() + permission mode + destination can be directory
# copy2() - copy() + copies metadata (file's creation and modification times)

# import shutil
#
#
# shutil.copyfile('test2.txt', 'test3.txt') # scr,dst
# shutil.copy2('test2.txt', 'C:\\Users\\indra\\Desktop\\copy.txt') # scr,dst

# moveing file

# import os
#
# file = 'test.txt'
# destination = 'file_test\\test.txt'
#
# try:
#     if os.path.exists(destination):
#         print("File already exist!")
#     else:
#         os.replace(file, destination)
#         print(file + " was moved.")
# except FileNotFoundError:
#     print(file + "was not found")

# remove file/folder

# import os
# import shutil
#
# path = 'file_test'
#
# try:
#     # os.remove(path)  # remove file
#     # os.rmdir(path) # remove empty folder
#     shutil.rmtree(path)  # remove a directory containing files 💀
#
# except FileNotFoundError:
#     print("File not found.")
# except PermissionError:
#     print("You don't have permission to delete that.")
# except OSError:
#     print("You can't delete that using that function")
# else:
#     print(path + " was removed!")

# module = a file containing python code. May contain functions, classes, etc
# Used with modular programming, which is to separate program into parts

# import messages
# import messages as m
# from messages import hello,bye
# from messages import *
#
# hello()
# bye()
#
# help("modules")
player = "indrabhusan"
print(player, "won")
