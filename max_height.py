def get_max_area(height):
    max_var=0
    for i in range(1,max(height)+1):
        lt=0
        rt=len(height)-1   
        while height[lt] < i:
            lt +=1
        while height[rt] < i:
            rt -= 1
        if max_var <= (rt-lt) * i:
            max_var = (rt-lt) * i
    return max_var
print(get_max_area([3,2,4,2,1,5,2,3,4]))