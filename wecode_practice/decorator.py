def deco(func):
    def wrapper():
        print("before")
        print("after")
        return func()
    return wrapper

@deco # deco(base) 와 같은 의미이다.
def base():
    print("base func")

base()