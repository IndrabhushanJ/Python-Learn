# ----------------------------------------------------------------------------------------------------------
import time

# ----------------------------------------------------------------------------------------------------------
# print(time.ctime(0)) # convert a time expression in seconds since epoch to a readable string
#                        epoch = when your computer thinks the time began (reference point)

# print(time.time()) # returns current seconds since epoch
# print(time.ctime(time.time()))

# time_obj = time.localtime()
# time_obj = time.gmtime() #UTC time
# print(time_obj)
# time = time.strftime("%a, %d-%b-%Y, %I:%M:%S %p", time_obj)
# print(time)

# timeString = "11-11-2022"
# print(time.strptime(timeString, "%d-%m-%Y"))

# (year, month, day, hours, minutes, seconds, # day of the week, # day of the year, dst)
timeTuple = (2020, 11, 10, 18, 49, 15, 0, 0, 0)
print(time.asctime(timeTuple))
print(time.mktime(timeTuple))
