#앞에 2와 뒤에 2가 아닌 수 교환 한다
arr = [2,3,3,3,1,2,1,3,4,5,2,1,3,3] # 
target=3
left_index=-1
right_index=100
right_not_target=1
while left_index < right_index:
    left_index=arr.index(target,left_index+1)
    print(left_index)
    for i in range(len(arr)-right_not_target,0,-1):
        if arr[i]==target:
            right_not_target+=1
            continue
        else:
            right_index=len(arr)-right_not_target
            right_not_target+=1
            break
    if left_index < right_index:
        arr[left_index], arr[right_index]=arr[right_index],arr[left_index]
print(arr)


# while left_index < right_index:
#     left_index=arr.index(target,left_index+1)
#     print(left_index)
#     for i in range(right_not_target,len(reverse_arr)):
#         if reverse_arr[i]==target:
#             right_not_target+=1
#             continue
#         else:
#             right_index=len(arr)-right_not_target-1
#             right_not_target+=1
#             break
#     if left_index < right_index:
#         arr[left_index], arr[right_index]=arr[right_index],arr[left_index]
# print(arr)