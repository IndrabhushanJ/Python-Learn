# thread = a flow of execution. Like a separate order of instruction
#          However each thread takes turn running to achieve concurrency
#          GIL = (global interpreter lock)
#          allows only one thread to hold the control of the python interpreter at any one time

# cpu bound = a program/task spends most of it's time waiting for internal events (CPU intensive)
#             use multiprocessing

# io bound =  a program/task spends most of it's time waiting for external events (user input, web scraping)
#             use multiprocessing

import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("You ate breakfast")

def drink_coffee():
    time.sleep(4)
    print("You drank the coffee")

def study():
    time.sleep(4)
    print("You finished studying")

# eat_breakfast()
# drink_coffee()
# study()

x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())