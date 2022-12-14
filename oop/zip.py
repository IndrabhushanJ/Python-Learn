# zip(*iterators) = aggregate elements from two or more iterables (list, tuples, sets etc)
#                   create a zip object with paired elements stored in tuples for each element

usernames = ["indra", "Dude", "Bro"]
passwords = ("p@ssw0rd", "1234", "123#abc")
login_date = ["1/2/2021","21/3/2019", "6/12/2022"]

users = list(zip(usernames, passwords,login_date))

for i in users:
    print(i)
