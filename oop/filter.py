# filter() = creates a collection of elements from iterable for which a function returns true

# filter(function, iterable)

friends = [("Sanket", 16),
           ("Chinmay", 17),
           ("Nirav", 24),
           ("Kunal", 22),
           ("Sanjay", 20)]

alcoholEligible = lambda data: data[1] >= 18

drinkBuddies = list(filter(alcoholEligible, friends))

for friend in drinkBuddies:
    print(friend)


