# sort() method = used with lists
# sort() method = used with iterables

# students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs"]
# students = ("Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs")
#
# # students.sort(reverse=True)
#
# sorted_list = sorted(students, reverse=True)
#
# for i in sorted_list:
#     print(i)


# students = [("Squidward", "F", 60),
#             ("Sandy", "A", 40),
#             ("Patrick", "D", 69),
#             ("Spongebob", "C", 100),
#             ("Mr. Krabs", "B", 66)]

students = (("Squidward", "F", 60),
            ("Sandy", "A", 40),
            ("Patrick", "D", 69),
            ("Spongebob", "C", 100),
            ("Mr. Krabs", "B", 66))

grade = lambda grades: grades[1]
age = lambda ages: ages[2]

# students.sort(key=grade)
# print(students[1])

# for i in students:
#     print(i)

sorted_tuple = sorted(students, key=age)

# print(sorted_tuple)

for i in sorted_tuple:
    print(i)