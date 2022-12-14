# dictionary comprehension = create dictionary using an expression
#                            can replace for loops and certain lambda functions

# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if condition}
# dictionary = {key: (if/else) for (key,value) in iterable}
# dictionary = {key: func(value) for (key,value) in iterable}

# --------------------------------------------------------------------------------------------------------------
# cities_in_F = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}
# cities_in_F = {key: round(((value - 32) * (5 / 9)), 2) for (key, value) in cities_in_F.items()}
# print(cities_in_F)

# --------------------------------------------------------------------------------------------------------------
# weather = {'New York': 'snowing', 'Boston': 'sunny', 'Los Angeles': 'sunny', 'Chicago': 'cloudy'}
# sunny_weather = {key: value for (key, value) in weather.items() if value == 'sunny'}
# print(sunny_weather)

# --------------------------------------------------------------------------------------------------------------
# cities = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}
# desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key,value) in cities.items()}
# print(desc_cities)

# --------------------------------------------------------------------------------------------------------------
def check(value):
    if value >= 40:
        return "WARM"
    else:
        return "COLD"

cities = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}
desc_cities = {key: check(value) for (key,value) in cities.items()}
print(desc_cities)

