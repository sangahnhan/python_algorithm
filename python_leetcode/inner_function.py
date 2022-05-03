def deco(func):
    print("shadow")
    def wrapper():
        print("before")
        ret = func()
        print("after")
        return ret
    print(f" inner function :: {wrapper}")
    return wrapper

# @deco
def base():
    print("base func")

f = deco(base)
f()
# base()


# def hello():
#     def hi():
#         print("hello")
#     return hi()

# hello()