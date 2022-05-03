strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
sorted_strs = []
for i in range(len(strs)):
    sort = ''.join(sorted(strs[i]))
    sorted_strs.append(sort)
print(sorted_strs)
set_sorted_strs = list(set(sorted_strs))
ln = len(set(sorted_strs))
result = []
for i in range(ln):
    lst=[]
    for j in range(len(strs)):
        if set_sorted_strs[i] == sorted_strs[j]:
            lst.append(strs[j])
            
    result.append(lst)
print(result)