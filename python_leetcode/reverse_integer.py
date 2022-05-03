def reverse(num):
    origin_num = num
    if num<0:
        num=abs(num)
    num=str(num)
    print(num)
    num=num[::-1]
    print(num)
    print(type(int(''.join(a))))
    print(b)
    if origin_num <0:
        return -res
    return res
print(reverse(1234))