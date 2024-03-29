# ***************************************
# Python multiprocessing
# ***************************************
# multiprocessing = running tasks in parallel on different cpu cores, bypass GIL used for threading
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for io bound takss (waiting around)

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    print(cpu_count())
    start = time.perf_counter()
    a = Process(target=counter,args=(1000000000,))
    # b = Process(target=counter,args=(500000000,))
    # c = Process(target=counter,args=(250000000,))
    # d = Process(target=counter,args=(250000000,))

    a.start()
    # b.start()
    # c.start()
    # d.start()

    a.join()
    # b.join()
    # c.join()
    # d.join()

    print("finished in:",time.perf_counter()-start,"seconds")


if __name__ == '__main__':
    main()
