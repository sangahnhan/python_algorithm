def top_k(nums, k):
    count = {}
    lst = []
    for i in nums:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    count = sorted(count,key=(lambda x : count[x]),reverse=True)

    for i in range(k):
        lst.append(count[i])
    return lst
nums = [1,1,1,2,2,3]
print(top_k(nums,1))
