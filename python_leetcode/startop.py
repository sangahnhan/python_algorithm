def more_than_half(nums):
    # 아래 코드를 입력해주세요.
    dict1={}
    for i in nums:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i]=1
    return max(dict1, key = lambda i: dict1[i])

# print(more_than_half([1,2,1,1,1]))
dict1={1:4,2:1}
key = lambda i: dict1[i]
print(key.__str__())