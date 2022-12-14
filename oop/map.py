# map() = applies function to each item in an iterable (list, tuple, etc)

# map(function. iterable)

store = [("shirt", 20.0),
         ("pants", 25.0),
         ("jacket", 50.0),
         ("socks", 10.0)]

toEuro = lambda data: (data[0], data[1]*0.95)
toUSD = lambda data: (data[0], data[1]/0.95)

storeEuro = list(map(toEuro, store))
storeUSD = list(map(toUSD, store))

for i in storeEuro:
    print(i)

# for i in storeUSD:
#     print(i)