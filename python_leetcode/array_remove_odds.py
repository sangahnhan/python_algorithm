numbers=[1,1,1,1,1]
def remove_odd_numbers(numbers):
    # 여기에 코드를 작성해주세요.
    for i in range(len(numbers)-1,-1,-1):
      if numbers[i] % 2==1:
        del numbers[i]
    return numbers
remove_odd_numbers(numbers)
print(numbers)

# def remove_odd_numbers(numbers):
#     # 여기에 코드를 작성해주세요.
#     for i in numbers:
#       if i % 2==1:
#         numbers.remove(i)
#     return numbers