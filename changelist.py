def selectionSort(nums):
  for i in range(len(nums)):
    min=999
    change=0
    for j in range(i,len(nums)):
      if min > nums[j]:
        min = nums[j]
        change=j
    nums[i],nums[change] = nums[change],nums[i]
  return nums

print(selectionSort([7,5,4,2]))