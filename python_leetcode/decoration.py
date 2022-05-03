def welcome_decorator(func):
   # 아래에 코드를 작성해 주세요.
  def wrapper():
    return func() + "welcome to WELCOME!"
  return wrapper
  
@welcome_decorator
def greeting():
   # 아래에 코드를 작성해 주세요.
  return "Hello, "

print(greeting())