import math
a=[-1,0,3,5,9,12]
key = 9

search = len(a)
while True:
    if a[math.floor(search/2)] == key:
        print(math.floor(search/2),a[math.floor(search/2)])
        print(math.floor(search/2))
        break
    elif a[math.floor(search/2)] > key:
        print(math.floor(search/2),a[math.floor(search/2)])
        search = round(search/2)
    else:
        print(math.floor(search/2),a[math.floor(search/2)])
        search = search + round(search/2)