import timeit
a=iter(range(1000))
def for_loop():
    num_list = []
    for i in range(1000):
        num_list.append(i)
def list_comprehension():
    num_list = [i for i in range(1000)]
def list_iterator():
    while True:
        try:
            next(a)
        except StopIteration:
            break

if __name__=="__main__":
    time1= timeit.Timer("for_loop()","from __main__ import for_loop")
    print("for loop time = ",time1.timeit(number=1000),"milliseconds")

    time2=timeit.Timer("list_comprehension()","from __main__ import list_comprehension")
    print("list_comprehension time = ",time2.timeit(number=1000),"milliseconds")

    time3=timeit.Timer("iterator()","from __main__ import iterator")
    print("list_iterator time = ",time2.timeit(number=1000),"milliseconds")