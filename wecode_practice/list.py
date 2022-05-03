def get_prefix(strs):
    result   = ''
    new_list = []
    if strs==[]:
        return ''
    else:
        while len(min(strs, key=len)) != 0:
            for i in range(0,len(strs)):
                if strs[i][0] == '': break
                new_list.append(strs[i][0])
                strs[i] = strs[i][1:]
            if len(set(new_list)) == 1:
                result += new_list[0]
            else: break
            new_list = []
        return result
print(get_prefix([]))


