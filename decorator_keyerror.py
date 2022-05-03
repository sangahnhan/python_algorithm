def decorator(func):
    def wrapper(self, a, *args):
        print(a)
        print(args)
        return func(self, a, *args)
    return wrapper
class View():
    @decorator
    def hello(self,a,product_id):
        print(a)
        print(product_id)
a = View()
a.hello(3,2,4,5,6)